import requests
import os
from time import time, sleep
import telegram
from dotenv import load_dotenv
import logging

logger = logging.getLogger('Logger')

class TelegramLogsHandler(logging.Handler):

    def __init__(self, tg_bot, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = tg_bot

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)


def main():
    load_dotenv()
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    dvmn_token = os.environ["DVMN_TOKEN"]
    chat_id = int(os.environ['TG_CHAT_ID'])
    tg_bot = telegram.Bot(token=telegram_token)

    long_polling_url = 'https://dvmn.org/api/long_polling/'
    headers = {'Authorization': dvmn_token}
    params = {'timestamp': time()}

    logger.setLevel(logging.INFO)
    logger.addHandler(TelegramLogsHandler(tg_bot, chat_id))
    logger.info('Бот в деле')

    while True:
        try:
            response = requests.get(long_polling_url, headers=headers, params=params, timeout=60)
            response.raise_for_status()
            checks = response.json()
            if checks['status'] == 'timeout':
                params = {'timestamp': checks['timestamp_to_request']}
                continue
            elif checks['status'] == 'found':
                last_attempt_timestamp = checks['last_attempt_timestamp']
                work_title = checks["new_attempts"][0]["lesson_title"]
                work_link = checks["new_attempts"][0]["lesson_url"]
                work_status = checks["new_attempts"][0]["is_negative"]
                if work_status:
                    tg_bot.send_message(chat_id=chat_id,
                                        text=f"Урок '{work_title}' не прошел ревью. [Что от тебя хотят в этот раз]({work_link})",
                                        parse_mode='Markdown', disable_web_page_preview=True)
                elif not work_status:
                    tg_bot.send_message(chat_id=chat_id, text=f"По уроку '{work_title}' зачет получен.\n{work_link}",
                                        parse_mode="html", disable_web_page_preview=True)
                params = {'timestamp': last_attempt_timestamp}
        except requests.exceptions.Timeout as error:
            continue
        except (requests.exceptions.HTTPError, requests.RequestException) as error:
            logger.critical(f'Error:  {error}')
            sleep(60)
        except requests.ConnectionError as error:
            logger.critical(f'Error:  {error}')
            sleep(60)


if __name__ == "__main__":
    main()
