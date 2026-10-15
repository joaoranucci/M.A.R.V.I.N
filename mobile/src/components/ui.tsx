import { Ionicons } from '@expo/vector-icons';
import type { ComponentProps, ReactNode } from 'react';
import {
  ActivityIndicator,
  Pressable,
  StyleSheet,
  Text,
  TextInput,
  View,
  type StyleProp,
  type TextInputProps,
  type ViewStyle,
} from 'react-native';
import { colors, radius, space, touch, type } from '../theme/tokens';

export type IconName = ComponentProps<typeof Ionicons>['name'];

export function Card({ children, style, tone }: { children: ReactNode; style?: StyleProp<ViewStyle>; tone?: 'amber' | 'danger' | 'cyan' }) {
  const border = tone === 'amber' ? colors.amber : tone === 'danger' ? colors.danger : tone === 'cyan' ? colors.borderStrong : colors.border;
  const bg = tone === 'amber' ? colors.amberSoft : tone === 'danger' ? colors.dangerSoft : colors.surface;
  return <View style={[styles.card, { borderColor: border, backgroundColor: bg }, style]}>{children}</View>;
}

type ButtonVariant = 'primary' | 'secondary' | 'ghost' | 'danger' | 'amber';

export function Button({
  label,
  onPress,
  icon,
  variant = 'secondary',
  disabled,
  loading,
  style,
  accessibilityHint,
  compact,
}: {
  label: string;
  onPress: () => void;
  icon?: IconName;
  variant?: ButtonVariant;
  disabled?: boolean;
  loading?: boolean;
  style?: StyleProp<ViewStyle>;
  accessibilityHint?: string;
  compact?: boolean;
}) {
  const palette = {
    primary: { bg: colors.cyan, fg: '#03121A', border: colors.cyan },
    secondary: { bg: colors.surface, fg: colors.text, border: colors.borderStrong },
    ghost: { bg: 'transparent', fg: colors.cyan, border: 'transparent' },
    danger: { bg: colors.dangerSoft, fg: colors.danger, border: colors.danger },
    amber: { bg: colors.amber, fg: '#1A1000', border: colors.amber },
  }[variant];
  return (
    <Pressable
      accessibilityRole="button"
      accessibilityLabel={label}
      accessibilityHint={accessibilityHint}
      accessibilityState={{ disabled: !!disabled || !!loading, busy: !!loading }}
      disabled={disabled || loading}
      onPress={onPress}
      style={({ pressed }) => [
        styles.button,
        compact && styles.buttonCompact,
        { backgroundColor: palette.bg, borderColor: palette.border, opacity: disabled ? 0.45 : pressed ? 0.75 : 1 },
        style,
      ]}
    >
      {loading ? <ActivityIndicator color={palette.fg} /> : icon ? <Ionicons name={icon} size={20} color={palette.fg} /> : null}
      <Text style={[styles.buttonLabel, { color: palette.fg }]} numberOfLines={1}>
        {label}
      </Text>
    </Pressable>
  );
}

export function IconButton({ icon, label, onPress, color = colors.textSecondary, size = 24 }: { icon: IconName; label: string; onPress: () => void; color?: string; size?: number }) {
  return (
    <Pressable
      accessibilityRole="button"
      accessibilityLabel={label}
      onPress={onPress}
      hitSlop={8}
      style={({ pressed }) => [styles.iconButton, pressed && { backgroundColor: colors.surfacePressed }]}
    >
      <Ionicons name={icon} size={size} color={color} />
    </Pressable>
  );
}

export function SectionTitle({ children, right }: { children: string; right?: ReactNode }) {
  return (
    <View style={styles.sectionRow}>
      <Text style={type.section} accessibilityRole="header">
        {children.toUpperCase()}
      </Text>
      {right}
    </View>
  );
}

export function Chip({ label, tone = 'default', icon }: { label: string; tone?: 'default' | 'cyan' | 'amber' | 'danger' | 'success' | 'muted'; icon?: IconName }) {
  const map = {
    default: [colors.surfaceSolid, colors.textSecondary],
    cyan: [colors.cyanSoft, colors.cyan],
    amber: [colors.amberSoft, colors.amber],
    danger: [colors.dangerSoft, colors.danger],
    success: [colors.successSoft, colors.success],
    muted: ['transparent', colors.textMuted],
  }[tone];
  return (
    <View style={[styles.chip, { backgroundColor: map[0] }]}>
      {icon && <Ionicons name={icon} size={13} color={map[1]} />}
      <Text style={[styles.chipText, { color: map[1] }]} numberOfLines={1}>
        {label}
      </Text>
    </View>
  );
}

export function EmptyState({ icon, title, text, action }: { icon: IconName; title: string; text: string; action?: ReactNode }) {
  return (
    <View style={styles.empty}>
      <View style={styles.emptyIcon}>
        <Ionicons name={icon} size={28} color={colors.cyan} />
      </View>
      <Text style={[type.title, { textAlign: 'center', fontSize: 19 }]}>{title}</Text>
      <Text style={[type.bodySecondary, { textAlign: 'center' }]}>{text}</Text>
      {action}
    </View>
  );
}

