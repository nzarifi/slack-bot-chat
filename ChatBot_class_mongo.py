
#from langchain_openai.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from pymongo import DESCENDING
from pymongo import MongoClient


class ChatBot:
    def __init__(
        self,
        system_message="You are a helpful assitant.",
        openai_api_key=None,
        mongo_client=None,
        BOT_ID=None,
        model_name="gpt-3.5-turbo",
        temperature=0.3,
  
        
    ):

        self.system_message = system_message
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            openai_api_key=openai_api_key,
        )
        
        self.BOT_ID = BOT_ID  # Set the BOT_ID attribute here
        self.mongo_client = mongo_client  # Store MongoDB client
        self.conversation_history = [SystemMessage(content=system_message)]
        print("ChatBot initialized with system message.")
        if not self.mongo_client:
            print("MongoDB client is not configured.")
        else:
            print("MongoDB client is configured successfully.")

    def load_chat_history(self, channel_id):
        if not self.mongo_client:
            print("MongoDB client is not configured.")
            return

        print(f"Loading chat history for channel_id: {channel_id}")
        db = self.mongo_client.slack_store
        chats_collection = db.chats_bot_channel
        last_chats = chats_collection.find({'channel_id': channel_id}).sort('_id', DESCENDING).limit(20)
        history_count = 0
        for chat in reversed(list(last_chats)):  # Reverse to maintain chronological order
            self.conversation_history.append(AIMessage(chat['response']))
            self.conversation_history.append(HumanMessage(chat['text']))      
            history_count += 1
            

        print(f"Loaded {history_count} messages into conversation history.")      

    def chat(self, message, channel_id):
        # Load the last 20 chats from the specified channel before appending the new human message
        self.conversation_history.clear()  # Clear existing conversation history
        self.conversation_history.append(SystemMessage(content=self.system_message))  # Re-add system message
        self.load_chat_history(channel_id)  # Load chat history from MongoDB
        self.conversation_history.append(HumanMessage(message))


        # Get AI response
        ai_response = self.llm.invoke(self.conversation_history)
        self.conversation_history.append(AIMessage(ai_response.content))
        print(self.conversation_history)

        return ai_response.content
    

