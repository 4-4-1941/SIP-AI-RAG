from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class ProviderResponse:
    text: str
    provider: str
    model: str

class LLMProvider(ABC):
    @abstractmethod
    async def chat(self, message: str) -> ProviderResponse:
        raise NotImplementedError
