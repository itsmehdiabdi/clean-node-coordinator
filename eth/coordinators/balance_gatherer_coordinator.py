from base.data_gatherer.data_gatherer import DataGatherer, BalanceInput, BalanceOutput
from eth.data_gatherer.balance_gatherer.eth_balance_gatherer import eth_balance_gatherer


class BalanceGathererCoordinator(DataGatherer[BalanceInput, BalanceOutput]):
    async def gather(self, input: BalanceInput) -> BalanceOutput:
        return await eth_balance_gatherer.gather(input)
