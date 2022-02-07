class Logger:

    def __init__(self):
        self.seen = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.seen :
            if self.seen[message] + 10 <= timestamp:
                self.seen[message] = timestamp
                return True
            else:
                return False
        else:
            self.seen[message] = timestamp
            return True
