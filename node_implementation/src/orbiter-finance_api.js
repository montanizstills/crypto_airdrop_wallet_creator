const orbiter = require('orbiter-sdk')
const { ethers, Signers } = require('ethers')
const { web3, Web3BaseProvider, HttpProvider, default: Web3 } = require('web3')

let mainnetBridge
let network
let web3Instance

/**
 * The type of network to create a bridge object on.
 * @param {string} network Either 'Mainnet' or 'Testnet'
 * @returns {orbiter.Bridge} The Orbiter SDK bridge object with the associated `network`
 */
const getMainnetBridge = (network) => {
    if (!network) this.network = network
    if (!mainnetBridge) mainnetBridge = new orbiter.Bridge(this.network)
    return mainnetBridge
}

/**
 * Transfer an amount of `coin` from `fromChain` to `toChain`
 * @param {*} signer 
 * @param {orbiter.BridgeToken} token 
 * @param {orbiter.BridgeChain} fromChain 
 * @param {orbiter.BridgeChain} toChain 
 * @param {string | number} amountBasedETH 
 */
const transferToken = async (signer, token, fromChain, toChain, amountBasedETH) => {
    const response = await getMainnetBridge().transfer(signer, token, fromChain, toChain, amountBasedETH)
    return response
}


const getWeb3Instance = async () => {
    if (!web3Instance) web3Instance = new Web3(remoteProvider);
    return web3Instance
}

