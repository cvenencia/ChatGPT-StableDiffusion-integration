import os
import nlpcloud

client = nlpcloud.Client(
    "stable-diffusion", os.getenv('STABLEDIFFUSION_TOKEN'), True)


def generate_image(prompt):
    try:
        print("Generating the image for the prompt")
        response = client.image_generation(prompt)
        return response['url']
    except Exception as e:
        print(e)
        return None
