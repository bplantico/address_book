from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/addresses')
def addresses_index():
    addresses = [
        {"name": "home",
         "address": "2862 W Long Dr",
         "city": "Littleton",
         "state": "CO",
         "zip": "80120"
         },
        {"name": "school",
         "address": "1331 17th",
         "city": "Denver",
         "state": "CO",
         "zip": "80202"
         }
    ]
    return render_template('addresses_index.html', addresses=addresses)
