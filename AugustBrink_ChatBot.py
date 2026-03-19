# -*- coding: utf-8 -*-
import random
import sys

# All data samlad i en dictionary
data = {
    "greetings": {
        "keywords": ["hello", "hi", "greetings"],
        "responses": ["Hello if you want to talk I'm all ears.", "Hi do you want to tell me about your day?"]
    },
    "happy": {
        "keywords": ["happy", "glad", "good"],
        "responses": ["That's great to hear! Anything else on your mind?", "I'm glad you're feeling good! Can you tell me more about it?", "Keep up the positive vibes!"]
    },
    "sad": {
        "keywords": ["sad", "down", "unhappy", "unwell"],
        "responses": ["I'm sorry to hear that. Do you want to talk about it?", "It's okay to feel sad sometimes. I'm here for you.", "If you want to share what's making you feel down, I'm here to listen."]
    },
    "school": {
        "keywords": ["school", "homework", "class", "teacher"],
        "responses": ["School can be tricky sometimes. Do you want to talk about what's going on at school?", "Homework can be tough. Do you need to talk about it?", "Teachers can be great or challenging. Do you want to share more about your school experience?"]
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you later"],
        "responses": ["Goodbye! Take care!", "See you later! Have a great day!", "Bye! If you ever want to chat again, I'm here!"]
    },
    "swear": {
        "keywords": ["damn", "fuck", "shit", "bitch", "ass", "whore", "pussy", "dick", "fuh"],
        "responses": ["Please watch your language.", "Let's keep the conversation respectful.", "I understand you're upset, but let's try to use kinder words."]
    },
    "six_seven": {
        "keywords": ["67", "six-seven", "sixty seven"],
        "responses": ["omg six seven", "67 67 67 67 67", "67 is a great number!"]
    }
    
}

fallback_responses = [
    "I'm not sure I understand. Can you tell me more?",
    "That's interesting! Can you explain it a bit more?",
    "I see. Can you elaborate on that?",
    "sorry i quit you suck at this"
]


def find_response(message: str) -> str:
    if not message:
        return random.choice(fallback_responses)

    msg = message.lower()

    for category in data.values():
        for keyword in category["keywords"]:
            if keyword in msg:
                return random.choice(category["responses"])

    return random.choice(fallback_responses)


def run_bot(bot_name="Fi"):
    print("=" * 50)
    print(f"Hello! My name is {bot_name}. Im the spirit of the master sword how can i help you?")
    print("(Type 'bye' to exit)")
    print("=" * 50)

    try:
        while True:
            user_input = input("\nYou: ").strip()

            if not user_input:
                continue

            response = find_response(user_input)
            print(f"{bot_name}: {response}")

            if any(word in user_input.lower() for word in data["goodbye"]["keywords"]):
                break

    except (KeyboardInterrupt, EOFError):
        print(f"\n{bot_name}: Goodbye.")
        sys.exit()


if __name__ == "__main__":
    run_bot() 