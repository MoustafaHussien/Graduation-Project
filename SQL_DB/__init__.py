# -*- coding: utf-8 -*-
# This is a script to prepossess the tweets and save all the necessary formatted data to a file
import os
import codecs
import HTMLParser
import re


def process_file(file_name, text_file_name):
    print "parsing file " + file_name
    data_file = codecs.open(file_name, "r", "utf-8")
    data = HTMLParser.HTMLParser().unescape(data_file.read()).replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    my_regex = '\s+[A-Z][a-z]{2},\s+\d{2}\s+Mar\s+2011\s+\d{2}:\d{2}:\d{2}\s+\+0000\s+[a-z]+\s+(\d+)'
    tweets_list = re.split(pattern=my_regex, string=data)
    tweet_file = codecs.open("tweet_per_line.txt", "a", "utf-8")
    for i in range(0, len(tweets_list), 2):
        if i + 1 >= len(tweets_list):
            break
        tweet_body = tweets_list[i].replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
        tweet_id = tweets_list[i + 1]
        tweet_file.write(tweet_body + "\t" + tweet_id + "\n")
    tweet_file.close()


def start_files_processing():
    files = os.listdir("/home/moustah/Downloads/first-week-run")
    for file_name in files:
        text_file_names = os.listdir("/home/moustah/Downloads/first-week-run" + "/" + str(file_name))
        for text_file_name in text_file_names:
            process_file("/home/moustah/Downloads/first-week-run" + "/" + str(file_name) + "/" + text_file_name, text_file_name)


if __name__ == '__main__':
    start_files_processing()
