from base.data_gatherer.balance_gatherer_interface import IBalanceGatherer
from aiohttp import ClientSession
import json


class EthHttpBalanceGatherer(IBalanceGatherer):
    def __init__(self, nodeRpc):
        super().__init__()
        self.nodeRpc = nodeRpc

    # TODO: error handling
    async def gather(self, address: str, tokens: list[str]) -> dict[str, int]:
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

            return balances
