from datetime import datetime
from conf.MyLogger import customlogger

logger = customlogger("CommonOperation")


class CommonOperation:

    def __init__(self):
        logger.info("Common Operation Initiated")

    @staticmethod
    def current_msg_with_time(msg):
        # Get the current date and time
        current_datetime = datetime.now()

        # Format the date and time as a string
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        logger.info(msg + formatted_datetime)

