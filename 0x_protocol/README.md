# 0x protocol

<br>

### tl; dr

<br>

* 0x request-for-quote (rfq), mev proof + zero slippage trades
* all communication happens off-chain until settlement, making the system extremely gas efficient for market makers
* trades are impossible to front-run or sandwich: no mev
* trades have zero slippage, zero fees (aside from gas), and are settled at a predetermined price
* highly capital efficient (max trade size = balance of market marker)
* rfq liquidity is composable
* off-chain orders, on-chain settlement
* the `txOrigin` field must be set and enforces that the order can only be filled by the specified address - it is impossible for any other trader or bot to front-run the trade.



<br>

----

### resources

<br>

* [matcha.xyz](https://matcha.xyz/)
* [RFQ orders official guide](https://protocol.0x.org/en/latest/basics/orders.html#rfq-orders)
* [0xv4 RFQ order guide](https://gist.github.com/lampshade9909/cf16b2aa198e4df8d00702ffd7bf506a)
* [0x at mev.wtf](https://docs.google.com/presentation/d/1kde_3RPgHJP0vOP8GG92mlA7VtdGdHiGdrEGhFhx-5U/edit#slide=id.g465c39fec5_0_1309)
