'''
This file runs all unit tests for the project.
Requires the current working directory to be ece651/src/
'''
import sys
import os

HEADER = '='*50

def run_scraper_tests():
    '''
    cd scraper
    python3 -m unittest
    cd ..
    '''
    print(HEADER)
    print('SCRAPER UNIT TESTS')
    os.chdir('scraper')
    os.system('python3 -m unittest')
    os.chdir('..')
    print(HEADER)
    print('')

def run_ml_tests():
    '''
    cd scraper
    python3 -m unittest
    cd ..
    '''
    print(HEADER)
    print('ML UNIT TESTS')
    os.chdir('ml')
    os.system('python3 -m unittest')
    os.chdir('..')
    print(HEADER)
    print('')

def run_web_tests():
    '''
    cd web
    python3 -m unittest
    cd ..
    '''
    print(HEADER)
    print('WEB UNIT TESTS')
    os.chdir('web')
    os.system('npm test')
    os.chdir('..')
    print(HEADER)
    print('')

def run_all():
    run_scraper_tests()
    run_ml_tests()
    run_web_tests()


if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    run_all()