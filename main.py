from Textsummerizer.logging import logger
from Textsummerizer.pipeline.stage_01_data_ingestion import DataInjestionTrainingPipeline

STAGE_NAME= "Data Ingestion Stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_ingestion = DataInjestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    raise e