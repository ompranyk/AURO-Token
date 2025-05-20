# AURO-Token
# AURA - Simple Cryptocurrency with Python & Flask

This project is a basic cryptocurrency simulation inspired by Bitcoin.  
It includes a Proof-of-Work blockchain, transaction signing, mining rewards with halving, and a Flask web interface.

---

## Features

- Blockchain with Proof-of-Work consensus (adjustable difficulty)
- Transactions signed with ECDSA keys (using `ecdsa` Python library)
- Mining rewards with halving every 10 blocks
- Wallet key pair generation (private/public keys)
- Web GUI for:
  - Viewing blockchain
  - Creating wallets
  - Sending transactions
  - Mining blocks

---

## Installation

Make sure you have Python 3 installed.

Install dependencies:

```bash
pip install flask ecdsa
