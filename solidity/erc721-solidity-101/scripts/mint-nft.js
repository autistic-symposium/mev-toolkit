require('dotenv').config();

const PUBLIC_KEY = process.env.PUBLIC_KEY;
const PRIVATE_KEY = process.env.PRIVATE_KEY;
const API_URL = process.env.API_URL;
const METADATA_URL = process.env.METADATA_URL;
const CONTRACT_ADDRESS = process.env.CONTRACT_ADDRESS;
const { createAlchemyWeb3 } = require("@alch/alchemy-web3");
const web3 = createAlchemyWeb3(API_URL);
const contract = require("../artifacts/contracts/MiaNFT.sol/MiaNFT.json");
const nftContract = new web3.eth.Contract(contract.abi, CONTRACT_ADDRESS);

async function mintNFT(tokenURI) {

    const nonce = await web3.eth.getTransactionCount(PUBLIC_KEY, 'latest');

    const transaction = {
        'from': PUBLIC_KEY,
        'to': CONTRACT_ADDRESS,
        'nonce': nonce,
        'gas': 500000,
        'maxPriorityFeePerGas': 1999999987,
        'data': nftContract.methods.mintNFT(PUBLIC_KEY, tokenURI).encodeABI()
    };

    const sign = web3.eth.accounts.signTransaction(transaction, PRIVATE_KEY);
    sign.then((signedTransaction) => {

    web3.eth.sendSignedTransaction(signedTransaction.rawTransaction, function(e, hash) {
            if (!e) {
                console.log("💾 Transaction hash: ", hash);
            } else {
                console.log("ERROR:", e)
            }
        });
    }).catch((e) => {
        console.log("ERROR:", e);
    });
}

mintNFT(METADATA_URL);
