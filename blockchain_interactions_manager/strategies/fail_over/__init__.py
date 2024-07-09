from typing import TypeVar

from blockchain_interactions_manager.interfaces.strategy import Strategy

T = TypeVar("T")


class FailOver(Strategy[T]):
    def run(self, functions, *args) -> T:
        for function in functions:
            try:
                response = function(*args)
                return response
            except Exception as error:
                print(error)

        raise Exception("Could not get response from any providers!")
