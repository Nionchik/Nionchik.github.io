import vk_api
import random
import time
token = "0421951dc8becb915b4fc6b496da3760fd9907464b925744ce0ac5e54d73ec5d2751acf7339146d7e6e36"

vk = vk_api.VkApi(token=token)

vk._auth_token()

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "кто я?":
                vk.method("messages.send", {"peer_id": id, "message": "ты хороший человек", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "как у тебя дела?":
                vk.method("messages.send", {"peer_id": id, "message": "у меня всё хорошо,я родился всего 2 дня назад, но с каждым днём я станослюсь умнее)", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "как твои дела?":
                vk.method("messages.send", {"peer_id": id, "message": "у меня всё хорошо,я родился всего 2 дня назад, но с каждым днём я станослюсь умнее)", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "Когда твоё обновление?":
                vk.method("messages.send", {"peer_id": id, "message": "скоро", "random_id": random.randint(1, 2147483647)})

            else:
                vk.method("messages.send", {"peer_id": id, "message": "я пока не знаю что значит " + str(body.lower()) + ".Попробуй узнать как у меня дела:)", "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)
