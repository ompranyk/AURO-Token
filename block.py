import hashlib, time, json

class Block:
    def __init__(self, index, transactions, previous_hash, difficulty):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.difficulty = difficulty
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        data = {
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': [tx.__dict__ for tx in self.transactions],
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }
        return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

    def mine(self):
        while not self.hash.startswith('0' * self.difficulty):
            self.nonce += 1
            self.hash = self.compute_hash()