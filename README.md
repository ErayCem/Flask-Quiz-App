# 🧠 Flask Quiz App

Bu proje, Flask framework'ü kullanılarak geliştirilmiş basit ve işlevsel bir çoktan seçmeli sınav (quiz) uygulamasıdır. Kullanıcılar soruları cevaplayarak puan alır ve sistem hem kullanıcının en yüksek skorunu hem de tüm kullanıcılar arasındaki en yüksek skoru takip eder.

## 🚀 Özellikler

- 📋 Çoktan seçmeli sınav yapısı  
- 🧑‍💻 Kullanıcı bazlı skor takibi  
- 🎨 Temel CSS ile kullanıcı dostu arayüz

## 🛠️ Kullanılan Teknolojiler

- Python (Flask)
- SQLite (veritabanı)
- HTML / CSS

⚠️ Uyarı
Aynı kullanıcı adını birden fazla kişi kullanmamalıdır. Aksi halde skorlar çakışabilir.

## 🔧 Kurulum

1. Depoyu klonlayın:

```bash
git clone https://github.com/ErayCem/Flask-Quiz-App.git
cd quiz-app

2. Sanal ortam oluşturun (opsiyonel ama önerilir)
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

3. Gerekli Paketleri Yükle

pip install -r requirements.txt

requirements.txt yoksa el ile yükleyebilirsin:

pip install flask flask_sqlalchemy

4. Veritabanını Oluştur
Python terminaline gir ve aşağıdaki komutları çalıştır:
from models import db
from app import app

with app.app_context():
    db.create_all()

Bu işlem exam.db adlı bir veritabanı dosyası oluşturur.

5. Uygulamayı Başlat
python app.py
Tarayıcında http://127.0.0.1:5000/ adresini açarak uygulamayı kullanmaya başlayabilirsin.

