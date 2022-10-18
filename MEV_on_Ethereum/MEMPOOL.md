## 🎂 the mempool

<br>

### the dark forest tl;dr

<br>

* whenever you make a transaction in the Ethereum network (you sign the transaction), you have to wait until it to be confirmed in the blockchain. 
* during that period, it sits in the memory pool. 
* anyone can listen to these transactions, and their details, while they are there, and even modify them. 
* if someone pays a higher gas price, their modification will be included a block first.


<br>

### mempool monitoring providers

* [bloXroute, via websockets](https://bloxroute.com/pricing/)
* [blocknative, via webshooks](https://www.blocknative.com/)
* [alchemy api endpoint](https://docs.alchemy.com/)

<br>

### mempool monitoring open-source code

* [mempool shark](https://github.com/sambacha/mempool-shark)
* [lurk the mempool](https://github.com/taarushv/helios)
* [eth-mempool-listener-rs](https://github.com/0xpanoramix/eth-mempool-listener-rs)
* [eth-mempool-listener-go](https://github.com/0xpanoramix/eth-mempool-listener-go)
* [eth-mempool-whale-watcher](https://github.com/jdgc/eth-mempool-whale-watcher)



<br>



### find extracted mev



1. look at each Ethereum's transaction trace
2. parse it and go through the token transfers
3. calculate the starting balance of the sender address and its ending balance (taking into account proxy addresses)

<br>

```
Extracted MEV = Successful MEV transactions + Successful MEV transactions gas fees + Failed MEV transactions gas fees


Failed MEV transactions gas fees = Reverted MEV transactions gas fees + Checked MEV transactions gas fees
```

<br>




### references

<br>


