from enum import Enum
from typing import Optional
from athlete import Athlete

class HockeyPosition(Enum):
    FORWARD = "Forward"
    DEFENSEMAN = "Defenseman"
    GOALIE = "Goalie"

class HockeyPlayer(Athlete):
    total_hockey_players = 0

    def __init__(
        self, 
        name : str, 
        age : int, 
        country : Optional[str] = None, 
        salary : Optional[float] = None,
        position : Optional[str] = None, 
        goal_scored : Optional[int] = None, 
        stick_brand : Optional[str] = None, 
        skates_size : Optional[int] = None
    ):
        super().__init__(name, age, country, salary)
        self._position = HockeyPosition(position) if position else None
        self._goal_scored = goal_scored
        self._stick_brand = stick_brand
        self._skates_size = skates_size

        HockeyPlayer.total_hockey_players += 1
        HockeyPlayer.print_creation_log(self)
            
    def print_stats(self):
        goals = self._goal_scored if self._goal_scored is not None else 0
        position = self._position.value if self._position else "Unknown Position"
        print(f"{self.name} scored {goals} goals as a {position}.")

    @staticmethod
    def print_creation_log(instance):
        print(f"Hockey Player '{instance.name}', {instance.age} created; total # of hockey players {HockeyPlayer.total_hockey_players}.")

    @staticmethod
    def parse(raw_data: str) -> "HockeyPlayer":
        try:
            prefix, data = raw_data.split(":", 1)
            if prefix.strip() != "HockeyPlayer":
                raise ValueError("Invalid player for HockeyPlayer")
            
            player_data = [item.strip() for item in data.split(",")]
            name = player_data[0]
            age = int(player_data[1])
            country = player_data[2] if len(player_data) > 2 and player_data[2] else None
            salary = float(player_data[3]) if len(player_data) > 3 and player_data[3] else None
            position = player_data[4] if len(player_data) > 4 and player_data[4] else None
            goal_scored = int(player_data[5]) if len(player_data) > 5 and player_data[5] else None
            stick_brand = player_data[6] if len(player_data) > 6 and player_data[6] else None
            skates_size = int(player_data[7]) if len(player_data) > 7 and player_data[7] else None

            return HockeyPlayer(
                name=name, 
                age=age, 
                country=country, 
                salary=salary, 
                position=position, 
                goal_scored=goal_scored, 
                stick_brand=stick_brand, 
                skates_size=skates_size
            )
        
        except Exception as e:
            print(f"Error parsing HockeyPlayer data: {e}")
            return None
