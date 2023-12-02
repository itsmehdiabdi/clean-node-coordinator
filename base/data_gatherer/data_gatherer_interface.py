from abc import ABC, abstractmethod


class IDataGatherer(ABC):
    @abstractmethod
    async def gather():
        pass
