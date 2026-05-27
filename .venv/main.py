from customer import Customer
from services import BikeService, ScooterService, TaxiService

def main():
    customer1 = Customer("Jan Kowalski")
    bike_service = BikeService()

    customer1.order_transport(bike_service)
    scooter_service = ScooterService()
    taxi_service = TaxiService()

    customer1.order_transport(scooter_service)
    customer1.order_transport(taxi_service)

if __name__ == "__main__":
    main()

