import os
from dotenv import load_dotenv

load_dotenv()

FIREWORKS_API_KEY = os.getenv("FIREWORKS_API_KEY")
MODEL_NAME = "accounts/fireworks/models/llama-v3p1-8b-instruct"