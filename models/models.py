from pymongo import *
from chatbot import chat


class DatabaseCreation:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client["fmsbpy"]
        self.schedules = self.db.schedules

    def insert_schedule(self, schedule):
        r = self.schedules.insert_one(schedule)
        if r:
            return True
        else:
            return False

    def find_schedule(self, name):
        found = self.schedules.find_one({"schedule": name})
        return found

    def get_all_schedules(self):
        sch = [i.schedule for i in list(self.db.schedules.find({}))]
        return sch