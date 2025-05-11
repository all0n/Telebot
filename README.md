# Twitter-Telegram Bot

Этот бот следит за вашими упоминаниями в Twitter и пересылает их в Telegram.

## 📦 Установка

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/yourusername/twitter-telegram-bot.git
   cd twitter-telegram-bot
   ```

2. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

3. Создайте файл `.env` и укажите в нём токены:

   ```
   TELEGRAM_TOKEN=...
   TELEGRAM_CHAT_ID=...
   TWITTER_BEARER_TOKEN=...
   TWITTER_USER_ID=...
   ```

## 🚀 Запуск

```bash
python bot.py
```

## 🛡 Безопасность

Никогда не публикуйте файл `.env`! Он добавлен в `.gitignore`.

## 📄 Лицензия

MIT