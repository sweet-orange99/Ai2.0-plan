import os

from dotenv import load_dotenv

load_dotenv(override=True)

MINIMAX_API_KEY = os.getenv("MINIMAX_API_KEY")
MINIMAX_BASE_URL = os.getenv(
    "MINIMAX_BASE_URL",
    "https://api.minimaxi.com/v1",
)
MINIMAX_MODEL = os.getenv(
    "MINIMAX_MODEL",
    "MiniMax-M3",
)