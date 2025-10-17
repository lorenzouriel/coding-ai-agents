# ChatMessageHistory: Manual Memory Management. For direct and simple control over a conversation's 
# history outside of a formal chain, the ChatMessageHistory class is ideal. 
# It allows for the manual tracking of dialogue exchanges.
from langchain.memory import ChatMessageHistory

# Initialize the history object
history = ChatMessageHistory()

# Add user and AI messages
history.add_user_message("I'm heading to New York next week.")
history.add_ai_message("Great! It's a fantastic city.")

# Access the list of messages
print(history.messages)


# ConversationBufferMemory: Automated Memory for Chains. For integrating memory directly into chains, ConversationBufferMemory 
# is a common choice. It holds a buffer of the conversation and makes it available to your prompt. 
# Its behavior can be customized with two key parameters:
# - memory_key: A string that specifies the variable name in your prompt that will hold the chat history. It defaults to "history".
# - return_messages: A boolean that dictates the format of the history.
#   - If False (the default), it returns a single formatted string, which is ideal for standard LLMs.
#   - If True, it returns a list of message objects, which is the recommended format for Chat Models.

from langchain.memory import ConversationBufferMemory

# Initialize memory
memory = ConversationBufferMemory()

# Save a conversation turn
memory.save_context({"input": "What's the weather like?"}, {"output": "It's sunny today."})

# Load the memory as a string
print(memory.load_memory_variables({}))
