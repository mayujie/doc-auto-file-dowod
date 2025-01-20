from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Optional, Dict


class AbstractInfo(ABC):
    @abstractmethod
    def to_placeholder_mapping(self) -> Dict[str, Optional[str]]:
        """
        Abstract method to return a dictionary mapping placeholders to their corresponding values.
        Must be implemented by subclasses.
        """
        pass
