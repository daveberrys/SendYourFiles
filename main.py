from src.front.window import startUp as s

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action="store_true", help="enable debug mode")
args = parser.parse_args()

debugMode = args.debug

if __name__ == "__main__":
    s(debugMode=debugMode)