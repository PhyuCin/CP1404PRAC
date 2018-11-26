"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    subjects = scores_data[0].strip().split(",")
    score_values = []
    scores_subject = []

    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    for i in range(len(subjects)):
        print(subjects[i], "Scores:")
        scores_subject.append([])

        for n in range(len(scores_data) - 1):
            # - 1 because of 1st line
            print(score_values[n][i])
            scores_subject[i].append(score_values[n][i])
        print("Max:", max(scores_subject[i]))
        print("Min:", min(scores_subject[i]))
        print("Avg: {:.2f}".format(sum(scores_subject[i])/(len(scores_data)-1)))
        #print(sum(scores_subject[i]))
    #print(scores_subject)

main()