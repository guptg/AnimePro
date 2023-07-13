# Python
import os
import glob

from abc import abstractmethod

# Third-party
import tensorflow as tf

class PreprocessData():
    """Class that handles raw data and processes it into curated data ready to work with. 
    """

    # Valid formats for data files, must be implemented in subclasses
    EXTENSION_KEY = NotImplemented

    def __init__(self, parameters: dict, logger: "logging.Logger"):
        """ Constructor

        Args:
            parameters (dict): Contains all needed parameters
            logger (logging.Logger): Standard logging object
        """

        self._logger = logger

        # Unpack parameters
        self._data_path = parameters.get("dataPath", None)

        # Other properties
        self._dataset_file_paths = None
        self._file_extensions = None

        # Check to see if the directory or file path exists
        if not os.path.exists(self._data_path):
            raise FileExistsError("f{self._data_path} does not exist.")

    @abstractmethod
    def get_processed_data(self, split: bool=False):
        """Loads and preprocesses the data.

        Args:
            split (bool, optional): Splits the data into training and test sets. Defaults to False
        """

    def _get_file_extension(self, file_path: str):
        """Gets the file format.

        Args:
            file_path (str): File path

        Raises:
            RuntimeError: File extension is not mappped in VALID_FORMATS

        Returns:
            str: File format 
        """

        file_extension = os.path.splitext(file_path)[1]

        if file_extension not in self.EXTENSION_KEY:
            raise RuntimeError(f"File {file_path} has an invalid extension.")
        
        return file_extension
    

    def _get_file_size(self, file_path):
        """Gets the file size.

        Args:
            file_path (str): File path

        Returns:
            int: The size of th file
        """

        return os.path.getsize(file_path) / (1024 * 1024)


class PreprocessImageData(PreprocessData):
    """Class that handles raw image data and processes it into curated data ready to work with.
    """

    EXTENSION_KEY = {".jpg": ["JPEG"]}

    def get_processed_data(self, split: bool=False):
        """Loads and preprocesses the data.

        Args:
            split (bool, optional): Splits the data into training and test sets. Defaults to False
        """
        
        # Get basic information
        self._log_first_glance()


    def _log_first_glance(self):
        """
        Outputs information logs about the dataset directory contents. 
        """

        if os.path.isfile(self._data_path):
            self._dataset_file_paths = [self._data_path]
            self._file_extensions = [self._get_file_extension(x) for x in self._dataset_file_paths]
            self._logger.info("Image is a " 
                              + self.EXTENSION_KEY[self._get_file_extension(self._data_path)][0] 
                              + f" of size {self._get_file_size(self._data_path):.4f} MB.")
        
        elif os.path.isdir(self._data_path):
            self._dataset_file_paths = glob.glob(self._data_path + "*")
            self._file_extensions = [self._get_file_extension(x) for x in self._dataset_file_paths]
            dataset_size = sum([self._get_file_size(x) for x in self._dataset_file_paths])

            self._logger.info(f"The dataset directory has {len(self._dataset_file_paths)} images "
                              + "with file formats "
                              + ", ".join(
                              map(lambda x: self.EXTENSION_KEY[x][0], set(self._file_extensions))) 
                              + f" and a total size of {dataset_size:.4f} MB.")



class PreprocessImageDataTf(PreprocessImageData):
    """Class that handles raw image data and processes it into curated tf data ready to work with.
    """

    EXTENSION_KEY = {".jpg": ["JPEG", tf.image.decode_jpeg]}
    RESIZE = 224
    WHITE = 255

    def get_processed_data(self, split: bool=False):
        """Loads and preprocesses the data.

        Args:
            split (bool, optional): Splits the data into training and test sets. Defaults to False

        Returns:
            tf.data.Dataset: TensorFlow dataset 
        """

        # Get basic information
        self._log_first_glance()

        # Make a tensorflow dataset
        data_paths = tf.data.Dataset.from_tensor_slices(self._dataset_file_paths)
        data = [self._process_data(path, extension) 
                  for path, extension in zip(data_paths, self._file_extensions)]

        return tf.data.Dataset.from_tensor_slices(data)
 
    def _process_data(self, file_path: tf.Tensor, file_extension: str):
        """Preprocesses raw image data. 

        Args:
            file_path (tf.Tensor): Image file path
            file_extension (str): Image file extension

        Returns:
            tf.Tensor: Preprocessed image data
        """
        image = tf.io.read_file(file_path)
        image = self.EXTENSION_KEY[file_extension][1](image, channels=3)
        image = tf.image.resize(image, [self.RESIZE, self.RESIZE]) 
        image = image / self.WHITE

        return image