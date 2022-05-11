from curses import flash
from flask import Flask, render_template, url_for, request
import json
from transformers import pipeline
from bs4 import BeautifulSoup
import requests
import googletrans
from googletrans import Translator

app = Flask(__name__);

summarizer = pipeline("summarization")

translator = Translator()

def LinkSummarize(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all(['h1', 'p'])
    text = [result.text for result in results]
    ARTICLE = ' '.join(text)
    
    max_chunk = 500

    ARTICLE = ARTICLE.replace('.', '.<eos>')
    ARTICLE = ARTICLE.replace('?', '?<eos>')
    ARTICLE = ARTICLE.replace('!', '!<eos>')
    sentences = ARTICLE.split('<eos>')

    current_chunk = 0 
    chunks = []

    for sentence in sentences:
        if len(chunks) == current_chunk + 1: 
            if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            chunks.append(sentence.split(' '))

    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])

    translated = translator.translate(chunks, dest='en')
    final_text = [trans.text for trans in translated]
    res = summarizer(final_text, max_length=200, min_length=30, do_sample=False)
    final_com = ' '.join([summ['summary_text'] for summ in res])
    pp = translator.translate(final_com, dest=translator.detect(chunks)[0].lang)
    return pp.text

def TextSummarize(Text):
    translated = translator.translate(Text, dest='en')
    res = summarizer(translated.text, max_length=200, min_length=30, do_sample=False)
    pp = translator.translate(res[0]['summary_text'], dest=translator.detect(Text).lang)
    return pp.text;

@app.route("/")
def first():
    return page1();

@app.route("/home")
def page1():
    return render_template('home.html')

@app.route("/linkemb")
def page2():
    return render_template('linkemb.html')

@app.route('/home', methods=['POST'])
def getText():
    userInput = request.get_json(force=True);
    return TextSummarize(userInput['text']);

@app.route('/linkemb', methods=['POST'])
def getLink():
    userInput = request.get_json(force=True);
    return LinkSummarize(userInput['text']);

if __name__ == "__main__":
    app.run(debug = True);