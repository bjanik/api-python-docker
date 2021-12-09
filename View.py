import readline
import sys

class View:
    def __init__(self):
        pass
    
    def read(self):
        return sys.stdin.readline()
        # return params['source']


    def show_lines(self, lines):
        print("="*25)
        print("Current file content:")
        for line in lines:
            print(line, end="")
        print("="*25)