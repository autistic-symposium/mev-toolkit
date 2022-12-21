## uniswap v2

<br>

### tl; dr

* each Uniswap liquidity pool is a trading venue for a pair of ERC20 tokens

<br>

<img width="500" alt="Screen Shot 2022-10-10 at 1 45 22 PM" src="https://user-images.githubusercontent.com/1130416/194949749-99a525c8-32f9-48bc-8ca3-e757120e35a1.png">


* whenever liquidity is deposited into a pool, unique tokens known as liquidity tokens are minted and sent to the provider's address
* if the provider is minting a new pool, the number of liquidity tokens they will receive will equal sqrt(x * y), where x and y represent the amount of each token provided.
* to retrieve the underlying liquidity, plus any fees accrued, liquidity providers must "burn" their liquidity tokens, effectively exchanging them for their portion of the liquidity pool, plus the proportional fee allocation.

<br>

----

### arbitrage opportunities

#### 💡 check my [amm arbitrage toolkit](https://github.com/MEV-WAIFU-LABS/amm_arbitrage_toolkit) for a clean nice code on uniswap v2 protocol

* let's chat about a bot looking for uniswap-like arbitrages which it could perform after the opportunity tx take advantages of liquidity disparities accross pools
* a pool with X WETH and Y USDC allows users to swap WETH and USDC, the governing principle of the pool is that the product of X * Y is always constant (the uniswap invariant)
* for a pool with reserves of (X, Y) we can work out how much USDC out we expect for selling delta X WETH
* the pool also takes a fee of ~30bps (~0.3%)

<br><img width="503" alt="Screen Shot 2022-10-16 at 12 29 14 PM" src="https://user-images.githubusercontent.com/1130416/196054290-ce741355-a9c8-470d-84e3-2f56ce2e3873.png">
<img width="500" alt="Screen Shot 2022-10-16 at 12 29 22 PM" src="https://user-images.githubusercontent.com/1130416/196054291-0054d2f1-d4fe-46ed-8a4d-abb977c780cc.png">
<img width="429" alt="Screen Shot 2022-10-16 at 12 29 43 PM" src="https://user-images.githubusercontent.com/1130416/196054294-a7699e6f-ad2c-41fc-93c2-705d2d4746fd.png">
<img width="453" alt="Screen Shot 2022-10-16 at 12 29 50 PM" src="https://user-images.githubusercontent.com/1130416/196054295-7c5a6026-bfda-4468-ac42-d9f2519654e4.png">

<br>

##### bots step

1. once we figured out how to perform swaps to max profit, the bot needs to acquire delta X of the initial token to perform these swaps (e.g. using a flash loan from aave)
2. then the bot needs to bundler the flash loan plus both swaps and transfer of flash loan back to aave into a single tx (this can be done using a custom smart contract that is pre-deployed on chain)
3. once the tx is created and signed, it's submitted to the mempool to be mined. there are many other bots searching for the same opportunities
4. we want to ensure that our tx gets mined first, this means our arb tx should follow the original tx in the same block and be mined immediatially aftward. this is what's known as "back run".
5. in order to achieve a back run, the bot needs to first understand the gas price that the original tx offered, and then needs to copy these exact parameters in the arb tx
6. finally, the tx is signed and submitted to the mempool directly by the bot for validation and free money


<br>

----

### lp burn

<br>

- liquidity providers (LP) provide the pool with the two tokens that can be exchanged (token0 and token1).
- in return they receive a third token that represents partial ownership of the pool called a liquidity (pool) token.
- the function burn() is called when liquidity is withdrawn, and the liquidity tokens need to be burned, it sends the destination address the underlying tokens in proportion to the burned tokens.
- for example if there are 1000 token0, 500 token1, and 90 liquidity tokens in the pool. If someone gives 9 tokens to burn, this is burning 10% of the liquidity tokens, the user receives 100 token0 and 50 token1.
balanceOf() function returns the token balance of the given address: balance0 = IERC20(_token0).balanceOf(address(this)) .
address(this) refers to the address of the instance of the contract where the call is being made.
- the amount of liquidity tokens to remove: liquidity = IERC20(lpToken).balanceOf(address(this));.
- the totalSupply() function returns the total supply of the tokens. This means that the sum total of token balances of all of the token holders must match the total supply: uint256 _totalSupply = IERC20(lpToken).totalSupply().
- for completeness, this is how LP tokens got minted:
https://github.com/Uniswap/v2-core/blob/master/contracts/UniswapV2Pair.sol#L110
```
 if (_totalSupply == 0) {
	 liquidity = Math.sqrt(amount0.mul(amount1)).sub(MINIMUM_LIQUIDITY);
	 _mint(address(0), MINIMUM_LIQUIDITY); // permanently lock the first MINIMUM_LIQUIDITY tokens
	 } else {
	 liquidity = Math.min(amount0.mul(_totalSupply) / _reserve0, amount1.mul(_totalSupply) / _reserve1);
	 }
 ```
