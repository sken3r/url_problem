class InputError(Exception):
    """ Represent an `input` error which can be caused by incorrect request/events sent to the service. """

    def __init__(self, message, code):
        self.message = message
        self.code = code
