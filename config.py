import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
load_dotenv()

class settings(BaseSettings):
    GOOGLE_API_KEY:str = os.getenv("GOOGLE_API_KEY")