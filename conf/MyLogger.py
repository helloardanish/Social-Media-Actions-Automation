import logging
import os
from datetime import datetime

class DailyRollingFileHandlerWithTag(logging.FileHandler):
    """
    Custom FileHandler that creates daily log files with class name tags.
    """

    def __init__(self, filename_prefix, tag, datefmt="%Y-%m-%d"):
        self.filename_prefix = filename_prefix
        self.tag = tag
        self.datefmt = datefmt
        self.current_date = datetime.now().strftime(self.datefmt)
        self.current_filename = self.compute_filename()
        # Call the superclass constructor with the initial filename
        super().__init__(self.current_filename)

    def compute_filename(self):
        """
        Compute the filename based on the current date and tag.
        """
        if datetime.now().strftime(self.datefmt) == self.current_date:
            return os.path.join(self.filename_prefix, "app.log")
        else:
            return os.path.join(self.filename_prefix, f"{self.current_date}_{self.tag}.log")

    def emit(self, record):
        """
        Emit a record, rolling over at midnight.
        """
        try:
            new_date = datetime.now().strftime(self.datefmt)
            if self.current_date != new_date:
                self.current_date = new_date
                self.current_filename = self.compute_filename()
                self.rotate_log_file()
                self.baseFilename = self.current_filename
                self.stream = self._open()
            logging.FileHandler.emit(self, record)
        except Exception:
            self.handleError(record)

    def rotate_log_file(self):
        """
        Rotate the log file by renaming the current 'app.log' to a date-prefixed file.
        """
        if os.path.exists(os.path.join(self.filename_prefix, "app.log")):
            new_filename = os.path.join(self.filename_prefix, f"{self.current_date}_{self.tag}.log")
            os.rename(os.path.join(self.filename_prefix, "app.log"), new_filename)

def customlogger(tag, filename_prefix="log"):
    """
    Creates a logger object with a DailyRollingFileHandlerWithTag.
    """
    logger = logging.getLogger(tag)
    logger.setLevel(logging.DEBUG)  # Adjust logging level as needed

    if not os.path.exists(filename_prefix):
        os.makedirs(filename_prefix)  # Create log directory if it doesn't exist

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
    file_handler = DailyRollingFileHandlerWithTag(filename_prefix, tag)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

# Usage example:
# logger = create_logger("app")
# logger.info("This is a test log message.")