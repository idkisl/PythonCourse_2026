# кнопки в боте

from PERSONAL_DATA import VK_TOKEN, GROUP_ID

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

def send_message(peer_id, text):
    vk.messages.send(
        peer_id=peer_id,
        message=text,
        keyboard=keyboard.get_keyboard(), # для выключения клавиатуры -- VkKeyboard.get_empty_keyboard()
        random_id=get_random_id()
    )

def get_answer(text):
    text = text.lower().strip()

    if text == "привет":
        return "Привет! Я учебный бот."
    elif text == "пока":
        return "Пока! До скорых встреч!"
    elif text == "помощь":
        return "Команды: привет, помощь"
    else:
        return "Неизвестная команда. Напиши: помощь"


vk_session = vk_api.VkApi(token=VK_TOKEN)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, GROUP_ID)


keyboard = VkKeyboard(one_time=False)
keyboard.add_button("Привет", color=VkKeyboardColor.PRIMARY)
keyboard.add_button("Пока", color=VkKeyboardColor.SECONDARY)
keyboard.add_line()
keyboard.add_button("Помощь", color=VkKeyboardColor.POSITIVE)


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        message = event.obj.message

        text = message["text"]
        peer_id = message["peer_id"]

        answer_text = get_answer(text)
        send_message(peer_id, answer_text)

        print(f"Получена информация {text}; \t дан ответ: {answer_text}")