import os

from flask import Flask, render_template, request

from model import Model, get_model

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['text']
        model = get_model()
        word = model.predict(input_text)
        return render_template('result.html', input_text=input_text, result=word)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
