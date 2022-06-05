from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entity import Entity

from components.base_component import BaseComponent

class Skill(BaseComponent):
    parent: Entity

    def __init__(self, name: str = "<Unnamed Trait>"):
        self.name = name