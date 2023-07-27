import logging
import os
import time

import hdwallet.hdwallet
import requests
from hdwallet.utils import generate_entropy
from web3 import Web3, HTTPProvider
from web3.main import BaseWeb3
from web3.middleware import construct_sign_and_send_raw_middleware

from utils.utils import print_and_log


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
        source_pk, dest_address: str, amount: str | BaseWeb3, coin: str, max_gas: int, gas_bid
):
    protocol = Web3(HTTPProvider(network))
    if not protocol.is_connected():
        print_and_log(logging.ERROR, f"Protocol not connected. Please check {network}.")
        exit(f"Protocol not connected. Please check {network}.")

    # try-catch account creation && address validation
    account = protocol.eth.account.from_key(source_pk)  # can use wallet.someMethod()?
    dest_address_in_bytes = protocol.to_checksum_address(dest_address)
    # from ens.auto import ns, address = ns.address('alice.eth'), https://docs.ens.domains/dapp-developer-guide/working-with-ens

    print_and_log(logging.INFO,
                  f"Wallet: '{account.address}', has a balance of {protocol.eth.get_balance(dest_address_in_bytes)}")
    print_and_log(logging.INFO, f"Attempting to sending {amount} {coin} to {dest_address}.")


    tx = {
        'nonce': protocol.eth.get_transaction_count(dest_address_in_bytes) + time.time_ns() + 1,
        'to': dest_address_in_bytes,
        'value': Web3.to_wei(1, coin),
        'gas': Web3.to_wei(max_gas, coin),
        'gasPrice': Web3.to_wei(gas_bid, coin)
    }
    # transaction_fee_estimate = protocol.eth.estimate_gas(tx) # tx['gas'] * (tx['gasPrice'] + tx['value'])
    transaction_fee = protocol.eth.generate_gas_price(tx)  # web3.gas_strategies.time_based.fast_gas_price_strategy
    print(f"Transaction min price: {transaction_fee}")

    # sign and send transactions
    # protocol.eth.default_account = account.address
    # protocol.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
    # signed_tx = protocol.eth.sign_transaction()
    # sent_tx = protocol.eth.send_transaction(tx)

    # print_and_log(logging.INFO, f"Sent transaction hash: {protocol.to_hex(sent_tx)}")
    # return protocol.to_hex(sent_tx)


def get_protocol():
    return Web3(HTTPProvider(os.environ.get('kcc_testnet_url')))  # network/exchange protocol


def bridge():
    pass


def swap():
    pass


if __name__ == "__main__":
    coin_type = 'gether'
    send_transaction(
        "https://rpc-testnet.kcc.network",
        '36fc2383ca9b0860b3a35a8d0562faf92805c26cb3f7ed7bf27ff931fede8257',
        '0x0a45Ef5ec2f8DF92E4BC2d1C881A2e446Ef94F4B',
        '20',
        coin_type,
        1,
        1
    )
