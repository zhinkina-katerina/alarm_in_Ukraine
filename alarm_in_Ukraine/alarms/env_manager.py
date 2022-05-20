import os
from dotenv import load_dotenv


load_dotenv()


class EnvManager:
    ALERTS_CONNECTOR_TOKEN = os.getenv("ALERTS_CONNECTOR_TOKEN")



env_manager = EnvManager()
