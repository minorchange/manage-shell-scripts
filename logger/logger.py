import logging
from logging import config
import telegram_handler
import json


f = open("logger/credentials-telegrambot.json")
tc = json.load(f)


logger_config_dict = {
    "version": 1,
    "formatters": {
        "std_out": {
            "format": "%(asctime)s - %(levelname)s in %(module)s - %(funcName)s line %(lineno)d\n    %(message)s",
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "formatter": "std_out",
            "class": "logging.StreamHandler",
            "level": "DEBUG",
        },
        "rotating_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "std_out",
            "level": "DEBUG",
            "filename": "rfh.log",
            "maxBytes": 2000000,
            "backupCount": 2,
        },
        "telegram": {
            "class": "telegram_handler.TelegramHandler",
            "token": f"{tc['SENDER_BOT_TOKEN']}",
            "chat_id": f"{tc['RECIEVER_CHAT_ID']}",
            "formatter": "std_out",
        },
    },
    "loggers": {
        "my_logger": {
            "handlers": ["console", "rotating_file", "telegram"],
            "level": "DEBUG",
        }
    },
}

config.dictConfig(logger_config_dict)
logger = logging.getLogger("my_logger")


if __name__ == "__main__":
    logger.error("Blubb!")
    logger.warning("Blubb?")
