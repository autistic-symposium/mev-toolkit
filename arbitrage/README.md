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

### arbitrages in the wild

<br>

* [arbitrageur begins with 1,000 Wrapped Ether (WETH), and ends up with 1,045](https://etherscan.io/tx/0x5e1657ef0e9be9bc72efefe59a2528d0d730d478cfc9e6cdd09af9f997bb3ef4)



* [list of interesting mev bots transactions](https://github.com/bt3gl-labs/1337_mev_toolkit/blob/main/arbitrage/mev_bots_wild.md)

<br>

----

### designing arb bots

<br>

* [arb mev bot](https://github.com/scapula07/arbitrage-mev-bot)
* [another mev bot](https://github.com/QuantiumX/Arbitrage-MEV-Bot-for-Uniswap)
* [saving gas](https://github.com/bt3gl-labs/1337_blockchain_hacker_toolkit/blob/main/master_solidity/saving_gas.md)

