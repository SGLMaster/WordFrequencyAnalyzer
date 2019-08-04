# WordFrequencyAnalyzer
Count the number of appearances of a word and its inflected forms in a text.

This is a simple CLI script that allows you to count the number of times a word appears inside a given file text.
Furthermore, it also has the ability to count the apperances of its inflected forms.

Command line options:
-f Input filename in which the world will be searched.
-o Output filename where the results of the analysis will be dumped.
-w Appends one word to the search list for the count.
-i Enables the program to also count apperances for the "-ing" inflected form of the given words.
-s Enables the program to also count apperances for the "-s" or "-es" inflected form of the given words.
-p Enables the program to also count apperances for the "-ed" or "-d" inflected form of the given words.
-e Enables the program to also count apperances for the "-er" or "-r" inflected form of the given words.

## Example:

Suppose you want to count how many times the word "wait" appears in a plain text file called "file.txt".
Also, you want to know the number of apperances for its present inflected forms "waiting" and "waits". 
Finally, you would like to get the results written in another text file called "results.txt".

All you need to do is run this inside the root program folder:

python main.py -f "file.txt" -o "results.txt" -w "wait" -i -s

That would generate a results file with the following format:

 wait:2
+waiting:1
+waits:3
----------------------------------------------------------------
 Total:6
