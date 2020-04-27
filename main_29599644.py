# -----------------------------------------------------------------------------
# Name: Nisheeth Shah
# Id: 29599644
# Start Date: 20/05/2018
# Last Modified Date: 26/05/2018
# Assignment 3: Task 5: Putting all the classes together
# -----------------------------------------------------------------------------

# Importing library & classes from another files
from preprocessor_29599644 import Preprocessor
from character_29599644 import CharacterAnalyser
from word_29599644 import WordAnalyser
from visualiser_29599644 import AnalysisVisualiser
import pandas as pd
import sys


def read_input(author, name, path):
    """Function to read file and show IO exception error if any error while reading the file"""

    # Initialise the variable that will hold the content of token file
    book_content = ""

    # Try block for exception handling
    try:
        # With block to read the file
        with open(path, 'r') as f:
            book_content = f.read()

            # Show the file info
            print("Read file " + name + " by " + author)

        # Show error if file empty
        if not book_content:
            print("No data in file " + name)

    # Exception handling for IO error with appropriate message
    except IOError:
        print("Cannot open file:-", name, "from location:-", path, "by author:-", author)

    # Exception handling for runtime error with appropriate message
    except RuntimeError:  # handle other exceptions such as attribute errors
        print("Unexpected error has occurred for:-", name, "from location:-", path, "by author:-", author)

    # Return the file content variable
    return book_content


