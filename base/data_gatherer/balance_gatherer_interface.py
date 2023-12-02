from abc import ABC, abstractmethod
from base.data_gatherer.data_gatherer_interface import IDataGatherer


class IBalanceGatherer(IDataGatherer, ABC):
    @abstractmethod
    async def gather(address: str, tokens: list[str]) -> list[int]:
        pass
