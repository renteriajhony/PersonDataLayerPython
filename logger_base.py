import logging as log

log.basicConfig(
    level=log.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - [File: %(filename)s: Line %(lineno)s] - Message: %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        log.FileHandler('/Users/jrenteria/PycharmProjects/BD/PersonDataLayerPython/register_logs_app/logger.log'),
        log.StreamHandler()
    ]
)

if __name__ == '__main__':
    log.debug('debug message')
    log.info('info message')
    log.warning('warning message')
    log.error('error message')
    log.critical('critical message')