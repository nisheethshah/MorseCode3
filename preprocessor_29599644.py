# -----------------------------------------------------------------------------
# Name: Nisheeth Shah
# Id: 29599644
# Start Date: 21/05/2018
# Last Modified Date: 22/05/2018
# Assignment 3: Task 1: Setting up the preprocessor
# -----------------------------------------------------------------------------


class Preprocessor:
    def __init__(self):
        """Constructor to define and initialise input toknize list"""
        self.individual_token_list = []

    def __str__(self):
        """method to present the number of occurrences for each of the tokens in a readable format"""
        return "Total number of tokens are: " + str(len(self.individual_token_list))

    def tokenise(self, input_sequence):
        """This function is made in order to preprocess the input tokenise list"""
        each_line_list = input_sequence.split("\n")
        # Iterate each line of line_list
        for each_line in each_line_list:
            each_char_list = each_line.split(" ")
            # Iterate each line of char_list
            for each_character in each_char_list:
                self.individual_token_list.append(each_character)
        self.individual_token_list = ' '.join(self.individual_token_list).split()

    def get_tokenised_list(self):
        """This function is returning the value"""
        return self.individual_token_list
