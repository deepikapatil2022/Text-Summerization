from Textsummerizer.logging import logger
from Textsummerizer.pipeline.stage_01_data_ingestion import DataInjestionTrainingPipeline
from Textsummerizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Textsummerizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME= "Data Ingestion Stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_ingestion = DataInjestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    raise e

STAGE_NAME= "Data Validation Stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    raise e

STAGE_NAME= "Data Transforamtion Stage"

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_validation = DataTransformationTrainingPipeline()
    data_validation.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    raise e


