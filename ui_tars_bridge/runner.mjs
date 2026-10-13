/** MARVIN -> SDK oficial UI-TARS (não inclui modelo VLM). */
const prefix = 'MARVIN_EVENT:';
function emit(type, message) {
  process.stdout.write(prefix + JSON.stringify({ type, message }) + '\n');
}
const task = process.argv[2] || '';
const baseURL = process.env.UI_TARS_BASE_URL;
const model = process.env.UI_TARS_MODEL;
const apiKey = process.env.UI_TARS_API_KEY || 'local';
const maxLoopCount = Math.min(25, Math.max(1, Number(process.env.UI_TARS_MAX_STEPS || 10)));
if (!task.trim() || !baseURL || !model) {
  emit('error', 'Informe tarefa, UI_TARS_BASE_URL e UI_TARS_MODEL.');
  process.exitCode = 2;
} else {
  try {
    // Import dinâmico evita erro de resolução antes de mostrar erro de configuração.
    const [{ GUIAgent }, { NutJSOperator }] = await Promise.all([
      import('@ui-tars/sdk'), import('@ui-tars/operator-nut-js')
    ]);
    const abortController = new AbortController();
    process.on('SIGINT', () => abortController.abort());
    let hitStepLimit = false;
    const guiAgent = new GUIAgent({
      model: { baseURL, apiKey, model },
      operator: new NutJSOperator(),
      signal: abortController.signal,
      maxLoopCount,
      onData: ({ data }) => {
        // Nunca transmitir base64 das capturas da tela para o log do MARVIN.
        const status = String(data?.status ?? 'RUNNING');
        if (status.toUpperCase().includes('MAX_LOOP')) hitStepLimit = true;
        emit('progress', 'UI-TARS: ' + status);
      },
      onError: ({ error }) => {
        emit('error', String(error?.message ?? error).slice(0, 260));
      },
    });
    emit('progress', 'Iniciando agente visual...');
    await guiAgent.run(task);
    if (hitStepLimit) {
      emit('error', 'Limite de passos atingido: confira a tela antes de continuar.');
      process.exitCode = 3;
    } else {
      emit('complete', 'O agente encerrou a execução; confirme o resultado na tela.');
    }
  } catch (error) {
    emit('error', String(error?.message ?? error).slice(0, 400));
    console.error(String(error?.stack ?? error).slice(0, 2500));
    process.exitCode = 1;
  }
}
