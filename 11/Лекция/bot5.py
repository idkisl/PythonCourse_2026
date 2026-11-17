# обработка команд бота

from PERSONAL_DATA import VK_TOKEN, GROUP_ID

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
import random
import datetime

def send_message(peer_id, text):
    vk.messages.send(
        peer_id=peer_id,
        message=text,
        random_id=random.randint(1, 2_000_000_000)
    )

def get_answer(text):
    text = text.lower().strip()

    if text == "привет":
        return "Привет! Я учебный бот."

    elif text == "помощь":
        return "Команды: привет, помощь, время, кубик"

    elif text == "время":
        now = datetime.datetime.now()
        return now.strftime("%H:%M")

    elif text == "кубик":
        number = random.randint(1, 6)
        return f"Выпало число {number}"

    else:
        return "Неизвестная команда. Напиши: помощь"


vk_session = vk_api.VkApi(token=VK_TOKEN)
vk = vk_session.get_api()

longpoll = VkBotLongPoll(vk_session, GROUP_ID)

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        message = event.obj.message

        text = message["text"]
        peer_id = message["peer_id"]

        answer_text = get_answer(text)
        send_message(peer_id, answer_text)

        print(f"Получена информация {text}; \t дан ответ: {answer_text}")