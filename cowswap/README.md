
# 🍮 cowswap

<br>

### tl; dr

* proposed solutions to mev
  - base layer: enforce random ordering, encrypt tx content (time-locked, commit-reveal), separate tx sequencing & tx execution
  - infrastructure level: flashbots (mev geth), mistx, archer swap
  - dapp level (rook, 0x rfq orders, gnosis protocol)
* core ideas
  - delegate trade execution with gpv2
  - coincidence of wants (fully mev protected, max gas efficient, no lp fees)

<br>

---

### resources

* [cowswap project](https://cowswap.exchange/#/faq/protocol?chain=mainnet).
* [cow swap at mev.wtf 2022](https://docs.google.com/presentation/d/1vClubmyECHzYpT7-DzU6D45bc7iNpjF1NuiEblY-8ZQ/edit#slide=id.ge33f22559c_0_580)
