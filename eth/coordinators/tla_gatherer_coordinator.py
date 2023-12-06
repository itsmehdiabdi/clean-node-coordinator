from base.data_gatherer.data_gatherer import DataGatherer, TlaInput, TlaOutput
from eth.data_gatherer.tla_gatherer.eth_tla_gatherer import eth_tla_gatherer


class TlaGathererCoordinator(DataGatherer[TlaInput, TlaOutput]):
    async def gather(self, input: TlaInput) -> TlaOutput:
        return await eth_tla_gatherer.gather(input)
