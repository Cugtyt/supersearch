"""Aggregator."""

from abc import abstractmethod
from asyncio import Task
from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict

from massivesearch.search_engine.base import SearchResT

type MassiveSearchTasks[T] = list[dict[str, Task[T]]]


AggResT = TypeVar("AggResT")


class BaseAggregator(BaseModel, Generic[SearchResT, AggResT]):
    """Aggregator class."""

    model_config = ConfigDict(extra="ignore")

    @abstractmethod
    async def aggregate(
        self,
        tasks: MassiveSearchTasks[SearchResT],
    ) -> AggResT:
        """Aggregate the search results."""
