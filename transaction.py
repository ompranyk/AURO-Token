import json
from wallet import sign_message, verify_signature

class Transaction:
    def __init__(self, sender, recipient, amount, signature=None):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature

    def to_dict(self):
        return {'sender': self.sender, 'recipient': self.recipient, 'amount': self.amount}

    def sign(self, private_key):
        msg = json.dumps(self.to_dict(), sort_keys=True)
        self.signature = sign_message(private_key, msg)

    def is_valid(self):
        if self.sender == "SYSTEM":
            return True
        msg = json.dumps(self.to_dict(), sort_keys=True)
        return verify_signature(self.sender, msg, self.signature)