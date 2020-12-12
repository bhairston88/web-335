# 
# ============================================
# Title: hairston_user_update.py
# Author: Professor Massoud
# Date:   10 December 2020
# Modified By: Brooklyn Hairston
# Description: Demonstrates how to update a collection document using python 
# ===========================================
#

#import statements
from pymongo import MongoClient 
import pymongo
import pprint
import datetime

#connect to MongoDB
client = MongoClient("localhost", 27017)
db = client.web335

#update user document
db.users.update_one(
    {"employee_id": "2583691"},
    {
        "$set": {
            "email": "bhairston@my365.bellevue.edu"
        }
    }
)

#output the updated document with specific fields
pprint.pprint(db.users.find_one(
    { "employee_id": "2583691" }, 
    { "email": 1, "first_name": 1, "last_name": 1 }
))