from base.data_gatherer.balance_gatherer_interface import IBalanceGatherer
from eth.data_gatherer.balance_gatherer.eth_http_balance_gatherer import (
    EthHttpBalanceGatherer,
)
from eth.data_gatherer.balance_gatherer.eth_web3_balance_gatherer import (
    EthWeb3BalanceGatherer,
)
from base.strategy.first_completed_strategy import FirstCompletedStrategy


class EthBalanceNodeCoordinator(IBalanceGatherer):
    balanceGatherers = list[IBalanceGatherer]

    def __init__(self) -> None:
        self.strategy = FirstCompletedStrategy()
        self.balanceGatherers = []
        # TODO: move node configs to settings
        self.balanceGatherers.append(
            EthHttpBalanceGatherer(
                "https://mainnet.infura.io/v3/522edcde5a9445eeb3e2b0249e55db73"
            )
        )
        self.balanceGatherers.append(
            EthWeb3BalanceGatherer(
                "https://mainnet.infura.io/v3/44a735d4387b48a2b5024f16b3159611"
            )
        )

    async def gather(self, address: str, tokens: list[str]) -> list[int]:
        return await self.strategy.execute(self.balanceGatherers, address, tokens)
