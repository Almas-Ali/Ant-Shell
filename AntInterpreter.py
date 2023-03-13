from TkTerm.backend.InterpreterInterface import InterpreterInterface
from TkTerm.backend.KThread import KThread

from Ant.src.lib.api import ANT_API

import re

# Global variables
API = ANT_API()
RETURNCODE = 0


def api_function_call(cmd):
    """ Function call to API """

    # Calling the API to parse the command
    if cmd == "exit":
        GUI_ELEMENT.destroy()
    API.parser(cmd)

    # Success: set a return code
    global RETURNCODE
    RETURNCODE = 0


class Wrapper():
    """ Wrapper context manager class needed to comply with Terminal """

    def __init__(self, command, gui_element):
        self.command = command
        self.process = None
        global GUI_ELEMENT
        GUI_ELEMENT = gui_element

    def __enter__(self):

        # NOTE: a trailing comma inside args() is needed!!!
        self.process = KThread(target=api_function_call, args=(self.command,), daemon=True)
        self.process.start()
        return self.process

    def __exit__(self, *exec):
        self.process.join()


class AntInterpreter(InterpreterInterface):

    def __init__(self, gui_element: object = None):
        super().__init__()
        self.process = None
        self.gui_element = gui_element

    def execute(self, command):
        return Wrapper(command, self.gui_element)

    def terminate(self, processThread):

        # Terminate a running thread
        processThread.kill()

        # Sets a return code
        global RETURNCODE
        RETURNCODE = -1

    def get_return_code(self, process):
        return RETURNCODE

    def get_prompt(self):
        config = API.get_config()

        # Strip color ANSI code
        return re.sub(r'\x1b\[([0-9,A-Z]{1,2}(;[0-9]{1,2})?(;[0-9]{3})?)?[m|K]?', '', config["PROMPT"])
