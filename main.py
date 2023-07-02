# Python
import argparse
import os
import sys

# Local
from SettingUp.logging import create_console_logger
from ExploratoryDataAnalysis.preprocess_data import PreprocessData

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
    
    # Check to see if dataset directory existss
    if not os.path.isfile(args.dataset_path):
        raise FileExistsError("f{args.dataset_path} does not exist")
    
    # Pre process the dataset   
    data_processor = PreprocessData({"datasetPath": args.dataset_path}, logger)
    data = data_processor.load_data()
    

    

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
