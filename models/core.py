import uuid
from abc import ABC
from datetime import datetime

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


class Company(BaseModel):
    def __init__(self, id=None, name=None, email=None, phone=None):
        super().__init__(id)
        self.name = name
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
            price=None,
            weight=None
    ):
        super().__init__(id)
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight


class Shipment(BaseModel):
    def __init__(
            self,
            id=None,
            package: Package = None,
            customer: Customer = None,
            company: Company = None,
            origin: City = None,
            destination: City = None
    ):
        super().__init__(id)
        self.package = package
        self.customer = customer
        self.company = company
        self.status = StatusEnum.PENDING
        self.origin = origin
        self.destination = destination
