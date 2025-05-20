from flask import Flask, request, jsonify, render_template
from blockchain import Blockchain
from transaction import Transaction
from wallet import create_wallet  # import new function

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chain')
def chain():
    return render_template('chain.html', chain=blockchain.chain)

@app.route('/wallet', methods=['GET', 'POST'])
def wallet():
    message = ''
    if request.method == 'POST':
        sender = request.form['sender']
        recipient = request.form['recipient']
        amount = float(request.form['amount'])
        private = request.form['private']
        tx = Transaction(sender, recipient, amount)
        tx.sign(private)
        if tx.is_valid():
            blockchain.add_transaction(tx)
            message = 'Transaction submitted!'
        else:
            message = 'Invalid transaction signature.'
    return render_template('wallet.html', message=message)

@app.route('/mine', methods=['GET', 'POST'])
def mine():
    message = ''
    if request.method == 'POST':
        miner = request.form['miner']
        blockchain.mine_pending(miner)
        message = 'Block mined and reward sent!'
    return render_template('mine.html', message=message)

@app.route('/create_wallet')
def create_wallet_route():
    private_key, public_key = create_wallet()
    return render_template('create_wallet.html', private=private_key, public=public_key)

if __name__ == '__main__':
    app.run(debug=True)