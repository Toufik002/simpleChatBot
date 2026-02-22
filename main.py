# main.py
from chatbot import SimpleBot

def main():
    bot = SimpleBot()
    print("Type /quit to exit.")

    while True:
        user_text = input("You: ").strip()
        if not user_text:
            continue
        if user_text.lower() in ["/quit", "/exit"]:
            break

        bot.add_user_text(user_text)
        reply = bot.fetch_reply()
        print("AI:", reply)

if __name__ == "__main__":
    main()