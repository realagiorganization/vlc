FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    DISPLAY=:0

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    ffmpeg \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    libxrender1 \
    libxshmfence1 \
    libxss1 \
    libxtst6 \
    python3 \
    python3-pip \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /repo

COPY test/bdd/requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt \
    && python3 -m playwright install --with-deps chromium

COPY test/bdd /repo/test/bdd
COPY scripts/run-bdd.sh /usr/local/bin/run-bdd
RUN chmod +x /usr/local/bin/run-bdd

ENTRYPOINT ["/usr/local/bin/run-bdd"]
