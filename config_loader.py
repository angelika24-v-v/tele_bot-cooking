from dataclasses import dataclass
from os import getenv

from environs import Env


@dataclass
class Bot:
    token: str


@dataclass
class Config:
    bot: Bot


env = Env()
env.read_env()


def load_config():

    return Config(bot=Bot(token=getenv("BOT_TOKEN")))
