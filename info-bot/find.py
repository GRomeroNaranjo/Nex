from transformers import pipeline

class Model():
    def __init__(self, model_name, framework, ):
        self.model_name = model_name
        self.framework = framework

    def find(self, question):
        generator = pipeline("text2text-generation", model=self.model_name, framework=self.framework)
        information = generator(question, max_length=20, min_length=10, truncation=True)
        
        return information[0]['generated_text']
    
class System():
    def __init__(self, model_name, framework):
        self.model_name = model_name
        self.framework = framework
        self.model = Model(model_name, framework)
    
    def find(self, prompt):
        information = self.model.find(prompt)
        return information
    

def find(prompt, database):
    system = System("google/flan-t5-large", "pt")
    processed_text = f"Find relevant information for this question: {prompt}. Based on this information: {database["Summatives"]}, {database["Trips"]}"
    information = system.find(processed_text)
    return information


database = {
    "Summatives": "Has one maths summative on Monday, and two English tests on Friday",
    "Trips": "Has a school trip to the museum on Thursday"
}
