const Kucoin = require('kucoin-node-sdk');

// Initialize the Kucoin SDK with the configuration from config.js
Kucoin.init(require('./config'));

// Define withdrawal parameters
const currency = 'ARB';
const address = ''; // replace with your BSC wallet address
const amount = ''; // replace with the amount of ETH you want to withdraw
const options = {
  chain: 'arbitrum',
  isInner: false, // specify if the withdrawal is to another Kucoin account
  remark: '', // add a remark to the withdrawal
};

// Apply the withdrawal
const main = async () => {
  const response = await Kucoin.rest.User.Withdrawals.applyWithdraw(currency, address, amount, options);
  console.log(response);
};

main().catch(console.error);