const settings = require("../../resources/settings.json");
const { printMessage } = require("../utils/utils");
const { Network } = require("alchemy-sdk");
const wallet_public_address = settings.user_settings.wallet_address

async function getAccountTokenBalances(wallet_public_address) {
    return await alchemy.core.getTokenBalances(wallet_public_address)
}

async function getTokenMetaData(token_payload) {
    let contractAddress = await alchemy.core.getTokenMetadata(token_payload['contractAddress'])
    let legibleAmount = parseInt(token_payload['tokenBalance'], 16)
    printMessage(contractAddress)
    printMessage(legibleAmount)
}

function getAlchemyNetwork(network_string) {
    network_map = {
        'arb_goerli': Network.ARB_GOERLI,
        'arb_mainnet': Network.ARB_MAINNET,
        'eth_mainnet': Network.ETH_MAINNET,
        'myfunky': Network.ETH_GOERLI,
        'eth_sepolia': Network.ETH_SEPOLIA,
        'astar_mainnet': Network.ASTAR_MAINNET,
        'matic_mainnet': Network.MATIC_MAINNET,
        'matic_mumbai': Network.MATIC_MUMBAI,
        'opt_goerli': Network.OPT_GOERLI,
        'opt_mainnet': Network.OPT_MAINNET,
        'polygonzkevm_mainnet': Network.POLYGONZKEVM_MAINNET,
        'polygonzkevm_testnet': Network.POLYGONZKEVM_TESTNET,
    }
    return network_map[network_string.toLowerCase()]
}

module.exports = { getAlchemyNetwork: getAlchemyNetwork }