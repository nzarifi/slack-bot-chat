
#from langchain_openai.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)



class ChatBot:
    def __init__(
        self,
        system_message="You are a helpful assitant.",
        openai_api_key=None,
        model_name="gpt-3.5-turbo",
        temperature=0.3,
    ):

        self.system_message = system_message
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            openai_api_key=openai_api_key,
        )
        self.conversation_history = [SystemMessage(content=system_message)]

    def chat(self, message):
        self.conversation_history.append(HumanMessage(message))

        # Get AI response
        ai_response = self.llm.invoke(self.conversation_history)
        self.conversation_history.append(AIMessage(ai_response.content))

        return ai_response.content
    

#chatbot = ChatBot(openai_api_key=openai_api_key)    

#ai_response = chatbot.chat(message = "My name is Niloofar. Nice to meet you")
#print(ai_response)