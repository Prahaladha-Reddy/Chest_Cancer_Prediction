from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_1_data_ingestion import *

STAGE_NAME='Data Ingestion'

try:
  logger.info(f'>>> Stage {STAGE_NAME} started <<<')
  obj=DataIngestionTrainingPipeline()
  obj.main()
  logger.info(f'>> stage {STAGE_NAME} completed <<')
except Exception as e:
  logger.exception(e)
  raise e
