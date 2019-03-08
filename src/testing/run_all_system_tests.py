'''
This file runs all unit tests for the project
'''
import sys
import os

HEADER = '='*50

def run_web_tests():
    '''
    cd web/test/gui_tests
    python3 -m unittest
    cd ..
    '''
    print(HEADER)
    print('WEB SYSTEM TESTS')
    os.chdir('web/test/gui_tests')
    os.system('python3 -m unittest')
    os.chdir('..')
    print(HEADER)
    print('')

def run_all():
    run_web_tests()

if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    run_all()