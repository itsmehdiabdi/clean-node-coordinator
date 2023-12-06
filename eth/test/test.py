from eth.coordinators.tla_gatherer_coordinator import TlaGathererCoordinator
from eth.coordinators.balance_gatherer_coordinator import BalanceGathererCoordinator
import asyncio


async def run():
    print(
        await TlaGathererCoordinator().gather(
            {"address": "0xF977814e90dA44bFA03b6295A0616a897441aceC"},
        )
    )

    print(
        await BalanceGathererCoordinator().gather(
            {
                "address": "0xF977814e90dA44bFA03b6295A0616a897441aceC",
                "tokens": [
                    "0xdAC17F958D2ee523a2206206994597C13D831ec7",
                    "0x0000000000000000000000000000000000000000",
                ],
            }
        )
    )


asyncio.run(run())
