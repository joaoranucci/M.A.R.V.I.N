import { Stack, router } from 'expo-router';
import * as SplashScreen from 'expo-splash-screen';
import { StatusBar } from 'expo-status-bar';
import { useEffect, useState } from 'react';
import { Text, View } from 'react-native';
import { GestureHandlerRootView } from 'react-native-gesture-handler';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { bootstrap, useShare } from '../core/bootstrap';
import { colors, type } from '../theme/tokens';

void SplashScreen.preventAutoHideAsync();

export default function RootLayout() {
  const [ready, setReady] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const shared = useShare((s) => s.payload);

  useEffect(() => {
    bootstrap()
      .then(() => setReady(true))
      .catch((e: unknown) => setError(e instanceof Error ? e.message : String(e)))
      .finally(() => void SplashScreen.hideAsync());
  }, []);

  useEffect(() => {
    if (ready && shared) router.push('/share');
  }, [ready, shared]);

  if (error) {
    return (
      <View style={{ flex: 1, backgroundColor: colors.bg, padding: 24, justifyContent: 'center', gap: 12 }}>
        <Text style={type.title}>Não foi possível iniciar o MARVIN</Text>
        <Text style={type.bodySecondary}>{error}</Text>
      </View>
    );
  }
  if (!ready) return <View style={{ flex: 1, backgroundColor: colors.bg }} />;

  return (
    <GestureHandlerRootView style={{ flex: 1, backgroundColor: colors.bg }}>
      <SafeAreaProvider>
        <StatusBar style="light" />
        <Stack
          screenOptions={{
            headerStyle: { backgroundColor: colors.bg },
            headerTintColor: colors.text,
            headerTitleStyle: { fontFamily: 'SpaceGrotesk_500Medium' },
            headerShadowVisible: false,
            contentStyle: { backgroundColor: colors.bg },
            animation: 'fade_from_bottom',
          }}
        >
          <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
          <Stack.Screen name="settings/index" options={{ title: 'Configurações' }} />
          <Stack.Screen name="settings/voice" options={{ title: 'Voz e fala' }} />
          <Stack.Screen name="settings/connection" options={{ title: 'Conexão com o PC' }} />
          <Stack.Screen name="settings/storage" options={{ title: 'Dados e privacidade' }} />
          <Stack.Screen name="settings/diagnostics" options={{ title: 'Diagnóstico' }} />
          <Stack.Screen name="pair" options={{ title: 'Vincular computador', presentation: 'modal' }} />
          <Stack.Screen name="history" options={{ title: 'Conversa' }} />
          <Stack.Screen name="memory/[id]" options={{ title: 'Memória' }} />
          <Stack.Screen name="document/[id]" options={{ title: 'Documento' }} />
          <Stack.Screen name="reference/[chunkId]" options={{ title: 'Referência' }} />
          <Stack.Screen name="share" options={{ title: 'Enviar ao MARVIN', presentation: 'modal' }} />
        </Stack>
      </SafeAreaProvider>
    </GestureHandlerRootView>
  );
}
