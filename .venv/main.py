from customer import Customer
from services import BikeService


def main():
    customer1 = Customer("Jan Kowalski")
    bike_service = BikeService()

    # Zamówienie transportu
    customer1.order_transport(bike_service)


if __name__ == "__main__":
    main()