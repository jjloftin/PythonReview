#ITERATOR REVIEW

'''
Try writing your own iterator class that allows you to specify the lengths of steps the iterator makes.
eg.
 when you call you step iterator class you specify the steps.

string = Steps('Drapsicle', 2)
    for char in rev:
        print(char)

which outputs
D,a,s,c,e

Then try writing a generator that does the same thing!
'''

class Steps:

    def __init__(self, data, numStep):
        self.data = data
        self.numStep = numStep
        self.index = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        returnVal = self.data[self.index]
        self.index += self.numStep

        return returnVal
        
def Main():
    x = Steps('Jogginga',4)
    print(list(x))

if __name__ == '__main__':
    Main()
