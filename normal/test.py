from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "meta-llama/Llama-2-7b-chat-hf"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

conversation_history = []

def generate_response(prompt):
    conversation_history.append(f"User: {prompt}")
    input_text = "Conversation History:\n" + "\n".join(conversation_history[-5:])
    input_text += "\n(This is the conversation history. Please generate the next response as the bot without continuing with user input. Do not mention the conversation history please.)"
    
    inputs = tokenizer(input_text, return_tensors="pt")
    response = model.generate(**inputs, max_new_tokens=50, return_dict_in_generate=True, output_scores=True)
    
    new_tokens = response.sequences[0][inputs['input_ids'].shape[-1]:]  # Only new tokens
    decoded_response = tokenizer.decode(new_tokens, skip_special_tokens=True)
    
    conversation_history.append(f"LLaMA: {decoded_response}")
    return decoded_response

while True:
    user_input = input("User: ")
    response = generate_response(user_input)
    print(response)
