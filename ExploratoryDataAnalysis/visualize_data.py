# Third-party

import matplotlib.pyplot as plt

class VisualizeImageData:
    """Class to visulize image data in different ways."""


    def __init__(self, parameters: dict, logger: "logging.Logger"):
        """ Constructor

        Args:
            parameters (dict): Contains all needed parameters
            logger (logging.Logger): Standard logging object
        """

        self._logger = logger

        # Unpack parameters
        self._image_data = parameters.get("imageData", None)



class VisualizeImageDataTf(VisualizeImageData):
    """Class to visulize tensorflow image data in different ways."""


    def view_snapshot(self):

        for image in self._image_data.take(2): 
            plt.imshow(image.numpy().astype("uint8"))
            plt.axis("off")
            plt.savefig("/home/ggupta/Datasets/NarutoFaces/plot.png")

    
    # Todo add logger info that snapshots have been saved to:
                





