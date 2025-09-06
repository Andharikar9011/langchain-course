from dotenv import load_dotenv
import os
load_dotenv()

def main():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    print("Hello from langchain-course!")
    print(f"OpenAI API Key: {openai_api_key}")
    print(f"Tavily API Key: {tavily_api_key}")


if __name__ == "__main__":
    main()
