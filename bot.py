import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.client.default import DefaultBotProperties

from calculator import generate_financial_model, extract_metrics_from_results
from gpt_analyzer import analyze_model_with_gpt  # 🧠 GPT-анализ

API_TOKEN = ""

# --- Состояния опроса ---
class Form(StatesGroup):
    project_type = State()
    region = State()
    investment = State()
    horizon = State()
    revenue_year1 = State()
    growth = State()
    fixed_costs = State()
    variable_costs = State()
    employees = State()
    avg_salary = State()

# --- Инициализация бота ---
storage = MemoryStorage()
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=storage)

# --- /start ---
@dp.message(F.text == "/start")
async def start(message: Message, state: FSMContext):
    builder = ReplyKeyboardBuilder()
    builder.add(
        types.KeyboardButton(text="IT/SaaS"),
        types.KeyboardButton(text="Marketplace"),
        types.KeyboardButton(text="Мобильное приложение"),
        types.KeyboardButton(text="Другое")
    )
    builder.adjust(2)
    await message.answer("👋 Добро пожаловать! Выберите тип проекта:", reply_markup=builder.as_markup(resize_keyboard=True))
    await state.set_state(Form.project_type)

@dp.message(Form.project_type)
async def get_project_type(message: Message, state: FSMContext):
    await state.update_data(project_type=message.text)
    await message.answer("🌍 В каком регионе планируется запуск?")
    await state.set_state(Form.region)

@dp.message(Form.region)
async def get_region(message: Message, state: FSMContext):
    await state.update_data(region=message.text)
    await message.answer("💰 Сколько планируете вложить (₽)?")
    await state.set_state(Form.investment)

@dp.message(Form.investment)
async def get_investment(message: Message, state: FSMContext):
    await state.update_data(investment=message.text)
    await message.answer("📆 На сколько лет строим модель?")
    await state.set_state(Form.horizon)

@dp.message(Form.horizon)
async def get_horizon(message: Message, state: FSMContext):
    await state.update_data(horizon=message.text)
    await message.answer("📈 Ожидаемая выручка в 1-й год (₽)?")
    await state.set_state(Form.revenue_year1)

@dp.message(Form.revenue_year1)
async def get_revenue(message: Message, state: FSMContext):
    await state.update_data(revenue_year1=message.text)
    await message.answer("📊 Годовой рост выручки (%)?")
    await state.set_state(Form.growth)

@dp.message(Form.growth)
async def get_growth(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("💸 Постоянные расходы в месяц (₽)?")
    await state.set_state(Form.fixed_costs)

@dp.message(Form.fixed_costs)
async def get_fixed_costs(message: Message, state: FSMContext):
    await state.update_data(fixed_costs=message.text)
    await message.answer("📦 Переменные расходы (% от выручки)?")
    await state.set_state(Form.variable_costs)

@dp.message(Form.variable_costs)
async def get_variable_costs(message: Message, state: FSMContext):
    await state.update_data(variable_costs=message.text)
    await message.answer("👥 Сколько сотрудников в команде?")
    await state.set_state(Form.employees)

@dp.message(Form.employees)
async def get_employees(message: Message, state: FSMContext):
    await state.update_data(employees=message.text)
    await message.answer("🧾 Средняя зарплата сотрудника в месяц (₽)?")
    await state.set_state(Form.avg_salary)

@dp.message(Form.avg_salary)
async def get_avg_salary(message: Message, state: FSMContext):
    await state.update_data(avg_salary=message.text)
    await message.answer("🔄 Рассчитываю модель...")

    data = await state.get_data()

    # 🧮 Генерация модели
    file_path, metrics = generate_financial_model(data, return_metrics=True)

    # 🧠 GPT-анализ
    analysis = analysis = analyze_model_with_gpt(data, metrics)
    await message.answer(f"<b>📋 GPT-анализ твоей модели:</b>\n\n{analysis}")

    # 📎 Excel-файл
    await message.answer_document(types.FSInputFile(file_path), caption="📊 Финансовая модель готова:")
    await state.clear()

# --- Запуск ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
