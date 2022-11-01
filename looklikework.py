import os
from time import sleep
from tqdm import tqdm
from random import *
import random


# Colors
class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[90m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# print(f'Successfully downloaded {BColors.OKGREEN}hello {BColors.ENDC} to {format}')
os.system('clear')

things = [
    "productize web-enabled web services",
    "repurpose ubiquitous users",
    "e-enable value-added dark web",
    "aggregate sticky users",
    "repurpose bleeding-edge SaaS"
]
verbs = ['aggregate', 'benchmark', 'deploy', 'extend', 'implement']
nouns = ['Database', 'Container', 'Virtual Machine', 'Data', 'Network']

for t in things:

    print(f'{BColors.OKBLUE}{t} {BColors.ENDC}')
    x = 0
    while x < 4:
        x = x + 1
        verb = random.choice(verbs)
        noun = random.choice(nouns)
        print(f'{verb} {noun} ...')
        for i in tqdm(range(randint(1, 20))):
            sleep(1)
        sleep(5)
        passfail = ['pass', 'fail']

        print(f'{BColors.WARNING} {random.choice(passfail)}{BColors.ENDC} ')
