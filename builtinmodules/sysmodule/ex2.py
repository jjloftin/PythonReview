import sys

##sys.stderr.write('test')
##sys.stderr.flush()
##
##sys.stdout.write('\nThis is stdouttext\n')
##
##print(sys.argv)

#make second argument in cmd prompt a number
if len(sys.argv) > 1:
    print(float(sys.argv[1]) + 5)
