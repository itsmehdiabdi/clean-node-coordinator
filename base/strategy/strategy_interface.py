from abc import ABC, abstractmethod
from base.data_gatherer.data_gatherer_interface import IDataGatherer


class IStrategy(ABC):
    @abstractmethod
    async def execute(dataGatherers: list[IDataGatherer], *args, **kwargs):
        pass
