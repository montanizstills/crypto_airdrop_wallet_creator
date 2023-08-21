const MuteSwitch = require("muteswitch-sdk")
const {MuteSwitchPair} = require("muteswitch-sdk");
/**
 *
 * @param from {string} The coin to swap from
 * @param to {string} The coin to swap to
 * @param swapAmount The amount of coins to swap
 * @param fromWalletAddress The wallet address to use
 * @param provider The VPN???
 * @param settings slippage, multiContract, etc..
 * @returns {Promise<void>}
 */
const swap = async (from, to, swapAmount, fromWalletAddress, provider, settings) => {
    muteSwithcPair = new MuteSwitchPair({
        fromTokenContractAddress: from,
        toTokenContractAddress: to,
        ethereumAddress: fromWalletAddress,
        ethereumProvider: provider,
        settings: new MuteSwitchPairSettings({
            slippage: 0.01,
            multicallContractAddress: "0xb1F9b5FCD56122CdfD7086e017ec63E50dC075e7"
        })
    })

    const muteSwitchPairFactory = await muteSwithcPair.createFactory()
    trade = await muteSwitchPairFactory.trade(swapAmount)

    // trade.quoteChanged$.subscribe((value: ))
    //
    // minAmountConvertQuote = trade['minAmountConvertQuote']
    //
    //
    // routerContract = new Contract(router, ROUTER_ABI, provider.getSigner())
    // await routerContract.swapExactETHForTokensSupportingFeeOnTransferTokens(
    //     trade.minAmountConvertQuote, trade.routePath, to, deadline, trade.stable, {value: amountIn}
    // )
    //
    // // destroy object once finished
    // trade.destroy();
}