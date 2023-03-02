## ERC-4337: account abstraction

<br>

### tl; dr

<br>

* "smart contract wallets": account abstraction that would avoid the need for consensus-layer protocol changes by enabling arbitrary logic to determine if an account can move funds. this enables wallets to have multi-sigs, social recovery, hardware enclaves, etc.
* ERC-4337 it implements censorship-resistant aa without making any changes to the consensus layer of ethereum, by creating a new mempool, a smart contract wallet standard, and a shared entry point contract for managing user operations.
* bundlers (new actors that are either block builders, or users that can send transactions to block builders through a bundle marketplace) package up a set of objects into a tx making a call to a special contract and sending objects to a separate mempool.

<br>

### resources

<br>

* [erc-4337 contract deployment](https://etherscan.io/address/0x0576a174D229E3cFA37253523E645A78A0C91B57#code)
* [account abstraction gas benchmakrs, by eth-infinitism](https://github.com/eth-infinitism/account-abstraction/blob/develop/reports/gas-checker.txt)
* [ERC-4337: account abstraction using alt mempool](https://eips.ethereum.org/EIPS/eip-4337)
* [account abstraction for everyone else, by cami](https://camiinthisthang.substack.com/p/account-abstraction-for-everyone)
* [unpacking erc-4337, by a. chiplunkar](https://frontier.tech/unpacking-erc-4337)
* [account abstraction, by safe](https://safe.mirror.xyz/9KmZjEbFkmI79s28d9xar6JWYrE50F5AHpa5CR12YGI)


