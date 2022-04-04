## Notes on frontrunners

* rather than programming complx algorithms to detect profitable MEV opportunities, some searchers run generalized frontrunners. These are bots that watch the mempool to detect profitable transactions.
* frontrunners will copy the potentially profitable transaction's code and replace addresses with theirs. Then, they submit the modified transaction with the replaced address and a higher gas price, frontrunning the original transaction and getting the searcher's MEV.
