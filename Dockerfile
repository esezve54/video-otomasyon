# Temel imaj
FROM python:3.11-slim

WORKDIR /app

# Gereksinimleri yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kodları kopyala
COPY . .

# Port ayarı
EXPOSE 5000

# Uygulamayı başlat
CMD ["python", "app.py"]
