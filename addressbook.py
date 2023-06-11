from uvicorn import run
from fastapi import FastAPI
from routes.route import my_router
from argparse import ArgumentParser
from common.common import LOGGER, set_logger, path

app = FastAPI()
app.include_router(my_router)


if __name__ == "__main__":
    parser = ArgumentParser(description='AddressBook.py is used to find nearest locations available near to provided coordinates')
    parser.add_argument('--host', default='localhost', help='host example localhost, 0.0.0.0')
    parser.add_argument('--port', default=9000, help='port number to host website')
    parser.add_argument('--log', default='debug', help='log level can be set to DEBUG, INFO, ERROR')

    args = parser.parse_args()
    set_logger(LOGGER, out_file=path.join('.', 'data', 'addressbook.log'), logger_level=args.log)
    run(app, host=args.host, port=args.port)
