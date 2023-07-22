import hdwallet.hdwallet
import requests
from hdwallet.utils import generate_entropy
from web3 import Web3, HTTPProvider
from web3.main import BaseWeb3


def create_wallet():
    wallet = hdwallet.HDWallet("ETH")
    wallet.from_entropy(generate_entropy(), passphrase="cheese_chasers")
    print(f"Created wallet: {wallet.dumps()}")
    return wallet


def send_transaction(wallet: hdwallet.HDWallet, network: str, address, send_to: str, amount: BaseWeb3, max_gas: int,
                     gas_price):
    protocol = Web3(HTTPProvider(network))  # "https://mainnet.infura.io/v3/<API-KEY>"
    nonce = protocol.eth.get_transaction_count(address)  # 0xabc123
    tx = {
        'nonce': None,
        'to': send_to,
        'value': amount,
        'gas': max_gas,
        'gasPrice': Web3.to_wei(gas_price, 'gwei')
    }
    signed_tx = Web3.eth.account.sign_transaction(tx, wallet.private_key())
    sent_tx = Web3.eth.send_raw_transaction(signed_tx)
    print(f"Sent transaction hash: {Web3.to_hex(sent_tx)}")
    return Web3.to_hex(sent_tx)


def get_gas():
    response = requests.get(
        f'')  # https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=YourApiKeyToken
    fast = response.json()['fastgasprice']  # json.loads
    suggested = response.json()['proposegasprice']  # json.loads
    slow = response.json()['safegasprice']  # json.loads
    print(f"Slow: {slow}, Mid: {suggested}, Fast: {fast}")


if __name__ == "__main__":
    pass