export function Banner({ tone, text, icon, children }: { tone: 'info' | 'warn' | 'error' | 'ok'; text: string; icon?: IconName; children?: ReactNode }) {
  const map = {
    info: [colors.cyanSoft, colors.cyan, 'information-circle-outline'],
    warn: [colors.amberSoft, colors.amber, 'alert-circle-outline'],
    error: [colors.dangerSoft, colors.danger, 'close-circle-outline'],
    ok: [colors.successSoft, colors.success, 'checkmark-circle-outline'],
  }[tone] as [string, string, IconName];
  return (
    <View style={[styles.banner, { backgroundColor: map[0], borderColor: map[1] + '55' }]} accessibilityLiveRegion="polite">
      <Ionicons name={icon ?? map[2]} size={20} color={map[1]} />
      <View style={{ flex: 1, gap: space.sm }}>
        <Text style={[type.bodySecondary, { color: colors.text }]}>{text}</Text>
        {children}
      </View>
    </View>
  );
}

export function Row({
  title,
  subtitle,
  icon,
  right,
  onPress,
  accessibilityLabel,
}: {
  title: string;
  subtitle?: string | null;
  icon?: IconName;
  right?: ReactNode;
  onPress?: () => void;
  accessibilityLabel?: string;
}) {
  const content = (
    <>
      {icon && (
        <View style={styles.rowIcon}>
          <Ionicons name={icon} size={20} color={colors.cyan} />
        </View>
      )}
      <View style={{ flex: 1, gap: 2 }}>
        <Text style={type.label}>{title}</Text>
        {!!subtitle && <Text style={type.caption}>{subtitle}</Text>}
      </View>
      {right ?? (onPress ? <Ionicons name="chevron-forward" size={18} color={colors.textMuted} /> : null)}
    </>
  );
  if (!onPress) return <View style={styles.row}>{content}</View>;
  return (
    <Pressable
      accessibilityRole="button"
      accessibilityLabel={accessibilityLabel ?? title}
      onPress={onPress}
      style={({ pressed }) => [styles.row, pressed && { backgroundColor: colors.surfacePressed }]}
    >
      {content}
    </Pressable>
  );
}

export function Field(props: TextInputProps & { label: string }) {
  const { label, style, ...rest } = props;
  return (
    <View style={{ gap: space.xs }}>
      <Text style={type.caption}>{label}</Text>
      <TextInput placeholderTextColor={colors.textMuted} selectionColor={colors.cyan} style={[styles.input, style]} accessibilityLabel={label} {...rest} />
    </View>
  );
}

export function Segmented<T extends string>({ value, options, onChange }: { value: T; options: { value: T; label: string }[]; onChange: (v: T) => void }) {
  return (
    <View style={styles.segmented} accessibilityRole="tablist">
      {options.map((option) => {
        const active = option.value === value;
        return (
          <Pressable
            key={option.value}
            accessibilityRole="tab"
            accessibilityState={{ selected: active }}
            onPress={() => onChange(option.value)}
            style={[styles.segment, active && styles.segmentActive]}
          >
            <Text style={[styles.segmentText, active && { color: colors.text }]} numberOfLines={1} maxFontSizeMultiplier={1.5}>
              {option.label}
            </Text>
          </Pressable>
        );
      })}
    </View>
  );
}

export function Dot({ color }: { color: string }) {
  return <View style={{ width: 8, height: 8, borderRadius: 4, backgroundColor: color }} />;
}

const styles = StyleSheet.create({
  card: { borderWidth: StyleSheet.hairlineWidth, borderRadius: radius.lg, padding: space.lg, gap: space.md },
  button: {
    minHeight: touch.min,
    paddingHorizontal: space.xl,
    borderRadius: radius.pill,
    borderWidth: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: space.sm,
  },
  buttonCompact: { paddingHorizontal: space.lg },
  buttonLabel: { fontSize: 16, fontWeight: '600', flexShrink: 1 },
  iconButton: { width: touch.min, height: touch.min, alignItems: 'center', justifyContent: 'center', borderRadius: radius.pill },
  sectionRow: { flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', marginTop: space.lg, marginBottom: space.sm },
  chip: { flexDirection: 'row', alignItems: 'center', gap: 4, paddingHorizontal: 10, paddingVertical: 4, borderRadius: radius.pill, alignSelf: 'flex-start' },
  chipText: { fontSize: 12, fontWeight: '600' },
  empty: { alignItems: 'center', gap: space.md, paddingVertical: space.xxxl, paddingHorizontal: space.xl },
  emptyIcon: { width: 64, height: 64, borderRadius: 32, backgroundColor: colors.cyanSoft, alignItems: 'center', justifyContent: 'center' },
  banner: { flexDirection: 'row', gap: space.md, padding: space.md, borderRadius: radius.md, borderWidth: 1, alignItems: 'flex-start' },
  row: { flexDirection: 'row', alignItems: 'center', gap: space.md, minHeight: 60, paddingVertical: space.sm, paddingHorizontal: space.sm, borderRadius: radius.md },
  rowIcon: { width: 36, height: 36, borderRadius: 18, backgroundColor: colors.cyanSoft, alignItems: 'center', justifyContent: 'center' },
  input: {
    minHeight: touch.min,
    borderRadius: radius.md,
    borderWidth: 1,
    borderColor: colors.borderStrong,
    backgroundColor: colors.surfaceSolid,
    color: colors.text,
    paddingHorizontal: space.lg,
    fontSize: 16,
  },
  segmented: { flexDirection: 'row', backgroundColor: colors.surfaceSolid, borderRadius: radius.pill, padding: 4, gap: 4 },
  segment: { flex: 1, minHeight: 40, alignItems: 'center', justifyContent: 'center', borderRadius: radius.pill, paddingHorizontal: space.sm },
  segmentActive: { backgroundColor: colors.surfacePressed, borderWidth: 1, borderColor: colors.borderStrong },
  segmentText: { color: colors.textMuted, fontWeight: '600', fontSize: 14 },
});