def main():
    """The Main function of the program"""

    # Read all the six files stored in 'Dataset' folder
    marlowe_edward = read_input("Marlowe", "Edward II", "Dataset\Edward_II_Marlowe.tok")
    marlowe_jew = read_input("Marlowe", "The Jew of Malta", "Dataset\Jew_of_Malta_Marlowe.tok")
    shakespeare_richard = read_input("Shakespeare", "Richard II", "Dataset\Edward_II_Marlowe.tok")
    shakespeare_hamlet = read_input("Shakespeare", "Hamlet", "Dataset\Hamlet_Shakespeare.tok")
    shakespeare_henry_part_1 = read_input("Shakespeare", "Henry VI Part 1", "Dataset\Henry_VI_Part1_Shakespeare.tok")
    shakespeare_henry_part_2 = read_input("Shakespeare", "Henry VI Part 2", "Dataset\Henry_VI_Part2_Shakespeare.tok")

    # ----------------------------------------------------------------------
    # Token 1
    # ----------------------------------------------------------------------

    # Preprocessor object
    preprocessor_obj = Preprocessor()
    # Feed string in the tokenise function
    preprocessor_obj.tokenise(marlowe_edward)
    # Get the tokenised list using the function
    tokenised_list = preprocessor_obj.get_tokenised_list()
    # Print the token list in appropriate format
    print(tokenised_list)

    # Character Analyser object
    character_analyser_obj = CharacterAnalyser()
    # Feed string in the analyse words function
    character_analyser_obj.analyse_characters(tokenised_list)
    # Provide with punctuation frequency count.
    punctuation_freq = character_analyser_obj.get_punctuation_frequency()
    # print the character and punctuation frequency.
    print("\nCharacterAnalyser:\n", character_analyser_obj)
    print("\nget_punctuation_frequency:\n", punctuation_freq[['character', 'occurrence']])

    # word Analyser object
    word_analyser_obj = WordAnalyser()
    # Feed string in the analyse words function
    word_analyser_obj.analyse_words(tokenised_list)
    # Get stop word frequency count.
    sw_freq = word_analyser_obj.get_stopword_frequency()
    word_length_freq = word_analyser_obj.get_word_length_frequency()
    # print the word, stopword and word_length frequency.
    print("\nWordAnalyser:\n", word_analyser_obj)
    print("\nget_stopword_frequency:\n", sw_freq[['word', 'occurrence']])
    print("\nget_word_length_frequency:\n", word_length_freq)

    get_char_df = character_analyser_obj.get_df()

    df_list = [get_char_df, sw_freq, word_length_freq]

    # Created the analysis_visualiser object to call the function and perform the analysis.
    analysis_visualiser_obj = AnalysisVisualiser(df_list)
    analysis_visualiser_obj.visualise_character_frequency()
    analysis_visualiser_obj.visualise_punctuation_frequency()
    analysis_visualiser_obj.visualise_word_length_frequency()

    # ----------------------------------------------------------------------
    # Token 2
    # ----------------------------------------------------------------------

    # Same as token 1
    preprocessor_obj = Preprocessor()
    preprocessor_obj.tokenise(marlowe_jew)
    tokenised_list = preprocessor_obj.get_tokenised_list()
    print(tokenised_list)

    character_analyser_obj = CharacterAnalyser()
    # print(character_analyser_obj)
    character_analyser_obj.analyse_characters(tokenised_list)
    punctuation_freq = character_analyser_obj.get_punctuation_frequency()
    print("\nCharacterAnalyser:\n", character_analyser_obj)
    print("\nget_punctuation_frequency:\n", punctuation_freq[['character', 'occurrence']])

    word_analyser_obj = WordAnalyser()
    word_analyser_obj.analyse_words(tokenised_list)
    sw_freq = word_analyser_obj.get_stopword_frequency()
    word_length_freq = word_analyser_obj.get_word_length_frequency()
    print("\nWordAnalyser:\n", word_analyser_obj)
    print("\nget_stopword_frequency:\n", sw_freq[['word', 'occurrence']])
    print("\nget_word_length_frequency:\n", word_length_freq)

    get_char_df = character_analyser_obj.get_df()

    df_list = [get_char_df, sw_freq, word_length_freq]

    analysis_visualiser_obj = AnalysisVisualiser(df_list)
    analysis_visualiser_obj.visualise_character_frequency()
    analysis_visualiser_obj.visualise_punctuation_frequency()
    analysis_visualiser_obj.visualise_word_length_frequency()

    # ----------------------------------------------------------------------
    # Token 3
    # ----------------------------------------------------------------------

    # Same as token 1
    preprocessor_obj = Preprocessor()
    preprocessor_obj.tokenise(shakespeare_richard)
    tokenised_list = preprocessor_obj.get_tokenised_list()
    print(tokenised_list)

    character_analyser_obj = CharacterAnalyser()
    # print(character_analyser_obj)
    character_analyser_obj.analyse_characters(tokenised_list)
    punctuation_freq = character_analyser_obj.get_punctuation_frequency()
    print("\nCharacterAnalyser:\n", character_analyser_obj)
    print("\nget_punctuation_frequency:\n", punctuation_freq[['character', 'occurrence']])

    word_analyser_obj = WordAnalyser()
    word_analyser_obj.analyse_words(tokenised_list)
    sw_freq = word_analyser_obj.get_stopword_frequency()
    word_length_freq = word_analyser_obj.get_word_length_frequency()
    print("\nWordAnalyser:\n", word_analyser_obj)
    print("\nget_stopword_frequency:\n", sw_freq[['word', 'occurrence']])
    print("\nget_word_length_frequency:\n", word_length_freq)

    get_char_df = character_analyser_obj.get_df()

    df_list = [get_char_df, sw_freq, word_length_freq]

    analysis_visualiser_obj = AnalysisVisualiser(df_list)
    analysis_visualiser_obj.visualise_character_frequency()
    analysis_visualiser_obj.visualise_punctuation_frequency()
    analysis_visualiser_obj.visualise_word_length_frequency()

    # ----------------------------------------------------------------------
    # Token 4
    # ----------------------------------------------------------------------

    # Same as token 1
    preprocessor_obj = Preprocessor()
    preprocessor_obj.tokenise(shakespeare_hamlet)
    tokenised_list = preprocessor_obj.get_tokenised_list()
    print(tokenised_list)

    character_analyser_obj = CharacterAnalyser()
    character_analyser_obj.analyse_characters(tokenised_list)
    punctuation_freq = character_analyser_obj.get_punctuation_frequency()
    print("\nCharacterAnalyser:\n", character_analyser_obj)
    print("\nget_punctuation_frequency:\n", punctuation_freq[['character', 'occurrence']])

    word_analyser_obj = WordAnalyser()
    word_analyser_obj.analyse_words(tokenised_list)
    sw_freq = word_analyser_obj.get_stopword_frequency()
    word_length_freq = word_analyser_obj.get_word_length_frequency()
    print("\nWordAnalyser:\n", word_analyser_obj)
    print("\nget_stopword_frequency:\n", sw_freq[['word', 'occurrence']])
    print("\nget_word_length_frequency:\n", word_length_freq)

    get_char_df = character_analyser_obj.get_df()

    df_list = [get_char_df, sw_freq, word_length_freq]

    analysis_visualiser_obj = AnalysisVisualiser(df_list)
    analysis_visualiser_obj.visualise_character_frequency()
    analysis_visualiser_obj.visualise_punctuation_frequency()
    analysis_visualiser_obj.visualise_word_length_frequency()

    # ----------------------------------------------------------------------
    # Token 5
    # ----------------------------------------------------------------------

    # Same as token 1
    preprocessor_obj = Preprocessor()
    preprocessor_obj.tokenise(shakespeare_henry_part_1)
    tokenised_list = preprocessor_obj.get_tokenised_list()
    print(tokenised_list)

    character_analyser_obj = CharacterAnalyser()
    # print(character_analyser_obj)
    character_analyser_obj.analyse_characters(tokenised_list)
    punctuation_freq = character_analyser_obj.get_punctuation_frequency()
    print("\nCharacterAnalyser:\n", character_analyser_obj)
    print("\nget_punctuation_frequency:\n", punctuation_freq[['character', 'occurrence']])

    word_analyser_obj = WordAnalyser()
    word_analyser_obj.analyse_words(tokenised_list)
    sw_freq = word_analyser_obj.get_stopword_frequency()
    word_length_freq = word_analyser_obj.get_word_length_frequency()
    print("\nWordAnalyser:\n", word_analyser_obj)
    print("\nget_stopword_frequency:\n", sw_freq[['word', 'occurrence']])
    print("\nget_word_length_frequency:\n", word_length_freq)

    get_char_df = character_analyser_obj.get_df()

    df_list = [get_char_df, sw_freq, word_length_freq]

    analysis_visualiser_obj = AnalysisVisualiser(df_list)
    analysis_visualiser_obj.visualise_character_frequency()
    analysis_visualiser_obj.visualise_punctuation_frequency()
    analysis_visualiser_obj.visualise_word_length_frequency()

    # ----------------------------------------------------------------------
    # Token 6
    # ----------------------------------------------------------------------

    # Same as token 1
    preprocessor_obj = Preprocessor()
    preprocessor_obj.tokenise(shakespeare_henry_part_2)
    tokenised_list = preprocessor_obj.get_tokenised_list()
    print(tokenised_list)

    character_analyser_obj = CharacterAnalyser()
    # print(character_analyser_obj)
    character_analyser_obj.analyse_characters(tokenised_list)
    punctuation_freq = character_analyser_obj.get_punctuation_frequency()
    print("\nCharacterAnalyser:\n", character_analyser_obj)
    print("\nget_punctuation_frequency:\n", punctuation_freq[['character', 'occurrence']])

    word_analyser_obj = WordAnalyser()
    word_analyser_obj.analyse_words(tokenised_list)
    sw_freq = word_analyser_obj.get_stopword_frequency()
    word_length_freq = word_analyser_obj.get_word_length_frequency()
    print("\nWordAnalyser:\n", word_analyser_obj)
    print("\nget_stopword_frequency:\n", sw_freq[['word', 'occurrence']])
    print("\nget_word_length_frequency:\n", word_length_freq)

    get_char_df = character_analyser_obj.get_df()

    df_list = [get_char_df, sw_freq, word_length_freq]

    analysis_visualiser_obj = AnalysisVisualiser(df_list)
    analysis_visualiser_obj.visualise_character_frequency()
    analysis_visualiser_obj.visualise_punctuation_frequency()
    analysis_visualiser_obj.visualise_word_length_frequency()

    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------

# Get visualization plotted.
    plt = analysis_visualiser_obj.return_plot()
    plt.show()


# Define that main() is the main function of the program
if __name__ == "__main__":
    main()
