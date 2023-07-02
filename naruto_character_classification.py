# Python
import argparse
import sys

# Local
from SettingUp.logging import create_console_logger

def main(argv):


    # Create logger
    logger = create_console_logger("Anime Project Logger")

    # Parse command line argument
    parser = argparse.ArgumentParser(description=
                                     "Recognizing characters from Naruto Face Dataset \
                                    from kaggle: \
                                    https://www.kaggle.com/neetuk/naruto-face-dataset/")
    



if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
