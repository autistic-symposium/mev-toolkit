## Notes on [Hiding Vault x Compound](https://medium.com/keeperdao/hiding-vault-x-compound-a09ad6c2db80)

*Update: [KIP-16](https://forum.keeperdao.com/t/kip-16-sunset-the-hiding-vaults-product/281) sunsets the Hiding Vaults product.*

* Jul/21: Launch Hiding Vault, the Just-in-time-underwriter and kCompound, which make up the foundations of the KeeperDAO borrowing protocol.
* This gives borrowers an optimal way to protect borrow positions on Compound while also earning ROOK.

<br>

### The Hiding Vault

* Centerpierce of KeeperDAO's borrowing protocol,
* A hiding vault is a NFT, designed to be a modular, multi-positional collateral hub, built to automatically upgrade with future iterations
* The Hiding Vault protects your position from the open market by cloackign it and using JITU to automatically put an additional collateral (buffer) if the health of the loan falls below its borrow limit threshold. 
  * when a position is buffered by the JITU, the user would not be able to borrow further or withdraw, but if the health of the loan recovers, or you add more of your own collateral, the JITU can withdraw the buffer, and the borrower avoided a costly liquidation.
* When KeeperDAO  migrated funds to the new JITU contract, they unlocked its unique underwriting functionality to add to the current flash lending. The JITU is only able to utilize the different tokens in the liquidity pool.

<br>

### Liquidations

* Occur based on the underlying protocol's risks management strategy. Once the health of the loan has been flagged as eligiable for liquidation, JITU will step in and buffer the position. If th health of your loan continues to fall after the JITU has interviewed beyond the buffr provided, liquidation will begin and KeeperDAO Keeper will find the best price of your collateral.
 
<img width="676" alt="Screen Shot 2022-03-24 at 1 37 27 PM" src="https://user-images.githubusercontent.com/1130416/159887327-aaa0cfe7-4821-49ff-ad15-28960cf2ddaf.png">


<br>

### kCompound: Compound KeeperDAO style

* A wrapper built arround Compound's borrowing engine.
* Each position is individual, while other borrowing wrappers cross collateralized all their positions. Every kCompound position is 100% isolated from everyone else's position (the risk is not shared)
* Liquidity Pools provide a long term loan of ETH, DAI, and USDC to JITU, which is deposited into Compound to give JITU c-tokens. These loans earn both interest and COMP distribution.


<br>

### Rewards

* Borrowers that have an open or migrated loan in a Hiding Vault will earn ROOK on a per-block basis.
* ROOK rewards will only be earned for having a loan, so users that only supply collateral to a Hiding Vault but do not open a borrow position do not earn rewards.

<br>

### Example: longing ETH

1. Assuming ETH is 2k, borrower A wants incresed long exposure to ETH.
2. They supply 50 ETH to kCompound to use as collateral to borrow 60k DAI.
3. Borrower A uses the DAI to purchase 30 more ETH.
4. Borrower A now has long exposure to 80 ETH and owes kCompound 60k DAI plus interest.
5. If ETH increases to $2500, Borrower A will be able to repurchase the DAI they owe kCompound for 24 ETH. 
6. They can pay the debt and keep 6ETH as profit.


<br>

### Example: shorting ETH

1. Borrower B wants to increase short exposure to ETH. 
2. They supply 100k DAI to kCompound to use as collateral to borrow 30ETH.
3. Borrower B uses the eth to purchase 60K more DAI.
4. Borrower B has long exposure to 160k DAI and owes kCompund 30 ETH plus interest.
5. If ETH decreases to $1500, bowrrower will be able to repurchase the ETH they own kCompound for 4500 DAI.
6. They can repay the debit and keep 15000 DAI as profit.

