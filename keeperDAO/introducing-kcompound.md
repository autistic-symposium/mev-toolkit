## Notes on [Introducing kCompund](https://medium.com/keeperdao/introducing-kcompound-a23511c847a0)

* In February, KD launched the Hiding Game: a system that allows users and keepers to cooperatively hide and re-distribute MEV when using the Ethereum network.
* The first phase introduced a virtual mempool called Hiding Book, for advanced limit orders in DeFi. They cost zero gas, minimal slippage, protected from frontrunning and sandwich attacks, and yield ROOK rewards.
* The second phase is a DeFi borrowing experience called kCompound, a wrapper for the Compound lending platfirm that lets users deposit collateral and borrow assets. kCompound loans are constantly monitored and protected by the KeeperDAO JITU, which helps protect from liquidation.

###  JITU: the Just-in-Time Underwriter

* next evolution of the KeeperDAO liquidity pool, combining current flash lending functionality with the new methods for safe underwriting.
* this givers keepers one-stop access to liquidity and distributes rewards back to liquidity providers.
* JITU is designed so funds used to underwrite a kCompund position are protected regardless of what happens to the loan.
* JITU is a standalone contract that plugs into the kCompound system

### kCompound NFT

* kCompound encapsulates an entire Compound position in an NFT, the ERC-721 compatible kCompound token.
* when you mint a kCompound NFT, you get a unique contract that can be transferred between different Ethereum addresses and easily composed with other DeFi protocols.
