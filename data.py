from hockey import HockeyPlayer
from swimmer import Swimmer
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
