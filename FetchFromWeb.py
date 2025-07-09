import requests
from urllib.parse import urlparse, parse_qs
import json

def get_build_id(session):
    try:
        r = session.get(
            "https://store.supercell.com/",
            timeout=10,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
            }
        )
        r.raise_for_status()
        
        build_id_part = r.text.split('"buildId":"')[1]
        build_id = build_id_part.split('"')[0]
        
        if not build_id or len(build_id) < 10: 
            raise ValueError("Invalid build ID format")
            
        return build_id
        
    except Exception as e:
        return None

def get_redirect_url(session, build_id):
    if not build_id:
        return None
        
    try:
        url = f"https://store.supercell.com/_next/data/{build_id}/en/oauth/begin.json"
        
        r = session.get(
            url,
            params={'redirectUri': '/'},
            timeout=10,
            headers={
                'Referer': 'https://store.supercell.com/',
                'Accept': 'application/json'
            }
        )
        r.raise_for_status()
        
        data = r.json()
        
        if not data.get('pageProps', {}).get('__N_REDIRECT'):
            raise ValueError("No redirect URL in response")
            
        return data['pageProps']['__N_REDIRECT']
        
    except Exception as e:
        return None

def get_auth_token(session, redirect_url):
    if not redirect_url:
        return None
        
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml',
            'Referer': 'https://store.supercell.com/',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'navigate',
        }
        
        r = session.get(
            redirect_url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )
        
        if not 300 <= r.status_code < 400:
            raise ValueError(f"Expected redirect status, got {r.status_code}")
            
        location = r.headers.get('Location')
        if not location:
            raise ValueError("No Location header in redirect response")
          # Parse token from URL
        parsed = urlparse(location)
        query = parse_qs(parsed.query)
        
        token = query.get('token', [None])[0]
        if not token or len(token) < 300:  
            raise ValueError("Invalid or missing token in redirect URL")
            
        return token
        
    except Exception as e:
        return None

def gen_auth():
    with requests.Session() as session:
        session.headers.update({
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
        })
        
        build_id = get_build_id(session)
        if not build_id:
            return

        redirect_url = get_redirect_url(session, build_id)
        if not redirect_url:
            return

        token = get_auth_token(session, redirect_url)
        
        if token:
            return token


print(gen_auth())
