from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def vehicle_type(self) -> str:
        pass

    @abstractmethod
    def arrival_time(self) -> str:
        pass

    @abstractmethod
    def travel_time(self) -> str:
        pass

class Bike(Transport):
    def vehicle_type(self) -> str:
        return "Bike"

    def arrival_time(self) -> str:
        return "5 minutes"

    def travel_time(self) -> str:
        return "15 minutes"