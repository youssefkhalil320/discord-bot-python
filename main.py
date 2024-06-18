from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from modules.responses import get_response


load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)
