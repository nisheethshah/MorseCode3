# -----------------------------------------------------------------------------
# Name: Nisheeth Shah
# Id: 29599644
# Start Date: 23/05/2018
# Last Modified Date: 24/05/2018
# Assignment 3: Task 2: Building a class for analysing characters
# -----------------------------------------------------------------------------
# Importing library
import pandas as pd
from bs4 import BeautifulSoup
import requests


class WordAnalyser:
    def __init__(self):

        # Load HTML
        page = requests.get("http://www.lextek.com/manuals/onix/stopwords1.html")
        soup = BeautifulSoup(page.content, 'html.parser')
        sw = []
        # Pull stopwords from HTML
        for x in soup.find_all('pre'):
            sw.append(str(x))
        self.valid_stopwords = str(sw[0]).split("\n")
        self.valid_stopwords = self.valid_stopwords[self.valid_stopwords.index("a"):self.valid_stopwords.index("</pre>")]
        # Remove blanks
        self.valid_stopwords = ' '.join(self.valid_stopwords).split()

        # Create a dataframe and initialise it
        self.pd_word_df = pd.DataFrame(columns=['word', 'occurrence', 'is_stop_word', 'length'])
        for each_stopword in self.valid_stopwords:
            self.pd_word_df.loc[len(self.pd_word_df.index)] = [each_stopword.lower(), 0, 1, len(each_stopword)]

    def __str__(self):
        return "\nOccurrence of words are:\n" + str(self.pd_word_df[['word', 'occurrence']])

    def analyse_words(self, tokenised_list):
        for each_word in tokenised_list:
            if each_word.lower() in self.pd_word_df['word'].tolist():
                index = self.pd_word_df['word'].tolist().index(each_word.lower())
                self.pd_word_df.ix[index, 'occurrence'] += 1
            else:
                self.pd_word_df.loc[len(self.pd_word_df.index)] = [each_word.lower(), 1, 0, len(each_word)]

    def get_stopword_frequency(self):
        return self.pd_word_df.ix[self.pd_word_df['is_stop_word'] == 1]

    def get_word_length_frequency(self):
        word_length_frequency_df = pd.DataFrame(columns=['length', 'total_frequency'])

        for each_unique in self.pd_word_df.length.unique():
            unique_df = self.pd_word_df.ix[self.pd_word_df['length'] == each_unique]
            sum_of_freq = sum(unique_df['occurrence'].tolist())
            word_length_frequency_df.loc[len(word_length_frequency_df.index)] = [each_unique, sum_of_freq]

        return word_length_frequency_df

    def get_df(self):
        return self.pd_word_df
