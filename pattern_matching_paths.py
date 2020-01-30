from sys import argv, exit, stdin
import select
import matching_helper


def process_input():
    input = [line.rstrip() for line in stdin]
    if len(input) <= 1:
        print("NO DATA")
        exit(1)

    # if select.select([stdin],[],[],0.0)[0]:
    #     print("DATA")
    # else:
    #     print("NO DATA")

    # input = []
    # for line in stdin:
    #     # print(i)
    #     print(line)
    #     # if line
    
    num_patterns = int(input[0])
    num_paths = int(input[num_patterns + 1])

    if num_patterns == 0 or num_paths == 0:
        print("NO MATCHES")
        exit(1)

    patterns = input[1:num_patterns+1]
    paths = input[num_patterns+2:]

    return patterns, paths


def main():
    
    # check if an input file is piped into terminal command
    if stdin.isatty():
        print("NO INPUT")
        exit(1)

    patterns, paths = process_input()

    matching_patterns = matching_helper.get_matching_patterns(patterns, paths)

    for m in matching_patterns:
        print(m)

    exit()

if __name__ == "__main__":
    main()