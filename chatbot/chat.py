"""
Chat interface for the app
"""

from chatbot.tags import TAGS


class Chat:
    def __init__(self, message, id):
        self.message = message
        self.id = id
        self.schedule = ""
        self.time = ""
        self.parsed_message = ""

    def __str__(self):
        return {"message": self.message, "id": self.id}

    def parse(self):
        if list(TAGS.keys()) in self.message.split():
            for word in self.message.split():
                tag = TAGS.get(word, False)
                if (tag):
                    if tag == "add":
                        self.schedule = self.message.split()[1]
                        self.time = self.message.split()[2]
                        self.parsed_message = self.schedule  # temp
                    else:
                        self.parsed_message = self.message
        return self.parsed_message

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


c = Chat("xyz", "hi")
c.parse()
print(c.parsed_message)
