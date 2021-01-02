# main.py

# Imports
import os
import multiprocessing


def react():
    os.chdir(os.path.join(os.getcwd(), 'frontend'))
    os.system('npm start')
    

def flask():
    os.chdir(os.path.join(os.getcwd(), 'backend'))
    os.system('python3.6 server.py')


if __name__ == '__main__':
    multiprocessing.Process(target=react).start()
    multiprocessing.Process(target=flask).start()

