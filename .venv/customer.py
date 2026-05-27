from services import TransportServices

class Customer:
    def __init__(self, name: str):
        self.name = name

    def order_transport(self, service: TransportServices):
        print(f"\nKlient {self.name} próbuje zamówić: {service.transport_name()}")
        service.order_transport()