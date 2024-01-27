import os
import sys
import requests
from LoggingClass import LoggingClass

# ----------------------------------------------------------------------
# Logger Settings
# ----------------------------------------------------------------------
LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG")
logger = LoggingClass(LOG_LEVEL)
log = logger.get_logger()

# ----------------------------------------------------------------------
# Main Function
# ----------------------------------------------------------------------
def main() -> None:
    log.debug("{}() Processing start".format(sys._getframe().f_code.co_name))
    print("Hello World")
    response = requests.get('https://www.google.com')
    print(response.status_code)
    print(response.text)
    log.debug("{}() Processing end".format(sys._getframe().f_code.co_name))

# ----------------------------------------------------------------------
# Entry Point
# ----------------------------------------------------------------------
def lambda_handler(event, context):
    log.debug("{}() Processing start".format(sys._getframe().f_code.co_name))
    try:
        main()
    except Exception as e:
        log.error("{}() Processing error: {}".format(sys._getframe().f_code.co_name, str(e)))
    log.debug("{}() Processing end".format(sys._getframe().f_code.co_name))