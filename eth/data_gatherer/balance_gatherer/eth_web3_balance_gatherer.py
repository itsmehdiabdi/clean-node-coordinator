from base.data_gatherer.data_gatherer import (
    DataGatherer,
    BalanceInput,
    BalanceOutput,
)
from base.abis.erc20 import erc20_abi

from web3 import AsyncWeb3, AsyncHTTPProvider


class EthWeb3BalanceGatherer(DataGatherer[BalanceInput, BalanceOutput]):
    def __init__(self, data):
        super().__init__()
        self.web3 = AsyncWeb3(AsyncHTTPProvider(data["nodeRpc"]))
        self.erc20_abi = erc20_abi

    # TODO: error handling
    async def gather(self, input: BalanceInput) -> BalanceOutput:
        address, tokens = input["address"], input["tokens"]
        balances = [
            await self.web3.eth.contract(address=token, abi=self.erc20_abi)
            .functions.balanceOf(address)
            .call()
            if token != "0x" + 40 * "0"
            else await self.web3.eth.get_balance(address)
            for token in tokens
        ]

        return {"success": True, "data": balances}
