from vk_api.longpol import VkLongPoll, VkEventType
import vk_api
from datetime import datetime

login, pasword = '',''
vk_session = vk_api.VkApi(login, pasword)
vk_session.auth()

#token = '0421951dc8becb915b4fc6b496da3760fd9907464b925744ce0ac5e54d73ec5d2751acf7339146d7e6e36'
#vk_session vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MASSEGE_NEW:
            print('New massage in: ' + str(datetime.strftime(datetime.now(), '%H:%M:S%')))
            print('Text message: ' + str(event.txt))

