# -----------------------------------------------------------------------------
# Name: Nisheeth Shah
# Id: 29599644
# Start Date: 26/05/2018
# Last Modified Date: 27/05/2018
# Assignment 3: Task 4: Building a class for visualising the analysis
# -----------------------------------------------------------------------------
import matplotlib.pyplot as plt


class AnalysisVisualiser:

    # Visualisation for all types of analysis

    def __init__(self, all_text_stats):
        self.all_text_stats = all_text_stats

    def visualise_character_frequency(self):
        df_type = self.all_text_stats[0]

        df_char = df_type.ix[df_type['is_punctuation'] == 0]
        df_char = df_char[['character', 'occurrence']]

        df_char.plot.bar(x='character', y='occurrence', rot=0)
        # plt.show()

    def visualise_punctuation_frequency(self):
        df_type = self.all_text_stats[0]

        df_char = df_type.ix[df_type['is_punctuation'] == 1]
        df_char = df_char[['character', 'occurrence']]

        df_char.plot.bar(x='character', y='occurrence', rot=0)
        # plt.show()

    def visualise_stopword_frequency(self):
        df_type = self.all_text_stats[1]

        df_char = df_type.ix[df_type['is_stop_word'] == 1]
        df_char = df_char[['word', 'occurrence']]

        df_char.plot.bar(x='word', y='occurrence', rot=0)
        # plt.show()

    def visualise_word_length_frequency(self):
        df_type = self.all_text_stats[2]

        # df_char = df_type.ix[df_type['is_stop_word'] == 1]
        # df_char = df_char[['word', 'occurrence']]

        df_type.plot.bar(x='length', y='total_frequency', rot=0)

    def return_plot(self):
        return plt
