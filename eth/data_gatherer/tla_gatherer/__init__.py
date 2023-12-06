from eth.data_gatherer.tla_gatherer.eth_http_tla_gatherer import EthHttpTlaGatherer
from eth.data_gatherer.tla_gatherer.eth_web3_tla_gatherer import EthWeb3TlaGatherer

mapper = {"HTTP": EthHttpTlaGatherer, "WEB3": EthWeb3TlaGatherer}
