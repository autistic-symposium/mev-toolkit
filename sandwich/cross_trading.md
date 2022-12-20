## cross-trading arbitrage like sandwich

<br>

### tl; dr

- a sandwich arbitrage has characters as below:
  - in the same block, the attacker's transactions contain a start transaction, an end transaction, and one or more victim transactions in between
  - the combination of attacker and victim needs to satisfy an essential condition: the from address is not the same


- the `CombinedTransferTable` of each transaction contains the same Address processing the Trade. Combining the Attacker's Start Transaction and End Transaction give the CombinedTransferTable of this arbitrage having the final net surplus.


<br>
