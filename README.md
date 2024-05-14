# slack-bot-chat
# Slack Chatbot with MongoDB and OpenAI Integration

This Slack chatbot enhances interactions within Slack channels by leveraging OpenAI's powerful language models for intelligent responses and MongoDB for storing conversation histories. It captures and stores the last 20 conversations and uses OpenAI's LLM to generate context-aware responses.

## Features

- **OpenAI Integration:** Utilizes OpenAI's language models to provide intelligent, context-aware responses.
- **Conversation Tracking:** Automatically stores all chat messages in a MongoDB database.
- **Memory Management:** Maintains a history of the last 20 conversations for quick retrieval and analysis.
- **Slack Integration:** Fully integrated with Slack, enabling dynamic interactions within any Slack channel.

## Setup

Follow these instructions to set up the chatbot in your Slack environment and connect it to MongoDB and OpenAI.

### Prerequisites

- A Slack account with administrative privileges to install apps.
- A MongoDB database setup either locally or hosted.
- Node.js installed on your server.
- An API key from OpenAI.

## Configuration

Before running the chatbot, you need to set up the necessary environment variables. These variables will store sensitive information such as your API keys and database connection strings securely. Follow these steps to configure your environment:

1. **Environment Variables Setup:**
   Create a `.env` file in the root directory of your project. This file will store your private keys and settings outside of your main codebase. Add the following variables to this file:

    ```plaintext
    SLACK_BOT_TOKEN=your-slack-bot-token-here
    MONGODB_URI=mongodb://your-mongodb-uri-here
    OPENAI_API_KEY=your-openai-api-key-here
    ```


2. **Securing Your API Keys:**
   Ensure that the `.env` file is listed in your `.gitignore` file to prevent it from being committed to your version control system. This helps in protecting your API keys and sensitive information from being exposed publicly.

## Usage

Once you have configured the environment variables and installed the necessary dependencies, you can start using the chatbot. Here's how to run and interact with the chatbot:


 **Interacting with the Chatbot:**
   - Go to your Slack workspace where the chatbot is installed.
   - You can interact with the chatbot by sending messages directly in the channels or via direct messages.
   - The chatbot will use OpenAI's language model to generate responses based on the conversation context and store these interactions in MongoDB.

 **Accessing Stored Conversations:**
   - To access the stored conversations, connect to your MongoDB database using a MongoDB client or a GUI tool like MongoDB Compass.
   - Navigate to the relevant collection where conversations are stored.
   - You can query the last 20 conversations or perform other data retrieval operations as needed for analysis or review.

These steps will help you effectively set up and utilize your Slack chatbot integrated with MongoDB and OpenAI for enhanced interactions in your Slack workspace.

slack set up reference: https://www.youtube.com/watch?v=6gHvqXrfjuo&t=19s


