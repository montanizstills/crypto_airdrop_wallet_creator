import logging


# def print_and_log(log_type, msg, mode, file_name):
#     # logging.basicConfig(filename=file_name, filemode=mode, level=log_type)
#     # logger = logging.getLogger()
#     # if log_type is 'debug': debug(logger, msg)
#     # if log_type is 'info': info(logger, msg)
#     # if log_type is 'warning | warn': warn(logger, msg)
#     # if log_type is 'error': error(logger, msg)
#     # if log_type is 'critical': critical(logger, msg)
#
# def debug(logger, msg):
#     logger.log(msg)


def print_and_log(log_type, msg):
    # Set up logging configuration
    logging.basicConfig(filename='app.log', level=logging.DEBUG, filemode='w')

    # Create a logger
    logger = logging.getLogger()

    # Map the log_type to the corresponding logging level
    log_level = {
        logging.DEBUG: logging.DEBUG,
        logging.INFO: logging.INFO,
        logging.WARNING: logging.WARNING,
        logging.WARN: logging.WARNING,
        logging.ERROR: logging.ERROR,
        logging.CRITICAL: logging.CRITICAL
    }.get(log_type, logging.INFO)

    # Set the logger level
    logger.setLevel(log_level)

    # Print the message
    print(msg)

    # Log the message
    logger.log(log_level, msg)
