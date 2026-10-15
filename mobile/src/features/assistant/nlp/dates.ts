import { fold } from './text.ts';

// Pure pt-BR date expressions for reminders. Returns the matched span so it can be removed from the title.
export interface DateMatch {
  date: Date;
  start: number;
  end: number;
  hasTime: boolean;
}

const NUMBERS: Record<string, number> = {
  um: 1, uma: 1, dois: 2, duas: 2, tres: 3, quatro: 4, cinco: 5, seis: 6, sete: 7, oito: 8, nove: 9, dez: 10,
  onze: 11, doze: 12, quinze: 15, vinte: 20, trinta: 30, quarenta: 40, cinquenta: 50, meia: 0.5,
};
const WEEKDAYS: Record<string, number> = { domingo: 0, segunda: 1, terca: 2, quarta: 3, quinta: 4, sexta: 5, sabado: 6 };
const MONTHS: Record<string, number> = {
  janeiro: 0, fevereiro: 1, marco: 2, abril: 3, maio: 4, junho: 5, julho: 6, agosto: 7, setembro: 8, outubro: 9, novembro: 10, dezembro: 11,
};

function num(value: string): number | null {
  if (/^\d+$/.test(value)) return Number(value);
  return NUMBERS[value] ?? null;
}

const TIME = String.raw`as\s+(\d{1,2})(?:(?::|h|\s*horas?\s*e?\s*)(\d{2}))?(?:\s*(?:h|horas?))?(?:\s+da\s+(manha|tarde|noite))?|ao meio[- ]dia|a meia[- ]noite`;

function applyTime(base: Date, hour: number, minute: number, period?: string): Date {
  let h = hour;
  if (period === 'tarde' || period === 'noite') h = h < 12 ? h + 12 : h;
  if (period === 'manha' && h === 12) h = 0;
  const date = new Date(base);
  date.setHours(h, minute, 0, 0);
  return date;
}

function parseTime(match: RegExpExecArray, offset: number, base: Date): { date: Date; ok: boolean } {
  const text = match[0];
  if (/meio[- ]dia/.test(text)) return { date: applyTime(base, 12, 0), ok: true };
  if (/meia[- ]noite/.test(text)) return { date: applyTime(base, 0, 0), ok: true };
  const hour = Number(match[offset]);
  const minute = match[offset + 1] ? Number(match[offset + 1]) : 0;
  if (hour > 23 || minute > 59) return { date: base, ok: false };
  return { date: applyTime(base, hour, minute, match[offset + 2]), ok: true };
}

