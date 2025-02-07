import datetime
import random

responses = {
    "hello": ["Hi there!", "Hello! How can I help you?", "Hey! What's up?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "I'm here to help you!", "I'm good! What about you?"],
    "what is your name?": ["I am just a chatbot", "You can call me ChatBot", "I do not have name yet"],
    "time": [f"Now is {datetime.datetime.now().strftime('%H:%M:%S')}"],
    "date": [f"Today's date is {datetime.date.today()}"],
    "bye": ["Bye, bye, see you soon!", "Goodbye! Have a nice day", "Bye and don't forget to code tomorrow! :)"],
    "the best university": ["TU - Sofia", "SoftUni", "TU - Sofia and SoftUni are the best in Bulgaria"],
    "the best city in bulgaria": ["Yambol", "Yambol, which is located in southern Bulgaria",
                                  "Yambol, the center of the universe"],
    "How much sleep i need": ["8 is good", "People should sleep 7-9 hours", "7.5 hours is the best you can get"],
    "season": [
        "winter" if datetime.date.today().month in [12, 1, 2] else "spring" if datetime.date.today().month in [3, 4,
                                                                                                               5] else
        "summer" if datetime.date.today().month in [6, 7, 8] else "autumn"]
}

learned_responses = {}


def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key == user_input:
            return random.choice(responses[key])
    if user_input in learned_responses:
        return random.choice(learned_responses[user_input])
    new_response = input("🤖 I don't know how to respond to that. How should I reply? ")
    if user_input in learned_responses:
        learned_responses[user_input].append(new_response)
    else:
        learned_responses[user_input] = [new_response]
    return "Got it! I'll remember that for next time."


def greet_user():
    current_hour = datetime.datetime.now().hour
    if 4 <= current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 18:
        return "Good afternoon!"
    elif 18 <= current_hour < 22:
        return "Good evening!"
    else:
        return "Good night!"


def chatbot():
    print("🤖 Chatbot: " + greet_user())
    print("🤖 Chatbot: How can I assist you today? (Type 'bye' to exit)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("🤖 Chatbot:", get_response(user_input))
            break
        print("🤖 Chatbot:", get_response(user_input))


if __name__ == "__main__":
    chatbot()
