class Athlete:
    total_athletes = 0

    def __init__(self, name: str, age: int, country: str, salary: float, ):
        self._name = name
        self._age = age
        self._country = country
        self._salary = salary

        Athlete.total_athletes += 1
        Athlete.print_creation_log(self)

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def age(self) -> int:
        return self._age
    
    @property
    def country(self) -> str:
        return self._country
    
    @property
    def salary(self) -> float:
        return self._salary
    
    @salary.setter
    def salary(self, new_salary: float):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = new_salary

    
    def print_stats(self):
        pass

    def print_endorsement(self):
        pass

    def decrement_counter(self):
        Athlete.total_athletes = max(0, Athlete.total_athletes - 1)

    def __str__(self):
        pass

    @staticmethod
    def print_creation_log(instance):
        print(f"Athlete '{instance.name}', {instance.age} created; total # of athletes {Athlete.total_athletes}.")

    @classmethod
    def get_total_athletes(cls) -> int:
        return cls.total_athletes
