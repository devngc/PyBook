"""This module shows the use of computed attributes."""


class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # Getting the computed attribute here
    def __getattr__(self, attr):
        if attr == 'rgbcolor':
            return (self.red, self.green, self.blue)
        elif attr == 'hexcolor':
            return '#{0:02x}{1:02x}{2:02x}'.format(self.red, self.green, self.blue)
        else:
            raise AttributeError
    
    def __setattr__(self, attr, val):
        if attr == 'rgbcolor':
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            # The following is important because these attributes are set in the init.
            # For each of those attributes, this part of the code will be executed.
            super().__setattr__(attr, val)
    
    def __dir__(self):
        return ('red', 'green', 'blue', 'rgbcolor', 'hexcolor')


sample = myColor()
print(sample.rgbcolor)
print(sample.hexcolor)
sample.rgbcolor = [125, 200, 86]
print(sample.rgbcolor)
print(sample.hexcolor)
sample.rgbcolors = [255, 200, 86]
print(sample.rgbcolors)
print(dir(sample))
