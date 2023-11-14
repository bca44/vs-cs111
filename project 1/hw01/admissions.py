def read_header_and_lines(filename):
    with open(filename) as file:
        header = file.readline()
        lines = file.readlines()
    return header, lines


def convert_row_type(a_list):
    # converts each element in a_list to float
    new_list = []
    for element in a_list:
        new_list.append(float(element))
    return new_list


def check_row_types(row):
    # Provided code
    # This function checks to ensure that a list is of length
    # 8 and that each element is type float
    # Parameters:
    # row - a list to check
    # Returns True if the length of row is 8 and all elements are floats
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True


def calculate_score(a_list):
    return ((a_list[0]/160) * 0.3) + ((a_list[1] * 2) * 0.4) + (a_list[2] * 0.1) + (a_list[3] * 0.2)


def write_lines(filename, content):
    with open(filename, "w") as file:
        file.writelines(content)


def is_outlier(scores):
    # takes one line at a time
    # returns True (i.e., student is outlier) if:
    # demonstrated interest score == 0
    if scores[2] == 0:
        return True
    # OR if normalized GPA is more than two points higher than normalized SAT score
    elif ((scores[1] * 2) - (scores[0]/160)) > 2:
        return True
    return False


def calculate_score_improved(scores):
    # returns True if:
    # score >= 6
    if calculate_score(scores) >= 6:
        return True
    # OR IF is_outlier()
    elif is_outlier(scores):
        return True
    return False


def grade_outlier(grades):
    # returns True if one single number is more than 20 points lower than all other numbers
    sorted_list = sorted(grades, reverse=True)
    if sorted_list[-2] - sorted_list[-1] > 20:
        return True
    return False


def grade_improvement(grades):
    # takes in list of grades
    # returns True if average score of each semester is higher than or equal to the previous
    for index in range(1, len(grades)):
        if grades[index] < grades[index - 1]:
            return False
    return True


def main():
    filename = "superheroes_tiny.csv"
    print("Processing " + filename + "...")

    # 1.1 - read in data
    header, lines = read_header_and_lines(filename)
    name_list = [line.split(",")[0] for line in lines]
    string_num_list = [line.split(",")[1:] for line in lines]

    # 1.2 - convert num elements to float
    num_list = [convert_row_type(line) for line in string_num_list]

    # 1.3 - check row type - make sure length and type are correct
    [check_row_types(line) for line in num_list]

    # 1.4 - split num_list into scores and grades lists
    scores = [line[0:4] for line in num_list]
    grades = [line[4:] for line in num_list]

    # 2.1 - create calculate_score()
    # 2.2 - write student's id and calculated score to "student_scores"
    name_score = [f"{name_list[index].strip()},{calculate_score(scores[index]):.2f}\n" for index in range(len(name_list))]
    write_lines("student_scores.csv", name_score)

    # 2.3 - write name to "chosen_students.txt" if score >= 6
    chosen_students_list = [f"{line.split(',')[0]}\n" for line in name_score if float(line.split(",")[1]) >= 6]
    write_lines("chosen_students.txt", chosen_students_list)

    # 3.1 - create is_outlier()
    # 3.2 - use is_outlier() to make outliers_list, add only names of outlier students
    outliers_list = [f"{name_list[index].strip()}\n" for index in range(len(name_list)) if is_outlier(scores[index])]
    write_lines("outliers.txt", outliers_list)

    # 3.3 - write names to "chosen_improved.txt"
    # if score >= 6 OR score >= 5 AND is_outlier()
    chosen_improved_list = [f"{name_score[index].split(',')[0]}\n" for index in range(len(name_list))
                            if float(name_score[index].split(',')[1]) >= 6 or (float(name_score[index].split(',')[1]) >= 5 and is_outlier(scores[index]))]
    write_lines("chosen_improved.txt", chosen_improved_list)

    # 4.1 -  create calculate_score_improved()
    # 4.2 - write to improved_chosen.txt, using calculate_score_improved()
    with open("improved_chosen.csv", "w") as file:
        for index in range(len(name_list)):
            if calculate_score_improved(scores[index]):
                file.write(f"{name_list[index]},{','.join([f'{score}' for score in scores[index]])}\n")

    # 5.1 - create grade_outlier()
    # 5.2 - create grade_improvement()
    # 5.3 - write extra_improved_chosen list with the following conditions:
        # score >= 6
        # or score >= 5 AND (is_outlier() OR grade_outlier() OR grade_improvement)
    extra_improved_chosen_list = [f"{name_list[index].strip()}\n" for index in range(len(name_list))
                                  if calculate_score(scores[index]) >= 6
                                  or calculate_score(scores[index]) >= 5 and (is_outlier(scores[index]) or grade_outlier(grades[index]) or grade_improvement(grades[index]))]
    write_lines("extra_improved_chosen.txt", extra_improved_chosen_list)

    print("done!")


if __name__ == "__main__":
    # this bit allows us to both run the file as a program or load it as a
    # module to just access the functions
    main()
