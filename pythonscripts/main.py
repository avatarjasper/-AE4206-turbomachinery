import subprocess


def run_executable(executable, command):
    with subprocess.Popen([executable], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True) as process:
        # Send input to the process
        process.stdin.write(command+'\n')


def change_meangen():
    pass

def change_stagen():
    pass




if __name__ == "__main__":
    # Specify the details for each executable
    executables = [
        {"path": "meangen-17.4.exe", "args": "F"},
        {"path": "stagen-18.1.exe", "args": "Y"},
    ]




    # Run executables sequentially
    for executable in executables:
        print(executable)
        if executable == 'meangen-17.4.exe':
            change_meangen()
        if executable == 'stagen-18.1.exe':
            change_stagen()
        run_executable(executable["path"], executable["args"])

    print("Multall is starting!")
    subprocess.run(['multall-open-20.9.exe'] + ['<', 'stage_new.dat', '>', 'results.txt'], check=True)
    print("Multall has ended!")
