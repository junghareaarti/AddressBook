from common.common import Base, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float


class AddressBook(Base):
    __tablename__ = "addressbook"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    building = Column("building", String(255))
    street = Column("street", String(255))
    city = Column("city", String(255))
    state = Column("state", String(255))
    country = Column("country", String(255))
    pincode = Column("pincode", Integer)
    latitude = Column("latitude", Float)
    longitude = Column("longitude", Float)

    def __init__(self, building, street, city, state, country, pincode, latitude, longitude):
        self.building = building
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.pincode = pincode
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"({self.id} {self.building} {self.state} {self.city} {self.state} {self.country} {self.pincode} {self.latitude} {self.longitude})"


Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
