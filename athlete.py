
class Athlete:
    def __init__(self, name : str, age : int, country : str, salary : float, ):
        self.__name = name
        self.__age = age
        self.__country = country
        self.__salary = salary

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def age(self) -> int:
        return self.__age
    
    @property
    def country(self) -> str:
        return self.__country
    
    @property
    def salary(self) -> float:
        return self.__salary
    
    @salary.setter
    def salary(self, new_salary: float):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = new_salary

    
    def _print_stats(self):
        pass

    def _print_endorsement(self):
        pass

    def __str__(self):
        return f"Athlete(name={self.__name}, age={self.__age}, country={self.__country}, salary={self.__salary})"
