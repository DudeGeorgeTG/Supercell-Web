import json
import base64
import time

def base64url_encode(data):
    json_str = json.dumps(data, separators=(',', ':'))  
    return base64.urlsafe_b64encode(json_str.encode()).decode().rstrip('=')

def gen_auth():
    header = {
        "kid": "c75a7f83e933",
        "typ": "JWT",
        "alg": "ES256"
    }

    current_time = int(time.time())
    expiration_time = current_time + 172800  

    payload = {
        "sub": "10DE8EFA-758A-4D81-8BB9-2EE86E847DB2",
        "iss": "scid:oauth:authorize",
        "aud": "scid:oauth:login-1",
        "redirect_uri": "https://supercell.com/oauth/supercell/callback",
        "state": "213d1a6a-8fed-4789-a87f-40345d04ada8.en",
        "iat": current_time,  # time rn
        "exp": expiration_time,  # time when token expires (after 2 days)
        "scope": "identify identity.connections social.profile social.profile_set_handle"
    }

    encoded_header = base64url_encode(header)
    encoded_payload = base64url_encode(payload)

    signature = "kL4OL0Dq7Pb9xDdjJthiInBz5R8wUWPmf_QvyQJF-3FenEA5gSkcgiOusNXAt2KOffGBwtYoEyLDsiYGgBLD4Q"
    jwt = f"{encoded_header}.{encoded_payload}.{signature}"
    return jwt 

print(gen_auth())
