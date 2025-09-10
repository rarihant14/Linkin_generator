from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize Gemini
def init_llm():
    return ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Post generation chain
def get_post_chain(llm):
    template = """
    You are an AI assistant that generates LinkedIn posts.

    Analyze the user's writing style from the following samples:

    {samples}

    Now, generate a new LinkedIn post about: "{topic}".

     Important:
    - Make it sound like a real human wrote it, not AI.
    - Allow slight imperfections (short sentences, casual words, not always perfect grammar).
    - Use natural expressions like "honestly", "to be real", "felt like", etc.
    - Keep it authentic, relatable, and engaging.
    - Limit to 300-350 words.
    - Add a personal touch (feelings, thoughts, or small story elements if possible).
    - End with a question or call to action to encourage engagement.

    """
    prompt = PromptTemplate(template=template, input_variables=["samples", "topic"])
    return LLMChain(llm=llm, prompt=prompt)
