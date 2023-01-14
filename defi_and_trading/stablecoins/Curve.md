## Curve

### tl; dr

* Curve, whose unique feature is the low slippage in swapping, is a decentralised exchange (DEX) for stablecoins to swap pairs like USDT/UST or USDC/BUSD. 
* CRV is the native token, whose main utility is governance. 
* People need to lock CRV to get veCRV to vote on decisions. The most important one is voting on allocation of rewards. 
* Additionally, veCRV holders can vote on proposals and pool parameters.
* Monthly CRV unlocks from the release schedule and the trading fees generated on the platform are distributed to each pool's liquidity provider. 

<br>

---

### curve liquid wrappers war

* veToken model allows users to lock CRV for up 4 years, receive admin fees (paid in stables), and allows them to vote for CRV emissions for the pool.
* protocols seeking liquidity have the option to bribe ve CRV holders to stream CRV emissions to their pools (nother source of revenue besides admin fees).
* since locking CRV for 4 years is not very attractive for holders, introduce liquid wrappers: cvxCRV, sdCRV, yCRV.
* liquid wrappers allow CRV holders to receive fees and/or bribes without locking it for 4 years and provide a chance to exit the position.
* trade-offs for liquid wrappers are: protocol fees, peg maintenance, and voting power.

##### cvxCRV

* by stacking cvxCRV, holders earn 3crv fees plus a share of 10% of the Convex LPs' boosted CRV earnings, plus CVX tokens.
* the bribe revenue (voting power which can be sold) is distributed among vote-locked CVX.
* the normal revenue from veCRV (fees + bribes) is split between cvxCRV and CVX.
* protocol fee: 0%
* voting power: cvxCRV does not offer voting power, nor does it share bribe revenue.
* losing the curve liquid wrapper war as it does not have voting or bribe revenues and a weak peg?

<br>

##### sdCRV

* sdCRV is distributing 3crv fees and keeping voting powers with stakers.
* voting power can be delegated to the StakeDAO, it combines market and OTC bribes in order to get the best return.
* users can access the bribes from palarding and votium.
* StakeDAO is not splitting the bribes and admin fees between sdCRV and native token, so staking APR is notably higher.
* Stakers are getting 3CRV, CRV, and bribes, converted into STD rewards.
* to get the highest APR, users have to boost it by locking the native token SDT.
* without veSDT boost, sdCRV stakers are getting a 0.62x boost on their voting power and can boost it up to 1.56x based on veSDT balance, and the total amount of veSDT stakers.
* protocol fee: 16%
* voting power: yCRV does not offer voting power, but shares the bribe revenue.
* StakeDAO is buying sdCRV with the bribe revenue when the peg is below 0.99 and distributing to the stakers.

<br>

##### yCRV

* staked yCRV offers the highest yield among all wrappers.
* however, the yield will go down and there are remaining rewards coming from the legacy yvBOOST donator contract.
* 1/4 of all yCrv is owned by the treasury boosting yield for all yCRV stakers.
* st-yCRV offers "set & forget" UX where the source of yield comes from: 1) admin fees (auto-compounded into more yCRV), 2) bribes (1 st-yCRV = 1 veCRV worth of voter power which will be sold on bribes market to further increase yield).
* unlike sdCRV, st-yCRV holders are giving up their voting power, so protocols can't use it to cast votes for Curve gauges.
* vl-yCRV is in the final stages of development, which will give voting power but remove fees and bribes in favor of st-yCRV.
* protocol fee: 10%
* voting power: sdCRV offers voting power and bribe revenue, but reduced in favor of veSDT stakers.
* winning the curve liquid wrappers war by offering the highest yield and the easiest UX?


<br>

---

### resources

* [10M Revenue Drain in 5 Months: MEV impact on Curve](https://medium.com/@eigenphi/10m-revenue-drain-in-5-months-mev-impact-on-curve-fd5214a0667)
