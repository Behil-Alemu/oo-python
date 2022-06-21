import random
import this

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in list(self.get_file)
    True
    >>> wf.random() in list(self.get_file)
    True

    >>> wf.random() in self.get_file
    True"""
 

    def __init__(self, file):
        self.file = file
        self.get_file = open(self.file,'r')

    # len(f.readlines())
    def __repr__(self):
        "The lenght of words in the file provide"
        return f"<{len(self.get_file.readlines())} words read>"


    # def random(self):
    #     for rand in self.get_file:
    #         return random.choice(rand)

    def random(self):
        "goes thought each file in line and choice a random word the returns it "
        lines = open(self.file).read().splitlines()
        myline =random.choice(lines)
        return myline



        # def SpecialWordFinder(cls):
        # return cls(str(file))

        
#     def __init__(self, path):
#         """Read dictionary and reports # items read."""

#         dict_file = open(path)

#         self.words = self.parse(dict_file)

#         print(f"{len(self.words)} words read")

#     def parse(self, dict_file):
#         """Parse dict_file -> list of words."""

#         return [w.strip() for w in dict_file]

#     def random(self):
#         """Return random word."""

#         return random.choice(self.words)


# class SpecialWordFinder(WordFinder):
#     """Specialized WordFinder that excludes blank lines/comments.
    
#     >>> swf = SpecialWordFinder("complex.txt")
#     3 words read

#     >>> swf.random() in ["pear", "carrot", "kale"]
#     True

#     >>> swf.random() in ["pear", "carrot", "kale"]
#     True

#     >>> swf.random() in ["pear", "carrot", "kale"]
#     True
#     """

#     def parse(self, dict_file):
#         """Parse dict_file -> list of words, skipping blanks/comments."""

#         return [w.strip() for w in dict_file
#                 if w.strip() and not w.startswith("#")]
    
    