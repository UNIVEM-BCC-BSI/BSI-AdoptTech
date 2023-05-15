from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/post_login", methods=["POST"])
def post_login():
    # Processar os dados do formulário de login aqui
    email = request.form.get("email")
    password = request.form.get("password")
    # Redirecionar para a página do usuário logado
    return render_template('user.html', email=email)

if __name__ == "__main__":
    app.run()

