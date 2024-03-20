# This file will be to run meangen.exe through python.
import subprocess

if __name__ == "__main__":
    # Run the executable and communicate with it
    with subprocess.Popen(['meangen-17.4.exe'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True) as process:
        # Send input to the process
        process.stdin.write('F\n')