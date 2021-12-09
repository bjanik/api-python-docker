from Model import Model
from View import View

class Controller:
    def __init__(self, model: Model, view: View, filename=None):
        self._model = model
        self._view = view
        self._filename = filename

    def get_line(self):
        line = self._view.read()
        self._model.add_line(line)

    def insert_lines(self):
        return self._model.lines[0]
        # with open(self._filename, "a+") as f:
        #     for line in self._model.lines:
        #         f.write(line)
