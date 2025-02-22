import os
from dotenv import find_dotenv, load_dotenv
from App import App

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

DB_URL = os.getenv("DB_URL")

if __name__ == '__main__':
    App(DB_URL)
