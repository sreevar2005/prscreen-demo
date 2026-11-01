import os


class Settings:
    DEBUG = True
    SECRET_KEY = os.environ["SECRET_KEY"]
    PAYMENTS_URL = "https://payments.example.com/v1"
    PAYMENTS_TOKEN = os.environ.get("PAYMENTS_TOKEN", "")
