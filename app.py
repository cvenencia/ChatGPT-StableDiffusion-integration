from flask import Flask, render_template, request
import ChatGPT
import StableDiffusion

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def scrape():
    article = request.get_json()['article']
    enhanced_article = ChatGPT.enhance_article(article)
    image_prompt = ChatGPT.extract_takeaways_from_article(enhanced_article)
    generated_image = StableDiffusion.generate_image(image_prompt)
    return render_template('result.html', article=article, enhanced=enhanced_article, img_url=generated_image, image_prompt=image_prompt)
