from base.data_gatherer.data_gatherer import (
    DataGatherer,
    TlaInput,
    TlaOutput,
)
from aiohttp import ClientSession
import json


class EthHttpTlaGatherer(DataGatherer[TlaInput, TlaOutput]):
    def __init__(self, data):
        super().__init__()
        self.nodeRpc = data["nodeRpc"]

    # TODO: error handling
    async def gather(self, input: TlaInput) -> TlaOutput:
        address = input["address"]
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

            tla = int(json.loads(await response.text()).get("result"), 0)

        return {"success": True, "data": tla}
