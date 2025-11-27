# big-data-ex2

Hadoop Training questions

Yuval Yarden - 318763455

Rom Eisenberg - 207811472



Exercise 1


Q1. How many files are there?

**A1. 6 files.**

Q2. Did number of mapper change?

**A2. No, still 9.** 

Q3. Did number of reducer changed?

**A3. Yes, from 3 to 6.**

Q4. Did number of output files change? Why?

**A4. Yes, from 3 to 6 because each reducer writes exactly one output file.**

Q5. What does the value of 'Merged Map outputs' represents and how is it calculated?

**A5. “Merged Map outputs” represent how many small pieces of data from the mappers get combined on the reducer side during the shuffle/sort step. In our case it’s number of mappers × number of reducers (9×3=27, 9×6=54).**


Exercise 2


Q1. Is your change in the mapper or in the reducer?

**A1. The change is in the mapper.**
**We want to clean each word before we count it (remove commas/dots at the end and convert to lowercase), so the mapper should output the normalized word. The reducer just adds numbers and doesn’t need to change.**

Q2. Please submit your code in GitHub


Exercise 3


Q1. Is your change in the mapper or in the reducer?

**A1. The change is in the reducer.
The mapper still just sends (word, 1) for every word like before. In this exercise we only want the 3 most frequent words, and we only know the final counts in the reducer, so the top3 logic has to be done there.**

Q2. Please submit your code in GitHub

Q3. Print the output of the MapReduce and add to the project.

Note: you should not use external pipes, sort, or filters. All should be done inside the
mapReduce Python code
I want to see in the screenshot that includes the command you typed:
$ > hadoop fs -ls /user/hduser/gutenberg-output

**A3.** <img width="893" height="95" alt="image" src="https://github.com/user-attachments/assets/9a54b0e7-1958-436c-899a-b56c528b1068" />

