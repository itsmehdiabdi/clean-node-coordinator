from base.data_gatherer.data_gatherer_interface import IDataGatherer
from base.strategy.strategy_interface import IStrategy
import asyncio


class FirstCompletedStrategy(IStrategy):
    async def execute(self, dataGatherers: list[IDataGatherer], *args, **kwargs):
        tasks = [dataGatherer.gather(*args, **kwargs) for dataGatherer in dataGatherers]
        while tasks:
            doneTasks, pendingTasks = await asyncio.wait(
                tasks, timeout=20, return_when=asyncio.FIRST_COMPLETED
            )
            for doneTask in doneTasks:
                result = doneTask.result()
                if result is not None:
                    for pendingTask in pendingTasks:
                        pendingTask.cancel()
                    if len(pendingTasks):
                        await asyncio.wait(pendingTasks)
                    return result

            tasks = pendingTasks
