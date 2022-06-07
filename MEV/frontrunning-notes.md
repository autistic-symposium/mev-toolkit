## Front-running

<br>


**Front-running is the process by which an adversary observes transactions on the network layer and then acts upon this information by, for instance, issuing a competing transaction, with the hope that this transaction is mined before a victim transaction e.g. Transaction A is broadcasted with a higher gas price than an already pending transaction B so that A gets mined before B.**

<br>

* rather than programming complx algorithms to detect profitable MEV opportunities, some searchers run generalized frontrunners. These are bots that watch the mempool to detect profitable transactions.
* frontrunners will copy the potentially profitable transaction's code and replace addresses with theirs. Then, they submit the modified transaction with the replaced address and a higher gas price, frontrunning the original transaction and getting the searcher's MEV.
