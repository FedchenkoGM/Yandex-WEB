import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--barbie", type=int, default=50)
parser.add_argument("--cars", type=int, default=50)
parser.add_argument("--movie", choices=['melodrama', 'football', 'other'],
                    default='other')
arg = parser.parse_args()

boy = 100 - (arg.barbie if 0 <= arg.barbie <= 100 else 50) + \
            (arg.cars if 0 <= arg.cars <= 100 else 50)

if arg.movie == 'other':
    boy += 50
elif arg.movie == 'football':
    boy += 100

boy = int(boy / 3)
print(f"boy: {boy}\ngirl: {100 - boy}")

