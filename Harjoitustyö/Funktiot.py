# Funktiot alustus

import time
import sys

def slowPrint(string, speed=0.05):
    for char in string + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)