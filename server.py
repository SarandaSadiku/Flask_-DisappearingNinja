from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    ninja='all'
    return render_template('ninja.html',ninja=ninja)

@app.route('/ninja/<ninja_color>')
def color(ninja_color):
    ninja = {'blue':'leonardo','orange':'michelangelo','red':'raphael', 'purple':'donatello'}
    if ninja_color in ninja:
        ninja = ninja[ninja_color]
    else:
        ninja='megan'
    return render_template('ninja.html',ninja=ninja)

app.run(debug=True)
