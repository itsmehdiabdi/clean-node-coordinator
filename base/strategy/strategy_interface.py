from abc import ABC, abstractmethod
from base.data_gatherer.data_gatherer import DataGatherer


class Strategy(ABC):
    @abstractmethod
    async def execute(dataGatherers: list[DataGatherer], *args, **kwargs):
        pass
