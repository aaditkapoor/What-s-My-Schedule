"""
Chat interface for the app
"""

from chatbot.tags import TAGS, TagNotFoundException
from chatbot.binder import *
import logging


def about():
    return "A Facebook Messenger Bot to remind you your schedules."


def give_example():
    return "You can try entering your schedule and time as: math 10:30pm (schedule_name <space> time)."


class Schedule:
    def __init__(self, schedule, time):
        self.schedule = schedule
        self.time = time

    @property
    def getSchedule(self):
        if self.schedule:
            return self.schedule
        else:
            return None

    @property
    def getTime(self):
        if self.time:
            return self.time
        else:
            return None

    @property
    def return_json(self):
        return {
            "schedule": self.schedule,
            "time": self.time
        }


class Chat:
    def __init__(self, message:str, id:str):
        # converting to lowercase for simple analysis
        self.message = message.lower()
        self.id = id
        self.schedule = ""
        self.time = ""
        self.parsed_message = ""
        self.schedule_object = None

    def __str__(self):
        return {"message": self.message, "id": self.id}

    def parse(self):
        for (index, key) in enumerate(TAGS):
            if key in self.message.split():
                if key == "add":
                    self.schedule, self.time = self.message.split()[1], self.message.split()[2]
                    self.schedule_object = Schedule(self.schedule, self.time)
                    self.parsed_message = "Saved Schedule!"
                elif key == "list":
                    self.parsed_message = None  # get the list of schedules.
                elif key == "stop":
                    pass  # stop all the processes
                elif key == "about":
                    self.parsed_message = about()
                elif key == "help":
                    self.parsed_message = ""  # Show help options
                elif key == "example":
                    self.parsed_message = give_example()
            else:
                self.parsed_message = "Could not understand: " + self.message


    def getScheduleObject(self):
        if (self.schedule_object):
            return self.schedule_object
        else:
            return None

    def getLength(self):
        return len(self.message.split())


    #send message
    def send_message(self, id):
        send_message(id, self.parsed_message)
