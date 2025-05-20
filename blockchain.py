from block import Block
from transaction import Transaction

class Blockchain:
    def __init__(self, difficulty=4, reward=50, halving_interval=10):
        self.difficulty = difficulty
        self.reward = reward
        self.chain = [self.create_genesis_block()]
        self.pending = []
        self.halving_interval = halving_interval

    def create_genesis_block(self):
        genesis = Transaction("SYSTEM", "network", 100)
        return Block(0, [genesis], "0", self.difficulty)

    def add_transaction(self, tx):
        if not tx.is_valid():
            raise Exception("Invalid transaction")
        self.pending.append(tx)

    def mine_pending(self, miner_address):
        reward_tx = Transaction("SYSTEM", miner_address, self.reward)
        block = Block(len(self.chain), self.pending + [reward_tx], self.chain[-1].hash, self.difficulty)
        block.mine()
        self.chain.append(block)
        self.pending = []

        # Halve reward every halving_interval blocks
        if len(self.chain) % self.halving_interval == 0:
            self.reward = max(1, self.reward / 2)

    def is_valid_chain(self):
        for i in range(1, len(self.chain)):
            if self.chain[i].hash != self.chain[i].compute_hash():
                return False
            if self.chain[i].previous_hash != self.chain[i-1].hash:
                return False
        return True

    def last_block(self):
        return self.chain[-1]