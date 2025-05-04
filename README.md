İşte GitHub `README.md` dosyasına **doğrudan yapıştırılabilir** ve **düzenli biçimde görünen** sürüm — metin ve kod blokları düzgün şekilde ayrılmıştır:

````markdown
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

> ⚠️ **Uyarı:**  
> Aynı kullanıcı adını birden fazla kişi kullanmamalıdır. Aksi halde skorlar çakışabilir.

---

## 🔧 Kurulum

### 1. Depoyu klonlayın:

```bash
git clone https://github.com/ErayCem/Flask-Quiz-App.git
cd quiz-app
````

### 2. Sanal ortam oluşturun (opsiyonel ama önerilir)

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. Gerekli Paketleri Yükleyin

```bash
pip install -r requirements.txt
```

Eğer `requirements.txt` yoksa elle yükleyebilirsiniz:

```bash
pip install flask flask_sqlalchemy
```

### 4. Veritabanını Oluşturun

Python terminalini açıp aşağıdaki komutları çalıştırın:

```python
from models import db
from app import app

with app.app_context():
    db.create_all()
```

> Bu işlem `exam.db` adlı bir veritabanı dosyası oluşturur.

### 5. Uygulamayı Başlatın

```bash
python app.py
```

Tarayıcınızda şu adresi açarak uygulamayı kullanmaya başlayabilirsiniz:

```
http://127.0.0.1:5000/
```

```

Yukarıdaki metni GitHub `README.md` kısmına yapıştırdığında hem metin hem kodlar doğru şekilde görünecektir. Başka açıklama veya görsel eklemek ister misin?
```
