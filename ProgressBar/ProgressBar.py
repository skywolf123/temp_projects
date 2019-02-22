import sys
import time
def progress_bar(total):
    _output=sys.stdout
    for count in range(0,total+1):
        _second=0.1
        time.sleep(_second)
        _output.write(f'\rcomplete percent:{count:.0f}')
    _output.flush()


if __name__ == "__main__":
    progress_bar(100)