"""Python serial number generator."""

from itertools import count


class SerialGenerator():
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    # python3 -m doctest -v serial.py

    def __init__(self, start):
        "generate a serial number from a start point,start from one less then add one each time"
        self.start = start
        self.value = self.start-1
    def __repr__(self):
        return f"<start is {self.start}>"

    def generate(self):
        "self.value will increase by 1 evertime generate is called"
        self.value = self.value + 1
        return self.value        
    def reset(self):
        "reset the value so start can begin one less"
        self.value = self.start-1
        return None


    # def __init__(self, start=0):
    #     """Make a new generator, starting at start."""

    #     self.start = self.next = start

    # def __repr__(self):
    #     """Show representation."""

    #     return f"<SerialGenerator start={self.start} next={self.next}>"

    # def generate(self):
    #     """Return next serial."""

    #     self.next += 1
    #     return self.next - 1

    # def reset(self):
    #     """Reset number to original start."""

    #     self.next = self.start