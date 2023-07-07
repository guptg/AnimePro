# Python
import argparse
import os
import sys

# Local
from SettingUp.logging import create_console_logger
from ExploratoryDataAnalysis.preprocess_data import PreprocessImageDataTf

def main(argv):
    
    # Create logger
    logger = create_console_logger("Anime Project Logger")

    # Parse command line argument
    parser = argparse.ArgumentParser(description=
                                     "Recognizing characters from Naruto Face Dataset \
                                    from kaggle: \
                                    https://www.kaggle.com/neetuk/naruto-face-dataset/")
    parser.add_argument("dataset_path", metavar="DATASETPATH", help="Path to folder \
                        containing files in the dataset.")
    args = parser.parse_args(argv)
    
    # Get a workable tf dataset from the raw data
    data_processor = PreprocessImageDataTf({"dataPath": args.dataset_path}, logger)
    data = data_processor.get_processed_data()
    

    

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
