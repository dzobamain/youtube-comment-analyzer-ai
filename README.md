# <p align="center">Analyzing comments on a YouTube video</p>

## About the program

To analyze comments under a YouTube video using GPT, just run the program, input the video link, and tell it what you want to know

## Installation Guide

Items 1-5 are websites:

<p align="center">
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/install-python-blue" alt="python">
    </a>
    <a href="https://pypi.org/project/python-dotenv/">
        <img src="https://img.shields.io/badge/install-python--dotenv-orange" alt="dotenv">
    </a>
    <a href="https://pypi.org/project/google-api-python-client/">
        <img src="https://img.shields.io/badge/install-google--api--python--client-red" alt="google-api">
    </a>
    <a href="https://pypi.org/project/openai/">
        <img src="https://img.shields.io/badge/install-openai-white" alt="openai">
    </a>
    <a href="https://pypi.org/project/rich/">
        <img src="https://img.shields.io/badge/install-rich-blue" alt="rich">
    </a>
</p>


1. Install **Python**
   + ```brew install python```
2. Install **dotenv** for .env
   + ```pip install python-dotenv```
3. Install **openai** for ChatGPT API
    + ```pip install openai```
4. Install **google api** for Youtube API
    + ```pip install google-api-python-client```
5. Install **rich** for markdown text in console
    + ```pip install rich```
6. Clone the Project
    + ```git clone https://github.com/Dzobamain/youtube-comment-analyzer-chatgpt-py```
    + ```cd youtube-comment-analyzer-chatgpt-py```
7. You need to create a .env file and write the following in it:
    + ```
        YOUTUBE_API_KEY=your_api_key
        OPENAI_API_KEY=your_api_key
        ```


## How to Run:
Execute the Script (Console)
```
python app.py
```