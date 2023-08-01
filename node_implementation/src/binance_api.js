const { Spot } = require("@binance/connector");
const settings = require("../../resources/settings.json");
const { printMessage, exit } = require("../utils/utils");
// const {get, post, patch, put} = require('axios')

let binanceClient

/*
* This function will retrieve the existing Binance Client or create a new one
* @param {string} The api key, defaults to settings.binanceApiKey
* @param {string} The api key secret, defaults to settings.binanceApiSecret
* */
function getBinanceClient(apiKey, apiKeySecret) {
    if (!apiKey && !settings.binance_settings.binance_api_key) exit("Please specify a API key in the method call or settings file.")
    if (!apiKeySecret && !settings.binance_settings.binance_api_secret) exit("Please specify a API key secret in the method call or settings file.")
    if (!binanceClient) binanceClient = new Spot(apiKey || settings.binance_settings.binance_api_key, apiKeySecret || settings.binance_settings.binance_api_secret)
    return binanceClient
}

/*
* This function will return the Account info of the connected Spot account / Binance Client
*
* */
const getBinanceAccountInfo = async () => {
    const response = await getBinanceClient().account().catch(err => printMessage(err['data']))
    printMessage(response.data)
    return response.data
}

/*
* This function will withdraw funds from Binance to a wallet/network specified
* @param {string} coinName -- the name of the coin to send
* @param {string} network -- the network to withdraw funds on. default is `return with default network of the coin`
* @param {string} address -- the address to withdraw funds to.
* @param {decimal} amount -- the amount of coin to send
* @param {long} timestamp -- the timestamp of the transaction
* */
const withdrawFromBinance = async (coinName, network, address, amount) => {
    const response = await getBinanceClient().withdraw(coinName.toUpperCase(), address, amount, { network: network.toUpperCase() }).catch(err => printMessage(err))
    return response.data
}

const getTransactionHash = async (transactionId) => {
    const payloads = await getBinanceClient().withdrawHistory().catch(err => printMessage(err))
    response = payloads['data'].find(transaction => transaction.id == transactionId)
    return response ? response.txId : exit("No transaction with id: " + transactionId)
}

const getCoinInfo = async (coin) => {
    const coinInfoPayloads = await getBinanceClient().coinInfo()
    desiredCoinInfo = coinInfoPayloads['data'].find(coinInfoPayload => coinInfoPayload.coin.toLowerCase() == coin)
    return desiredCoinInfo
}

/*
*
*
*
*
*
*
* */

function main() {
  
}

main()
