import re
from flask import Blueprint, jsonify, current_app, request
from flask_swagger_ui import get_swaggerui_blueprint

DOCS_URL = "/docs"
SPEC_URL = f"{DOCS_URL}/openapi.json"

openapi_bp = Blueprint("openapi_bp", __name__)

TYPE_MAP = {
    "int": {"type": "integer"},
    "float": {"type": "number"},
    "path": {"type": "string"},
    "string": {"type": "string"},
    "uuid": {"type": "string", "format": "uuid"},
}
_param_re = re.compile(r"<(?:(?P<conv>\w+):)?(?P<name>\w+)>")

def _rule_params(rule_str: str):
    params = []
    for m in _param_re.finditer(rule_str):
        conv = (m.group("conv") or "string").lower()
        name = m.group("name")
        schema = TYPE_MAP.get(conv, {"type": "string"})
        params.append({"in": "path", "name": name, "required": True, "schema": schema})
    return params

def _op_obj(path: str, method: str, params):
    tag = path.strip("/").split("/", 1)[0] or "root"
    return {
        "tags": [tag],
        "summary": f"{method.upper()} {path}",
        "parameters": params,
        "responses": {
            "200": {"description": "OK"},
            "201": {"description": "Created"},
            "204": {"description": "No Content"},
            "400": {"description": "Bad Request"},
            "404": {"description": "Not Found"},
            "500": {"description": "Server Error"}
        }
    }

@openapi_bp.route(f"{DOCS_URL}/openapi.json")
def openapi_json():
    paths = {}
    METHODS = {"GET","POST","PUT","PATCH","DELETE"}
    for rule in current_app.url_map.iter_rules():
        if rule.endpoint.startswith("static"):
            continue
        path = str(rule.rule)
        if path.startswith(DOCS_URL):
            continue
        allowed = set(rule.methods or set()) & METHODS
        if not allowed:
            continue
        openapi_path = _param_re.sub(lambda m: "{" + m.group("name") + "}", path)
        params = _rule_params(path)
        op = paths.setdefault(openapi_path, {})
        for m in sorted(allowed):
            op[m.lower()] = _op_obj(openapi_path, m, params)

    scheme = "https" if request.is_secure else "http"
    return jsonify({
        "openapi": "3.0.0",
        "info": {"title": "Project API (auto)" , "version": "1.0.0"},
        "servers": [{"url": f"{scheme}://{request.host}"}],
        "paths": paths
    })

swagger_ui_bp = get_swaggerui_blueprint(DOCS_URL, SPEC_URL, config={"app_name": "Project API (auto)"})
