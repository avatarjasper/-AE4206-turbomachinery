import subprocess


def run_executable(executable, command):
    with subprocess.Popen([executable], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True) as process:
        # Send input to the process
        process.stdin.write(command+'\n')


if __name__ == "__main__":
    # Specify the details for each executable
    executables = [
        {"path": "meangen-17.4.exe", "args": "F"},
        {"path": "stagen-18.1.exe", "args": "Y"},
    ]

    # Run executables sequentially
    for executable in executables:
        print(executable)
        run_executable(executable["path"], executable["args"])

    print("Multall is starting!")
    subprocess.run(['multall-open-20.9.exe'] + ['<', 'stage_new.dat', '>', 'results.txt'], check=True)
    print("Multall has ended!")
