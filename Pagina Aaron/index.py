from flask import Flask, render_template

app = Flask(__name__)

"""
@app.route('/')
def principal():
    return "Bienvenido al sitio web de Aaron / Suscribete"

@app.route('/contacto')
def Contacto():
    return "Aquí podemos ponernos en contacto"
"""
@app.route('/')
def Lit():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
    
    
    