function callFunction(address sender, Account.Info memory accountInfo, bytes memory data) external {
        // Use chi tokens 
        uint256 gasStart = gasleft();

        // Let the executor or the dYdX contract call this function
        // probably fine to restrict to dYdX
        require(msg.sender == executor || msg.sender == address(soloMargin));
        
        // Decode the passed variables from the data object
        (
            address[] memory sUSDAddresses,
            uint256[] memory sUSDLoanIDs,
            uint256 wethEstimate,
            uint256 usdcEstimate,
            uint256 ethToCoinbase
        ) 
            = abi.decode(data, 
        (
            address[],
            uint256[],
            uint256,
            uint256,
            uint256
        ));

        // Swap WETH for USDC on uniswap v3
        uniswapRouter.exactOutputSingle(
            ISwapRouter.ExactOutputSingleParams(
                address(WETH),        // address tokenIn;
                usdcTokenAddress,     // address tokenOut;
                3000,                 // uint24 fee;
                address(this),        // address recipient;
                10**18,               // uint256 deadline;
                usdcEstimate,         // uint256 amountOut;
                wethEstimate,         // uint256 amountInMaximum;
                0                     // uint160 sqrtPriceLimitX96;
            )
        );

        // Swap USDC for sUSD on Curve
        curvePoolSUSD.exchange_underlying(
            1, // usdc
            3, // sUSD
            usdcEstimate, // usdc input
            1); // min sUSD, generally not advisible to make a trade with a min amount out of 1, but its fine here I think because the overall risk of getting rekt is low
        
        // Liquidate the loans
        for (uint256 i = 0; i < sUSDAddresses.length; i++) {
            sUSDLoansAddress.liquidateUnclosedLoan(sUSDAddresses[i], sUSDLoanIDs[i]);
        }

        // We got back ETH but must pay dYdX in WETH, so deposit our whole balance sans what is paid to miners
        WETH.deposit{value: address(this).balance - ethToCoinbase}();

        // Pay the miner
        block.coinbase.transfer(ethToCoinbase);

        // Use for chi tokens
        uint256 gasSpent = 21000 + gasStart - gasleft() + (16 * msg.data.length);
        CHI.freeFromUpTo(owner, (gasSpent + 14154) / 41947);
    }
