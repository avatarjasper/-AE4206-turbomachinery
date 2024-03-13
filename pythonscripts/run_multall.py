'''this code is to run multall in case you have ran meangen and stagen manually.'''

import subprocess

def run_multall():
    subprocess.run(['multall-open-20.9.exe'] + ['<', 'stage_new.dat', '>', 'results.txt'], check=True)

if __name__=="__main__":
    run_multall()