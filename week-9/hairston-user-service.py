# 
# ============================================
# Title: hairston_user_service.py
# Author: Professor Massoud
# Date:   10 December 2020
# Modified By: Brooklyn Hairston
# Description: Demonstrates how to create and insert documents to MongoDB using python
# ===========================================
#


# import statements 
import pymongo
from pymongo import MongoClient
import pprint
import datetime

#connect to MongoDB
client = MongoClient("localhost", 27017)
db = client.web335

#create new user document
user = {
    "first_name": "Spencer",
    "last_name": "Reid",
    "email": "SReid@baufbi.gov",
    "employee_id": "2583691",
    "date_created": datetime.datetime.utcnow()
}

#insert user document
user_id = db.users.insert_one(user).inserted_id

#output the user_id
print(user_id)

#query the users collection and output the document 
pprint.pprint(db.users.find_one({"employee_id": "2583691"}))



