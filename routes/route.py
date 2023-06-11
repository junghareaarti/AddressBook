from geopy import distance
from fastapi import APIRouter
from common.common import LOGGER
from models.model import Session, AddressBook
from schemas.schema import AddressBookSchema, AddressBookEditSchema

my_router = APIRouter()


@my_router.get("/")
async def get_address():
    LOGGER.debug(f"Getting information of all the addresses from the database")
    session = Session()
    results = session.query(AddressBook).all()
    LOGGER.debug(f"query run successfully, result count: {len(results)}")
    session.close()
    return results


@my_router.get("/{id}")
async def get_address_by_id(_id: int):
    LOGGER.debug(f"Searching the address by id: {_id}")
    session = Session()
    results = session.query(AddressBook).filter(AddressBook.id == _id).all()
    session.close()
    if len(results) != 1:
        LOGGER.error(f"Address not found for the id:{_id} provided")
    else:
        LOGGER.debug(f"Address found by id result: {results}")
    return results


@my_router.post("/")
async def add_address(addressbook: AddressBookSchema):
    LOGGER.debug(f"Adding address with following data: {addressbook}")
    session = Session()
    a1 = AddressBook(addressbook.building, addressbook.street, addressbook.city, addressbook.state, addressbook.country,
                     addressbook.pincode, addressbook.latitude, addressbook.longitude)
    session.add(a1)
    session.commit()
    session.close()
    LOGGER.debug(f"Successfully added address with following data: {addressbook}")
    return {"msg": "New Address has been added to the database"}


@my_router.put("/{id}")
async def edit_address(_id: int, addressbook: AddressBookEditSchema):
    session = Session()
    a1 = session.query(AddressBook).filter(AddressBook.id == _id).all()
    if len(a1) == 1:
        temp_addressbook = dict()
        temp_dict = addressbook.__dict__
        for key in temp_dict.keys():
            if temp_dict[key] is not None:
                temp_addressbook[key] = temp_dict[key]
        LOGGER.debug(f"Editing address entry with id:{_id} with following data: {temp_addressbook}")
        session.query(AddressBook).filter(AddressBook.id == _id).update(temp_addressbook)
        session.commit()
        LOGGER.debug(f"Successfully updated address with the following data: {temp_addressbook}")
        message = {"msg": "Address has been updated with the provided information"}
    else:
        LOGGER.error(f"The Address you wants to update is not available for the id:{_id}")
        message = {"msg": "The Address you wants to update is not available"}
    session.close()
    return message


@my_router.delete("/{id}")
async def delete_address(_id: int):
    session = Session()
    a1 = session.query(AddressBook).filter(AddressBook.id == _id).all()
    if len(a1) == 1:
        LOGGER.debug(f"Deleting address with id:{_id}")
        session.delete(a1[0])
        session.commit()
        LOGGER.debug(f"Successfully deleted address with id:{_id}")
        message = {"msg": "Address deleted successfully"}
    else:
        LOGGER.error(f"The Address you wants to delete is not available for the id:{_id}")
        message = {"msg": "The Address you wants to delete is not available"}
    session.close()
    return message


@my_router.get("/find_nearby/{lattitude}/{logitude}/{distance_km}")
async def get_nearby_addresses(lattitude: float, logitude: float, distance_km: float):
    final_result = []
    LOGGER.debug(f"Getting information of all the nearby addresses from the database")
    session = Session()
    results = session.query(AddressBook).all()
    session.close()
    cords_1 = (lattitude, logitude)
    for result in results:
        cords_2 = (result.latitude, result.longitude)
        difference_in_km = distance.geodesic(cords_1, cords_2).km
        if difference_in_km < distance_km:
            final_result.append([difference_in_km, result])

    return final_result
