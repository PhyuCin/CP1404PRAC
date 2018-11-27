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

    print("\nScores table")
    print("-" * 61)
    print("Student No.     ", end="")
    print("     ".join(subjects))
    print("-"*61)

    #for i in range(len(subjects)):
        #scores_subject.append([])
    for n in range(len(scores_data)-1):
            # - 1 because of 1st line
        print("{:>11}{:10}{:10}{:10}{:10}{:10}".format(n+1, score_values[n][0], score_values[n][1],
              score_values[n][2], score_values[n][3], score_values[n][4]))

    average = []
    for i in range(len(subjects)):
        scores_subject.append([])
        for n in range(len(scores_data) - 1):
            # - 1 because of 1st line
            scores_subject[i].append(score_values[n][i])
        average.append(sum(scores_subject[i])/(len(scores_data)-1))
    #print(average)
    print("-" * 61)

    print("       Max:{:10}{:10}{:10}{:10}{:10}".format(max(scores_subject[0]), max(scores_subject[1]),
          max(scores_subject[2]), max(scores_subject[3]), max(scores_subject[4])))
    print("       Min:{:10}{:10}{:10}{:10}{:10}".format(max(scores_subject[0]), max(scores_subject[1]),
          max(scores_subject[2]), max(scores_subject[3]), max(scores_subject[4])))
    print("       Avg:{:10.2f}{:10.2f}{:10.2f}{:10.2f}{:10.2f}".format(average[0], average[1], average[2],
          average[3], average[4]))
    print("-" * 61)

main()