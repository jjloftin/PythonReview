#GENERATOR REVIEW

#yield makes this for loop act like an iterator, you can call next on it
def Reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

def Main():
    rev = Reverse('Lofty')

    while True:
        try:
            print(next(rev))
        except StopIteration:
            print('DONE')
            break
    data = 'Jackelope'

    #x[i] for i in range() creates a generator
    #list takes in the generator which is iterable and produces a list out of it
    print(list(data[i] for i in range(len(data)-1,-1,-1)))

    print(list(Reverse(data)))
if __name__ == '__main__':
    Main()
