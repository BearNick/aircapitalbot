# 🤖 Telegram-бот для финансового моделирования | Financial Modeling Telegram Bot

## 🇷🇺 Описание

Этот бот позволяет пользователям создавать базовую финансовую модель стартапа, введя ключевые параметры.  
После ввода бот рассчитывает модель, формирует файл Excel и — при подключении GPT — проводит интеллектуальный анализ с рекомендациями.

### 🚀 Возможности
- Интерактивный ввод параметров в Telegram
- Расчёт метрик: NPV, IRR, Payback, EBITDA и др.
- Автоматическая генерация Excel-файла (с листами: Summary, P&L, Assumptions, Multiples, Справка)
- Подключение GPT-анализа (опционально)

### 📦 Установка

```bash
git clone https://github.com/your-username/aircapitalbot.git
cd aircapitalbot
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Создайте файл .env (или вставьте ключи в bot.py/gpt_analyzer.py) с переменными:
BOT_TOKEN=ваш_токен_бота
OPENAI_API_KEY=ваш_api_ключ
▶️ Запуск
source venv/bin/activate
python bot.py
🛠️ Использование на VPS

Рекомендуется запускать бота в фоновом режиме через tmux:
sudo apt install tmux -y
tmux new -s airbot
source venv/bin/activate
python bot.py
# затем Ctrl+B, D — и бот будет работать в фоне
🇬🇧 Description

This Telegram bot helps users create a basic financial model for a startup by entering key assumptions.
After data input, it calculates core metrics and generates an Excel model. If GPT is connected, the bot also provides smart financial analysis and suggestions.

🚀 Features
	•	Interactive Telegram questionnaire
	•	Calculates NPV, IRR, Payback, EBITDA and more
	•	Generates Excel file with Summary, P&L, Assumptions, Multiples, Glossary
	•	Optional GPT-powered analysis

📦 Installation
git clone https://github.com/your-username/aircapitalbot.git
cd aircapitalbot
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Create a .env file (or set in code):
BOT_TOKEN=your_bot_token
OPENAI_API_KEY=your_openai_key
▶️ Launch
source venv/bin/activate
python bot.py
🛠️ Run on VPS (background mode)

We recommend using tmux to keep bot running in background:
sudo apt install tmux -y
tmux new -s airbot
source venv/bin/activate
python bot.py
# then press Ctrl+B, D to detach
📂 Структура проекта / Project Structure
aircapitalbot/
├── bot.py               # Основная логика Telegram-бота
├── calculator.py        # Финансовые расчёты и генерация Excel
├── gpt_analyzer.py      # GPT-анализ (если подключён)
├── output/              # Сюда сохраняются Excel-файлы
├── requirements.txt     # Зависимости
└── README.md            # Это описание
📧 Связь / Contact

Telegram: @conservathor

Поддержка моделей: gpt-3.5-turbo, gpt-4 (если есть доступ).
Requires OpenAI API key.
