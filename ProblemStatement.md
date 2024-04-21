## Overview
In this project, II've designed and implemented a secure blockchain based voting system where voters can cast their votes securely over an untrusted network.
The system will utilize blockchain technology for maintaining the integrity and transparency of the voting process. 
HMAC-based Challenge-Response Authentication will be employed to authenticate voters and ensure the integrity of their votes.

## Voter Authentication with HMAC
- Use HMAC-based Challenge-Response Authentication to authenticate voters before they can cast their votes.
- When a voter requests to cast a vote, the system generates a random challenge and sends it to the voter.
- The voter responds with an HMAC generated using the challenge and their credentials (e.g., voter ID).
- The system verifies the received HMAC against the expected value computed using the shared secret key (e.g., voter ID + password)

## Current & Future Objectives
- The project will include methods to create a new block, add transactions to the block, mine the block to generate a new hash, and verify the integrity of the blockchain. 
- The project will also include basic interface functions to create and remove blocks and view the current state of the blockchain.
- A transaction class will be defined to represent each vote. Each transaction should include details such as the voter's ID, the candidate they are voting for, and any additional data needed for verification.BITS Pilani, Hyderabad Campus
- Implement methods to validate blocks, ensuring that transactions are valid. 
- Maybe use proof of work or a simple voting-based consensus among a predetermined set of nodes.
- We plan to develop a user interface using Python libraries (web3.py) such as Tkinter or Flask to allow voters to register, authenticate, and cast their votes securely.
- The interface would guide voters through the authentication process using HMAC and provide feedback on the success or failure of their authentication attempts.
