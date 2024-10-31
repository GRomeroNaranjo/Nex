import generate
from summarize import summarize

class Conversation:
    def __init__(self, model_name, user_name, database, model, tokenizer):
        self.database = database
        self.model_name = model_name
        self.user_name = user_name
        self.model = model
        self.tokenizer = tokenizer

    def summarize(self, inputs):
        return summarize(inputs)

    def start(self):
        previous_conversations = ""
        run = True
        while run:
            prompt = input(f"{self.user_name}: ")

            if prompt.lower() == "quit":
                run = False
                break

            summary = self.summarize(previous_conversations)
            conversation_input = f"{prompt}"
            response = generate.search(conversation_input, self.database, self.model, self.tokenizer)

            previous_conversations += f"User: {prompt}, Bot: {response}\n"
            print(f"{response}")

def start_conversation(model_name, user_name, database, model, tokenizer):
    conversation = Conversation(model_name, user_name, database, model, tokenizer)
    conversation.start()
