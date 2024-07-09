from blockchain_interactions_manager.interfaces.manager import (
    Manager as ManagerInterface,
)
from blockchain_interactions_manager.types.network import Network
from blockchain_interactions_manager.types.manager import Config, Connectors
from blockchain_interactions_manager.types.requirement import Requirement


class Manager(ManagerInterface):
    def __init__(
        self,
        network: Network,
        connectors: Connectors,
        config: Config,
    ) -> None:
        self.network = network
        self.connectors = connectors
        self.config = config
        self._validate_properties()

    def get_balance(self, requirement: Requirement, wallet_address: str) -> int:
        connector_name = self.config.get(requirement).get("connector_name")
        connector = self.connectors.get(connector_name)
        strategy = self.config.get(requirement).get("strategy")

        return connector.get_balance(self.network, strategy, wallet_address)

    def _validate_properties(self):
        self._check_config_for_invalid_connector_name()

    def _check_config_for_invalid_connector_name(self):
        connector_names = self.connectors.keys()
        for requirement in self.config:
            connector_name = self.config.get(requirement).get("connector_name")
            if connector_name not in connector_names:
                raise Exception(
                    f"invalid connector: {connector_name} for requirement: ({requirement})"
                )
