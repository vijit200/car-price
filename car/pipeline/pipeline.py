from car.config.configuration import Configuartion
from housing.logger import logging
from car.exception import HousingException

from car.entity.artifact_entity import DataIngestionArtifact
from car.entity.config_entity import DataIngestionConfig
from car.component.data_ingestion import DataIngestion
import os, sys


class pipeline:

    def __init__(self, config: Configuartion = Configuartion()) -> None:
        try:
            self.config = config

        except Exception as e:
            raise HousingException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:

            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()


    def start_data_validation(self):
        pass

    def start_data_transformation(self):
        pass

    def start_model_trainer(self):
        pass

    def start_model_evaluation(self):
        pass

    def start_model_pusher(self):
        pass

    def run_pipeline(self):
        try:
            # data ingestion

            data_ingestion_artifact = self.start_data_ingestion()




        except Exception as e:
            raise HousingException(e, sys) from e