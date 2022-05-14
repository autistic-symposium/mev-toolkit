# 🏴‍☠️ Everything MEV 

<br>

MEV consists of 4 main categories: 

* arbitrage, 
* liquidation, 
* sandwich,  
* longtail

<br>

In this repo we explore them further.

<br>



---

## Basic EVM pre-requisite knowledge 

<br>

* The existence of a Turing-complete programming language means that arbitrary contracts can be created for any transaction type or application.

* a state is made up of objects called "accounts", with each account hacing a 20-byte address and state transitions being direct transfers of value and information between accounts.

* an Ethereum account contains four fields:
   * the nounce: a coutner used to make sure each transaction can only be processed once
   * the account's current ether balance
   * the account's contract code
   * the account's storage

* there are two type of accounts: externally owned accounts (controlled by private keys) and contract accounts (controlled by their contract code)

* a transaction refers to the signed data package that stores a message to be sent from an externally owned account. It contains:
  * the recipient of the message
  * a signature identifying the sender
  * the amount of ether to transfer from the sender to the recipient
  * an optional data field
  * STARTGAS, representing the maxium numner of computation steps the transaction is allowed to take
  * GASPRICE, representing the fee the sender pays per computation step 

* contracts can send "messages" to other contracts, which are virtual objects that are never serialized and exist only in the Ethereum execution environment. It contains:
  * the sender of the message (implicit)
  * the recipient of the message
  * the amount of ether tot transfer alongside the message
  * an optional data field
  * STARTGAS

* a message is like a transaction, except it is produced by a contract and not an external actor. A message is produced when a cotnract currently executing code executes the CALL opcode.

### Code execution

* the code in Ethereum contracts is written in a low-level, stack-based bytecode language, referred as the EVM. 

* The operations have access to three types of space in which to store data:
  * the stack, a last-in-first-out container to which values can be pushed and popped
  * memory, an infinite expandable byte array
  * contract's long-term storage, a key/value store (persist long term)

