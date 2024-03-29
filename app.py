from flask import Flask, session,render_template, request, redirect, url_for
from main import Ahorcado

app = Flask(__name__)
app.secret_key = 'GiveUsFullMarksPleaseeeeeeee' 


juego = Ahorcado()

def iniciar_juego():
    juego.iniciar()

    session['palabra']= juego.palabra_adivinar
    session['palabraAhorcado'] = juego.palabra_ahocardo
    session['vidas'] = juego.vidas
    session['incorrectas']=juego.letras_incorrectas

@app.route('/')
def index(): 
 # If the game hasn't started yet, initialize it
    if 'palabra' not in session:
        iniciar_juego()
    
    return render_template('jugar.html',palabra=session['palabra'],palabraAhorcado=session['palabraAhorcado'],vidas=session['vidas'],incorrectas=session['incorrectas'])




@app.route('/adivinar', methods=['POST'])
def adivinar():

    input_user = request.form['input']



    if juego.arriesgar(input_user):
        if juego.gano():
            return render_template("win.html", palabra=session['palabra'])
        
        session['palabraAhorcado'] = juego.palabra_ahocardo
        return redirect(url_for("index"))

    if juego.perdio():
        return render_template("lose.html", palabra=session['palabra'])

    
    session['palabra']= juego.palabra_adivinar
    session['palabraAhorcado'] = juego.palabra_ahocardo
    session['vidas'] = juego.vidas
    session['incorrectas']=juego.letras_incorrectas

    return redirect(url_for("index"))


    
@app.route("/play_again", methods=["GET","POST"])
def play_again():
    iniciar_juego()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()
