import os
from groq import Groq
from dotenv import load_dotenv 


load_dotenv()

client = Groq(
    api_key = os.getenv("GROQ_API_KEY")

)

#building prompt

def build_prompt(question, results):
    context = "\n\n".join(
        results["documents"][0]
    )
    
    prompt = f"""
    You are a helpful African Travel Assistant.
    
    Use ONLY the safari information below to answer.
    
    Safari Data:
    {context}
    
    Question:
    {question}
    
    Answer:
    
    """
    
    return prompt



#generate an answer
def generate_answer(question, results):
    
    prompt = build_prompt(question, results)
    
    response = client.chat.completions.create(
        model= "llama-3.1-8b-instant",
        messages = [{
            "role": "user",
            "content": prompt
        }]
    )
    
    
    return response.choices[0].message.content