
class NotPositiveNumberError(Exception):
    def __init__(self, wrong_value):
        self.wrong_value = wrong_value

    def __str__(self):
        return f"{self.wrong_value} is not positive number!"
