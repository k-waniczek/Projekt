from abc import ABC, abstractmethod
from transport import Transport, Bike, Scooter, Taxi

class TransportServices(ABC):
    def __init__(self):
        self.available = True

    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    @abstractmethod
    def transport_name(self) -> str:
        pass

    def order_transport(self):
        transport = self.create_transport()
        print(f"\n--- Informacje o zamówieniu ---")
        print(f"Typ pojazdu: {transport.vehicle_type()}")
        print(f"Przewidywany czas przyjazdu: {transport.arrival_time()}")
        print(f"Przewidywany czas podróży: {transport.travel_time()}")

class BikeService(TransportServices):
    def create_transport(self) -> Transport:
        return Bike()

    def transport_name(self) -> str:
        return "Bike"

class ScooterService(TransportServices):
    def create_transport(self) -> Transport:
        return Scooter()

    def transport_name(self) -> str:
        return "Scooter"

class TaxiService(TransportServices):
    def create_transport(self) -> Transport:
        return Taxi()

    def transport_name(self) -> str:
        return "Taxi"