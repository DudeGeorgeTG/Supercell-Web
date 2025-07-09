# 🎮 Supercell JWT Token Generator ⚡

![Supercell Logo](https://supercell.com/images/supercell_logo.png)

A Python script to generate JWT tokens for Supercell's OAuth authentication system. Perfect for game developers working with Supercell APIs! 🏰✨

## 🌟 Features

- 🔐 Generates standards-compliant JWT tokens  
- ⏱️ Automatic timestamp generation (iat/exp)  
- 🔄 Base64URL encoding for all components  
- 🎯 Pre-configured for Supercell's OAuth flow  
- ⏳ 48-hour token validity (172800 seconds)

## 🚀 Quick Start

```bash
python3 supercell_jwt.py
```

## 🧩 Token Structure

### 🔖 Header
```json
{
  "kid": "c75a7f83e933",
  "typ": "JWT",
  "alg": "ES256"
}
```

### 📦 Payload
```json
{
  "sub": "PLAYER_UUID",
  "iss": "scid:oauth:authorize",
  "aud": "scid:oauth:login-1",
  "redirect_uri": "https://supercell.com/oauth/supercell/callback",
  "state": "UNIQUE_STATE",
  "iat": CURRENT_TIMESTAMP,
  "exp": EXPIRATION_TIMESTAMP,
  "scope": "identify identity.connections social.profile social.profile_set_handle"
}
```

## ⚠️ Important Notes

🔴 This is example code only!  
🛡️ **Production use requires**:
- 🔑 Proper cryptographic signing  
- 🆔 Real credentials (`kid`, `sub`, etc.)  
- 🔄 Dynamic state generation  

## 📚 Dependencies

| Library | Usage                  |
|---------|------------------------|
| `json`  | JSON serialization     |
| `base64`| URL-safe encoding      |
| `time`  | Timestamp generation   |
