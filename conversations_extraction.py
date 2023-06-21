import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['rasa_bot']
collection = db['conversations']

# Query the collection to retrieve conversations
conversations = collection.find()

# Prepare a list to store conversation data
conversation_data = []

# Iterate over conversations and extract relevant information
for conversation in conversations:
    messages = conversation['events']
    user_messages = [msg for msg in messages if msg['event'] == 'user']
    conversation_text = [msg['text'] for msg in user_messages]
    conversation_data.append(conversation_text)

# Export conversation data as JSON
json_data = json.dumps(conversation_data, indent=4)

# Save JSON data to a file
with open('conversations.json', 'w') as file:
    file.write(json_data)
