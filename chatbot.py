import re
import long_responses as long

# Function to calculate message probability
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Check how many words in the user message are recognised
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculate the percentage of recognised words in the message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Check if all required words are present
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Return the message probability
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

# Function to check all messages
def check_all_messages(message):
    highest_prob_list = {}

    # Function to simplify response creation
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------

    # Example responses with recognized words and conditions
    response('Hello, sir!', ['hello', 'hi', "what's up", 'how you doing', 'how you doin' ], single_response=True)
    response("I'm just chilling nigga. What about you?", ['how', 'are', 'you', 'doing'], required_words=["how", "you"]) 
    response("Ahh, that's good to here.", ["fine"], required_words=["fine"])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_ADVICE, ['what', 'you',"know", 'help', "who", "know"], required_words=['what', 'you', 'help', "who", "know"])

    response("I am not completely sure about my feelings", ['how', 'are', 'you', 'feeling'], required_words=['feeling'])
    response("I not have a preference on that topic.", ['what', 'is', 'your', 'favorite', 'color'], required_words=["color"])
    response("I don't know that nigga.", ['who', 'is', 'the', 'president'], required_words=['who', 'is'])
    response("Google it, kalaiya!", ['what', 'is', 'the', ], required_words=['what', 'is'])
    response("I'm just a program, so I don't have personal experiences! But right now I am chatting with you nigga!", ['tell', 'me', 'about', 'yourself'], required_words=['yourself'])
    response("I'm always ready to chat with you!", ['when', 'are', 'you', 'available'], required_words=["available"])
    response("I'm not sure, it depends on the context!", ['what', 'does', 'that', 'mean'], required_words=['mean'])
    response("I don't have preferences, I'm just a computer program!", ['what', 'is', 'your', 'favorite', 'food'], required_words=['your', 'favorite', 'food'])
    

    # Determine the best match
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

# Function to get a response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Testing the response system
while True:
    print("Bot chachu: " + get_response(input("You: ")))
