import ssl
import pymongo
from flask import Flask


app = Flask(__name__)
#Flask App creation
app = Flask(__name__)

#MongoDb Connection
def connect_to_monogodb():
    connection_string = "mongodb+srv://manp:manpS1@cluster0.hkfcr.mongodb.net/sample_restaurants?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connection_string, ssl_cert_reqs=ssl.CERT_NONE)
    print(my_client)
    db = my_client["HotelReservation"]
    return db;


from application import routes



