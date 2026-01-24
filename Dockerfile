FROM python:3.11-slim-bookworm

# تعيين مجلد العمل
WORKDIR /app

# نسخ ملف المتطلبات
COPY requirements.txt .

# تثبيت المتطلبات الأساسية
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# تحديث pip وتثبيت المتطلبات
RUN pip3 install --no-cache-dir -U pip \
    && pip3 install --no-cache-dir -U -r requirements.txt

# نسخ جميع الملفات
COPY . .

# تشغيل البوت
CMD ["python3", "-m", "anony"]
