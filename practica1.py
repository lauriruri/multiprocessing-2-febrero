#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 09:11:53 2023

@author: alumno
"""

from time import sleep
from random import random
"""
DocumentaciÃ³n multiprocessing
https://docs.python.org/3.6/library/multiprocessing.html
"""
from multiprocessing import Process
def f():
    for i in range(5):
        print ("hola", i)
        sleep(random())
        if __name__ == "__main__":
            p = Process(target=f)
            q = Process(target=f)
            p.start()
            q.start()
            print ("fin")