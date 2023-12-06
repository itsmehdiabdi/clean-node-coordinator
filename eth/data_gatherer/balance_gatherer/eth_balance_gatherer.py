from base.data_gatherer.strategical_data_gatherer import StrategicalDataGatherer
from base.data_gatherer.data_gatherer import BalanceInput, BalanceOutput
from eth.data_gatherer.balance_gatherer import mapper as data_gatherer_mapper
from base.strategy import mapper as strategy_mapper


def getBalanceGatherer(node_settings, worker_settings):
    balance_gatherers = [
        data_gatherer_mapper[node_settings[provider]["type"]](node_settings[provider]["data"])
        for provider in worker_settings["providers"]
    ]
    strategy = strategy_mapper[worker_settings["strategy"]]()
    return StrategicalDataGatherer[BalanceInput, BalanceOutput](
        balance_gatherers, strategy
    )


# imagine these are read from settings!
node_settings = {
    "h1": {
        "type": "HTTP",
        "data": {
            "nodeRpc": "https://mainnet.infura.io/v3/522edcde5a9445eeb3e2b0249e55db73"
        },
    },
    "w1": {
        "type": "WEB3",
        "data": {
            "nodeRpc": "https://mainnet.infura.io/v3/44a735d4387b48a2b5024f16b3159611"
        },
    },
}

worker_settings = {"strategy": "FIRST_COMPLETED", "providers": ["h1", "w1"]}

eth_balance_gatherer = getBalanceGatherer(node_settings, worker_settings)
