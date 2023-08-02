from aiogram import Bot, Dispatcher, executor, types

from dotenv import load_dotenv, find_dotenv
import os

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


from calculation_def import calculation_p22, get_Gmax, update_value, \
    get_table, stability_check, stability_check_elements, calculation_of_welded, base_plate_calculation
from verification import is_num, isfloat, metals, is_metal
from keyboards import get_kb_start, get_kb_cancel, get_kb_metal
from text_message import CALCULATION_TEXT, HELP_COMMAND, START_COMMAND

from picture.charting import all_img
from Doc_final.final import doc_final


storage = MemoryStorage()
load_dotenv(find_dotenv())
bot = Bot(os.getenv('TOKEN_API'))
dp = Dispatcher(bot=bot, storage=storage)


class ClientStatesGroup(StatesGroup):
    Ra_list = State()
    value = State()
    variant = State()
    metal = State()
    val = State()


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message) -> None:
    await message.answer(text=START_COMMAND,
                         reply_markup=get_kb_start())
    await message.delete()


@dp.message_handler(Text(equals=['Help', '/help'], ignore_case=True))
async def help_cmd(message: types.Message) -> None:

    await message.answer(text=HELP_COMMAND,
                         parse_mode='HTML')
    await message.delete()


@dp.message_handler(Text(equals='Отменить', ignore_case=True), state='*')
async def cancel_cmd(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return



    await message.answer(text='Отмена',
                         reply_markup=get_kb_start())
    await message.delete()
    await state.finish()


@dp.message_handler(Text(equals='начать расчет', ignore_case=True))
async def calculation(message: types.Message) -> None:
    photo_url = 'https://downloader.disk.yandex.ru/preview/38ce24ffdeafafd297d4c9978925f78faae709c062f977dba4337e799116d0c1/64426aab/o_xP_5WFErQCGZh8kaheqfYkM7csdSj4LNkV2Z7LFCaglX-tFV-d2W48vzrhsxDSnYlqRv188l705NnuMFD9PA%3D%3D?uid=0&filename=beam_section.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1918x992'

    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo_url,
                         caption=CALCULATION_TEXT,
                         reply_markup=get_kb_cancel(),
                         parse_mode='HTML')

    await ClientStatesGroup.variant.set()

    await message.delete()


@dp.message_handler(lambda message: not isfloat(message.text),
                    state=ClientStatesGroup.variant)
async def process_calculation_invalid(message: types.Message):
    return await message.answer('Не правильно, попробуй еще раз')


@dp.message_handler(lambda message: isfloat(message.text),
                    state=ClientStatesGroup.variant)
async def process_calculation(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        value, Ra_dict = calculation_p22(message.text)
        data['value'] = value
        data['Ra_dict'] = Ra_dict

    await ClientStatesGroup.next()
    await message.answer(text='Чтобы продолжить нужно выбрать сталь',
                         reply_markup=get_kb_metal())


@dp.message_handler(lambda message: not is_metal(message.text),
                    state=ClientStatesGroup.metal)
async def process_metal_invalid(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы продолжить нужно выбрать сталь',
                         reply_markup=get_kb_metal())


@dp.message_handler(lambda message: is_metal(message.text),
                    state=ClientStatesGroup.metal)
async def process_metal(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['metal'] = metals.get(message.text)
        val, h_dict = get_Gmax(data.get('value'), data.get('metal'))
        data['val'] = val
        data['value'].update(data['metal'])
        data['value'].update(h_dict)

    await message.answer(text=f'Ты выбрал <b>{message.text}</b>\n'
                              f'Характеристики:\n'
                              f'R = {data["metal"]["R"]}, '
                              f'Rср = {data["metal"]["Rsr"]}, '
                              f'Rсм.т = {data["metal"]["Rsm"]}',
                         parse_mode='html')

    await message.delete()

    for i in range(len(val)):
        await message.answer(
            f'Вариант {i + 1}:\n'
            f'Sв = {val[i + 1]["Sv"]}\n'
            f'Sг = {val[i + 1]["Sg"]}\n'
            f'Bг = {val[i + 1]["Bg"]}\n'
            f'Hв = {val[i + 1]["Hv"]}\n'
            f'H = {val[i + 1]["H"]}\n'
            f'Jф = {val[i + 1]["Jf"]}\n'
            f'Gmax = {val[i + 1]["Gmax"]}'
        )
    await message.answer('Введи номер нужного тебе варианта',
                         reply_markup=get_kb_cancel())
    await ClientStatesGroup.next()


@dp.message_handler(lambda message: not is_num(message.text),
                    state=ClientStatesGroup.val)
async def choice_invalid(message: types.Message):
    return await message.answer('Нужно ввести номер варианта')


@dp.message_handler(lambda message: is_num(message.text),
                    state=ClientStatesGroup.val)
async def choice(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if int(message.text) in data['val']:
            data['val'] = data['val'][int(message.text)]
            data['value'] = update_value(data['value'], data['val'])
            data['value'] = update_value(data['value'], data['Ra_dict'])
            data['value'] = get_table(data['value'])
            data['value'] = stability_check(data['value'])
            data['value'] = stability_check_elements(data['value'])
            data['value'] = calculation_of_welded(data['value'])
            data['value'] = base_plate_calculation(data['value'])
        else:
            await message.answer('Нужно ввести номер варианта')

        # финал
        await message.answer("<b>Нужно чуть-чуть подождать...</b>",
                             parse_mode='html')
        print(data['value'])
        await all_img(data['value'])
        file_path = await doc_final(data['value'])
        with open((file_path), 'rb') as file:
            await message.answer_document(
                document=file,
                reply_markup=get_kb_start())

        await state.finish()




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
