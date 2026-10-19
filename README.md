# Cyber Security Base Demonstration Project

A small Django "private notes" application built for educational purposes. It deliberately contains five security flaws from the OWASP Top 10 (2021). Each flaw is marked in the source code with a `# FLAW n` comment, and the corresponding fix is included next to it as commented-out code (`# FIX n`).



## Flaws included

| # | OWASP category | Where to look |
|---|----------------|---------------|
| 1 | A01: Broken Access Control | `core/views.py`: `note_detail`, `note_delete` |
| 2 | A02: Cryptographic Failures | `core/hashers.py`, `config/settings.py`: `PASSWORD_HASHERS`, `SECRET_KEY` |
| 3 | A03: Injection | `core/views.py`: `search` |
| 4 | A07: Identification and Authentication Failures | `core/views.py`: `login_view`, `config/settings.py`: `AUTH_PASSWORD_VALIDATORS`, `SESSION_COOKIE_AGE` |
| 5 | A09: Security Logging and Monitoring Failures | `core/views.py` (`login_view`, `note_delete`), `config/settings.py`: `LOGGING` |



## Requirements

- Python 3.12 or newer
- Git
- On Debian/Ubuntu, the venv package: `sudo apt install python3-venv`

## Getting started

### 1. Clone the repository


### 2. Create and activate a virtual environment

Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```


### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the database

The SQLite database is not part of the repository, so create it:

```bash
python manage.py migrate
```

### 5. Start the server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser. You will be redirected to the login page.




## Also, just in case if the port 8000 does not work for you:


- **Port 8000 already in use**: `python manage.py runserver 8001`.