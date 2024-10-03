from code.core.caching import bootstrap_caching

from code.core.parsing import read_file
from code.core.chunking import chunk_file
from code.core.embedding import embed_files
from code.core.qa import query_folder
from code.core.utils import get_llm
from dotenv import load_dotenv
import os
from io import BytesIO
import constants

load_dotenv()
model = constants.MODEL

def process_files():
    # for file_name in constants.FILES:
    f = open(constants.FILES, "rb")
    file = read_file(f)
    chunked_file = chunk_file(file, chunk_size=300, chunk_overlap=0)

    folder_index = embed_files(
            files=[chunked_file],
            embedding=constants.EMBEDDING if model != "debug" else "debug",
            vector_store=constants.VECTOR_STORE if model != "debug" else "debug",
            openai_api_key=constants.OPENAI_API_KEY,
        )

    return folder_index