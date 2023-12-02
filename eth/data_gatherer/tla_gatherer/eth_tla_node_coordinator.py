from base.data_gatherer.tla_gatherer_interface import ITlaGatherer
from eth.data_gatherer.tla_gatherer.eth_http_tla_gatherer import EthHttpTlaGatherer
from eth.data_gatherer.tla_gatherer.eth_web3_tla_gatherer import EthWeb3TlaGatherer
from base.strategy.first_completed_strategy import FirstCompletedStrategy


class EthTlaNodeCoordinator(ITlaGatherer):
    tlaGatherers = list[ITlaGatherer]

    def __init__(self) -> None:
        self.strategy = FirstCompletedStrategy()
        self.tlaGatherers = []
        # TODO: move node configs to settings
        self.tlaGatherers.append(
            EthHttpTlaGatherer(
                "https://mainnet.infura.io/v3/522edcde5a9445eeb3e2b0249e55db73"
            )
        )
        self.tlaGatherers.append(
            EthWeb3TlaGatherer(
                "https://mainnet.infura.io/v3/44a735d4387b48a2b5024f16b3159611"
            )
        )

    async def gather(self, address: str) -> int:
        return await self.strategy.execute(self.tlaGatherers, address)
