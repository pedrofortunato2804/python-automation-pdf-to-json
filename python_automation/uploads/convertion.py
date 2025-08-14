import os
import json
import tempfile
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def make_convertion_pdf_to_json(pdf_file):

    client = OpenAI(
        api_key = OPENAI_API_KEY
    )

    file = client.files.create(
        file = open("uploads/temp_files/" + pdf_file.name, "rb"),
        purpose = "user_data"
    )

    prompt = """
    Leia o conteúdo da minuta em PDF e transforme-o emm um objeto JSON estruturado.
    Apenas retorne o JSON e nada mais.
    """

    response = client.responses.create(
        model = "gpt-5",
        input = [
            {"role": "user", 
            "content": [
                {"type": "input_file", "file_id": file.id},
                {"type": "input_text", "text": prompt}
            ]}
        ]
    )
    
    return response

