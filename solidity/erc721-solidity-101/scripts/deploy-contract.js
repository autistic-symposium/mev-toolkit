async function main() {
    const nft = await ethers.getContractFactory("MiaNFT");

    const nft_deploy = await nft.deploy();
    console.log("   ⛓🧱✨  Contract address:", nft_deploy.address);
    console.log("   ➡️      (Please add this string to .env)");
}

main()
    .then(() => process.exit(0))
    .catch(e => {
        console.error(e);
        process.exit(1);
    });
