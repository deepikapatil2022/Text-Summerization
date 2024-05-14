from Textsummerizer.config.configuration import ConfigurationManager
from Textsummerizer.components.model_trainer import ModelTrainer
from Textsummerizer.logging import logger

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
             config = ConfigurationManager()
             model_trainer_config = config.get_model_trainer_config()
             model_trainer_config = ModelTrainer(config=model_trainer_config)
             model_trainer_config.train()
        except Exception as e:
            raise e