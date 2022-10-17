chatbot = GenericAssistant('/intents.json')
chatbot.train_model()
chatbot.save_model()