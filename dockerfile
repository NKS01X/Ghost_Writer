FROM ubuntu:24.04

WORKDIR /app
COPY . /app

RUN apt-get update && \
    apt-get install -y python3 python3-pip nodejs npm git curl && \
    rm -rf /var/lib/apt/lists/*

RUN if [ -f "package.json" ]; then \
    npm install; \
    elif [ -f "requirements.txt" ]; then \
    pip3 install --break-system-packages --no-cache-dir -r requirements.txt; \
    fi

CMD ["/bin/bash", "-c", "\
    if [ -f 'package.json' ]; then \
    npm test; \
    elif [ -f 'requirements.txt' ]; then \
    python3 -m pytest tests/ -v; \
    else \
    for file in tests/*.py; do python3 \"$file\"; done; \
    fi"]