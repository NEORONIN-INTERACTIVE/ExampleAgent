"""
Example agent.
"""

from w4a import CompetitionAgent
from SimulationInterface import (
    Faction, PlayerEventCommit, AdversaryContact, EntitySpawned, 
    ComponentSpawned, ControllableEntity, UnitEngagement, UnitWeaponUsage
)


class MyAgent(CompetitionAgent):
    """
    Example agent that randomly performs operations.
    
    """
    
    def __init__(self, faction: Faction, config):
        super().__init__(faction, config)
        
        self.log("Constructed my agent")
    
    @property
    def log_prefix(self):
        """Prefix for log messages (matches original)."""
        # frame_index comes from SimAgent base class
        return f"{self.faction.name} {self.__class__.__name__} (frame {self._sim_agent.frame_index}): "
    
    def log(self, message):
        """Log a message with faction prefix."""
        print(f"{self.log_prefix}{message}")
    
    def select_action(self, observation):
        return super().select_action(observation)

