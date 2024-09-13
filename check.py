import os
import csv
import logging




def list_files_in_directory(directory):
    file_paths = []  # This list will store all file paths

    for root, _, all_files in os.walk(directory):
        for each in all_files:
            file_path = os.path.join(root, each)
            file_paths.append(file_path)

    return file_paths


def count_columns_in_csv(file_path):
    counts = []
    with open(file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row_number, row in enumerate(csv_reader, start=1):
            num_columns = len(row)
            # print(f"Line {row_number}: {num_columns} columns")
            counts.append(num_columns)
    counts = set(counts)
    try:
        counts.remove(0)
        counts.remove(1)
    except Exception as e:
        logging.info(f"An error occurred while reading the file {file_path}: {e}")

    if counts.__len__() > 1:
        return False
    else:
        logging.info(f"The number of column doesn't equal")
        return True


def check_directory(path):
    red_flag_list = []
    for file in list_files_in_directory(path):
        if count_columns_in_csv(file):
            pass
        else:
            red_flag_list.append(file)
    for each in red_flag_list:
        with open(path + '/report.txt', 'a') as file:
            file.write('\n' + each)
    return red_flag_list


if __name__ == '__main__':
    TEST_DIRECTORY = 'output'
    check_directory(TEST_DIRECTORY)
