FROM ghcr.io/qwertyuiop8899/toastflix-sidecar:latest

USER root
COPY run.py /run.py
ENTRYPOINT []
CMD ["sh", "-c", "exec $(command -v python3 || command -v python) /run.py"]
