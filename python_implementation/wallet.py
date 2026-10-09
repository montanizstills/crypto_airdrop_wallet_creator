import logging
import time

import hdwallet.hdwallet
import requests
from hdwallet.utils import generate_entropy
from web3 import Web3, HTTPProvider
from web3.middleware import construct_sign_and_send_raw_middleware

from python_implementation.utils.utils import print_and_log


def create_wallet():
    wallet = hdwallet.HDWallet("ETH")
    wallet.from_entropy(generate_entropy(), passphrase="cheese_chasers")
    print_and_log(logging.INFO, f"Created wallet: {wallet.dumps()}")
    return wallet


def get_wallet(private_key: str):
    wallet = hdwallet.HDWallet("ETH")
    print_and_log(logging.DEBUG, f'found wallet {wallet.private_key()}')
    return wallet.from_private_key(private_key)


def get_gas():
    # if tx:
    #     transaction_fee = protocol.eth.generate_gas_price(tx)
    response = requests.get(
        f'https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=<etherscan-api-key>')
    print_and_log(logging.DEBUG, response.text)
    fast = response.json()['fastgasprice']  # json.loads
    suggested = response.json()['proposegasprice']  # json.loads
    slow = response.json()['safegasprice']  # json.loads
    print_and_log(logging.INFO, f"Slow: {slow}, Mid: {suggested}, Fast: {fast}")


def send_transaction(
        network: str,  # "https://mainnet.infura.io/v3/<API-KEY>"
        source_pk, dest_address: str, amount: any, max_gas: int, gas_bid
):
    protocol = Web3(HTTPProvider(network))
    if not protocol.is_connected():
        print_and_log(logging.ERROR, f"Protocol not connected. Please check {network}.")
        exit(f"Protocol not connected. Please check {network}.")

    # try-catch account creation && address validation
    account = protocol.eth.account.from_key(source_pk)  # can use wallet.someMethod()?
    protocol.eth.default_account = account.address  # middleware
    protocol.middleware_onion.add(construct_sign_and_send_raw_middleware(account))  # middleware

    dest_address_in_bytes = protocol.to_checksum_address(dest_address)
    # from ens.auto import ns, address = ns.address('alice.eth'), https://docs.ens.domains/dapp-developer-guide/working-with-ens

    print_and_log(logging.INFO,
                  f"Wallet: '{account.address}', has a balance of {protocol.eth.get_balance(dest_address_in_bytes)} wei.")
    print_and_log(logging.INFO, f"Attempting to sending {amount} to {dest_address}.")

    tx = {
        'nonce': protocol.eth.get_transaction_count(dest_address_in_bytes) + time.time_ns() + 1,
        'to': dest_address_in_bytes,
        'value': amount,
        'gas': max_gas,
        'gasPrice': gas_bid
    }
    # transaction_fee_estimate = tx['gas'] * (tx['gasPrice'] + tx['value'])
    transaction_hash = protocol.eth.send_transaction(tx)
    print_and_log(logging.INFO, f"Sent transaction hash: {transaction_hash.hex()}")

    # save receipt
    receipt = protocol.eth.wait_for_transaction_receipt(transaction_hash)
    print_and_log(logging.INFO, receipt)
    return receipt


def get_protocol():
    return Web3(HTTPProvider("https://rpc-testnet.kcc.network"))  # network/exchange protocol


def bridge():
    pass


def swap():
    pass


def get_transaction_count(address):
    return get_protocol().eth.get_transaction_count(address)

def get_account_balance(address):
    return get_protocol().eth.get_balance(address)



if __name__ == "__main__":
