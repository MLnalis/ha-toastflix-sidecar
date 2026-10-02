import json, os, sys

with open("/data/options.json") as f:
    o = json.load(f)

os.environ["SIDECAR_PUBLIC_URL"] = o.get("public_url") or ""
os.environ["SIDECAR_AUDIO_PROXY"] = o.get("audio_proxy") or ""
os.environ["OFFSET_API_URL"] = o.get("offset_api_url") or ""
os.environ["CORS_ORIGINS"] = o.get("cors_origins") or "*"
os.environ["SIDECAR_CACHE_DIR"] = "/data"

if os.path.isdir("/app"):
    os.chdir("/app")
os.execv(sys.executable, [sys.executable, "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3107"])
