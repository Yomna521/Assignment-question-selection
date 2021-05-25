# Assignment-question-selection
Imagine a pandemic situation that happened in the middle of a session and results in an immediate closure of offline education. In such a scenario universities have to come up with some solution so as to finish with the evaluation process of the current semester. They decided to end the semester not by giving grades based on marks, instead proposed to just declare if a student has passed the subject or not.<br>
The process they adopted is as detailed here. As its mid of the running semester each subject has already finished with a few of the sessional components comprising of some marks out of the maximum marks in that subject. In addition, the maximum marks that can be scored in a subject may vary from one subject to another. Therefore, each subject has to decide the minimum marks, say MINMARKS, which should be greater than the total marks of the sessional components that are completed by now in offline mode for the subject. Every student has to score at least MINMARKS to pass that subject. Once decided, for each subject, inform students about the MINMARKS and also declare the marks obtained in the sessional finished so far.<br>
One assignment per subject is given to students so that they can score the remaining marks. The pattern of the assignment remains same for all the subjects. An assignment consists of a set of questions and students are free to attempt as many questions as they want, i.e. all questions are not mandatory. Each assignment question has a maximum score and some number of sub-parts. The difficulty level of a question is based on the following criteria:<br>
•	More is the number of sub-parts easier is the question irrespective of the maximum score of that question.<br>
•	In case two or more questions have same number of sub-parts then difficulty level is decided via ratio of maximum score and number of sub-parts. Lesser is the ratio easier is the question.<br>
Knowing the assignment pattern and the fact that one just has to score MINMARKS, students decided to score only the remaining marks by selecting the easiest assignment questions. You have to help these students in this selection by proposing the strategy to be followed.<br>
## Input:
•	Line 1 contains three space separated integers MINMARKS, S, and N, i.e. minimum marks to pass the subject, total number of students, and total number of assignment questions, respectively.<br>
•	Line 2 contains S integers separated by space. These are the sessional marks of S students.<br>
•	Following NN lines contain space separated 2 integers, representing the maximum score and the number of sub-parts in a question.<br>
## Output:
•	There will be S lines in the output. The first number in each line, say x, represents the count of questions a student has to attempt to score at least MINMARKS. It is followed by space separated x integers, sorted in increasing order, representing the question numbers to be attempted.<br>
## Constraints
•	All values range in between 1 and 1000.
## Sample Input:
75 3 5<br>
15 50 35<br>
6 3<br>
11 1<br>
13 4<br>
27 1<br>
18 2<br>
## Sample Output:
5 1 2 3 4 5<br>
3 1 3 5<br>
4 1 2 3 5
## EXPLANATION:
MINMARKS = 75. There are 3 students and their sessional scores are 15, 50, and 35, respectively. There are 5 assignment questions: Q1 is of 6 marks and has 3 subparts; Q2 is of 11 marks and has 1 subparts; Q3 is of 13 marks and has 4 subparts; Q4 is of 27 marks and has 1 subparts; and Q5 is of 18 marks and has 2 subparts. Q3 is the easiest as it has maximum number of subparts, then comes Q1 followed by Q5. Q2 and Q4 has same number of sub-parts, so the ratio of maximum score and number of sub-parts is computed for each of the two questions. For Q2 ratio is 11/1 = 11 and for Q4 ratio is 27/1 = 27. 11 < 27 therefore Q2 is easier than Q4.<br>
Score of first student is 15, so the selection goes like this. Select Q3, score becomes 15 + 13 = 28. Select Q1, score becomes 28 + 6 = 34. Select Q5, score becomes 34 + 18 = 52. Select Q2, score becomes 52 + 11 = 63. Select Q4, score becomes 63 + 27 = 90. Thus all the five questions are selected.<br>
Score of second student is 50, so the selection goes like this. Select Q3, score becomes 50 + 13 = 63. Select Q1, score becomes 63 + 6 = 69. Select Q5, score becomes 69 + 18 = 87. Thus only three questions are selected.<br>
Score of third student is 35, so the selection goes like this. Select Q3, score becomes 35 + 13 = 48. Select Q1, score becomes 48 + 6 = 54. Select Q5, score becomes 54 + 18 = 72. Select Q2, score becomes 72 + 11 = 83. Thus four questions are selected.<br>
