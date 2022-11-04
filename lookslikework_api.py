import os
from time import sleep
from tqdm import tqdm
from random import *
import random
import requests


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

working = "not working"
passfail = ['pass', 'fail']

while working != "working":
    tech = requests.get('http://127.0.0.1:5000/tech')
    t = tech.json()
    
    print(f'{BColors.OKBLUE}{t["quote"]} {BColors.ENDC}')
    x = 0
    while x < 4:
        x = x + 1
        verb = requests.get('http://127.0.0.1:5000/tech/verb').json()
        noun = requests.get('http://127.0.0.1:5000/tech/noun').json()
        print(f'{verb["verb"]} {noun["noun"]} ...')
        for i in tqdm(range(randint(1, 20))):
            sleep(1)
        sleep(5)
        
        if(random.choice(passfail) == 'pass'):
            print(f'{BColors.OKGREEN} PASS {BColors.ENDC} ')
        else:
            print(f'{BColors.FAIL} FAIL {BColors.ENDC} ')


        

