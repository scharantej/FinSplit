
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount = db.Column(db.Float)
    date = db.Column(db.Date)

class PaymentRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount = db.Column(db.Float)
    status = db.Column(db.String(120))

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/sync', methods=['POST'])
def sync():
    # Retrieve and store transaction data in the database
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    transactions = Transaction.query.all()
    payment_requests = PaymentRequest.query.all()
    return render_template('dashboard.html', transactions=transactions, payment_requests=payment_requests)

@app.route('/split', methods=['POST'])
def split():
    # Split payments and send notifications
    return redirect(url_for('dashboard'))

@app.route('/request', methods=['POST'])
def request():
    # Accept or decline payment requests
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run()
