# AddressBook
I have developed this project using Python FastAPI 
AddressBook is used to find nearest locations available from given coordinates


# How to Run the application
1. Please install all the requirements from the [requirements.txt](https://github.com/junghareaarti/AddressBook/blob/main/requirements.txt)
2. Use --help command to check the usage 
```
> python addressbook.py --help
   
usage: addressbook.py [-h] [--host HOST] [--port PORT] [--log LOG]

AddressBook.py is used to find nearest locations available near to provided coordinates

options:
  -h, --help   show this help message and exit
  --host HOST  host example localhost, 0.0.0.0
  --port PORT  port number to host website
  --log LOG    log level can be set to DEBUG, INFO, ERROR
```

Example 1
```
> python addressbook.py
```
This will run the AddressBook application on default paramiters as host: localhost and port: 9000

Example 2
```
> python addressbook.py --host localhost --port 8000 --log debug
```
This will run the AddressBook application on http://localhost:8000 so you can visit it from browser or use postman to call the APIs.
To get to know more about the APIs provided by this application visit the Swagger documentation by visiting http://localhost:8000/docs

