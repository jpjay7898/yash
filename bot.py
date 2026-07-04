print("EduAI Bot Started! (type 'exit' to stop)")

reward = 1

while True:
    user_input = input("\nYou: ").lower()

    if user_input == "exit":
        print("Bot: Goodbye!")
        break

    elif "hello" in user_input:
        print("Bot: Hello! Ask me something..")
        reward += 1
        print("Reward +1")

    elif "ai" in user_input:
        print("Bot: AI means smart machines that help humans.")
        reward += 1
        print("Reward +1")

    elif "education" in user_input:
        print("Bot: AI in education helps students learn better.")
        reward += 1
        print("Reward +1")

    elif "thank" in user_input:
        print("Bot: You're welcome")
        reward += 2
        print("Reward +2")

    else:
        print("Bot: I don't understand. Try asking about AI.")
        print("Reward 0")

print("\nTotal Reward:", reward)