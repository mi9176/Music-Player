from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN", "7926548341:AAEAvZ-3VvyE8wzqC1RpiCyna0WwSZFfkGM")
BOT_USERNAME = getenv("BOT_USERNAME", "audioplay_bot")
admins = {}
API_ID = int(getenv("API_ID","22278010"))
API_HASH = getenv("API_HASH", "cfe38cba8df4cc60e1b75d4df4f2693c")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
