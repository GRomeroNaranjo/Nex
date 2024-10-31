import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from dataclasses import dataclass
from huggingface_hub import login
import find

login("my-private-token")

@dataclass
class Config:
    max_length = 250
    temperature = 0.7
    top_k = 50
    model_name = "meta-llama/Llama-2-7b-chat-hf"

class Model:
    def __init__(self, max_length, temperature, top_k, tokenizer, model, model_name):
        self.model_name = model_name
        self.max_length = max_length
        self.temperature = temperature 
        self.top_k = top_k
        self.tokenizer = tokenizer 
        self.model = model
        self.tokenizer = tokenizer
        self.conversation_history = []

    def find(self, prompt, database):
        information = find.find(prompt, database)
        return information

    def generate(self, prompt, database):
        information = self.find(prompt, database)
        processed_input = "Conversation History:\n" + "\n".join(self.conversation_history[-5:])
        processed_input += f"\nUser: {prompt}\nRelevant Information: {information}\n(This is the conversation history. Please generate the next response as the bot without continuing with user input. Do not mention the conversation history please.)"
        input_ids = self.tokenizer.encode(processed_input, return_tensors="pt")
        attention_mask = input_ids.ne(self.tokenizer.eos_token_id).long()
        output = self.model.generate(
            input_ids, 
            attention_mask=attention_mask,
            temperature=self.temperature,
            top_k=self.top_k,
            max_new_tokens=50, 
            pad_token_id=self.tokenizer.eos_token_id
        )
        decoded_response = self.tokenizer.decode(output[0][input_ids.shape[-1]:], skip_special_tokens=True)
        self.conversation_history.append(f"User: {prompt}")
        self.conversation_history.append(f"LLaMA: {decoded_response}")
        return decoded_response

class System:
    def __init__(self, config, database, model, tokenizer):
        self.database = database
        self.config = config
        self.model = Model(config.max_length, config.temperature, config.top_k, tokenizer, model, config.model_name)

    def generate(self, prompt):
        output = self.model.generate(prompt, self.database)
        return output

def respond(prompt, database, model, tokenizer):
    config = Config()
    system = System(config, database, model, tokenizer)
    return system.generate(prompt)

def search(prompt, database, model, tokenizer):
    config = Config()
    text = respond(prompt, database, model, tokenizer)
    return text
