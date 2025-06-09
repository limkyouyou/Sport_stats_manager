from typing import Optional
from athlete import Athlete

class BallPlayer(Athlete):
    total_ball_players = 0

    def __init__(
        self,
        name: str,
        age: int,
        team_name: str,
        jersey_number : str,
        country: Optional[str] = None,
        salary: Optional[float] = None,
        endorsement: Optional[str] = None,
    ):
        super().__init__(name, age, country, salary)
        self._team_name = team_name
        self._jersey_number = jersey_number
        self._endorsement = endorsement

        BallPlayer.total_ball_players += 1
        BallPlayer.print_creation_log(self)

    def print_stats(self):
        pass

    def print_endorsement(self):
        if self._endorsement:
            print(f"{self.name} endorses {self._endorsement}.")
        else:
            print(f"{self.name} has no endorsement.")

    @staticmethod
    def print_creation_log(instance):
        print(f"Ball Player '{instance.name}', {instance.age} created; total # of ball players {BallPlayer.total_ball_players}.")
