""" possible tags for the chat system"""


TAGS = {
    "add":"add",
    "list":"list",
    "stop":"stop",
    "about":"about",
    "help":"help",
    "example":"example"
}



"""
    custom exception for not finding a tag
"""
class TagNotFoundException(Exception):
    def __init__(self, message):
        pass

