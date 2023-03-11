from TkTerm.backend.InterpreterInterface import InterpreterInterface
from TkTerm.backend.KThread import KThread

# TODO:
# dhanoo : Unsure how to intergrate this to your API. I have provide a simple function that can be called
from Ant.src.lib.api import ANT_API

import time
import threading

# Global variable return code as it is not easy to get value from a thread
returnCode = 0

# Sample function to be run
def loop(cmd):

    i = 0

    # Calling the API to parse the command
    ant = ANT_API()
    ant.parser(cmd)
    
    # Run for 5 seconds
    # while i < 5:
    #     print(cmd)
    #     time.sleep(1)
    #     i += 1

    # Success: set a return code
    global returnCode
    returnCode = 0



class Wrapper():
    """ Wrapper context manager class needed to comply with Terminal """

    def __init__(self, command):
        self.command = command
        self.process = None

    def __enter__(self):

        # NOTE: a trailing comma inside args() is needed!!!
        self.process = KThread(target=loop, args=(self.command,), daemon=True)
        self.process.start()
        return self.process

    def __exit__(self, *exec):
        self.process.join()

class AntInterpreter(InterpreterInterface):

    def __init__(self):
        super().__init__()
        self.process = None

    def execute(self, command):
        return Wrapper(command)

    def terminate(self, processThread):

        # Terminate a running thread
        processThread.kill()

        # Sets a return code
        global returnCode
        returnCode = -1

    def getReturnCode(self, process):
        return returnCode