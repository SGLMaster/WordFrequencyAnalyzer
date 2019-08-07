# Word Frequency Analyzer

**Count the number of appearances of a word and its inflected forms in a text file.**

Word Frequency Analizer is a program that allows you to count the number of times a word appears inside a given file text.
Furthermore, it also has the ability to count the apperances of its inflected forms with suffixes like "-ing" or "-s".
You can run this program as in CLI or GUI version using the main.py or main.pyw files respectively.

## Command line options (CLI Version)

-f Input filename in which the word will be searched.<br>
-o Output filename where the results of the analysis will be dumped (omit it to see the results in the console output).<br>
-w Appends one word to the search list for the count.<br>
-i Enables the program to count apperances for the "-ing" inflected form of the given words.<br>
-s Enables the program to count apperances for the "-s" or "-es" inflected form of the given words.<br>
-p Enables the program to count apperances for the "-ed" or "-d" inflected form of the given words.<br>
-e Enables the program to count apperances for the "-er" or "-r" inflected form of the given words.<br>

## CLI Example

Suppose you want to count how many times the word "wait" appears in a plain text file called "file.txt".
Also, you want to know the number of apperances for its present inflected forms "waiting" and "waits".
Finally, you would like to get the results written in another text file called "results.txt".

All you need to do is run this inside the root program folder:

```
python main.py -f "file.txt" -o "results.txt" -w "wait" -i -s
```

That would generate a results file with the count for each form of the word and the total count.
