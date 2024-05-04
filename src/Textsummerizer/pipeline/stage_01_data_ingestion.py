from Textsummerizer.config.configuration import ConfigurationManager
from Textsummerizer.components.data_ingestion import DataInjestion
from Textsummerizer.logging import logger

class DataInjestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:

            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataInjestion(config = data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e


    