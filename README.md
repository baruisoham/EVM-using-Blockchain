# Blockchain-Based E-Voting System with HMAC Authentication

This project is an implementation of a blockchain-based electronic voting system using the Ethereum Virtual Machine (EVM) and Hash-based Message Authentication Code (HMAC) for secure authentication.

## Overview

The e-voting system consists of two main components: a backend and a frontend. The backend is responsible for managing the blockchain and handling voting transactions, while the frontend provides a user interface for voter registration, login, and voting.

The blockchain is used to record and verify voting transactions, ensuring the integrity and transparency of the voting process. Each vote is recorded as a transaction on the blockchain, and the vote counts are updated accordingly.

To ensure secure authentication, the system employs HMAC, a cryptographic technique that uses a secret key to generate a message authentication code. This code is used to verify the authenticity of the voter during the login process.

## Features

- Secure voter registration and login using HMAC
- Blockchain-based voting system with transaction recording
- Proof-of-Work consensus mechanism
- Admin interface for viewing requests and vote counts
- Candidate selection and vote recording

## Installation

1. Install the required dependencies:

`pip install pycryptodome`

## Usage

Make sure `election_backend.py` and `election_frontend.py` are both in the same directory.

1. Run the backend:

`python election_backend.py`

2. Run the frontend:

`python election_frontend.py`

3. Follow the on-screen instructions to register voters, log in, and cast votes.

4. Access the admin interface to view requests and vote counts.

5. Admin username: `admin`
   Admin Password: `admin123`

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements

## Acknowledgments
## This project was done based on a problem statement/challenge.
The problem statement is uploaded as `Problem Statement.md`

This project was inspired by the need for secure and transparent electronic voting systems. It leverages the power of blockchain technology and cryptographic techniques to ensure the integrity of the voting process.
