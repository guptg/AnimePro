# Python
import logging


def create_console_logger(logger_name: str) -> logging.Logger:
    """Returns a logging object that outputs messages to the console at the debug level of 
    verbosity.

    Args:
        logger_name (str): Name of the logger.

    Returns:
        logging.logger: Cosole logging object. 
    """

    # Create a logger
    logger = logging.getLogger(name=logger_name)

    # Set the log level
    logger.setLevel(logging.DEBUG)

    # Create a console handler
    console_handler = logging.StreamHandler()

    # Set the log level for the console handler
    console_handler.setLevel(logging.DEBUG)

    # Create a formatter
    formatter = logging.Formatter('%(threadName)s - %(relativeCreated)d - %(name)s - %(levelname)s \
                                  %(message)s')

    # Add the formatter to the handler
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)

    return logger
