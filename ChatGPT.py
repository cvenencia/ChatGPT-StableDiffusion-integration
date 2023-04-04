import os
import openai

openai.api_key = os.getenv('CHATGPT_API_KEY')
CHATGPT_MODEL = "gpt-3.5-turbo"


def enhance_article(article):
    print("Enhancing the article")
    response = openai.ChatCompletion.create(
        model=CHATGPT_MODEL,
        messages=[
            {
                "role": "system",
                "content": f"""Enhance the quality of this article by improving its grammar, coherence, and overall readability. Do not add or remove information. Try to keep it as close as possible to the original. Do not try to make it shorter or longer.
                ```
                {article}
                ```
                """
            },
        ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content

    return result


def extract_takeaways_from_article(article):
    print("Writing a summary of the article")
    response = openai.ChatCompletion.create(
        model=CHATGPT_MODEL,
        messages=[
            {
                "role": "system",
                "content": f"""Write a prompt suitable for an Image Generation AI based on this article. Do not add or remove information. Try to keep it as short as possible.
                ```
                {article}
                ```
                """
            },
        ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content

    return result
