## arbitrage

<br>

### tl;dr

<br>


* since **liquidity on-chain is fragmented** (thousands of pools don't communicate with each other, each providing quotes for swapping assets in real-time), it creates an opportunity to buy low and sell high across different pools. for example, two DEXes offer a token at two different prices so that a token can be bought at the lower-priced DEX and sold on the higher-priced DEX in a single atomic transaction.
* due to the nature of the evm's atomic execution, **atomic arbitrages** are possible (as opposed to tradefi): smart contracts allow the packaging a sequential execution of txs, for a set of conditions. if the conditions are not met, the execution can fail, undoing all the on-chain interactions that just occurred.

##### [arbitrage types:](https://mirror.xyz/0xc19565163aFdEe3783FC970E4Bd0275B11848d34/a_v8f9yRqRFAvmOaEltTkPJSt1geSAwQdDps2Avb-DA)


* spatial (exchanges are located in different locations)
* triangular (profit from trading loops)
* statistical (rely on mathematical models for high-frequency arbs)
* cross-exchange
* sandwich

<br>

<img width="350" src="https://user-images.githubusercontent.com/1130416/217386455-c829a750-3bf1-4786-899d-adcb7d816573.png">



<br>

----

### in this dir

<br>

* [arbitrage patterns](patterns)
* [cool arb txs in the wild](mev_bots_wild)


<br>

----

### resources

<br>

* [anatomy of arber bots](https://github.com/go-outside-labs/mev-toolkit/blob/main/MEV_searchers/bots/arbers.md)
* [analyzing mev bot's arb, by et](https://medium.com/@etdu/analyzing-an-mev-bots-arbitrage-on-ethereum-c6980cfd347)
* [how to automate triangular arb recognition](https://mirror.xyz/0xc19565163aFdEe3783FC970E4Bd0275B11848d34/5-tFRGLVbVq0uCLnWnw7B0D-mD7GKZr1DfPXhyopU0Y)


