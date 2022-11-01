import os
from time import sleep
from tqdm import tqdm
from random import *


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


# Print(f'Successfully downloaded {bcolors.OKGREEN}hello {bcolors.ENDC} to {format}')
os.system('clear')

things = [
    "productize web-enabled web services",
    "repurpose ubiquitous users",
    "e-enable value-added dark web",
    "aggregate sticky users",
    "repurpose bleeding-edge SaaS"
]

for t in things:

    print(f'{BColors.OKBLUE}{t} {BColors.ENDC}')
    x = 0
    while x < 10:
        x = x + 1
        print('Setup...')
        for i in tqdm(range(randint(1, 20))):
            sleep(3)
        sleep(5)
