import unittest
from transport import Bike
from services import BikeService

#Jakis tam fajny komentarz
class TestTransportSystem(unittest.TestCase):
    def test_create_transport(self):
        """Sprawdza tworzenie transportu i działanie metod."""
        service = BikeService()
        transport = service.create_transport()

        self.assertIsInstance(transport, Bike)
        self.assertEqual(transport.vehicle_type(), "Bike")
        self.assertEqual(transport.arrival_time(), "5 minutes")

    def test_availability_mechanism(self):
        """Sprawdza mechanizm dostępności transportu."""
        service = BikeService()

        self.assertTrue(service.available)
        service.order_transport()
        self.assertFalse(service.available)


if __name__ == '__main__':
    unittest.main()