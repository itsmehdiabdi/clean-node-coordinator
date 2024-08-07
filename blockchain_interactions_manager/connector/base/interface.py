from abc import abstractmethod

from ..base.type import Connection
from ...api_service import Network
from ...strategy import StrategyType
from ...utils import Singleton


class Connector(metaclass=Singleton):
    """
    Description
    ----------
    A Connector abstracts the connection to the workers. so manager doesn't know anything about connection type.
    we may connect to worker with a queue, http request, direct function call to local worker, ... .

    Attributes
    ----------
    connection: Connection
        specifies the connection type that the connector handles

    Methods
    -------
    def get_balance(
        self, network: Network, strategy: StrategyType, wallet_address: str
    ) -> int:
        connects to worker.

        returns wallet_address's native balance.
    """

    connection: Connection

    @abstractmethod
    def get_balance(
        self, network: Network, strategy: StrategyType, wallet_address: str
    ) -> int:
        pass
