# inline-кнопки в боте и секретные сообщения

from PERSONAL_DATA import VK_TOKEN, GROUP_ID

import vk_api, random, json, sys
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def send_message(peer_id, text):
    vk.messages.send(
        peer_id=peer_id,
        message=text,
        keyboard=keyboard.get_keyboard(),
        random_id=random.randint(1, 2_000_000_000)
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


keyboard = VkKeyboard(inline=True)
keyboard.add_button("Привет", color=VkKeyboardColor.PRIMARY)
keyboard.add_button("Пока", color=VkKeyboardColor.SECONDARY, payload={"command": "exit"})
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

        payload = message.get("payload")

        if payload:
            data = json.loads(payload)
            print(data)
            sys.exit()