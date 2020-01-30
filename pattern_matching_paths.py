from sys import argv, exit, stdin
import matching_helper


def process_input():
    input = [line.rstrip() for line in stdin]
    
    # check if input file has any data and exit if it is empty
    if len(input) <= 1:
        print("NO MATCH")
        exit(1)
    
    num_patterns = int(input[0])
    num_paths = int(input[num_patterns + 1])

    if num_patterns == 0 or num_paths == 0:
        print("NO MATCH")
        exit(1)

    patterns = input[1:num_patterns+1]
    paths = input[num_patterns+2:]

    return patterns, paths


def main():
    
    # check if an input file is piped into terminal command
    if stdin.isatty():
        print("NO MATCH")
        exit(1)

    patterns, paths = process_input()

    matching_patterns = matching_helper.get_matching_patterns(patterns, paths)

    for m in matching_patterns:
        print(m)

    exit()

if __name__ == "__main__":
    main()