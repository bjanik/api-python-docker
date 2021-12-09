import sys

from Controller import Controller
from Model import Model
from View import View

FILENAME = "lines.txt"

controller = Controller(Model(), View(), FILENAME)
try:
    for _ in range(2):
        controller.get_line()
    controller.insert_lines()
except KeyboardInterrupt:
    sys.exit(130)