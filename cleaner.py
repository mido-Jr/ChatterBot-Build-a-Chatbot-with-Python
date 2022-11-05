# cleaner.py

import re


def remove_chat_metadata(chat_file):
    date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)" # ex-> "9/05/22, 06:29"
    WhiteSpace = r"\s-\s" # ex-> " - "
    username = r"([\w\s]+)" # ex-> "Mido"
    meta_data = r":\s" # ex-> ": "
    
    pattern = date_time + WhiteSpace + username + meta_data
    
    with open(chat_file , "r") as corpus_file:
        content = corpus_file.read()
    
    cleand_corpus = re.sub(pattern , "", content)
    return tuple(cleand_corpus.split('\n'))

def remove_non_message_text(text_lines):
    message = text_lines[1:-1]
    
    filter_out = ("<Media omitted>",)
    return tuple((msg for msg in message if msg not in filter_out ))


def clean_corpus(chat_export_file):
    meassage_corpus = remove_chat_metadata(chat_export_file)
    cleaned_corpus = remove_non_message_text(meassage_corpus)
    return(cleaned_corpus)