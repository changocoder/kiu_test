import uuid
from abc import ABC
from datetime import datetime
from datetime import date

from models.enums import StatusEnum


class BaseModel(ABC):
    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = id if id else str(uuid.uuid4())
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()


class Person(BaseModel):
    def __init__(self, id=None, name=None, last_name=None, birth_date=None):
        super().__init__(id)
        self.nombre = name
        self.apellido = last_name
        self.birth_date = birth_date


class Customer(Person):
    def __init__(
            self, id=None,
            name=None,
            last_name=None,
            birth_date=None,
            email=None,
            phone=None
    ):
        super().__init__(id, name, last_name, birth_date)
        self.email = email
        self.phone = phone


class City(BaseModel):
    def __init__(
            self,
            id=None,
            name=None,
            state=None,
            country=None,
            postal_code=None
    ):
        super().__init__(id)
        self.name = name
        self.state = state
        self.country = country
        self.postal_code = postal_code


class Package(BaseModel):
    def __init__(
            self,
            id=None,
            name=None,
            description=None,
            weight=None
    ):
        super().__init__(id)
        self.name = name
        self.description = description
        self.weight = weight


class Shipment(BaseModel):
    def __init__(
            self,
            id=None,
            package: Package = None,
            customer: Customer = None,
            origin: City = None,
            destination: City = None,
            price: float = 0.0

    ):
        super().__init__(id)
        self.package = package
        self.customer = customer
        self.status = StatusEnum.PENDING
        self.origin = origin
        self.destination = destination
        self.price = price
        self.sale_date = datetime.date(datetime.now())

class Company(BaseModel):
    def __init__(self, id=None, name=None, email=None, phone=None):
        super().__init__(id)
        self.name = name
        self.email = email
        self.phone = phone
        self.shipments = []

    def shipments(self):
        return self.shipments

    def add_shipment(self, shipment: Shipment):
        self.shipments.append(shipment)
        return self.shipments

    def remove_shipment(self, shipment: Shipment):
        self.shipments.remove(shipment)
        return self.shipments

    def update_shipment(self, shipment: Shipment):
        self.shipments.remove(shipment)
        self.shipments.append(shipment)
        return self.shipments

    def get_shipments_by_date(self, date: date):
        return [shipment for shipment in self.shipments if shipment.sale_date == date]

    def get_shipments_by_status(self, status: StatusEnum):
        return [shipment for shipment in self.shipments if shipment.status == status]

    def get_shipments_by_customer(self, customer: Customer):
        return [shipment for shipment in self.shipments if shipment.customer == customer]

    def get_all_shipments(self):
        return self.shipments

    def get_total_sales(self):
        return sum([shipment.price for shipment in self.shipments])

    def report_shipments_and_sales_by_date(self, date_requested: date):
        shipments = self.get_shipments_by_date(date_requested)
        total_sales = sum([shipment.price for shipment in shipments])
        return shipments, total_sales

