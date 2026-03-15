import google.generativeai as genai

genai.configure(api_key="YOUR API KEY")

model = genai.GenerativeModel("gemini-flash2.5")

def ask_ai(question, sequence):

    prompt = f"""
You are a protein biology expert.

Protein sequence:
{sequence}

User question:
{question}

Explain clearly.
"""

    response = model.generate_content(prompt)

    return response.text
