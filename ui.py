import random
import gradio as gr
from query_data import query_rag

def alternatingly_agree(message, history):
    response, _ = query_rag(message)

    final_response = f"""{response.content}
    """

    return final_response

gr.ChatInterface(alternatingly_agree).launch()