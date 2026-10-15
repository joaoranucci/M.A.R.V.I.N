import { useEffect, useState } from 'react';

/** Time-dependent labels update predictably, including after a minute spent on the same screen. */
export function useClock(intervalMs = 60000): number {
  const [now, setNow] = useState(() => Date.now());
  useEffect(() => {
    const timer = setInterval(() => setNow(Date.now()), intervalMs);
    return () => clearInterval(timer);
  }, [intervalMs]);
  return now;
}
