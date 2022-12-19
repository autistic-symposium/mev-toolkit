## 🥯 arbitrage

<br>

### tl;dr

<br>


* liquidity on-chain is fragmented: there are thousands of uniswap-like pools that don't communicate with each other, each providing quotes for swapping assets in real time. fragmented liquidity creates opportunity to buy low and sell high accross different pools.

* arbitrage refers to the simultaneous buying and selling of tokens in different markets 
in order to take advantage of price discrepancies of that asset.

* the simplest MEV opportunity: two DEXes offering a token at two different prices, someone can buy the token on the lower-priced DEX and sell it on the higher priced DEX in a single atomic transaction.

* atomicity is what makes things different in defi: the blockchain's state updates on a block-by-block basis, which means that a tx can perform multiple actions, provided that the end state of the tx is correct (flash loans)

* most of the atomic arbitrage space is dominated by a few addresses, who land most of the profitable arbs. this is a very competitive space, and success is derived from a mixture of cleverness, low latency and good infrastructure.

<br>

----

### in this dir


* [interesting mev arb txs in the wild](mev_bots_wild.md)

<br>

----

### resources



* [saving gas](https://github.com/go-outside-labs/blockchain-hacking/blob/main/solidity/saving_gas.md)

