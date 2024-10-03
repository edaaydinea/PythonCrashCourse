def send_messages(messages, sent_messages):
    """Print each message and move it to the sent messages list."""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

# List of text messages
text_messages = ["Hello, how are you?", "Don't forget to call me!", "Happy Birthday!"]
sent_messages = []

# Call the function with a copy of the list
send_messages(text_messages[:], sent_messages)

# Show the lists after sending messages
print("\nOriginal messages:", text_messages)
print("Sent messages:", sent_messages)


