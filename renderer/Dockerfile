FROM python:3.11-slim

# Устанавливаем зависимости для PyOpenGL + pygame с поддержкой X11
RUN apt-get update && apt-get install -y \
    python3-pygame \
    libgl1-mesa-glx \
    libglu1-mesa \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY renderer.py .

CMD ["python", "renderer.py"]