from Textsummerizer.config.configuration import ConfigurationManager
from Textsummerizer.components.data_transformation import DataTransformation
from Textsummerizer.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise e
