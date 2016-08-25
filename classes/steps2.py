#GENERATOR REVIEW

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

def Steps(data,numStep):
    return (data[i] for i in range(0,len(data),numStep))

def Steps2(data, numStep):
    for i in range(0,len(data),numStep):
        yield data[i]
        
def Main():
    x = Steps('Jogginga',1)
    print(list(x))
    x = Steps2('Jogging',2)
    print(list(x))

if __name__ == '__main__':
    Main()
