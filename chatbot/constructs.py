"""
A class to create message constructs
"""

"""
    MessageConstructs
    refactor the message to make it able to parse beter.
"""


class MessageConstructs:

    @staticmethod
    def refactor(message):
        message = message.lower()  # tolowercase
        message = message.strip()  # removing whitespaces
        # may add more
        return message
