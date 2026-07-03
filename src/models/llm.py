import os
import re
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import pipeline
import json

from langchain_ollama import OllamaLLM

class LLM:
    '''
    def __init__(self, 
                 model_path: str = r"""E:/Jigyasa/internn/rag_chatbot/assets/tiny-llama""",
                 temperature: float = 0.3,
                 max_new_tokens: int = 512):
        
        self.model_path = os.path.abspath(model_path)  # normalize to absolute
        self.temperature = temperature
        self.max_new_tokens = max_new_tokens
        self.model = None
        self._load_model()
    
    def _load_model(self):
        try:
            print(f"Loading LLM from: {self.model_path}")

            if not os.path.isdir(self.model_path):
                raise FileNotFoundError(f"Model directory not found: {self.model_path}")
            
            pipe = pipeline(
            "text-generation",
            model=self.model_path,
            max_new_tokens=self.max_new_tokens,  # move here, controls output length only
            truncation=True,                      # truncates input if too long
            )
            
            llm = HuggingFacePipeline(
                pipeline=pipe,
                pipeline_kwargs=dict(
                    temperature=self.temperature,
                )
            )
            
            self.model = ChatHuggingFace(llm=llm)
            print("LLM loaded successfully!")
        
        except Exception as e:
            print(f"Error loading LLM: {e}")
            raise
    
    def generate(self, prompt: str) -> str:
        result = self.model.invoke(prompt)
        return result.content
    
    def call_llm_json(self, prompt: str) -> str:
        full_prompt = f"You are an evaluation judge. Respond ONLY with valid JSON, no extra text.\n\n{prompt}"
        result = self.model.invoke(full_prompt)
        raw = result.content

        #match = re.search(r"\{.*\}", raw, re.DOTALL)
        if not match:
            raise ValueError(f"No JSON found in model output:\n{raw}")
        
        return match.group()
        '''

    def __init__(self,model_name: str="qwen3:latest", temperature: float=0.3):
        self.model_name=model_name
        self.temperature=temperature
        self.model=None
        self.load_model()
        

    def load_model(self):
       self.model=OllamaLLM(
            model=self.model_name,
            temperature=self.temperature
        ) 
       
    def call_llm(self,prompt):
        return self.model.invoke(prompt)
    
    def generate_answer(self,query:str,context:str)->str:
        prompt=f"""You are a helpful assistant.
         Answer the question using only the context given below:
         Context:{context}
         Question:{query}
         """
        raw = self.call_llm(prompt)
    
        # Remove thinking part if present
        if "</think>" in raw:
            raw = raw.split("</think>")[-1].strip()
        
        return raw

    def call_llm_json(self, prompt: str) -> dict:
        full_prompt = f"""You are an evaluation judge. Respond ONLY with valid JSON, no extra text.\n\n{prompt}"""
        raw = self.call_llm(full_prompt)
        print("------------call_llm_json-----------------")
        print(raw)
        # Remove thinking part if present
        if "</think>" in raw:
            raw = raw.split("</think>")[-1].strip()
        
        # Extract JSON
        match = re.search(r"\{.*\}", raw, re.DOTALL)
        if not match:
            raise ValueError(f"No JSON found in model output:\n{raw}")
        
        json_str = match.group()
        
        # Clean common model mistakes
        json_str = json_str.replace('"}', '"}')   # fix extra quotes
        json_str = re.sub(r'(\d+)"}', r'\1}', json_str)  # remove quote after numbers
        json_str = re.sub(r'(\d+\.\d+)"', r'\1', json_str)  # remove quote after decimals
        
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            # Last resort — try ast.literal_eval
            import ast
            try:
                return ast.literal_eval(json_str)
            except Exception as e:
                raise ValueError(f"Invalid JSON from model:\n{json_str}\nError: {e}")
        
        
        