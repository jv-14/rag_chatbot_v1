import json
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class LLMAsAJudge:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def llm_judge(self, question, ground_truth, answer, context):
        prompt = f"""Evaluate the following and return a JSON object with two keys:
- "faithfulness": a score from 0 to 1 indicating if the answer is faithful to the context
- "answer_relevance": a score from 0 to 1 indicating if the answer is relevant to the question

Question: {question}
Ground Truth: {ground_truth}
Answer: {answer}
Context: {context}

Respond ONLY with a JSON object like this: {{"faithfulness": 0.8, "answer_relevance": 0.9}}"""

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "You are an evaluation judge. Respond ONLY with JSON."},
                {"role": "user", "content": prompt}
            ]
        )

        return json.loads(response.choices[0].message.content)