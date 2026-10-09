const {Alchemy, fromHex, Network} = require('alchemy-sdk');
const {printMessage, exit} = require('../utils/utils.js')
const settings = require('../../resources/settings.json')
const {alchemy_helper} = require('../src/alchemy_helper.js')
const {Spot} = require('@binance/connector')


// get command line arguments
const args = require('minimist')(process.argv.slice(2))

// assign blockChain operator api key
if (!args['alchemy_api_key'] && !settings.alchemy_settings.apiKey) exit("Please provide API key.")
const alchemy = new Alchemy(
    {
        "apiKey": settings.alchemy_settings.apiKey,
        // "network": alchemy_helper.getAlchemyNetwork(settings.alchemy_settings.network)
        "network": Network.ARB_GOERLI
    }
);

// printMessage(alchemy.config.apiKey)
// printMessage(alchemy.config.network)








