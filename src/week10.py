def find_longest_line(filename):
    longest_line_number = -1
    longest_line_length = -1
    counter = 1
    for line in open(filename):
        line = line.strip()
        line_length = len(line)
        if line_length > longest_line_length:
            longest_line_length = line_length
            longest_line_number = counter
        counter += 1
    return longest_line_number, longest_line_length
