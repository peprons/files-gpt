from dotenv import load_dotenv
import os
load_dotenv()

APP_NAME = "OPS GURU"
EMBEDDING = "openai"
VECTOR_STORE = "faiss"
MODEL_LIST = ["gpt-3.5-turbo"]
MODEL = MODEL_LIST[0]
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
FILES = 'resources/survey.pdf'