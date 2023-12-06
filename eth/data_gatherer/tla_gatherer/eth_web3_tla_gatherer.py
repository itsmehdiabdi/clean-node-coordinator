from base.data_gatherer.data_gatherer import (
    DataGatherer,
    TlaInput,
    TlaOutput,
)
from web3 import AsyncWeb3, AsyncHTTPProvider


class EthWeb3TlaGatherer(DataGatherer[TlaInput, TlaOutput]):
    def __init__(self, data):
        super().__init__()
        self.web3 = AsyncWeb3(AsyncHTTPProvider(data["nodeRpc"]))

    # TODO: error handling
    async def gather(self, input: TlaInput) -> TlaOutput:
        address = input["address"]
        tla = await self.web3.eth.get_transaction_count(address)

        return {"success": True, "data": tla}
