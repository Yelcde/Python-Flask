from flask import Flask, render_template, request

app = Flask(__name__)

frutas = []

@app.route('/', methods=["GET", "POST"])
def principal():
    # frutas = ['Morango', "Uva", "Laranja", "Mamão", "Maçã", "Pera", "Melão", "Abacaxi"]

    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
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