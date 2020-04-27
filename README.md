Introduction
	
In this assignment, we implement a simple stylometric analyser to investigate the linguistic behaviours of both authors. The analyser is able to perform basic statistical analysis on a number of linguistic features and also present the analysis results using some form of visualisation. 
For the purpose of this assignment, six specific written works were selected from a public available corpus1 — two of which where the authorship was attributed to the specific author; and two other works which were known to be disputed between the two authors (but were attributed to Shakespeare). Table 1 presents the title of each work and the corresponding file name.
 

	This assignment has 5 tasks which defines different functionalities as described further in this document.
	This project is created using PyCharm IDE using Anaconda.
 
Flow of the main function:
-	Take 6 files input by reading the files.
-	Exceptional handling in reading the taken files – input/output and runtime errors.
-	Call individual classes – each class to perform analysis of characters, words, punctuations and stopwords.
-	Finally, visualise all the analytical using Mathplotlib. 

Run Manual
To run the program efficiently – 
	Should have all the token files in the dataset folder in the project folder.
	Just run the main file and the program will fetch and read all the token file.
	The program will find analytics from the files.
	And create visualization for all the files.
	The program will exit.
	

 
Sample Output
Character frequencies:
 
Punctuation frequencies
 
Word frequencies
 
Word length frequencies
 

Graphs
 
 
 
  
References

•	Stackoverflow.com. How to be using the dataframes. Referred from https://stackoverflow.com/questions/14196013/python-creating-dataframe-from-excel-data?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa (Accessed 23/03/2018)
•	CrazyCasta. Stackoverflow.com. Check string handling. Retrieved from https://stackoverflow.com/questions/12595051/check-if-string-handling-ways/12595533?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
•	Python Reference Manual. Function definitions. Referred ‘how to return data from dataframe’ from https://docs.python.org/2.0/ref/dataframes.html
•	Community♦ (Last edited May 23 '17 at 12:02), Stênio Elson. Stackoverflow.com. File error handling methods. Referred from https://stackoverflow.com/questions/8023306/different-types-file-exception-handling?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
•	Mathplotlib Reference Manual. Create visualisations using Mathplotlib from dataframes from https://docs.python.org/2.0/ref/dataframes.html
