from abc import ABC, abstractmethod
from typing import TypedDict, Generic, TypeVar

Input = TypeVar("Input")
Output = TypeVar("Output")


class DataGatherer(ABC, Generic[Input, Output]):
    @abstractmethod
    def gather(input: Input) -> Output:
        pass


class BalanceInput(TypedDict):
    address: str
    tokens: list[str]


class TlaInput(TypedDict):
    address: str


class BalanceOutput(TypedDict):
    success: bool
    balances: list[int]


class TlaOutput(TypedDict):
    success: bool
    tla: int
