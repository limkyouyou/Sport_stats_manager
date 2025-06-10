from collections import defaultdict
from athlete import Athlete
from hockey import HockeyPlayer
from swimmer import Swimmer
from ball import BallPlayer, FootballPlayer, BasketballPlayer
from util import get_leaf_subclasses, is_leaf_class



class Data:
    def __init__(self):
        self._athletes = []         # Parsed data
        self._filename = None
        self._dirty = False         # Indicates if athlete data has been modified since the last save 

    @property
    def athletes(self):
        return self._athletes
    
    @property
    def dirty(self) -> bool:
        return self._dirty

    @dirty.setter
    def dirty(self, toggle: bool):
        self._dirty = toggle
    
    def filename(self) -> str:
        return self._filename
    
    def load_data(self, rawData: list[str], filename: str) -> bool:
        if not rawData:
            return False
        
        self._filename = filename
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
    
    def get_statistics(self):
        stats = [
            ("Athletes", Athlete.total_athletes),
            ("Hockey Players", HockeyPlayer.total_hockey_players),
            ("Ball Players", str(BallPlayer.total_ball_players) + " (" + str(BasketballPlayer.total_basketball_players) + " Basketball and " + str(FootballPlayer.total_football_players) + " Football Players)"),
            ("Swimmers", Swimmer.total_swimmers),
        ]
        
        endorsements = []
        goals_scored = []
        touchdowns = []
        endorsement_dict = {}           # Used for counting endorsements
        for athlete in self._athletes:
            if isinstance(athlete, HockeyPlayer):
                goals_scored.append((athlete.name, athlete._goal_scored if athlete._goal_scored is not None else 0))
            elif isinstance(athlete, BallPlayer):
                if athlete._endorsement:
                    if athlete._endorsement not in endorsement_dict:
                        endorsement_dict[athlete._endorsement] = 1
                    else:
                        endorsement_dict[athlete._endorsement] += 1
                if isinstance(athlete, FootballPlayer):
                    touchdowns.append((athlete.name, athlete._touchdowns if athlete._touchdowns is not None else 0))

        for endorsement, count in endorsement_dict.items():
            endorsements.append((endorsement, count))
            
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
        self._dirty = True

    def save_data(self) -> list[str]:
        """Returns a list of stringifyed the object so that it can be saved to a file"""
        if not self._filename:
            return []  # no known file to overwrite
        
        return [str(athlete) for athlete in self.athletes]

    def get_athlete_info(self, athlete_name: str) -> Athlete:
        return next((athlete for athlete in self._athletes if athlete.name.lower() == athlete_name.lower()), None)
    
    def get_level_1_athlete_counts(self) -> dict[str, int]:
        counts = {}
        direct_subclasses = Athlete.__subclasses__()
        for subclass in direct_subclasses:
            counts[subclass.__name__] = subclass.get_total_athletes()
        return counts
    
    def get_leaf_athlete_counts(self) -> dict[str, int]:
        counts = {}
        leaf_classes = get_leaf_subclasses(Athlete)
        for cls in leaf_classes:
            counts[cls.__name__] = cls.get_total_athletes()
        return counts
    
    def get_level_1_athlete_average_salary(self) -> dict[str, int]:
        salary_sums = defaultdict(int)
        counts = defaultdict(int)

        for athlete in self._athletes:
            cls = type(athlete)

            # walk up to level 1 
            while cls not in Athlete.__subclasses__() and cls != Athlete:
                cls = cls.__base__

            if athlete.salary is not None:
                salary_sums[cls.__name__] += athlete.salary
                counts[cls.__name__] += 1

        average = {
            name: (salary_sums[name] / counts[name]) for name in salary_sums if counts[name] > 0
        }

        return average
    
    def get_leaf_level_athlete_average_salary(self) -> dict[str, int]:
        salary_sums = defaultdict(int)
        counts = defaultdict(int)

        for athlete in self._athletes:
            cls = type(athlete)

            if is_leaf_class(cls) and athlete.salary is not None:
                salary_sums[cls.__name__] += athlete.salary
                counts[cls.__name__] += 1

        average = {
            name: (salary_sums[name] / counts[name]) for name in salary_sums if counts[name] > 0
        }

        return average

    def get_endorsement_counts(self) -> dict[str, int]:
        counts = defaultdict(int)

        for athlete in self.athletes:
            if isinstance(athlete, BallPlayer) and athlete.endorsement is not None:
                counts[athlete.endorsement] += 1

        return counts
