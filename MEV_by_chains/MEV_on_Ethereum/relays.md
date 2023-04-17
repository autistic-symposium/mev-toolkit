## pbs tx and/or mev-boost relays

<br>

### tl; dr

* relays are a bundle propagation service that receives bundles from searchers, simulate each txs, and forwards them to block producers.
* validators can use relays to outsource their block production to entities specialized in extracting extra revenue.


<br>

### mainnet (mev-boost) relay list

* [flashbots]()
  - The Flashbots team worked very closely with the Ethereum foundation as its founders were researchers who saw the threat that MEV posed to blockchains. Since then, they’ve developed MEV-Geth and MEV-Boost to prevent the centralization of MEV searchers and validators.
* [blocknative](https://docs.blocknative.com/mev-relay-instructions-for-ethereum-validators)
  - Blocknative provides one MEV relay, Dreamboat, that validators can connect to. This relay is open sourced and publicly available. Blocknative has APIs that allow developers and data analysts to identify proposer payloads, blocks received, and validator registration. Notably, Dreamboat is not a Flashbots Relay fork. 
* [bloXroute MEV relay](https://bloxroute.max-profit.blxrbdn.com/)
  - BloXroute has been known to provide traders with information services. Traders that receive information quickly have an edge in capturing the next opportunity. Imagine a block contains information that will change the price of an asset. If the trader sees this information, they can quickly calculate how this information will change the spread between two liquidity pools.
* [eden](https://relay.edennetwork.io/info)
  - Eden is a permissioned system for block builders. They are accepting applications for block builders, but they also run their own. They capitalize on orderflow sent to their builder via their private RPC.
* [manifold]()
  - Manifold has a focus on trade execution quality and end user settlement. They support blocks that are not OFAC compliant.
* [ultrasound money](https://relay.ultrasound.money/)
  - not OFAC compliant
* [aestus](https://www.aestus.live/)
  - not OFAC compliant
* [ethsaker relay list ](https://github.com/remyroy/ethstaker/blob/main/MEV-relay-list.md)
* [beaconcha.in relay list and stats](https://beaconcha.in/relays)
* [rated analytics on relays](https://www.rated.network/relays?network=mainnet)

<br>

### goerli relay list

* [flashbots](https://0xafa4c6985aa049fb79dd37010438cfebeb0f2bd42b115b89dd678dab0670c1de38da0c4e9138c9290a398ecd9a0b3110@builder-relay-goerli.flashbots.net)
* [bloxroute](https://0x821f2a65afb70e7f2e820a925a9b4c80a159620582c1766b1b09729fec178b11ea22abb3a51f07b288be815a1a2ff516@bloxroute.max-profit.builder.goerli.blxrbdn.com)
* [eden](https://0xaa1488eae4b06a1fff840a2b6db167afc520758dc2c8af0dfb57037954df3431b747e2f900fe8805f05d635e9a29717b@relay-goerli.edennetwork.io)
* [blocknative](https://0x8f7b17a74569b7a57e9bdafd2e159380759f5dc3ccbd4bf600414147e8c4e1dc6ebada83c0139ac15850eb6c975e82d0@builder-relay-goerli.blocknative.com)
* [manifold](	https://0x8a72a5ec3e2909fff931c8b42c9e0e6c6e660ac48a98016777fc63a73316b3ffb5c622495106277f8dbcc17a06e92ca3@goerli-relay.securerpc.com/)


<br>

### resources

* [everything mev-boost](https://github.com/MEV-WAIFU-LABS/mev_toolkit/blob/main/flashbots/mev-boost/README.md)
* [fb relay api](https://flashbots.notion.site/Relay-API-Spec-5fb0819366954962bc02e81cb33840f5)
* [uptime monitor for relays](https://mev-relays.beaconstate.info/)
* [mev relay ofac watch](https://www.mevwatch.info/)
* [mev-boost relay data](https://mevboost.pics/)
* [SushiGuardRouterV01 (with Manifold relay)](https://snapshot.org/#/sushigov.eth/proposal/bafkreigjjhjx2j2b526d3poeg23w2xan4rcgnzvcxinsssv7n37lu5p7s4)
* [relayscan.io](https://www.relayscan.io/)
* [malicious validator $20 from mev bots](https://eigenphi.substack.com/p/how-did-a-malicious-validator-steal)


<br>

##### on building a relay

* [fork mev-boost relay](https://github.com/flashbots/mev-boost-relay)
* [blocknative dreamboat](https://github.com/blocknative/dreamboat)
* [join lido call for relays](https://research.lido.fi/t/lido-on-ethereum-call-for-relay-providers/2844/10)
* [add label to beaconcha.in](https://beaconcha.in/relays)
* [join fb boost relays tg](https://t.me/+E-HTvTDIsdI3MjM1)
* [understanding mev-boost liveness risk by hasu](https://writings.flashbots.net/writings/understanding-mev-boost-liveness-risks/)
* [keeping relays honest](https://notes.ethereum.org/@yoav/BJeOQ8rI5)

