# rasa_chatbot
RASA :
For building conversational AI and virtual assistants there are several options such as Dialogflow, Microsoft Bot Framework, Amazon Lex, and Rasa.
Here rasa which is an open-source framework is selected for creating the bot. Where , It gives programmers access to a collection of tools and frameworks that let them build complex, context-aware chatbots that can comprehend user input and reply to it in a conversational way.
Rasa consists of two main components: Rasa NLU and Rasa Core.
Rasa NLU (Natural Language Understanding): This part is concerned with understanding and extracting user messages. It classifies intents—the user's intention—and extracts entities—relevant data—from the user's input using machine learning models. Rasa NLU is capable of handling natural language variants, synonyms, and contextual understanding and may be trained on customized data to understand domain-specific language.
Rasa Core: This component deals with the dialogue management and conversation flow of the chatbot. By creating stories, which are instances of possible conversations, and training a machine learning model to predict the next action based on the conversation history, it enables developers to construct interactive and dynamic conversations. Rasa Core handles the chatbot's actions, responses, and dialogue flow.

STEPS FOR CREATING A CHATBOT:
1. Createavirtualenvironmentandactivatethevirtualenvironment
2. Intheactivatedenvironmentinstallrasa.
python -m pip install rasa ------> installing rasa pip3install--upgraderasa ------->upgradingrasaifalreadyrasa installed before.
3. pip install spacy (rasa uses spacy library):
 4. python -m spacy download en_core_web_md:
The command python -m spacy download en_core_web_md is used to download the "en_core_web_md" model for the spaCy natural language processing library.
The "en_core_web_md" model is a medium-sized model for English language processing, which includes word vectors, named entity recognition, part-of-speech tagging, dependency parsing, and other linguistic features. This model is trained on a large corpus of web text and is designed to handle a wide range of natural language processing tasks.
By downloading and installing this model, we can use it in your Python code to process text in English, extract relevant information, and perform various NLP tasks such as sentiment analysis, text classification, and more.
5. Afterinstallingrasawecanstarttheassistantbyrunningtherasainitcommand. python -m rasa init
Rasa will create a new directory with the specified name and pre-populate it with some initial files and directories, Here a new assistant will be created. The assistant that you'll create is called "moodbot". It just asks whether we are happy sad etc.
The files inside the rasa are : ┣━━ actions
📂
┃ ┣━━
🐍
__init__.py actions.py ┃ ┗━━
🐍
┣━━ data
📂
┃ ┣━━
📄
nlu.yml
┃ ┣━━
rules.yml 📄
stories.yml ┃ ┗━━
📄
┣━━ models 📂
┣━━ tests
📂
┃ ┗━━ test_stories.yml 📄
┣━━ config.yml 📄
┣━━ credentials.yml 📄
┣━━ domain.yml 📄
┗━━ endpoints.yml 📄
 
A. Domain.yml: In this file, everything comes together
B. Comfig.yml;Configurationofmachinelearningmodels.
C. Data:Datafromwhichassistantslearn.
D. Nlu.yml: Examples for intent and entities.
E. Stories .yml: Example of conversion turns.
F. Rules.yml: Predefined rules for dialogue policies.
This environment contains an inbuilt rasa chatbot with some sample questions and answers we can train this model for these questions.
4. Design the Conversational Flow: Define the dialogue flow and user interactions by creating stories. Stories represent example conversations between the user and the chatbot and help train the dialogue management model.
5. Create Intents and Entities: Identify the different intents (user's intentions) and entities (relevant information) that the chatbot needs to understand. Define the intents and entities in the Rasa NLU training data.
6. Train the Chatbot: Train the Rasa NLU and Rasa Core models using the training data you have prepared. Run the command rasa train to train the models.
7. Define Custom Actions: If required custom actions are to be performed, define them in your Rasa project. Create custom action classes that handle the logic for each action. But Our chatbot doesn't require any custom actions so this set is not done.
8. Connect to database: here we connected to MongoDB. And the conversations are stored as JSON files using Python code.
9. Connect External Services
10. Test and Evaluate: Test the chatbot using sample conversations to ensure it understands user inputs and provides appropriate responses. Make any necessary adjustments or refinements based on the test results.

11. Deploy the Chatbot: Deploy your chatbot to the desired platform or channel, such as a website.
Additionally, we created a Python code to extract data from a CSV file and convert it into the required format for Rasa NLU, stories, and domain files can indeed simplify the process, especially when dealing with large amounts of data.

WORKFLOW OF RASA
nlu.yml
1. The user asks a question
2. It will go to nlu.yml and find the intent where the question include
(intent: greet)
Stories.yml
1. It will go to stories.yml and find the action for the question (action for greet: utter_greet)
Domain.yml
1. It will go to domain.yml and the text that attach with the action 2. Dispalys the answe
