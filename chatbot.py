from datetime import datetime
import random
import string

from responses import (
    RESPONSES,
    GREETINGS,
    THANKS,
    GOODBYE,
    random_response
)

# Main Chatbot Function
def get_response(message):

    message = message.lower().strip()

    # Greetings
    if message in [ "hello",
    "hi",
    "hey",
    "hii",
    "hlo",
    "namaste",
    "good morning",
    "good afternoon",
    "good evening",
    "good night"]:
        current_hour = datetime.now().hour

        if 5 <= current_hour < 12:
            greeting = "🌅 good morning"
        elif 12 <= current_hour < 17:
            greeting = "☀️ good afternoon"
        elif 17 <= current_hour < 21:
            greeting = "🌇 good evening"
        else:
            greeting = "🌙 good night"

        return f"{greeting}!\n\n{random.choice(GREETINGS)}"

    # Thanks
    elif message in ["thanks", "thank you", "thx"]:
        return random.choice(THANKS)

    # Goodbye
    elif message in ["bye", "goodbye", "see you", "exit"]:
        return random.choice(GOODBYE)

    # Roll Dice
    elif message in ["roll dice", "dice"]:
        return f"🎲 You rolled: {random.randint(1, 6)}"

    # Flip Coin
    elif message in ["flip coin", "coin"]:
        return random.choice(["🪙 Heads", "🪙 Tails"])

    # Guess Number
    elif message == "guess number":
        return f"🎯 My lucky number is {random.randint(1, 100)}"

    # Password Generator
    elif message == "password":
        chars = string.ascii_letters + string.digits + "@#$%"
        password = "".join(random.choice(chars) for _ in range(10))
        return f"🔐 Random Password\n\n{password}"

    # OTP Generator
    elif message == "otp":
        otp = random.randint(100000, 999999)
        return f"📱 Your OTP is\n\n{otp}"

    # Current Time
    elif message == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        return f"🕒 Current Time\n\n{current_time}"

    # Current Date
    elif message == "date":
        current_date = datetime.now().strftime("%d %B %Y")
        return f"📅 Today's Date\n\n{current_date}"

    # Joke
    elif message in ["joke", "tell me a joke"]:
        return random_response("joke")

    # Motivation
    elif message in ["motivate me", "motivation"]:
        return random_response("motivate")

    # Programming Quote
    elif message in ["quote", "coding quote"]:
        return random_response("quote")

    # Fun Fact
    elif message in ["fact", "fun fact"]:
        return random_response("fact")

    # Riddle
    elif message in ["riddle", "puzzle"]:
        return random_response("riddle")

    # Compliment
    elif message in ["compliment", "praise me"]:
        return random_response("compliment")

    # Basic Responses
    elif message in RESPONSES:
        return random.choice(RESPONSES[message])

    # Default Response
    return (
        "❌ Sorry, I don't understand that.\n\n"
        "Type 'help' to see the available commands."
    )