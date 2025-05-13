from openai import OpenAI
from config import OPENAI_API_KEY
import pandas as pd

client = OpenAI(api_key=OPENAI_API_KEY)

class CrewAIAgent:
    def __init__(self, data_schema: str):
        """
        Initialize the agent with the data schema or description.
        """
        self.data_schema = data_schema

    def generate_query(self, prompt: str) -> str:
        """
        Use OpenAI API to generate a query based on the natural language prompt and data schema.
        """
        system_message = f"You are an AI assistant that generates SQL or pandas queries based on the following data schema:\n{self.data_schema}\n"
        user_message = f"Generate a query for the following request:\n{prompt}\n"

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            max_tokens=200,
            temperature=0
        )
        query = response.choices[0].message.content.strip()
        return query

    def execute_query(self, query: str, data: pd.DataFrame) -> pd.DataFrame:
        """
        Execute the generated query on the pandas DataFrame.
        This assumes the query is a pandas query expression or Python code.
        """
        try:
            # For simplicity, we will use pandas query method if possible
            result = data.query(query)
            return result
        except Exception as e:
            print(f"Error executing query: {e}")
            return None
