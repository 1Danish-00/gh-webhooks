import io
import logging
import random
import sys
import traceback
from decouple import config
from telethon import Button, TelegramClient, events
from flask import Flask, request, Response

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)

tgbot = TelegramClient("kensur", APP_ID, API_HASH).start(bot_token=BOT_TOKEN)

app = Flask("Kek")

print("Successfully deployed!")

@app.route('/webhook', methods=['POST'])
def respond():
    result = request.json
    #print(request.json)
    try:
        #check_s = result["check_suite"]
        #umm = check_s["app"]["head_commit"]
        umm = result["head_commit"]
        commit_msg = umm["message"]
        commit_id = umm["id"]
        commit_url = umm["url"]
        commit_timestamp = umm["timestamp"]
        committer_name = umm["author"]["username"]
        committer_mail = umm["author"]["email"]
        async def start():
            await tgbot.send_message(-1001237141420,
                f"Commit: `{commit_id}`\nMessage: *{commit_msg}*\nTimeStamp: `{commit_timestamp}`\nCommiter: {committer_name} <{committer_email}>")
    except:
        traceback.print_exc()
    return Response(status=200)
port = int(config('PORT', default=6969))
app.run(host="0.0.0.0", port=port)
