# election_frontend.py
import hmac
import hashlib
import random
import secrets
from getpass import getpass
from Crypto.Hash import SHA3_256
from election_backend import Transaction, Backend

class UserInterface:
    def __init__(self, backend):
        self.backend = backend
        self.users_database = {}
        self.challenges = {}

    def register_voter(self, voter_id, password):
        salt = secrets.token_hex(16)
        secret_key = SHA3_256.new((voter_id + password + salt).encode()).hexdigest()
        self.users_database[voter_id] = {
            "secret_key": secret_key,
            "salt": salt
        }
        print(f"Voter {voter_id} registered successfully.")
        print(f"Salt: {salt}")
        # print(f"Secret Key: {secret_key}")
        print()

    def generate_challenge(self, voter_id):
        challenge = secrets.token_hex(16)
        self.challenges[voter_id] = challenge
        print(f"Generated Challenge for {voter_id}: {challenge}")
        print()
        return challenge

    def verify_hmac(self, voter_id, received_bit, received_hmac):
        if voter_id not in self.users_database or voter_id not in self.challenges:
            return False

        secret_key = self.users_database[voter_id]["secret_key"]
        salt = self.users_database[voter_id]["salt"]
        challenge = self.challenges[voter_id]

        expected_hmac = hmac.new(secret_key.encode(), (challenge + received_bit).encode(), hashlib.sha256).hexdigest()

        print(f"Verifying HMAC for {voter_id}:")
        print(f"Challenge: {challenge}")
        print(f"Received Bit: {received_bit}")
        print(f"Received HMAC: {received_hmac}")
        print(f"Expected HMAC: {expected_hmac}")
        print()

        if not hmac.compare_digest(expected_hmac, received_hmac):
            return False

        del self.challenges[voter_id]
        return True

    def login(self):
        voter_id = input("Enter your voter ID: ")
        password = getpass("Enter your password: ")

        if voter_id not in self.users_database:
            print("Voter not registered. Please register first.")
            return None

        secret_key = self.users_database[voter_id]["secret_key"]
        salt = self.users_database[voter_id]["salt"]

        # Verify the password
        entered_secret_key = SHA3_256.new((voter_id + password + salt).encode()).hexdigest()
        if entered_secret_key != secret_key:
            print("Invalid credentials. Please try again.")
            return None

        challenge = self.generate_challenge(voter_id)
        print(f"Challenge sent to voter: {challenge}")

        verifier_bit = secrets.token_hex(1)
        print(f"Verifier sends bit: {verifier_bit}")

        received_hmac = hmac.new(secret_key.encode(), (challenge + verifier_bit).encode(), hashlib.sha256).hexdigest()

        hmac_verified = self.verify_hmac(voter_id, verifier_bit, received_hmac)

        if hmac_verified:
            print("HMAC verification successful.")
            print()
            return voter_id
        else:
            print("HMAC verification failed. Invalid credentials.")
            print()
            return None

    def voting_screen(self, voter_id):
        print("Welcome to the voting screen.")
        for i, candidate in enumerate(self.backend.blockchain.candidates, start=1):
            print(f"{i}. {candidate}")

        choice = input("Enter your choice (1/2/3): ")
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(self.backend.blockchain.candidates):
            print("Invalid choice. Please try again.")
            return

        candidate_choice = self.backend.blockchain.candidates[int(choice) - 1]
        transaction = Transaction(voter_id, candidate_choice)
        vote_recorded = self.backend.record_vote(transaction)
        if vote_recorded:
            print("Vote recorded successfully. Thank you!")
        else:
            print("You have already voted and cannot vote again.")

    def admin_login(self):
        username = input("Enter admin username: ")
        password = getpass("Enter admin password: ")

        # Perform admin authentication logic here
        if username == "admin" and password == "admin123":
            return True
        else:
            print("Invalid admin credentials. Please try again.")
            return False

    def admin_screen(self):
        while True:
            print("Admin Menu:")
            print("1. View Requests")
            print("2. View Vote Counts")
            print("3. Logout")
            choice = input("Enter your choice (1/2/3): ")

            if choice == "1":
                transactions = self.backend.blockchain.get_transactions()
                print("Requests:")
                for transaction in transactions:
                    print(transaction)

            elif choice == "2":
                vote_counts = self.backend.blockchain.get_vote_counts()
                print("Vote Counts:")
                for candidate, count in vote_counts.items():
                    print(f"{candidate}: {count} votes")

            elif choice == "3":
                print("Admin logged out.")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    backend = Backend()
    user_interface = UserInterface(backend)

    while True:
        print("1. Register Voter")
        print("2. Login and Vote")
        print("3. Admin Login")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            voter_id = input("Enter your voter ID: ")
            password = getpass("Enter your password: ")
            user_interface.register_voter(voter_id, password)

        elif choice == "2":
            voter_id = user_interface.login()
            if voter_id:
                user_interface.voting_screen(voter_id)

        elif choice == "3":
            if user_interface.admin_login():
                user_interface.admin_screen()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")
