from pydantic import BaseModel


class AddressBookSchema(BaseModel):
    building: str
    street: str
    city: str
    state: str
    country: str
    pincode: int
    latitude: float
    longitude: float


class AddressBookEditSchema(BaseModel):
    building: str | None
    street: str | None
    city: str | None
    state: str | None
    country: str | None
    pincode: int | None
    latitude: float | None
    longitude: float | None
