from flask import Flask, render_template, request, redirect, url_for, session
import os
from datetime import datetime
import base64

app = Flask(__name__)
app.secret_key = 'supersecretkey'

COMMENTS = [
    "Infelizmente, ainda vemos muito preconceito em várias religiões.",
    "Precisamos de mais respeito e compreensão entre as crenças.",
    "A intolerância religiosa destrói comunidades. Precisamos agir!"
]

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'SAMUELQ' and password == 'Martins2025':
            session['logged_in'] = True
            return redirect(url_for('blog'))
    return render_template('login.html')

@app.route('/blog', methods=['GET', 'POST'])
def blog():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        comment = request.form['comment']
        COMMENTS.append(comment)
        image_data = request.form['image_data']
        if image_data:
            header, encoded = image_data.split(",", 1)
            data = base64.b64decode(encoded)
            filename = datetime.now().strftime("photo_%Y%m%d_%H%M%S.png")
            with open(filename, "wb") as f:
                f.write(data)
    return render_template('blog.html', comments=COMMENTS)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)
