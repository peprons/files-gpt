import streamlit as st
from code.file_processing import process_files
import constants

from code.ui import (
    wrap_doc_in_html,
    is_query_valid,
    is_file_valid,
    is_open_ai_key_valid,
    display_file_read_error,
)
from code.core.parsing import read_file
from code.core.chunking import chunk_file
from code.core.embedding import embed_files
from code.core.qa import query_folder
from code.core.utils import get_llm

@st.cache_resource
def initialize_resource():
    # Your one-time initialization code goes here
    print("This runs only once when the script is first executed")
    # You can perform any setup tasks, like:
    # - Setting up database connections
    # - Loading large datasets
    # - Initializing machine learning models
    # - Setting global variables
    folder_index = process_files()
    print("folder_index ", folder_index)
    return folder_index

# Your regular Streamlit app code starts here
def main():
    # Call the initialization function
    folder_index = initialize_resource()
    
    # st.set_page_config(page_title="Ops Guru", page_icon="📖", layout="wide")
    st.header(constants.APP_NAME)

    with st.form(key="qa_form"):
        query = st.text_area("Ask a question about the SOPs")
        submit = st.form_submit_button("Submit")

    if submit:
        if not is_query_valid(query):
            st.stop()

        # Output Columns
        answer_col, sources_col = st.columns(2)

        llm = get_llm(model=constants.MODEL, openai_api_key=constants.OPENAI_API_KEY, temperature=0)
        result = query_folder(
            folder_index=folder_index,
            query=query,
            return_all=False,
            llm=llm,
        )

        # with answer_col:
        st.markdown("#### Answer")
        st.markdown(result.answer)

#        with sources_col:
        st.markdown("#### Sources")
        for source in result.sources:
            st.markdown(source.page_content)
            st.markdown(source.metadata["source"])
            st.markdown("---")

if __name__ == "__main__":
    main()
