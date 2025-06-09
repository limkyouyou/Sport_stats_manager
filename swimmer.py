from typing import Optional
from athlete import Athlete

class Swimmer(Athlete):
    def __init__(
        self,
        name: str,
        age : int,
        stroke_style : Optional[str] = None,
        country : Optional[str] = None,
        salary : Optional[float] = None,
        personal_best_time : Optional[float] = None,
    ):
        super().__init__(name, age, country, salary)
        self._stroke_style = stroke_style
        self._personal_best_time = personal_best_time

    def print_stats(self):
        time = self._personal_best_time if self._personal_best_time is not None else "N/A"
        stroke = self._stroke_style if self._stroke_style else "Unknown Stroke Style"
        print(f"{self.name} swims {stroke} with a personal best time of {time} seconds.")

    @staticmethod
    def parse(raw_data: str) -> "Swimmer":
        try:
            prefix, data = raw_data.split(":", 1)
            if prefix.strip() != "Swimmer":
                raise ValueError("Invalid player for Swimmer")
            
            swimmer_data = [item.strip() for item in data.split(",")]
            name = swimmer_data[0]
            age = int(swimmer_data[1])
            stroke_style = swimmer_data[2] if len(swimmer_data) > 2 and swimmer_data[2] else None
            country = swimmer_data[3] if len(swimmer_data) > 3 and swimmer_data[3] else None
            salary = float(swimmer_data[4]) if len(swimmer_data) > 4 and swimmer_data[4] else None
            personal_best_time = float(swimmer_data[5]) if len(swimmer_data) > 5 and swimmer_data[5] else None

            return Swimmer(
                name=name,
                age=age,
                stroke_style=stroke_style,
                country=country,
                salary=salary,
                personal_best_time=personal_best_time
            )
        except (ValueError, IndexError) as e:
            print(f"Error parsing Swimmer data: {e}")
            return None
