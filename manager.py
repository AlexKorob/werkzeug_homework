from pymongo import MongoClient
from datetime import datetime
import pymongo


class Manager(object):
    def __init__(self, host='localhost', port=27017):
        self.client = MongoClient(host, port)
        self.db = self.client.local
        self.collection = self.db.notes

    def all_notes(self):
        notes = []
        for note in self.collection.find().sort("date_creation", pymongo.DESCENDING):
            notes.append(note)

        return notes

    def add_note(self, **data):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data["date_creation"] = time
        self.collection.insert_one(data)

    def close(self):
        self.db.close()