export function parseDate(input: string, now: Date = new Date()): DateMatch | null {
  const text = fold(input);

  const relative = new RegExp(String.raw`\b(?:daqui a|daqui|em)\s+(\d+|[a-z]+)\s+(minutos?|min|horas?|dias?)\b|\bdaqui a meia hora\b|\bem meia hora\b`).exec(text);
  if (relative) {
    if (/meia hora/.test(relative[0])) {
      return { date: new Date(now.getTime() + 30 * 60000), start: relative.index, end: relative.index + relative[0].length, hasTime: true };
    }
    const amount = num(relative[1]);
    if (amount != null) {
      const unit = relative[2].startsWith('min') ? 60000 : relative[2].startsWith('hora') ? 3600000 : 86400000;
      return { date: new Date(now.getTime() + amount * unit), start: relative.index, end: relative.index + relative[0].length, hasTime: true };
    }
  }

  const dayWord = new RegExp(String.raw`\b(hoje|amanha|depois de amanha)(?:\s+(?:de\s+manha|a\s+tarde|a\s+noite))?(?:\s+(${TIME}))?`).exec(text);
  if (dayWord) {
    const base = new Date(now);
    if (dayWord[1] === 'amanha') base.setDate(base.getDate() + 1);
    if (dayWord[1] === 'depois de amanha') base.setDate(base.getDate() + 2);
    const timeText = dayWord[2];
    let date = applyTime(base, /tarde/.test(dayWord[0]) ? 15 : /noite/.test(dayWord[0]) ? 20 : 9, 0);
    let hasTime = /manha|tarde|noite/.test(dayWord[0]);
    if (timeText) {
      const time = new RegExp(TIME).exec(timeText);
      if (time) {
        const period = /tarde/.test(dayWord[0]) ? 'tarde' : /noite/.test(dayWord[0]) ? 'noite' : undefined;
        const parsed = parseTime(time, 1, base);
        if (parsed.ok) {
          date = period && !time[3] ? applyTime(base, parsed.date.getHours(), parsed.date.getMinutes(), period) : parsed.date;
          hasTime = true;
        }
      }
    }
    return { date, start: dayWord.index, end: dayWord.index + dayWord[0].length, hasTime };
  }

  const weekday = new RegExp(String.raw`\b(?:na |no |nesta |neste |proxima |proximo )?(domingo|segunda|terca|quarta|quinta|sexta|sabado)(?:-feira| feira)?(?:\s+(${TIME}))?`).exec(text);
  if (weekday) {
    const target = WEEKDAYS[weekday[1]];
    const base = new Date(now);
    let delta = (target - base.getDay() + 7) % 7;
    if (delta === 0) delta = 7;
    base.setDate(base.getDate() + delta);
    let date = applyTime(base, 9, 0);
    let hasTime = false;
    if (weekday[2]) {
      const time = new RegExp(TIME).exec(weekday[2]);
      if (time) {
        const parsed = parseTime(time, 1, base);
        if (parsed.ok) {
          date = parsed.date;
          hasTime = true;
        }
      }
    }
    return { date, start: weekday.index, end: weekday.index + weekday[0].length, hasTime };
  }

  const dayOfMonth = new RegExp(String.raw`\bdia\s+(\d{1,2})(?:\s+de\s+([a-z]+))?(?:\s+(${TIME}))?`).exec(text);
  if (dayOfMonth) {
    const day = Number(dayOfMonth[1]);
    const month = dayOfMonth[2] ? MONTHS[dayOfMonth[2]] : undefined;
    if (day >= 1 && day <= 31 && (dayOfMonth[2] === undefined || month !== undefined)) {
      const base = new Date(now);
      if (month !== undefined) base.setMonth(month, day);
      else base.setDate(day);
      if (base.getTime() < now.getTime() - 86400000) {
        if (month !== undefined) base.setFullYear(base.getFullYear() + 1);
        else base.setMonth(base.getMonth() + 1, day);
      }
      let date = applyTime(base, 9, 0);
      let hasTime = false;
      if (dayOfMonth[3]) {
        const time = new RegExp(TIME).exec(dayOfMonth[3]);
        if (time) {
          const parsed = parseTime(time, 1, base);
          if (parsed.ok) {
            date = parsed.date;
            hasTime = true;
          }
        }
      }
      return { date, start: dayOfMonth.index, end: dayOfMonth.index + dayOfMonth[0].length, hasTime };
    }
  }

  const timeOnly = new RegExp(String.raw`\b(?:${TIME})`).exec(text);
  if (timeOnly) {
    const parsed = parseTime(timeOnly, 1, now);
    if (parsed.ok) {
      let date = parsed.date;
      if (date.getTime() <= now.getTime()) date = new Date(date.getTime() + 86400000);
      return { date, start: timeOnly.index, end: timeOnly.index + timeOnly[0].length, hasTime: true };
    }
  }
  return null;
}

export function formatWhen(date: Date, now: Date = new Date()): string {
  const sameDay = date.toDateString() === now.toDateString();
  const tomorrow = new Date(now);
  tomorrow.setDate(now.getDate() + 1);
  const hm = `${String(date.getHours()).padStart(2, '0')}:${String(date.getMinutes()).padStart(2, '0')}`;
  if (sameDay) return `hoje às ${hm}`;
  if (date.toDateString() === tomorrow.toDateString()) return `amanhã às ${hm}`;
  return `${String(date.getDate()).padStart(2, '0')}/${String(date.getMonth() + 1).padStart(2, '0')} às ${hm}`;
}
