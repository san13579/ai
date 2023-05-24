#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk
from nltk.chat.util import Chat, reflections

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

pairs = [
    [
        r"hi|hey|hello",
        ["Hello! How can I assist you today?", "Hi there! How can I help you?",]
    ],
    [
        r"balance inquiry",
        ["Sure! Could you please provide me your account number?",]
    ],
    [
        r"my account number is (.*)",
        ["Your current account balance is $1000. How else can I assist you?",]
    ],
    [
        r"transfer money",
        ["Certainly! Please provide me the recipient's account number and the amount you wish to transfer.",]
    ],
    [
        r"(.*) account number is (.*) and transfer (.*) dollars",
        ["Money transfer of $%3 from account %2 to %1 has been initiated successfully.",]
    ],
    [
        r"thank you|thanks",
        ["You're welcome! If you need any further assistance, feel free to ask.",]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day ahead.",]
    ]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()


# In[ ]:




