from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    frutas = ['Morango', "Uva", "Laranja", "Mamão", "Maçã", "Pera", "Melão", "Abacaxi"]
    return render_template("index.html", frutas=frutas)

@app.route('/sobre')
def sobre():
    notas = [
        {
            "aluno": "Fulano",
            "nota": 5.0
        },
        {
            "aluno": "Beltrano",
            "nota": 6.0
        },
        {
            "aluno": "Aluni",
            "nota": 7.0
        },
        {
            "aluno": "Sicrano",
            "nota": 8.5
        },
        {
            "aluno": "Rodrigo",
            "nota": 9.5
        }
    ]
    return render_template("sobre.html", notas=notas)