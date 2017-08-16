#I want you to add a __str__ method to the Letter class that loops 
# through the pattern attribute of an instance and returns "dot" for
# every "." (period) and "dash" for every "_" (underscore). Join them 
# with a hyphen.
#I've included an S class as an example (I'll generate the others when 
# I test your code) and it's __str__ output should be "dot-dot-dot".

class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        output = []
        for element in self.pattern:
            if element == ".":
                output.append("dot")
            if element == "_":
                output.append("dash")
        print("-".join(output))

    @classmethod
    def from_string(cls, dash_dots):
        output = []
        dash_dots.split('-')
        for blip in dash_dots:
            if blip == 'dash':
                output.append('_')
            if blip == 'dot':
                output.append('.')
        return cls(output)
    

class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)