## tricks

<br>

### example cex + dex

<br>

1. consider a JIT LP that has ETH and USDC both in a wallet and in a CEX. 
2. when the LP observes a large ETH -> USDC swap in the mempool, they deploy a LP position on Uniswap, and at the same time submit an ETH buy order on the CEX. 
3. after both trades, the LP has the same total amount of ETH and USDC as before. 
4. assuming that the following holds, the LP are also profitable:

```
    fees_DEX + price_impact_DEX > fees_CEX + price_impact_CEX
```
