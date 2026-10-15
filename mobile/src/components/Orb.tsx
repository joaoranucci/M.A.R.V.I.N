import {
  BlurMask,
  Canvas,
  Circle,
  DashPathEffect,
  Group,
  Path,
  Points,
  RadialGradient,
  Skia,
  useClock,
  vec,
} from '@shopify/react-native-skia';
import { memo, useMemo } from 'react';
import { useDerivedValue, useFrameCallback, useSharedValue } from 'react-native-reanimated';
import type { Phase } from '../features/assistant/controller';
import { audioLevel } from '../features/voice/level';

/**
 * The MARVIN core: glow, energy core, orbiting rings and particles.
 * Everything animates on the UI thread (Skia + Reanimated); React re-renders only
 * when the phase changes. Amplitude comes from the real mic/playback level.
 */
interface Palette {
  core: string[];
  glow: string;
  ringA: string;
  ringB: string;
  particle: string;
  speed: number;
  particles: boolean;
}

const PALETTES: Record<Phase, Palette> = {
  idle: { core: ['#F2FCFF', '#5FE3FF', '#1A6BFF00'], glow: '#2E6BFF', ringA: '#38D6FF', ringB: '#2E6BFF', particle: '#9BEBFF', speed: 1, particles: true },
  listening: { core: ['#FFFFFF', '#7BEBFF', '#38D6FF00'], glow: '#38D6FF', ringA: '#7BEBFF', ringB: '#38D6FF', particle: '#D5F7FF', speed: 1.4, particles: true },
  processing: { core: ['#E6F0FF', '#5B8CFF', '#3047FF00'], glow: '#3D5BFF', ringA: '#6F8DFF', ringB: '#38D6FF', particle: '#A9BCFF', speed: 3.2, particles: true },
  speaking: { core: ['#FFFFFF', '#8FF0FF', '#38D6FF00'], glow: '#38D6FF', ringA: '#B4F4FF', ringB: '#38D6FF', particle: '#E2FBFF', speed: 1.6, particles: true },
  executing: { core: ['#EAF2FF', '#4F86FF', '#2E6BFF00'], glow: '#2E6BFF', ringA: '#38D6FF', ringB: '#6F8DFF', particle: '#9FD0FF', speed: 2.4, particles: true },
  awaiting: { core: ['#FFF8EC', '#FFC56B', '#FF9F1A00'], glow: '#FF9F1A', ringA: '#FFB547', ringB: '#FFD18A', particle: '#FFE2B0', speed: 0.8, particles: true },
  offline: { core: ['#C9D6E2', '#6E869B', '#3A4B5A00'], glow: '#24313D', ringA: '#5D7183', ringB: '#3E4F5E', particle: '#7F93A5', speed: 0.35, particles: false },
};

const PARTICLES = 26;

function arc(cx: number, cy: number, r: number, start: number, sweep: number) {
  return Skia.PathBuilder.Make().addArc({ x: cx - r, y: cy - r, width: r * 2, height: r * 2 }, start, sweep).detach();
}

function OrbBase({ phase, size, reduceMotion }: { phase: Phase; size: number; reduceMotion: boolean }) {
  const palette = PALETTES[phase];
  const clock = useClock();
  const c = size / 2;
  const smooth = useSharedValue(0);

  useFrameCallback(() => {
    // Smooth the raw amplitude so the core breathes instead of flickering.
    smooth.value += (audioLevel.value - smooth.value) * 0.22;
  });

  const speed = reduceMotion ? 0 : palette.speed;
  const breathe = useDerivedValue(() => (reduceMotion ? 0.5 : Math.sin(clock.value / 1500) * 0.5 + 0.5));
  const coreR = useDerivedValue(() => size * 0.15 * (1 + 0.06 * breathe.value + 0.5 * smooth.value));
  const glowR = useDerivedValue(() => size * 0.36 * (1 + 0.04 * breathe.value + 0.22 * smooth.value));
  const glowOpacity = useDerivedValue(() => (phase === 'offline' ? 0.25 : 0.42 + 0.25 * smooth.value + 0.08 * breathe.value));
  const ringScale = useDerivedValue(() => 1 + 0.07 * smooth.value);

  const rotA = useDerivedValue(() => [{ rotate: (clock.value / 4200) * speed }, { scale: ringScale.value }]);
  const rotB = useDerivedValue(() => [{ rotate: -(clock.value / 6100) * speed }, { scale: ringScale.value }]);
  const rotC = useDerivedValue(() => [{ rotate: (clock.value / 2600) * speed }]);

  const ringA = useMemo(() => arc(c, c, size * 0.3, -40, 250), [c, size]);
  const ringB = useMemo(() => arc(c, c, size * 0.37, 120, 200), [c, size]);
  const ringC = useMemo(() => arc(c, c, size * 0.44, 0, 360), [c, size]);

  const points = useDerivedValue(() => {
    const t = clock.value / 1000;
    const out = [];
    for (let i = 0; i < PARTICLES; i++) {
      const seed = i * 2.399963; // golden angle spread
      const orbit = size * (0.25 + ((i * 37) % 17) / 100 + 0.05 * smooth.value);
      const angle = seed + (reduceMotion ? 0 : t * (0.15 + (i % 5) * 0.05) * palette.speed);
      const wobble = reduceMotion ? 0 : Math.sin(t * 1.3 + i) * size * 0.012;
      out.push(vec(c + Math.cos(angle) * (orbit + wobble), c + Math.sin(angle) * (orbit + wobble)));
    }
    return out;
  });

  return (
    <Canvas style={{ width: size, height: size }}>
      <Circle cx={c} cy={c} r={glowR} opacity={glowOpacity} color={palette.glow}>
        <BlurMask blur={size * 0.12} style="normal" />
      </Circle>
      <Group origin={vec(c, c)} transform={rotC} opacity={0.35}>
        <Path path={ringC} style="stroke" strokeWidth={1} color={palette.ringB}>
          <DashPathEffect intervals={phase === 'executing' ? [18, 10] : [2, 9]} />
        </Path>
      </Group>
      <Group origin={vec(c, c)} transform={rotB}>
        <Path path={ringB} style="stroke" strokeWidth={2} strokeCap="round" color={palette.ringB} opacity={0.75} />
      </Group>
      <Group origin={vec(c, c)} transform={rotA}>
        <Path path={ringA} style="stroke" strokeWidth={3} strokeCap="round" color={palette.ringA}>
          <BlurMask blur={2} style="solid" />
        </Path>
      </Group>
      {palette.particles && (
        <Points points={points} mode="points" style="stroke" strokeWidth={size * 0.012} strokeCap="round" color={palette.particle} opacity={0.75} />
      )}
      <Circle cx={c} cy={c} r={coreR}>
        <RadialGradient c={vec(c, c)} r={size * 0.24} colors={palette.core} />
      </Circle>
    </Canvas>
  );
}

export const Orb = memo(OrbBase);
