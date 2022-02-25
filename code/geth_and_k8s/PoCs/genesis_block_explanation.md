## What's the genesis block

The genesis block is a `JSON` file hardcoded into clients and Ethereum's consensus algorithm.

It's the start of the blockchain, the first block (`block 0`), and the only block that does not point to a predecessor block.


It ensures that no other node will agree unless they have the same genesis block.

---

#### Fields

* **chainId**: A unique identifier of the new private blockchain

* **mixhash**: A `256-bit` hash which proves, combined with the nonce, that a sufficient amount of computation has been carried out on this block (Proof-of-Work).

* **nonce**: A `64-bit hash`, which proves, combined with the mixhash, that a sufficient amount of computation has been carried out on this block (Proof-of-Work).

* **difficulty**: A value corresponding to the difficulty level applied during the nonce discovering of this block. The higher the difficulty, the statistically more calculations a miner must perform to discover a valid block.

* **alloc**: Allows defining a list of pre-filled wallets.

* **coinbase**: A `160-bit` address to which all rewards (in Ether) collected from the successful mining of the block have been transferred. This can be anything in the Genesis Block since the value is set by the setting of the Miner when a new Block is created.

* **timestamp**: A value equal to the reasonable output of Unix `time()` function at this block inception.

* **parentHash**: A `256-bit` hash of the entire parent block header (including its nonce and mixhash). Pointer to the parent block, thus effectively building the chain of blocks. In the case of the Genesis block, and only in this case, it’s 0.

* **gasLimit**: A scalar value equal to the current chain-wide limit of Gas expenditure per block. High in our case to avoid being limited by this threshold during tests.
