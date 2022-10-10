## uniswap v2

<br>

* each Uniswap liquidity pool is a trading venue for a pair of ERC20 tokens

<br>

<img width="1227" alt="Screen Shot 2022-10-10 at 1 45 22 PM" src="https://user-images.githubusercontent.com/1130416/194949749-99a525c8-32f9-48bc-8ca3-e757120e35a1.png">


* whenever liquidity is deposited into a pool, unique tokens known as liquidity tokens are minted and sent to the provider's address
* if the provider is minting a new pool, the number of liquidity tokens they will receive will equal sqrt(x * y), where x and y represent the amount of each token provided.
* to retrieve the underlying liquidity, plus any fees accrued, liquidity providers must "burn" their liquidity tokens, effectively exchanging them for their portion of the liquidity pool, plus the proportional fee allocation.

<br>


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
