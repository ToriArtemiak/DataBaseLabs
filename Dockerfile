FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    pip install --no-cache-dir gunicorn pymysql

COPY . /app/

RUN python - <<'PY'
import os, re, io

def patch(path, rules):
    try:
        s = io.open(path, 'r', encoding='utf-8', errors='replace').read()
    except FileNotFoundError:
        return
    orig = s
    for a,b in rules:
        s = re.sub(a, b, s, flags=re.M)
    if s != orig:
        io.open(path, 'w', encoding='utf-8').write(s)

for pkg in ["controllers","dao","domain","service","root"]:
    d = os.path.join("/app", pkg)
    if os.path.isdir(d):
        init_p = os.path.join(d, "__init__.py")
        if not os.path.exists(init_p):
            open(init_p, "w").close()

for f in ["/app/wsgi.py", "/app/app.py"]:
    if os.path.exists(f):
        patch(f, [
            (r'from\s+app\s+import\s+create_app', 'from __init__ import create_app'),
        ])

if os.path.exists("/app/wsgi.py"):
    patch("/app/wsgi.py", [
        (r'(^\s*app\s*=\s*create_app\(\)\s*$)', 'import os\n\\1'),
        (r'port\s*=\s*8010', 'port=int(os.getenv("PORT","8000"))'),
    ])

for root, _, files in os.walk("/app"):
    for name in files:
        if name.endswith(".py"):
            p = os.path.join(root, name)
            patch(p, [
                (r'\bfrom\s+app\.root\b', 'from root'),
                (r'\bfrom\s+app\.controllers\b', 'from controllers'),
                (r'\bfrom\s+app\.dao\b', 'from dao'),
                (r'\bfrom\s+app\.domain\b', 'from domain'),
                (r'\bfrom\s+app\.service\b', 'from service'),
                (r'\bimport\s+app\.root\b', 'import root'),
                (r'\bimport\s+app\.controllers\b', 'import controllers'),
                (r'\bimport\s+app\.dao\b', 'import dao'),
                (r'\bimport\s+app\.domain\b', 'import domain'),
                (r'\bimport\s+app\.service\b', 'import service'),
            ])

for r, _, files in os.walk("/app/root"):
    for name in files:
        if name.endswith(".py"):
            p = os.path.join(r, name)
            patch(p, [
                (r'^from\s+\.\.controllers\s+import\s+', 'from controllers import '),
                (r'^from\s+\.\.service\s+import\s+',     'from service import '),
                (r'^from\s+\.\.dao\s+import\s+',         'from dao import '),
                (r'^from\s+\.\.domain\s+import\s+',      'from domain import '),
            ])

f = "/app/root/__init__.py"
if os.path.exists(f):
    patch(f, [(r'from\s+app\.root\.error_handler', 'from .error_handler')])
PY

ENV PORT=8000
EXPOSE 8000

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "wsgi:app"]
