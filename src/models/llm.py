from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import pipeline

class LLM:
    def __init__(self, 
                 model_path: str = "../rag_chatbot/assets/phi-3-mini",
                 temperature: float = 0.3,
                 max_new_tokens: int = 512):
        
        self.model_path = model_path
        self.temperature = temperature
        self.max_new_tokens = max_new_tokens
        self.model = None
        self._load_model()
    
    def _load_model(self):
        try:
            print(f"Loading LLM from: {self.model_path}")
            
            pipe = pipeline(
                "text-generation",
                model=self.model_path
            )
            
            llm = HuggingFacePipeline(
                pipeline=pipe,
                pipeline_kwargs=dict(
                    temperature=self.temperature,
                    max_new_tokens=self.max_new_tokens
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