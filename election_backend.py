import datetime
import hashlib
import random
from Crypto.Hash import SHA3_256

class Transaction:
    def __init__(self, voter_id, candidate_choice):
        self.voter_id = voter_id
        self.candidate_choice = candidate_choice

    def __str__(self):
        return f"Voter ID: {self.voter_id}, Vote for Candidate: {self.candidate_choice}"

class Blockchain:
    def __init__(self):
        self.chain = []
        self.candidates = ["Candidate A", "Candidate B", "Candidate C"]
        self.vote_counts = {candidate: 0 for candidate in self.candidates}
        self.admin_account = "admin"
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = self.create_block(prev_hash='0', transactions=[], candidates=self.candidates)
        self.chain.append(genesis_block)

    def create_block(self, prev_hash, transactions, candidates):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': datetime.datetime.now(),
            'prev_hash': prev_hash,
            'transactions': transactions,
            'candidates': candidates,
            'nonce': 0
        }
        return block

    def create_block_with_transactions(self, prev_hash, transactions):
        new_block = self.create_block(prev_hash, transactions, self.candidates)
        new_block = self.proof_of_work(new_block)
        self.chain.append(new_block)
        return new_block

    def proof_of_work(self, block):
        while True:
            block['nonce'] += 1
            block_hash = self.calculate_hash(block)
            if block_hash.startswith('0000'):
                return block

    def is_admin(self, account):
        return account == self.admin_account

    def record_vote(self, transaction):
        prev_hash = self.chain[-1]['prev_hash']
        if self.verify_transaction(transaction):
            new_block = self.create_block_with_transactions(prev_hash, [transaction])
            self.vote_counts[transaction.candidate_choice] += 1
            print(f"New block added to the blockchain: {new_block}")
            return True
        else:
            print("Invalid transaction.")
            return False

    def verify_transaction(self, transaction):
        # Implement transaction verification logic here
        return True

    def get_vote_counts(self):
        return self.vote_counts

    def get_transactions(self):
        transactions = []
        for block in self.chain:
            transactions.extend(block['transactions'])
        return transactions

    def print_blocks(self):
        for block in self.chain:
            print(f"Block {block['index']}:")
            print(f"Timestamp: {block['timestamp']}")
            print(f"Previous Hash: {block['prev_hash']}")
            print("Transactions:")
            for transaction in block['transactions']:
                print(f"  {transaction}")
            print(f"Hash: {self.calculate_hash(block)}")
            print()

    def calculate_hash(self, block):
        block_string = str(block['index']) + str(block['timestamp']) + str(block['prev_hash']) + str(block['transactions']) + str(block['candidates']) + str(block['nonce'])
        return SHA3_256.new(block_string.encode()).hexdigest()

class Backend:
    def __init__(self):
        self.blockchain = Blockchain()

    def record_vote(self, transaction):
        self.blockchain.record_vote(transaction)

    def print_blocks(self):
        self.blockchain.print_blocks()

if __name__ == "__main__":
    backend = Backend()
    backend.print_blocks()