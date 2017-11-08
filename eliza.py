greetings = ["hello", "hey", "hi", "good morning", "good evening"]
x = raw_input()
while True:
    if x in greetings:
        name = raw_input("Hello! What's your name?")
        break
    else:
        x = raw_input("I'm sorry. I can't understand you. Please try to express yourself differently.")

good_mood = ["good", "fine", "great", "excellent"]
mood = input("It's nice to meet you," + name + ". How are you doing today?")
if mood in good_mood:
	

