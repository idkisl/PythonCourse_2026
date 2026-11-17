# сообщение от бота

from PERSONAL_DATA import VK_TOKEN, GROUP_ID

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
import random

vk_session = vk_api.VkApi(token=VK_TOKEN)
vk = vk_session.get_api()

longpoll = VkBotLongPoll(vk_session, GROUP_ID)

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        message = event.obj.message

        text = message["text"]
        peer_id = message["peer_id"]

        vk.messages.send(
            peer_id=peer_id,
            message="Привет! Я бот.",
            random_id=random.randint(1, 2_000_000_000)
            # случайное число для проверки на несовпадение посылок
            # from vk_api.utils import get_random_id
        )