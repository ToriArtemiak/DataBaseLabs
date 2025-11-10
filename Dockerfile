FROM python:3.11-slim

WORKDIR /app

COPY . /app/

RUN python - <<'PY'
import os, re

def patch(path, patterns):
    try:
        s = open(path, 'r', encoding='utf-8', errors='replace').read()
    except FileNotFoundError:
        return
    for a,b in patterns:
        s = re.sub(a, b, s)
    open(path, 'w', encoding='utf-8').write(s)

for f in ("wsgi.py", "app.py"):
    if os.path.exists(f):
        patch(f, [(r'from app import create_app', 'from __init__ import create_app')])

for root, _, files in os.walk("."):
    for name in files:
        if name.endswith(".py"):
            p = os.path.join(root, name)
            txt = open(p, 'r', encoding='utf-8', errors='replace').read()
            if "from app." in txt or "import app." in txt:
                patch(p, [
                    (r'from app\.root', 'from root'),
                    (r'from app\.controllers', 'from controllers'),
                    (r'from app\.dao', 'from dao'),
                    (r'from app\.domain', 'from domain'),
                    (r'from app\.service', 'from service'),
                ])

if os.path.exists("root/__init__.py"):
    patch("root/__init__.py", [(r'from app\.root\.error_handler', 'from .error_handler')])
PY

RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn

EXPOSE 8000
ENV PORT=8000

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "wsgi:app"]
