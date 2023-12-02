from base.data_gatherer.tla_gatherer_interface import ITlaGatherer
from aiohttp import ClientSession
import json


class EthHttpTlaGatherer(ITlaGatherer):
    def __init__(self, nodeRpc):
        super().__init__()
        self.nodeRpc = nodeRpc

    # TODO: error handling
    async def gather(self, address):
        async with ClientSession() as session:
            response = await session.post(
                url=self.nodeRpc,
                json={
                    "jsonrpc": "2.0",
                    "method": "eth_getTransactionCount",
                    "params": [
                        address,
                        "latest",
                    ],
                    "id": 1,
                },
                headers={"Content-Type": "application/json"},
            )

            return int(json.loads(await response.text()).get("result"), 0)

