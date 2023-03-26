from TkTerm.backend.InterpreterInterface import InterpreterInterface
from TkTerm.backend.KThread import KThread

from Ant.src.lib.api import ANT_API

import re
import subprocess
import os
import sys

# Adjust this according to where ANT is found
ANT_EXECUTABLE = f"{sys.executable} -u Ant/src/ant.py"

API = ANT_API()

class AntInterpreter2(InterpreterInterface):

    def __init__(self, gui_element: object = None):
        super().__init__()
        self.gui_element = gui_element

        self.history = []

        self.process_options = {
            "shell"                 : True,
            "stdout"                : subprocess.PIPE,
            "stderr"                : subprocess.PIPE,
            "universal_newlines"    : True,
            "cwd"                   : os.getcwd()
        }

        # Ignore utf-8 decode error which sometimes happens on early terminating
        if os.name != "nt":
            self.process_options["errors"] = "ignore"

    def execute(self, command):

        if command == "exit":
            self.gui_element.destroy()

        return subprocess.Popen(f"{ANT_EXECUTABLE} -c '{command}'", **self.process_options)

    def terminate(self, processThread):

        stdout = ""
        stderr = ""

        if (os.name == 'nt'):
            process = subprocess.Popen(
                "TASKKILL /F /PID {} /T".format(processThread.pid),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )

            for line in process.stdout:
                stdout += line
            for line in process.stderr:
                stderr += line

        else:

            try:
                os.system("pkill -TERM -P %s" % processThread.pid)
                os.system("kill -2 {}".format(processThread.pid))
                os.system("kill -9 {}".format(processThread.pid))
            except:
                pass

        return (stdout, stderr)

    def get_return_code(self, process):
        return process.poll()

    def get_prompt(self):
        config = API.get_config()

        # Strip color ANSI code
        return re.sub(r'\x1b\[([0-9,A-Z]{1,2}(;[0-9]{1,2})?(;[0-9]{3})?)?[m|K]?', '', config["PROMPT"])

    def get_history(self):

        # TODO: Still not able to get history properly
        # return API.get_history()

        return self.history