# dvmn-notifications-bot
Костыль для сайта [ДЕВМАНА](https://dvmn.org/modules/)
Данный бот сообщает в чат о проверке учебной работы.

## Требования к окружению

Получите токены [ДЕВМАНА](https://dvmn.org/api/docs/) и [Телеграм](https://t.me/BotFather), затем определите [chat_id](https://t.me/messageinformationsbot)  поместите в переменные окружения (файл .env). Пример файла:

```
TELEGRAM_TOKEN="78869833434:Alkhlj;hoihyiu986ohlknl"
DVMN_TOKEN='Token ghkhli679tutd45yrtiuhnkhiu8'
TG_CHAT_ID=166678946879
``` 

Python 3.xx и выше (должен быть уже установлен)

``` 
requests==2.13.0
python-dotenv==0.15.0
python-telegram-bot==13.14
``` 

Можно установить командой  
``` 
PIP install -r requirement.txt
```

# Запуск
Обычный запуск без виртуального окружения:
``` 
python3 main.py.
``` 

Запуск через docker:

[Установите docker](https://docs.docker.com/engine/install/debian/).
Создаем контейнер с именем "app_name", а затем запускаем докер с именем "app_name" с переменными окружения из файла ".env".
```
docker build -t app_name 
docker run -d --env-file ./.env -it --rm --name my-running-app app_name 
```

## Отказ от ответственности

Автор программы не несет никакой ответственности за то, как вы используете этот код или как вы используете сгенерированные с его помощью данные. Эта программа была написана для обучения автора и других целей не несет. Не используйте данные, сгенерированные с помощью этого кода в незаконных целях.
