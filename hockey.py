from enum import Enum
from typing import Optional
from athlete import Athlete

class HockeyPosition(Enum):
    FORWARD = "Forward"
    DEFENSEMAN = "Defenseman"
    GOALIE = "Goalie"

class HockeyPlayer(Athlete):
    
    def __init__(
        self, 
        name : str, 
        age : int, 
        country : Optional[str] = None, 
        salary : Optional[float] = None,
        team : Optional[str] = None, 
        position : Optional[str] = None, 
        goal_scored : Optional[int] = None, 
        stick_brand : Optional[str] = None, 
        skates_size : Optional[int] = None
    ):

        super().__init__(name, age, country, salary)
        self._team = team
        self._position = HockeyPosition(position)
        self._goal_scored = goal_scored
        self._stick_brand = stick_brand
        self._skates_size = skates_size
            
    def print_stats(self):
        goals = self._goal_scored if self._goal_scored is not None else 0
        team = self._team if self._team else "Unknown Team"
        position = self._position if self._position else "Unknown Position"
        print(f"{self.name} scored {goals} goals for {team} as a {position}.")

    def print_endorsement(self):
        if self._stick_brand:
            print(f"{self.name} endorses {self._stick_brand} sticks.")
        else:
            print(f"{self.name} has no stick endorsement.")

    @staticmethod
    def parse(raw_data: str) -> "HockeyPlayer":
        try:
            position, data = raw_data.split(":", 1)
            if position.strip() != "HockeyPlayer":
                raise ValueError("Invalid position for HockeyPlayer")
            
            player_data = [item.strip() for item in data.split(",")]
            name = player_data[0]
            age = int(player_data[1])
            country = player_data[2] if len(player_data) > 2 else None
            salary = float(player_data[3]) if len(player_data) > 3 else None
            team = player_data[4] if len(player_data) > 4 else None
            position = player_data[5] if len(player_data) > 5 else None
            goal_scored = int(player_data[6]) if len(player_data) > 6 else None
            stick_brand = player_data[7] if len(player_data) > 7 else None
            skates_size = int(player_data[8]) if len(player_data) > 8 else None

            return HockeyPlayer(
                name=name, 
                age=age, 
                country=country, 
                salary=salary, 
                team=team, 
                position=position, 
                goal_scored=goal_scored, 
                stick_brand=stick_brand, 
                skates_size=skates_size
            )
        
        except Exception as e:
            print(f"Error parsing HockeyPlayer data: {e}")
            return None
