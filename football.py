from typing import Optional
from ball import BallPlayer

class FootballPlayer(BallPlayer):
    total_football_players = 0

    def __init__(
        self,
        name: str,
        age: int,
        team_name: str,
        jersey_number: str,
        country: Optional[str] = None,
        salary: Optional[float] = None,
        endorsement: Optional[str] = None,
        touchdowns: Optional[int] = None,
        passing_yards: Optional[int] = None,
    ):
        super().__init__(name, age, team_name, jersey_number, country, salary, endorsement)
        self._touchdowns = touchdowns
        self._passing_yards = passing_yards

        FootballPlayer.total_football_players += 1
        FootballPlayer.print_creation_log(self)

    def print_stats(self):
        touchdowns = self._touchdowns if self._touchdowns is not None else 0
        passing_yards = self._passing_yards if self._passing_yards is not None else 0
        print(f"{self.name} scored {touchdowns} touchdowns and has passed {passing_yards} yards.")

    def decrement_counter(self):
        super().decrement_counter()
        FootballPlayer.total_football_players = max(0, FootballPlayer.total_football_players - 1)

    def __str__(self):
        values = [
            self._name,
            str(self._age),
            self._team_name or "",
            str(self._jersey_number) if self._jersey_number is not None else "",
            self._country or "",
            str(self._salary) if self._salary is not None else "",
            self._endorsement or "",
            str(self._touchdowns) if self._touchdowns is not None else "",
            str(self._passing_yards) if self._passing_yards is not None else "",
        ]
        return f"FootballPlayer: {','.join(values)}"

    
    @staticmethod
    def print_creation_log(instance):
        print(f"Football Player '{instance.name}', {instance.age} created; total # of football players {FootballPlayer.total_football_players}.")

    @staticmethod
    def parse(raw_data: str) -> "FootballPlayer":
        try:
            prefix, data = raw_data.split(":", 1)
            if prefix.strip() != "FootballPlayer":
                raise ValueError("Invalid player for FootballPlayer")
            
            player_data = [item.strip() for item in data.split(",")]
            name = player_data[0]
            age = int(player_data[1])
            team_name = player_data[2]
            jersey_number = player_data[3]
            country = player_data[4] if len(player_data) > 4 and player_data[4] else None
            salary = float(player_data[5]) if len(player_data) > 5 and player_data[5] else None
            endorsement = player_data[6] if len(player_data) > 6 and player_data[6] else None
            touchdowns = int(player_data[7]) if len(player_data) > 7 and player_data[7] else None
            passing_yards = player_data[8] if len(player_data) > 8 and player_data[8] else None

            return FootballPlayer(
                name=name,
                age=age,
                team_name=team_name,
                jersey_number=jersey_number,
                country=country,
                salary=salary,
                endorsement=endorsement,
                touchdowns=touchdowns,
                passing_yards=passing_yards
            )
        except (ValueError, IndexError) as e:
            print(f"Error parsing FootballPlayer data: {e}")
            return None
