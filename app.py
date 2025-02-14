
from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
#from forms import ContactForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # セキュリティキ

# メール設定（Gmailを使用する場合）
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = '556pluto1102@gmail.com'  # 送信元メール
app.config['MAIL_PASSWORD'] = 'mjiw vkiw lpor xqqh'  # メールパスワード
app.config['MAIL_DEFAULT_SENDER'] = '556pluto1102@gmail.com'


mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')
"""
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    try:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(
            subject=f"お問い合わせ: {name}",
            sender=email,
            recipients=['your_email@gmail.com'],  # 受信するメールアドレス
            body=f"名前: {name}\nメール: {email}\n\n{message}"
        )

        mail.send(msg)
        flash('お問い合わせを送信しました！', 'success')
        return "メール送信成功！"

    except Exception as e:
        print(f"エラー: {e}")  # エラーを表示
        return "メール送信失敗！", 500  # Internal Server Error
"""
if __name__ == '__main__':
    #app.debug = True  # デバッグモード有効化
    #app.run(debug=True)

    #port = int(os.environ.get("PORT", 10000))
    #app.run(host="0.0.0.0", port=port)0
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
