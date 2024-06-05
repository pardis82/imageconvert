class Logger:
    _instance = None

    def __new__(cls,*args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        with open(self.filename, "a") as f:
            f.write(f"{message}\n")


logger_1 = Logger("error.log")

logger_1.log("Error: there is a syntax error in app.py, line 123")


logger_2 = Logger("error.log")

logger_2.log("Error: there is a syntax error in app.py, line 135")

if logger_1 is logger_2: 
    print('Both logger_1 and logger_2 refer to the exact same object.')
else: 
    print('logger_1 and logger_2 are two indivisual objects')

