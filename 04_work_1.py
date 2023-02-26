import argparse


parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*', default=['no args'])
print(*parser.parse_args().arg, sep='\n')