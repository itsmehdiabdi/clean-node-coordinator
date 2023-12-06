from base.data_gatherer.data_gatherer import DataGatherer
from base.strategy.strategy_interface import Strategy
import asyncio


class FirstCompletedStrategy(Strategy):
    async def execute(self, dataGatherers: list[DataGatherer], *args, **kwargs):
        tasks = [dataGatherer.gather(*args, **kwargs) for dataGatherer in dataGatherers]
        while tasks:
            doneTasks, pendingTasks = await asyncio.wait(
                tasks, timeout=20, return_when=asyncio.FIRST_COMPLETED
            )
            for doneTask in doneTasks:
                result = doneTask.result()
                if result is not None and result["success"]:
                    for pendingTask in pendingTasks:
                        pendingTask.cancel()
                    if len(pendingTasks):
                        await asyncio.wait(pendingTasks)
                    return result

            tasks = pendingTasks
