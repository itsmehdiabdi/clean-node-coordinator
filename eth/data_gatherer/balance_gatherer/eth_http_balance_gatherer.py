from base.data_gatherer.data_gatherer import (
    DataGatherer,
    BalanceInput,
    BalanceOutput,
)
from aiohttp import ClientSession
import json


class EthHttpBalanceGatherer(DataGatherer[BalanceInput, BalanceOutput]):
    def __init__(self, data):
        super().__init__()
        self.nodeRpc = data["nodeRpc"]

    # TODO: error handling
    async def gather(self, input: BalanceInput) -> BalanceOutput:
        address, tokens = input["address"], input["tokens"]
        balances = []
        async with ClientSession() as session:
            for token in tokens:
                if token == "0x" + 40 * "0":
                    response = await session.post(
                        url=self.nodeRpc,
                        json={
                            "jsonrpc": "2.0",
                            "method": "eth_getBalance",
                            "params": [
                                address,
                                "latest",
                            ],
                            "id": 1,
                        },
                        headers={"Content-Type": "application/json"},
                    )
                else:
                    data = "0x70a08231" + "000000000000000000000000" + address[2:]
                    response = await session.post(
                        url=self.nodeRpc,
                        json={
                            "jsonrpc": "2.0",
                            "method": "eth_call",
                            "params": [
                                {"to": token, "data": data},
                                "latest",
                            ],
                            "id": 1,
                        },
                        headers={"Content-Type": "application/json"},
                    )

                balances.append(int(json.loads(await response.text()).get("result"), 0))

            return {"success": True, "data": balances}
