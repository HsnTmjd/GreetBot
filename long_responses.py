import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "I am really not sure. ",
                "But the point is sir, YOU ARE BLACK. So I don't have an answer for you.",
                "What does that mean?"
                "I think you should commit suicide"][random.randrange(5)]
    
    return response
