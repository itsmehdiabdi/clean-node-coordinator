from eth.data_gatherer.balance_gatherer.eth_http_balance_gatherer import (
    EthHttpBalanceGatherer,
)
from eth.data_gatherer.balance_gatherer.eth_web3_balance_gatherer import (
    EthWeb3BalanceGatherer,
)

mapper = {"HTTP": EthHttpBalanceGatherer, "WEB3": EthWeb3BalanceGatherer}
