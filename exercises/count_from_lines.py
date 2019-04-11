import re


def main():
    file_name = input("Enter file name: ")

    if len(file_name) < 1:
        file_name = "mbox_short.txt"

    file = open(file_name)
    words = words_in_file(file)
    file.close()

    print("There were", len(words), "lines in the file with From as the first word.")


def words_in_file(file):
    result = []
    for line in file:
        if re.search('^From ', line):
            words = line.split()
            result.append(words[1])

    return result


if __name__ == "__main__":
    main()
