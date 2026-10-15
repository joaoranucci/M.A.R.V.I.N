import { useReducedMotion } from 'react-native-reanimated';
import { useSettings } from './settings';

/** System "remove animations" setting, overridable in MARVIN preferences. */
export function useReduceMotion(): boolean {
  const system = useReducedMotion();
  const preference = useSettings((s) => s.reduceMotion);
  return preference === 'on' ? true : preference === 'off' ? false : system;
}
