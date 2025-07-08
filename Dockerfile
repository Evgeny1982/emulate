FROM ubuntu:22.04

# Установим зависимости
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-uinput \
    udev \
    && rm -rf /var/lib/apt/lists/*

# Копируем скрипт
WORKDIR /app
COPY emulator.py ./
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt || true  # на случай если пустой

CMD ["python3", "emulator.py"]
