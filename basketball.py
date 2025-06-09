from typing import Optional
from ball import BallPlayer

class BasketballPlayer(BallPlayer):
    total_basketball_players = 0

    def __init__(
        self,
        name: str,
        age: int,
        team_name: str,
        jersey_number: str,
        country: Optional[str] = None,
        salary: Optional[float] = None,
        endorsement: Optional[str] = None,
        three_point_pct: Optional[float] = None,
        rebounds: Optional[int] = None,
    ):
        super().__init__(name, age, team_name, jersey_number, country, salary, endorsement)
        self._three_point_pct = three_point_pct
        self._rebounds = rebounds

        BasketballPlayer.total_basketball_players += 1
        BasketballPlayer.print_creation_log(self)

    def print_stats(self):
        three_point_pct = self._three_point_pct if self._three_point_pct is not None else 0.0
        rebounds = self._rebounds if self._rebounds is not None else 0
        print(f"{self.name} has a three-point percentage of {three_point_pct:.2f} and {rebounds} rebounds.")

    @staticmethod
    def print_creation_log(instance):
        print(f"Basketball Player '{instance.name}', {instance.age} created; total # of basketball players {BasketballPlayer.total_basketball_players}.")

    @staticmethod
    def parse(raw_data: str) -> "BasketballPlayer":
        try:
            prefix, data = raw_data.split(":", 1)
            if prefix.strip() != "BasketballPlayer":
                raise ValueError("Invalid player for BasketballPlayer")
            
            player_data = [item.strip() for item in data.split(",")]
            name = player_data[0]
            age = int(player_data[1])
            team_name = player_data[2]
            jersey_number = player_data[3]
            country = player_data[4] if len(player_data) > 4 and player_data[4] else None
            salary = float(player_data[5]) if len(player_data) > 5 and player_data[5] else None
            endorsement = player_data[6] if len(player_data) > 6 and player_data[6] else None
            three_point_pct = float(player_data[7]) if len(player_data) > 7 and player_data[7] else None
            rebounds = int(player_data[8]) if len(player_data) > 8 and player_data[8] else None

            return BasketballPlayer(
                name=name,
                age=age,
                team_name=team_name,
                jersey_number=jersey_number,
                country=country,
                salary=salary,
                endorsement=endorsement,
                three_point_pct=three_point_pct,
                rebounds=rebounds
            )
        except (ValueError, IndexError) as e:
            print(f"Error parsing BasketballPlayer data: {e}")
            return None
