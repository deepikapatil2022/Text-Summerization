from Textsummerizer.constant import *
from Textsummerizer.utils.common import read_yaml,create_directories
from Textsummerizer.entity import DataInjestionConfig
from Textsummerizer.entity import DataValidationConfig

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH):
            self.config = read_yaml(config_filepath)
            self.params = read_yaml(params_filepath)

            create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataInjestionConfig:
        config=self.config.data_ingestion

        create_directories([config.root_dir])
        data_injestion_config = DataInjestionConfig(
             root_dir=config.root_dir,
             source_URL= config.source_URL,
             local_data_file= config.local_data_file,
             unzip_dir= config.unzip_dir
                            
            )
        return data_injestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )

        return data_validation_config 