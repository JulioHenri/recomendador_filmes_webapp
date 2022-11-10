import pickle

from flask import Flask, render_template, request

app = Flask(__name__)

file = open(
    r'C:\Users\julio\OneDrive\Área de Trabalho\deploy_ml_project\deploy\model.pkl', 'rb')
codedata = pickle.load(file)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
