"""Explicit search providers with bounded requests and a short lived result cache."""
import json
import os
import threading
import time
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen

_cache = {}
_lock = threading.Lock()


def search_web(query, provider=None):
    provider = provider or os.getenv('MARVIN_SEARCH_PROVIDER', 'google')
    query = query.strip()[:400]
    if not query:
        raise ValueError('Informe o assunto da pesquisa.')
    key = (provider, query, os.getenv('SEARXNG_URL', ''))
    with _lock:
        saved = _cache.get(key)
        if saved and time.monotonic()-saved[0]<120:
            return [dict(row) for row in saved[1]]
    headers = {'Accept': 'application/json', 'User-Agent': 'MARVIN/0.7'}
    if provider == 'brave':
        token = os.getenv('BRAVE_SEARCH_API_KEY', '').strip()
        if not token:
            raise ValueError('Configure BRAVE_SEARCH_API_KEY no .env. Brave usa cotas do seu plano.')
        url = 'https://api.search.brave.com/res/v1/web/search?' + urlencode({'q':query, 'count':5, 'search_lang':'pt-br'})
        headers['X-Subscription-Token'] = token
    elif provider == 'searxng':
        base = os.getenv('SEARXNG_URL', '').rstrip('/')
        parsed = urlsplit(base)
        if parsed.scheme not in ('http','https') or not parsed.hostname or parsed.username or parsed.password:
            raise ValueError('Configure SEARXNG_URL para sua instância com a API JSON habilitada.')
        url = base+'/search?' + urlencode({'q':query, 'format':'json', 'language':'pt-BR'})
    else:
        raise ValueError('Pesquisa Google é executada pela integração Gemini com fontes.')
    with urlopen(Request(url, headers=headers), timeout=12) as response:
        raw = response.read(512001)
    if len(raw)>512000:
        raise ValueError('Resposta de pesquisa excedeu o limite.')
    payload = json.loads(raw)
    rows = payload.get('web', {}).get('results', []) if provider=='brave' else payload.get('results', [])
    results = []
    for row in rows[:5]:
        url = row.get('url','')
        if urlsplit(url).scheme in ('http','https'):
            results.append({'title':str(row.get('title',url))[:250], 'url':url[:4096],
                            'snippet':str(row.get('description',row.get('content','')))[:1800]})
    with _lock:
        if len(_cache)>100:
            _cache.clear()
        _cache[key] = (time.monotonic(), results)
    return results
