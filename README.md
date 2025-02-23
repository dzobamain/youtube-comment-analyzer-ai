# <p align="center">The program for analyzing comments on a YouTube video</p>

## About the program

To analyze comments under a YouTube video using GPT, just run the program, input the video link, and tell it what you want to know

## Installation Guide
Items 1-4 are websites:

[![python](https://img.shields.io/badge/install-python-:color)](https://www.python.org/)
[![dotenv](https://img.shields.io/badge/install-python--dotenv-blue)](https://pypi.org/project/python-dotenv/)
[![openai](https://img.shields.io/badge/install-openai-blue)](https://pypi.org/project/openai/)
[![google-api](https://img.shields.io/badge/install-google--api--python--client-blue)](https://pypi.org/project/google-api-python-client/)

1. Install **Python**
   + ```brew install python```
2. Install **dotenv** for .env
   + ```pip install python-dotenv```
3. Install **openai** for ChatGPT API
    + ```pip install openai```
4. Install **google api** for Youtube API
    + ```pip install google-api-python-client```
5. Clone the Project
    + ```git clone https://github.com/Dzobamain/youtube-comment-analyzer-chatgpt-py```
    + ```cd youtube-comment-analyzer-chatgpt-py```
6. You need to create a .env file and write the following in it:
    + ```
        YOUTUBE_API_KEY=your_api_key
        OPENAI_API_KEY=your_api_key
        ```


## How to Run:
Execute the Script (Console)
```
python main.py
```