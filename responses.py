import random
GREETINGS = [

    "😊 How can I help you today?",

    "🤖 I'm ready to assist you.",

    "😄 Nice to see you!",

    "🌟 Welcome back!",

    "🚀 Let's get started.",

    "💙 Ask me anything.",

    "😁 Hope you're having a wonderful day.",

    "✨ I'm here to help.",

    "🙌 What would you like to know?",

    "😎 Ready for another conversation?"
]

THANKS = [

    "❤️ You're welcome!",
    "😊 Happy to help.",
    "😁 Anytime!",
    "🤝 My pleasure.",
    "😄 Glad I could help.",
    "🌟 Always here for you.",
    "🚀 You're most welcome.",
    "💙 No problem at all.",
    "🙌 It's my pleasure.",
    "😊 Keep learning!"
]

GOODBYE = [

    "👋 Goodbye! Have a wonderful day.",
    "😊 See you again soon.",
    "🌟 Take care!",
    "💙 Bye! Keep smiling.",
    "🚀 Happy coding!",
    "😄 Catch you later.",
    "🤖 Hope to chat again soon.",
    "👋 Stay safe and take care.",
    "😁 Bye! Have fun.",
    "✨ Wishing you a great day!"
]
# BASIC RESPONSES
RESPONSES = {
    "how are you": [
        "I'm doing great! 😊",
        "I'm fine. Thanks for asking!",
        "Everything is working perfectly. 😄"
    ],

    "who are you": [
        "I'm Smart ChatBot built using Python and CustomTkinter."
    ],

    "your name": [
        "My name is Smart ChatBot 🤖"
    ],

    "creator": [
        "I was created by Akash using Python."
    ],

    "python": [
        "Python is a simple, powerful and beginner-friendly programming language."
    ],

    "java": [
        "Java is an object-oriented programming language used for desktop, web and Android development."
    ],

    "c++": [
        "C++ is a powerful programming language used in competitive programming and game development."
    ],

    "html": [
        "HTML is used to create the structure of web pages."
    ],

    "css": [
        "CSS is used to style web pages."
    ],

    "javascript": [
        "JavaScript makes websites interactive."
    ],

    "sql": [
        "SQL is used to manage databases."
    ],

    "mongodb": [
        "MongoDB is a NoSQL database."
    ],

    "ai": [
        "Artificial Intelligence enables computers to learn and solve problems."
    ],

    "machine learning": [
        "Machine Learning is a branch of AI that learns from data."
    ],

    "help": [
        """Available Commands

👋 Greetings
• hello
• hi
• hey

📚 Programming
• python
• java
• c++
• html
• css
• javascript
• sql
• mongodb
• ai
• machine learning

⏰ Utilities
• time
• date

😂 Fun
• joke
• motivate me
• quote
• fun fact

❓ Others
• who are you
• creator
• your name
• thanks
• bye
"""
    ]
}
# JOKES
JOKES = [

    "😂 Why do programmers prefer dark mode? Because light attracts bugs.",

    "😂 Why was the computer cold? It left its Windows open.",

    "😂 Why do Java developers wear glasses? Because they don't C#.",

    "😂 Debugging is like being the detective and the criminal at the same time."

]

# MOTIVATION
MOTIVATION = [

    "💪 Success comes from consistency.",

    "💪 Don't stop until you're proud.",

    "💪 Believe in yourself.",

    "💪 Every expert was once a beginner.",

    "💪 Keep learning. Keep growing."

]

# QUOTES
QUOTES = [

    "💡 First, solve the problem. Then write the code.",

    "💡 Programs must be written for people to read.",

    "💡 Code is like humor. If you have to explain it, it's bad."

]

# RIDDLES
RIDDLES = [

    "🤔 What has keys but can't open locks?\n\nAnswer: A Keyboard ⌨️",

    "🤔 What has hands but cannot clap?\n\nAnswer: A Clock 🕒",

    "🤔 What gets wetter as it dries?\n\nAnswer: A Towel 🧺",

    "🤔 What has one eye but can't see?\n\nAnswer: A Needle 🪡",

    "🤔 What comes once in a minute, twice in a moment, but never in a thousand years?\n\nAnswer: The letter 'M'.",

    "🤔 What has many teeth but can't bite?\n\nAnswer: A Comb.",

    "🤔 What can travel around the world while staying in one corner?\n\nAnswer: A Stamp.",

    "🤔 What has a neck but no head?\n\nAnswer: A Bottle."
]
# FACTS
FACTS = [

    "📚 Python was created by Guido van Rossum in 1991.",

    "💻 The first computer bug was an actual moth found in a computer.",

    "🌍 More than 700 programming languages exist.",

    "🤖 AI stands for Artificial Intelligence.",

    "⌨️ The first programmer was Ada Lovelace.",

    "📱 Android apps are mainly developed using Java and Kotlin.",

    "🌐 HTML is not a programming language.",

    "🚀 Git was created by Linus Torvalds."
]

# COMPLIMENTS
COMPLIMENTS = [

    "😊 You're doing a great job!",

    "🔥 Keep coding, you're improving every day!",

    "💪 Believe in yourself.",

    "🚀 You can build amazing projects!",

    "😎 You're becoming a better programmer every day.",

    "🌟 Your consistency will make you successful.",

    "👏 Keep learning and never give up.",

    "💯 You're smarter than you think!"
]


def random_response(category):
    if category == "riddle":
        return random.choice(RIDDLES)

    elif category == "compliment":
        return random.choice(COMPLIMENTS)

    elif category == "joke":
        return random.choice(JOKES)

    elif category == "motivate":
        return random.choice(MOTIVATION)

    elif category == "quote":
        return random.choice(QUOTES)

    elif category == "fact":
        return random.choice(FACTS)

    return None