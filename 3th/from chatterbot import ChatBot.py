from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# إنشاء الشات بوت
chatbot = ChatBot('MyBot')

# تدريب الشات بوت باستخدام corpus data
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# استخدام الشات بوت للتفاعل مع المستخدم
while True:
    try:
        user_input = input("You: ")
        response = chatbot.get_response(user_input)
        print("Bot:", response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
