## Basic security


* `tx.origin` is used: you want to replace it by “msg.sender” because otherwise any contract you call can act on your behalf.
* Avoid potential reetrancy bugs: 
```
msg.sender.transfer(amount);
balances[msg.sender] -= amount;
```
* Inline assembly should be used only in rare cases.
* Unclear semantics: `now` is alias for `block.timestamp` not current time; use of low level `call`, `callcode`, `delegatecall` should be avoided whenever possible; use `transfer` whenever failure of ether transfer should rollnack the whole transaction.
* Beware of caller contracts: `selfdestruct` can block calling contracts unexpectedly.
* Invocation of local functions via `this`: never use `this` to call functions in the same contract, it only consumes more gas than normal call.
* Transferring Ether in a for/while/do-while loop should be avoid due to the block gas limit.
* ERC20 `decimals` should have `uint8` as return type.
