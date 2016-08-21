import sys

sys.stderr.write('test')
sys.stderr.flush()

sys.stdout.write('\nThis is stdouttext\n')

print(sys.argv)

if len(sys.argv) > 1:
    print(sys.argv[1])
