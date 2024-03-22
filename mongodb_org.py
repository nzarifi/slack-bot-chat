import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter
from ChatBot_class import ChatBot
from pymongo import MongoClient

# Load environment variables
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
print('test')
######
app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)

# Setup MongoDB Client
mongo_client = MongoClient(os.environ['MONGO_URI'])
db = mongo_client.slack_store  # Use your actual database name
chats_collection = db.chats_bot_channel  # Use your actual collection name

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']
chatbot = ChatBot(openai_api_key=os.environ['openai_api_key'])

@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    
    if BOT_ID != user_id:
        response = chatbot.chat(text)
        client.chat_postMessage(channel=channel_id, text=str(response))
        
        # Save the chat to MongoDB
        chat_data = {
            'user_id': user_id,
            'channel_id': channel_id,
            'text': text,
            'response': str(response)
        }
        chats_collection.insert_one(chat_data)

if __name__ == "__main__":
    app.run(debug=True)


# from pymongo import MongoClient

# # Replace with your actual database name
# db_name = "slack_store"

# # Connect to MongoDB
# client = MongoClient('mongodb://localhost:27017/')
# db = client[db_name]

# # Query all documents in the 'chats' collection
# chats = db.chats_bot_channel.find()   


# # Print each document
# for chat in chats:
#     print(chat)    
