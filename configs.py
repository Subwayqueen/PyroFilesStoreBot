# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Storage Flix Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @Iggie

👥 **Support Bot:** [Flix Help Bot](https://t.me/FlixHelpBot)

📢 **Updates Channel:** [Flix Bots](https://t.me/FlixBots)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @Iggie

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://www.paypal.me/PremiumBarn) (PayPal)
"""
	HOME_TEXT = """**𝗛𝗲𝗹𝗹𝗼 [{}](tg://user?id={}), 𝗜'𝗺 𝗮 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗤𝗨𝗜𝗖𝗞 𝗦𝗧𝗢𝗥𝗔𝗚𝗘 𝗕𝗢𝗧 😀\n\nHow To Use This Bot & Benefits??\n\n📍 Send Me Any File & It'll Be Uploaded Into My Database & You Get The File Link.\n\n⚠️ Benifit : If You Have Telegram Movie Channel, Then Its Useful For Your Daily Usage, You can Send Me Your File & I'll Send You The Link Of Your File So Your Subscribers Can Get The File From Me & Your Channel Will Be Safe From COPYRIGHT INFRINGEMENT Issue.\n\n❌ 𝗣𝗢𝗥𝗡𝗢𝗚𝗥𝗔𝗣𝗛𝗜𝗖 𝗖𝗢𝗡𝗧𝗘𝗡𝗧𝗦 Are Strictly Prohibited & Will Get You Banned Permanently.**"""



