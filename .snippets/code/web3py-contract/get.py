# 1. Import the ABI
from compile import abi
from web3 import Web3

# 2. Add the Web3 provider logic here:
provider_rpc = {
    'development': 'http://localhost:9944',
    'alphanet': 'https://rpc.api.moonbase.moonbeam.network',
}
web3 = Web3(Web3.HTTPProvider(provider_rpc['development']))  # Change to correct network

# 3. Create address variable
contract_address = 'CONTRACT_ADDRESS_HERE'

print(f'Making a call to contract at address: { contract_address }')

# 4. Create contract instance
Incrementer = web3.eth.contract(address=contract_address, abi=abi)

# 5. Call Contract
number = Incrementer.functions.number().call()
print(f'The current number stored is: { number } ')