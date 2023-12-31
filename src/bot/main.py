import os
import discord
from bot import LethalCompagnion
import asyncio


class Main():
    @staticmethod
    def run():
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        try:
            token = open(os.path.join(__location__, "token.txt"), "r").read().strip("\n")
        except FileNotFoundError:
            quit("Please create a token.txt file and place your token in it!")
        if token is None:
            quit("Please create a token.txt file and place your token in it!")
        else:
            intent = discord.Intents.all()
            intent.members = True
            intent.message_content = True
            bot = LethalCompagnion(intent)
            bot.run(open("./src/bot/token.txt", "r").readline())

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(Main.run())