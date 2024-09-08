from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    tshirts = [
        {"id": 1, "name": "Classic T-shirt", "price": "$20"},
        {"id": 2, "name": "Graphic T-shirt", "price": "$25"},
        {"id": 3, "name": "Vintage T-shirt", "price": "$30"}
    ]
    return render_template('index.html', tshirts=tshirts)

@app.route('/tshirt/<int:tshirt_id>')
def tshirt_detail(tshirt_id):
    tshirts = {
        1: {"name": "Classic T-shirt", "price": "$20", "description": "A classic T-shirt with a simple design."},
        2: {"name": "Graphic T-shirt", "price": "$25", "description": "A T-shirt with a cool graphic design."},
        3: {"name": "Vintage T-shirt", "price": "$30", "description": "A vintage-style T-shirt."}
    }
    tshirt = tshirts.get(tshirt_id)
    return render_template('tshirt_detail.html', tshirt=tshirt)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
