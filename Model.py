# class ListeChaine:
#     def __init__(self):
#         self._lines = []
    
#     def add_line(self, line):
#         self._lines.append(line.upper())

#     @property
#     def lines(self):
#         return self._lines
 
class Model:
    # Model aggregate lines read on standard input and saves them into a file
    def __init__(self):
        self._lines = []

    def add_line(self, line):
        self._lines.append(line.upper())

    @property
    def lines(self):
        return self._lines