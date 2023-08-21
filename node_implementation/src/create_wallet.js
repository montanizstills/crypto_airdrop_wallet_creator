const { ethers } = require('ethers');
const fs = require('fs');
const fastcsv = require('fast-csv');

const NUM_WALLETS = 100;
const FILE_NAME = 'wallets.csv';

let wallets = [];

// Check if the CSV file already exists
if (fs.existsSync(FILE_NAME)) {
  const stream = fs.createReadStream(FILE_NAME);
  const csvData = [];
  
  // Load the existing wallets
  fastcsv
    .parseStream(stream, { headers: true })
    .on('data', (data) => {
      csvData.push(data);
    })
    .on('end', () => {
      wallets = csvData;
      generateWallets();
    });
} else {
  generateWallets();
}

function generateWallets() {
    // Generate wallets
    const existingAddresses = new Set(wallets.map(wallet => wallet.address));
    while (wallets.length < NUM_WALLETS) {
      const wallet = ethers.Wallet.createRandom();
      if (!existingAddresses.has(wallet.address)) {
        wallets.push({ address: wallet.address, privateKey: wallet.privateKey });
        existingAddresses.add(wallet.address);
      }
    }
  
    // Write wallets to CSV file
    const ws = fs.createWriteStream(FILE_NAME);
    fastcsv
      .write(wallets, { headers: true })
      .pipe(ws)
      .on('finish', () => console.log(`Wrote ${NUM_WALLETS} wallets to ${FILE_NAME}`));
}