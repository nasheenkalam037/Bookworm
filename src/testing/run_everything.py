'''
This file will automatically run every test
'''
import os
import run_all_unit_tests
import run_all_system_tests

def run_all():
    print('*'*50)
    print('* UNIT TESTS')
    print('*'*50)
    run_all_unit_tests.run_all()

    print('\n')
    print('*'*50)
    print('* UNIT TESTS')
    print('*'*50)
    run_all_system_tests.run_all()



if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    os.chdir('..')

    run_all()