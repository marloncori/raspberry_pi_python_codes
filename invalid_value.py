
class InvalidValueError(BaseException):
    def __init__(self, err_msg):
        super.__init__(err_msg)
        self.err_msg = err_msg
