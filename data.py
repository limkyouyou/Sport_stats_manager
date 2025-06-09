from athlete import Athlete
from hockey import HockeyPlayer
from swimmer import Swimmer
from ball import BallPlayer
from football import FootballPlayer
from basketball import BasketballPlayer

class Data:
    def __init__(self):
        self._athletes = []
    
    def load_data(self, rawData : list[str]) -> bool:
        if not rawData:
            return False
        
        for line in rawData:
            line = line.strip()
            if not line:
                continue

            if line.startswith("HockeyPlayer:"):
                athlete = HockeyPlayer.parse(line)
            elif line.startswith("Swimmer:"):
                athlete = Swimmer.parse(line)
            elif line.startswith("FootballPlayer:"):
                athlete = FootballPlayer.parse(line)
            elif line.startswith("BasketballPlayer:"):
                athlete = BasketballPlayer.parse(line)
            else:
                print(f"Unknown athlete type in line: {line}")
                continue

            if athlete:
                self._athletes.append(athlete)
        return True

    @property
    def athletes(self):
        return self._athletes
    
    def get_statistics(self):
        stats = {
            "Athletes": Athlete.total_athletes,
            "Hockey Players": HockeyPlayer.total_hockey_players,
            "Ball Players": str(BallPlayer.total_ball_players) + " (" + str(BasketballPlayer.total_basketball_players) + " Basketball and " + str(FootballPlayer.total_football_players) + " Football Players)",
            "Swimmers": Swimmer.total_swimmers,
        }
        
        endorsements = {}
        goals_scored = {}
        touchdowns = {}
        for athlete in self._athletes:
            if isinstance(athlete, HockeyPlayer):
                if athlete._name not in goals_scored:
                    goals_scored[athlete._name] = athlete._goal_scored if athlete._goal_scored else 0
                else:
                    if athlete._goal_scored: 
                        goals_scored[athlete._name] += athlete._goal_scored 
            elif isinstance(athlete, BallPlayer):
                if athlete._endorsement:
                    if athlete._endorsement not in endorsements:
                        endorsements[athlete._endorsement] = 1
                    else:
                        endorsements[athlete._endorsement] += 1
                if isinstance(athlete, FootballPlayer):
                    if athlete._name not in touchdowns:
                        touchdowns[athlete._name] = athlete._touchdowns if athlete._touchdowns else 0
                    else:
                        if athlete._touchdowns: 
                            touchdowns[athlete._name] += athlete._touchdowns
        
        return {
            "Statistics": stats,
            "Endorsements": endorsements,
            "Goals scored": goals_scored,
            "Touchdowns": touchdowns
        }

    def find_athlete_by_name(self, name: str) -> list[Athlete]:
        return [athlete for athlete in self._athletes if athlete.name.lower() == name.lower()]
    
    def delete_athlete(self, name: str):
        remaining_athletes = []
        for athlete in self._athletes:
            if athlete.name.lower() != name.lower():
                remaining_athletes.append(athlete)
            else:
                athlete.decrement_counter()
        self._athletes = remaining_athletes
