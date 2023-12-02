from base.data_gatherer.balance_gatherer_interface import IBalanceGatherer
import json
from base.abis.erc20 import erc20_abi

from web3 import AsyncWeb3, AsyncHTTPProvider


class EthWeb3BalanceGatherer(IBalanceGatherer):
    def __init__(self, nodeRpc):
        super().__init__()
        self.web3 = AsyncWeb3(AsyncHTTPProvider(nodeRpc))
        self.erc20_abi = erc20_abi

    # TODO: error handling
    async def gather(self, address: str, tokens: list[str]) -> dict[str, int]:
        return [
            await self.web3.eth.contract(address=token, abi=self.erc20_abi).functions.balanceOf(address).call()
            if token == "0x" + 40 * "0"
            else await self.web3.eth.get_balance(address)
            for token in tokens
        ]