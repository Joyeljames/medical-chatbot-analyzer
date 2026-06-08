import sys

def error_message(message):
    _, _, exc_tb = sys.exc_info()
    return str(message)