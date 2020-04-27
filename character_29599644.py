# -----------------------------------------------------------------------------
# Name: Nisheeth Shah
# Id: 29599644
# Start Date: 22/05/2018
# Last Modified Date: 23/05/2018
# Assignment 3: Task 2: Building a class for analysing characters
# -----------------------------------------------------------------------------

# Importing library
import pandas as pd


class CharacterAnalyser:

    def __init__(self):
        """Constructor to define a dataframe to store the frequency of the characters"""
        ascii_counter = 47
        char_list = []
        is_punc = []
        while ascii_counter <= 122:
            if (48 <= ascii_counter <= 57) or (65 <= ascii_counter <= 90) or (97 <= ascii_counter <= 122):
                char_list.append(chr(ascii_counter))
                is_punc.append(0)
            ascii_counter += 1

        # only defined for the punctuation.
        ascii_counter = 33
        while ascii_counter <= 122:
            if (33 <= ascii_counter <= 47) or \
                    (58 <= ascii_counter <= 64) or \
                    (91 <= ascii_counter <= 96) or \
                    (123 <= ascii_counter <= 126):
                char_list.append(chr(ascii_counter))
                is_punc.append(1)
            ascii_counter += 1

        # creating the dataframe for counting the frequency occurrence of the characters.
        self.pd_char_df = pd.DataFrame(columns=['character', 'occurrence', 'is_punctuation'])
        self.pd_char_df['is_punctuation'] = is_punc
        self.pd_char_df['character'] = char_list
        self.pd_char_df['occurrence'] = 0

    def __str__(self):
        """method to present the number of occurrences for each characters in a readable format"""
        return "\nOccurrence of characters" + str(self.pd_char_df[['character', 'occurrence']])

    def analyse_characters(self, tokenised_list):
        """This function is made to count the frequency occurreneces of each and every character in the input tokenize list"""
        for each_word in tokenised_list:
            # Iterate each line of each_word
            for each_char in each_word:
                char_list = self.pd_char_df['character'].tolist()
                if each_char in char_list:
                    index = char_list.index(each_char)
                    # occurrence_count = int(self.pd_char_df.iloc[index, 'occurrence'])
                    self.pd_char_df.ix[index, 'occurrence'] += 1

    def get_punctuation_frequency(self):
        """This function is made to count the frequency occurreneces of punctuation in the input tokenize list"""
        return self.pd_char_df.ix[self.pd_char_df['is_punctuation'] == 1]

    def get_df(self):
        """This is defined in order to return pd_char"""
        return self.pd_char_df
