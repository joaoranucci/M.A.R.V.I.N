// MARVIN visual identity: deep graphite, cyan/blue energy, soft white text, amber for attention.
export const colors = {
  bg: '#04070C',
  bgRaised: '#08101A',
  surface: 'rgba(16, 28, 44, 0.72)',
  surfaceSolid: '#0D1724',
  surfacePressed: 'rgba(30, 52, 78, 0.8)',
  border: 'rgba(120, 200, 255, 0.12)',
  borderStrong: 'rgba(120, 200, 255, 0.28)',
  text: '#E8F4FB',
  textSecondary: '#A3B8CA',
  textMuted: '#6E869B',
  cyan: '#38D6FF',
  cyanSoft: 'rgba(56, 214, 255, 0.14)',
  blue: '#2E6BFF',
  blueSoft: 'rgba(46, 107, 255, 0.16)',
  amber: '#FFB547',
  amberSoft: 'rgba(255, 181, 71, 0.14)',
  danger: '#FF7A7A',
  dangerSoft: 'rgba(255, 122, 122, 0.14)',
  success: '#4BE3A6',
  successSoft: 'rgba(75, 227, 166, 0.14)',
  slate: '#5D7183',
} as const;

export const space = { xs: 4, sm: 8, md: 12, lg: 16, xl: 20, xxl: 24, xxxl: 32 } as const;
export const radius = { sm: 10, md: 14, lg: 20, xl: 28, pill: 999 } as const;

// Embedded at build time by the expo-font config plugin (no runtime download).
export const fonts = {
  display: 'SpaceGrotesk_600SemiBold',
  displayMedium: 'SpaceGrotesk_500Medium',
} as const;

export const type = {
  hero: { fontFamily: fonts.display, fontSize: 28, lineHeight: 34, color: colors.text, letterSpacing: 0.2 },
  title: { fontFamily: fonts.display, fontSize: 22, lineHeight: 28, color: colors.text },
  section: { fontFamily: fonts.displayMedium, fontSize: 13, lineHeight: 18, color: colors.textMuted, letterSpacing: 1.2 },
  body: { fontSize: 16, lineHeight: 23, color: colors.text },
  bodySecondary: { fontSize: 15, lineHeight: 21, color: colors.textSecondary },
  caption: { fontSize: 13, lineHeight: 18, color: colors.textMuted },
  label: { fontSize: 15, lineHeight: 20, fontWeight: '600' as const, color: colors.text },
} as const;

export const touch = { min: 48 } as const;
