from base.data_gatherer.tla_gatherer_interface import ITlaGatherer
from web3 import AsyncWeb3, AsyncHTTPProvider


class EthWeb3TlaGatherer(ITlaGatherer):
    def __init__(self, nodeRpc):
        super().__init__()
        self.web3 = AsyncWeb3(AsyncHTTPProvider(nodeRpc))

    # TODO: error handling
    async def gather(self, address):
        return await self.web3.eth.get_transaction_count(address)
