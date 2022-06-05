from __future__ import annotations

from typing import TYPE_CHECKING, List
from components.skill import Skill

if TYPE_CHECKING:
    from entity import Entity

from components.base_component import BaseComponent

class Mind(BaseComponent):
    parent: Entity

    def __init__(self):
        self.skills: List[Skill] = []

    def learn_skill(self, skill: Skill) -> None:
        """
        Removes an item from the inventory and restores it to the game map, at the player's current location.
        """
        self.skills.append(skill)
        self.engine.message_log.add_message(f"{self.parent.name} learned {skill.name}!")