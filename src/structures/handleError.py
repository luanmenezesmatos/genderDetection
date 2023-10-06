import json

class handleError:
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code

    def __str__(self):
        return self.message

    def getStatusCode(self):
        return self.status_code
    
    def getMessage(self):
        return self.message
    
    def getError(self):
        return self.message, self.status_code
    
    def sendErrorMessage(self):
        print(self.message)