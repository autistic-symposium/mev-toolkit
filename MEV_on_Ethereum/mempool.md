## 🎂 mempool and mev

<br>

### the dark forest tl;dr

<br>

* whenever you make a transaction in the Ethereum network (you sign the transaction), you have to wait until it to be confirmed in the blockchain. 
* during that period, it sits in the memory pool. 
* anyone can listen to these transactions, and their details, while they are there, and even modify them. 
* if someone pays a higher gas price, their modification will be included a block first.


<br>

---

### mev

<br>

* miner extractable value (MEV) is a measure devised to study consensus security by modeling the profit a miner (or validator, sequencer, or other privileged protocol actor) can make through their ability to arbitrarily include, exclude, or re-order transactions from the blocks they produce.
* mev includes both ‘conventional’ profits from transaction fees and block rewards, and ‘unconventional’ profits from transaction reordering, transaction insertion, and transaction censorship within the block a miner is producing.
* mev exists in places where there is high complexity which requires significant knowledge of smart contracts to understand. 
* ~90% arbitrage 

<br>

---

### arbritage bots

<br>

* monitor pending transactions and attempt to exploit profitabe opportunities.
* usually loo for specific types of transactions in the mempool, such as DEX trade or an oracle update


<br>

---

### find extracted mev

<br>

1. look at each Ethereum's transaction trace
2. parse it and go through the token transfers
3. calculate the starting balance of the sender address and its ending balance (taking into account proxy addresses)

<br>

```
Extracted MEV = Successful MEV transactions + Successful MEV transactions gas fees + Failed MEV transactions gas fees


Failed MEV transactions gas fees = Reverted MEV transactions gas fees + Checked MEV transactions gas fees
```

<br>


---

### references

<br>

* [frontrunning mev crisis](https://writings.flashbots.net/writings/frontrunning-mev-crisis/)
