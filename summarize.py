from transformers import pipeline

class Model():
    def __init__(self, model_name, framework, ):
        self.model_name = model_name
        self.framework = framework

    def summarize(self, text):
        generator = pipeline("text2text-generation", model=self.model_name, framework=self.framework)
        summary = generator(text, max_length=100, min_length=50, truncation=True)
        
        return summary[0]['generated_text']
    
class System():
    def __init__(self, model_name, framework):
        self.model_name = model_name
        self.framework = framework
        self.model = Model(model_name, framework)
    
    def summarize(self, prompt):
        summary = self.model.summarize(prompt)
        return summary
    

def summarize(prompt):
    system = System("google/flan-t5-large", "pt")
    processed_text = f"summarize this: {prompt}"
    summary = system.summarize(processed_text)
    return summary
