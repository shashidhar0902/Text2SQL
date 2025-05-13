from openai import OpenAI
#from config import OPENAI_API_KEY

def test_openai_api_key():
    try:
        OPENAI_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcHAiLCJleHAiOjE3OTk5OTk5OTksInN1YiI6MzA0MzA1OSwiYXVkIjoiV0VCIiwiaWF0IjoxNjk0MDc2ODUxfQ.6eqbGG0f5RcCw_RW30oSpxJN1ff0zPJ4e4hCSJXkse8"
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say hello"}
            ],
            max_tokens=10,
            temperature=0
        )
        print("OpenAI API key is working. Response:")
        print(response.choices[0].message.content.strip())
    except Exception as e:
        print(f"Error testing OpenAI API key: {e}")

if __name__ == "__main__":
    test_openai_api_key()