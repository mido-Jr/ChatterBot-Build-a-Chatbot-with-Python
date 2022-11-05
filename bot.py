# bot.py 

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

CORPUS_FILE = "chat.txt"

chatbot = ChatBot('Chatpot')

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, friend :)"
])
trainer.train([
    "Are you a plant?",
    "No, I`m the Bot below the plant!"
])

trainer.train([
    "The Devloper",
    "Ahmed ELnassag, you can make a connection wit him ",
])
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)


exit_conditions = (":q", "quit", "exit")

while True:
    query = input("-> ")
    if query in exit_conditions:
        break
    else:
        print(f'🤖 {chatbot.get_response(query)}')