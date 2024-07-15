pip install flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing_page():
    # Dados da empresa e curso
    nome_empresa = "Ski na Neve Inc."
    curso = "Curso Avançado de Ski na Neve"
    descricao_curso = "Aprenda técnicas avançadas de ski na neve com instrutores experientes."

    return render_template('landing_page.html', nome_empresa=nome_empresa, curso=curso, descricao_curso=descricao_curso)

if __name__ == '__main__':
    app.run(debug=True)
