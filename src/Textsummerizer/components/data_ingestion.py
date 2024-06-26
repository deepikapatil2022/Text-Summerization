import os
import urllib.request as request
import zipfile
from Textsummerizer.logging import logger
from Textsummerizer.utils.common import get_size
from pathlib import Path
from Textsummerizer.entity import DataInjestionConfig

class DataInjestion:
    def __init__(self, config: DataInjestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers =request.urlretrieve(
                url =self.config.source_URL,
                filename =self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size : {get_size(Path(self.config.local_data_file))}")


    def extract_zip_file(self):
        """zip_file_path:str
        Exctarcts the zip file into the data directory
        Function returns none
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
            zip_ref.extractall(unzip_path)
