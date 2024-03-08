from datetime import datetime
from unittest import TestCase

from models.core import Customer, Company, Package, Shipment, City


class TestReports(TestCase):
    def setUp(self):
        self.customer = Customer(
            name='John',
            last_name='Doe',
            birth_date='1990-01-01',
            email='sarasa@hotmail.com',
            phone='1234567890'
        )

        self.customer2 = Customer(
            name='John',
            last_name='Doe',
            birth_date='1990-01-01',
            email='sarasa2@hotmail.com',
            phone='1234567890'
        )

        self.company = Company(
            name='Company 1',
            phone='1234567890',
        )

        self.package = Package(
            name='Package 1',
            description='Description 1',
            weight=10
        )

        self.package2 = Package(
            name='Package 2',
            description='Description 2',
            weight=20
        )

        self.city = City(
            name='City 1',
            state='State 1',
            country='Country 1',
            postal_code='1234'
        )

        self.city2 = City(
            name='City 2',
            state='State 2',
            country='Country 2',
            postal_code='5678'
        )

        self.shipment = Shipment(
            package=self.package,
            customer=self.customer,
            origin=self.city,
            destination=self.city2
        )

        self.shipment2 = Shipment(
            package=self.package2,
            customer=self.customer2,
            origin=self.city2,
            destination=self.city
        )

    def test_shipments(self):
        shipment = Shipment(
            package=self.package,
            customer=self.customer,
            origin=self.city,
            destination=self.city2
        )

        shipment2 = Shipment(
            package=self.package2,
            customer=self.customer2,
            origin=self.city2,
            destination=self.city
        )

        self.assertEqual(shipment.customer, self.customer)
        self.assertEqual(shipment.package, self.package)
        self.assertEqual(shipment.origin, self.city)
        self.assertEqual(shipment.destination, self.city2)

        self.assertEqual(shipment2.customer, self.customer2)
        self.assertEqual(shipment2.package, self.package2)
        self.assertEqual(shipment2.origin, self.city2)
        self.assertEqual(shipment2.destination, self.city)

    def test_company_shipments(self):
        self.company.add_shipment(self.shipment)
        self.company.add_shipment(self.shipment2)

        self.assertEqual(len(self.company.shipments), 2)
        self.assertEqual(self.company.shipments[0], self.shipment)
        self.assertEqual(self.company.shipments[1], self.shipment2)

    def test_get_shipments(self):
        self.company.add_shipment(self.shipment)
        self.company.add_shipment(self.shipment2)

        self.assertEqual(self.company.get_all_shipments(), self.company.shipments)

    def test_get_shipments_by_customer(self):
        self.company.add_shipment(self.shipment)
        self.company.add_shipment(self.shipment2)

        self.assertEqual(self.company.get_shipments_by_customer(self.customer), [self.shipment])
        self.assertEqual(self.company.get_shipments_by_customer(self.customer2), [self.shipment2])

    def test_get_shipments_by_date(self):
        current_datetime = datetime.date(datetime.now())
        self.company.add_shipment(self.shipment)
        self.company.add_shipment(self.shipment2)

        self.assertEqual(self.company.get_shipments_by_date(current_datetime), self.company.shipments)

    def test_report(self):
        self.company.add_shipment(self.shipment)
        self.company.add_shipment(self.shipment2)

        date_requested = datetime.date(datetime.now())
        shipments, total_sales = self.company.report_shipments_and_sales_by_date(date_requested)

        self.assertEqual(shipments, self.company.shipments)
        self.assertEqual(total_sales, sum([shipment.price for shipment in self.company.shipments]))

