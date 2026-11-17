# сообщение от бота в функии

from PERSONAL_DATA import VK_TOKEN, GROUP_ID

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from vk_api.utils import get_random_id

def send_message(peer_id, text):
    vk.messages.send(
        peer_id=peer_id,
        message=text,
        random_id=get_random_id()
    )
vk_session = vk_api.VkApi(token=VK_TOKEN)
vk = vk_session.get_api()

longpoll = VkBotLongPoll(vk_session, GROUP_ID)

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        message = event.obj.message

        text = message["text"]
        peer_id = message["peer_id"]

        send_message(peer_id, "Привет! Я бот внутри функции.")
