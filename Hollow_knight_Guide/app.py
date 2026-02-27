from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(): return render_template('index.html')

@app.route('/charms')
def charms(): return render_template('charms.html')

@app.route('/slots')
def slots(): return render_template('slots.html')

@app.route('/vessels')
def vessels(): return render_template('vessels.html')

@app.route('/masks')
def masks(): return render_template('masks.html')

@app.route('/endings')
def endings(): return render_template('endings.html')

@app.route('/enemies')
def enemies(): return render_template('enemies.html')

@app.route('/abilities')
def abilities(): return render_template('abilities.html')

if __name__ == '__main__':
    app.run(debug=True)