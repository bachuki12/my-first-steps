from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def mainpg():
    return render_template("main.pg.html")

@app.route("/Authorization")
def Authorization():
    return render_template("Authorization.html")

@app.route("/Registracion")
def Registracion():
    return render_template("Registracion.html")

if __name__=="__main__":
    app.run(debug=True)