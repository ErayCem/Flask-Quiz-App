from app import app
from models import db, Question

def add_questions():
    with app.app_context():
        questions = [
            Question(
                text="Discord botu başlatmak için kullanılan metot hangisidir?",
                option_a="start", option_b="run", option_c="launch", option_d="connect",
                correct_option="B", category="Discord.py"
            ),
            Question(
                text="Flask'ta bir rota tanımlamak için hangi dekoratör kullanılır?",
                option_a="@route", option_b="@flask.route", option_c="@app.route", option_d="@web.route",
                correct_option="C", category="Flask"
            ),
            Question(
                text="Yapay zeka modelinin eğitilmesinde kullanılan veri nedir?",
                option_a="Yapı taşı", option_b="Kod", option_c="Eğitim verisi", option_d="Doğal dil",
                correct_option="C", category="Yapay Zeka"
            ),
            Question(
                text="TensorFlow hangi alanla ilgilidir?",
                option_a="Web tasarımı", option_b="Veritabanı yönetimi", option_c="Bilgisayarla Görü", option_d="Sunucu kurulumu",
                correct_option="C", category="Computer Vision"
            ),
            Question(
                text="NLTK kütüphanesi ne için kullanılır?",
                option_a="Resim işleme", option_b="Doğal Dil İşleme", option_c="Web geliştirme", option_d="Veritabanı yönetimi",
                correct_option="B", category="NLP"
            ),
            # Yeni eklenen 5 soru
            Question(
                text="Discord.py'de bir mesaj yanıtlamak için hangi metot kullanılır?",
                option_a="message.reply()", option_b="ctx.send()", option_c="channel.response()", option_d="bot.answer()",
                correct_option="A", category="Discord.py"
            ),
            Question(
                text="Flask'ta dinamik URL parametresi nasıl tanımlanır?",
                option_a="/user/<username>", option_b="/user/{username}", option_c="/user/:username", option_d="/user/[username]",
                correct_option="A", category="Flask"
            ),
            Question(
                text="BeautifulSoup kütüphanesi genellikle ne için kullanılır?",
                option_a="Web scraping", option_b="Veri analizi", option_c="Makine öğrenimi", option_d="Veritabanı yönetimi",
                correct_option="A", category="Web Geliştirme"
            ),
            Question(
                text="ImageAI kütüphanesi hangi tür modeller sağlar?",
                option_a="Nesne tanıma", option_b="Metin sınıflandırma", option_c="Ses işleme", option_d="Veri temizleme",
                correct_option="A", category="Computer Vision"
            ),
            Question(
                text="NLTK ile bir metni kelimelere ayırmak için hangi metot kullanılır?",
                option_a="word_tokenize()", option_b="text_split()", option_c="break_text()", option_d="analyze_words()",
                correct_option="A", category="NLP"
            )
        ]
        db.session.add_all(questions)
        db.session.commit()
        print(f"{len(questions)} soru başarıyla eklendi.")


if __name__ == '__main__':
    add_questions()