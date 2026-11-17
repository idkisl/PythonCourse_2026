# получение информации от пользователя бота

from PERSONAL_DATA import VK_TOKEN, GROUP_ID

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType


vk_session = vk_api.VkApi(token=VK_TOKEN)

longpoll = VkBotLongPoll(vk_session, GROUP_ID)

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        message = event.obj.message

        text = message["text"]
        user_id = message["from_id"]

        print("ID отправителя:", user_id)
        print("Текст сообщения:", text)