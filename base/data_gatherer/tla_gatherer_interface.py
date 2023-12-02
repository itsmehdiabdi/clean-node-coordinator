from abc import ABC, abstractmethod
from base.data_gatherer.data_gatherer_interface import IDataGatherer


class ITlaGatherer(IDataGatherer, ABC):
    @abstractmethod
    async def gather(address: str) -> int:
        pass
