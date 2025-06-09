
class Athlete:
    total_athletes = 0

    def __init__(self, name : str, age : int, country : str, salary : float, ):
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
        return self.__salary
    
    @salary.setter
    def salary(self, new_salary: float):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = new_salary

    
    def print_stats(self):
        pass

    def print_endorsement(self):
        pass

    def __str__(self):
        return f"Athlete(name={self._name}, age={self._age}, country={self._country}, salary={self._salary})"

    @staticmethod
    def print_creation_log(instance):
        print(f"Athlete '{instance.name}', {instance.age} created; total # of athletes {Athlete.total_athletes}.")
