import abc

class Preprocessor(abc.ABC):

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def preprocess_image(self, image):
        self.processed_image = image
        return self.processed_image

    @abc.abstractmethod
    def get_preprocessed_image(self):
        return self.processed_image