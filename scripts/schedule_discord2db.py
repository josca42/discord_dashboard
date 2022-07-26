from time import sleep
import schedule
from src.data.discord2db import discord2db


schedule.every().day.at("02:00").do(discord2db)
while True:
    schedule.run_pending()
    sleep(60 * 30)  # check once every 30 minute
