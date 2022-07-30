
from car.pipeline.pipeline import pipeline
from car.exception import HousingException
from car.logger import logging
def main():
    try:
        pipe = pipeline()
        pipe.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()