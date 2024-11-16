from .settings import *
from decouple import config
from config.utils.logging_config import ANSIColorFormatter

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Configura los detalles de conexión a Papertrail
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'custom_format': {
            '()': ANSIColorFormatter,
            'format': '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',  # Formato de fecha y hora
        },
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'custom_format',  # Usa el formato personalizado
        },
        'papertrail': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'custom_format',  # Usa el formato personalizado para Papertrail
            'address': (config('HOST_PAPERTRAIL'), int(config('PORT_PAPERTRAIL'))),
        },
    },
    'root': {
        'handlers': ['console', 'papertrail'],
        'level': 'DEBUG',
    },
}