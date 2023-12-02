from eth.data_gatherer import EthBalanceNodeCoordinator, EthTlaNodeCoordinator
import asyncio

tla = EthTlaNodeCoordinator()
balance = EthBalanceNodeCoordinator()

print(
    "tla",
    asyncio.run(
        tla.gather(
            address="0xF977814e90dA44bFA03b6295A0616a897441aceC",
        )
    ),
)

print(
    "balance",
    asyncio.run(
        balance.gather(
            address="0xF977814e90dA44bFA03b6295A0616a897441aceC",
            tokens=[
                "0xdac17f958d2ee523a2206206994597c13d831ec7",
                "0x0000000000000000000000000000000000000000",
            ],
        )
    ),
)
