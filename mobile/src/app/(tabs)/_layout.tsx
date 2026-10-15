import { Ionicons } from '@expo/vector-icons';
import type { ComponentProps } from 'react';
import { Tabs } from 'expo-router';
import { Pressable, StyleSheet, Text, View } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { useAssistant } from '../../features/assistant/controller';
import { colors, space } from '../../theme/tokens';

const TABS: Record<string, { label: string; icon: keyof typeof Ionicons.glyphMap; active: keyof typeof Ionicons.glyphMap }> = {
  index: { label: 'MARVIN', icon: 'radio-button-on-outline', active: 'radio-button-on' },
  library: { label: 'Biblioteca', icon: 'library-outline', active: 'library' },
  activities: { label: 'Atividades', icon: 'pulse-outline', active: 'pulse' },
  devices: { label: 'Dispositivos', icon: 'hardware-chip-outline', active: 'hardware-chip' },
};

type BottomTabBarProps = Parameters<NonNullable<ComponentProps<typeof Tabs>['tabBar']>>[0];

function TabBar({ state, navigation }: BottomTabBarProps) {
  const insets = useSafeAreaInsets();
  const approval = useAssistant((s) => s.approval || s.commandPreview);
  return (
    <View style={[styles.bar, { paddingBottom: Math.max(insets.bottom, space.sm) }]}>
      {state.routes.map((route, index) => {
        const tab = TABS[route.name];
        if (!tab) return null;
        const focused = state.index === index;
        return (
          <Pressable
            key={route.key}
            accessibilityRole="tab"
            accessibilityState={{ selected: focused }}
            accessibilityLabel={tab.label}
            onPress={() => {
              const event = navigation.emit({ type: 'tabPress', target: route.key, canPreventDefault: true });
              if (!focused && !event.defaultPrevented) navigation.navigate(route.name);
            }}
            style={styles.tab}
          >
            <View style={[styles.iconWrap, focused && styles.iconActive]}>
              <Ionicons name={focused ? tab.active : tab.icon} size={22} color={focused ? colors.cyan : colors.textMuted} />
              {route.name === 'index' && approval && !focused && <View style={styles.badge} />}
            </View>
            <Text style={[styles.label, focused && { color: colors.text }]} numberOfLines={1} maxFontSizeMultiplier={1.3}>
              {tab.label}
            </Text>
          </Pressable>
        );
      })}
    </View>
  );
}

export default function TabsLayout() {
  return (
    <Tabs tabBar={(props) => <TabBar {...props} />} screenOptions={{ headerShown: false, sceneStyle: { backgroundColor: colors.bg } }}>
      <Tabs.Screen name="index" />
      <Tabs.Screen name="library" />
      <Tabs.Screen name="activities" />
      <Tabs.Screen name="devices" />
    </Tabs>
  );
}

const styles = StyleSheet.create({
  bar: {
    flexDirection: 'row',
    backgroundColor: 'rgba(6, 11, 18, 0.96)',
    borderTopWidth: StyleSheet.hairlineWidth,
    borderTopColor: colors.border,
    paddingTop: space.sm,
  },
  tab: { flex: 1, alignItems: 'center', gap: 2, minHeight: 52 },
  iconWrap: { width: 52, height: 30, borderRadius: 15, alignItems: 'center', justifyContent: 'center' },
  iconActive: { backgroundColor: colors.cyanSoft },
  label: { fontSize: 11, color: colors.textMuted, fontWeight: '600' },
  badge: { position: 'absolute', top: 2, right: 10, width: 8, height: 8, borderRadius: 4, backgroundColor: colors.amber },
});
