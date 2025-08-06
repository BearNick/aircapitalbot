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
