# запуск сессии

from PERSONAL_DATA import VK_TOKEN

import vk_api

vk_session = vk_api.VkApi(token=VK_TOKEN)
vk = vk_session.get_api()
print(vk_session, vk, sep="\n")