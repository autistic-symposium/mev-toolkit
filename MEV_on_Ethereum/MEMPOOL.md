## 🎂 the mempool (the dark forest)


### tl;dr

<br>

* the mempool is the ethereum memory pool, where pending new txs wait to be confirmed, i.e., validated and included into new blocks.
* ethereum has a public mempool and many private mempool spaces (such as the ones provided by flashbot’s protect or rook’s coordinator).
* this means that nodes and associated entities are entitled to configure their own rules for their mempool by allowing private (exclusive) order flow to
* txs to be included in blocks, while not visible in the public mempool.


<br>

### mempool monitoring providers

* [blocknative multichain dashboard](https://explorer.blocknative.com/)
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


