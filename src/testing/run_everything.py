'''
This file will automatically run every test
'''
import os
import time
import run_all_unit_tests
import run_all_system_tests

def run_all():
    print('PLEASE ENSURE THAT THE WEBSERVER IS RUNNING ON 127.0.0.1:3000')
    count = 5
    for c in range(count, 0, -1):
        print(c)
        time.sleep(1)

    print('')
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