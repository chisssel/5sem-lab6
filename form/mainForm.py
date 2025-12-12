from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', 'Гость')
    return f"<h1>Привет, {name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)