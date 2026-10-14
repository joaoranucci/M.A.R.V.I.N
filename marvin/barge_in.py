"""Sustained voice onset detector; adaptive noise floor, no acoustic echo cancellation."""
from array import array
import math
from functools import lru_cache


@lru_cache(maxsize=1)
def _vad():
    import webrtcvad
    return webrtcvad.Vad(2)


def is_voice(pcm, rate):
    import numpy as np
    samples = np.frombuffer(pcm, dtype=np.int16)
    if rate != 16000:
        size = int(len(samples)*16000/rate)
        if size < 160:
            return False
        samples = np.interp(np.arange(size)*rate/16000, np.arange(len(samples)), samples).astype(np.int16)
    raw = samples.tobytes()
    return any(_vad().is_speech(raw[i:i+320],16000) for i in range(0,len(raw)-319,320))


class SpeechOnset:
    def __init__(self, threshold=650, duration=.18, use_vad=False):
        self.threshold = max(100, min(10000, threshold))
        self.duration = duration
        self.floor = 80.0
        self.above = 0.0
        self.use_vad = use_vad

    def feed(self, pcm, rate, *, playing=False):
        samples = array('h')
        samples.frombytes(pcm)
        if not samples:
            return False
        rms = math.sqrt(sum(x*x for x in samples)/len(samples))
        if not playing:
            self.floor = self.floor*.96 + min(rms, self.threshold)*.04
            self.above = 0
            return False
        limit = max(self.threshold, self.floor*3.5)
        voiced = rms>limit and (not self.use_vad or is_voice(pcm,rate))
        self.above = self.above+len(samples)/rate if voiced else 0.0
        return self.above >= self.duration
