import sys
import time


def main(argv):

    print("Going to sleep")
    # Wait for 10 seconds
    time.sleep(10)

    print("waking up")


# -----------------< Main Program>---------------------------------------
if __name__ == "__main__":
    main(sys.argv[1:])
