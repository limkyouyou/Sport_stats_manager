from hockey import HockeyPlayer

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
            else:
                print(f"Unknown athlete type in line: {line}")
                continue

            if athlete:
                self._athletes.append(athlete)
        return True

    @property
    def athletes(self):
        return self._athletes
