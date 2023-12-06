from base.data_gatherer.data_gatherer import DataGatherer
from base.strategy.strategy_interface import Strategy
from typing import TypeVar, Generic

Input = TypeVar("Input")
Output = TypeVar("Output")


class StrategicalDataGatherer(Generic[Input, Output], DataGatherer[Input, Output]):
    gatherers = list[DataGatherer[Input, Output]]
    strategy: Strategy

    def __init__(
        self, gatherers: list[DataGatherer[Input, Output]], strategy: Strategy
    ):
        self.gatherers = gatherers
        self.strategy = strategy

    async def gather(self, input: Input) -> Output:
        return await self.strategy.execute(self.gatherers, input)
