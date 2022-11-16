import csv

file_name = "NASA_access_log_Jul95"

# Read lines from file into a list 'log'
with open(file_name, encoding="utf8") as f:
    log = list([line] for line in f)

# Give some information about what was read.
print(f"{len(log)} lines of logging were read.")
print(log[:10])

def extract_data(line: list[str]):
    """
    Helper method to split a single log file line into its parts
    """
    line_string = line[0].split(' - - [')
    who = line_string[0]
    line_string = line_string[1].split('/1995:')
    line_string = line_string[1].split(' -0400]')
    when = line_string[0]
    line_string = line_string[1].split('"')
    line_string = line_string[1].split(" ")
    what = line_string[1]
    return [who, when, what]

def print_line(line_data:list[str], col_width:list[int]):
    """
    Print a single line of log infos with 
    given column widths in table style .
    """
    print(f"| {line_data[0]:{col_width[0]}s}| {line_data[1]:{col_width[1]}s}| {line_data[2]:{col_width[2]}s}|")

def print_table(log_data:list[list[str]]):
    """
    Print multiple lines of log info
    as a pretty table with automatically
    calculated column widths.
    """
    col_width = [max(len(line[col]) for line in log_data) + 1 for col in range(3)]
    line_width = sum(col_width) + 7
    print("-" * line_width)
    print_line(["wer", "wann", "was"], col_width)
    print("-" * line_width)
    for line in log_data:
        print_line(line,col_width)
    print("-" * line_width)

#Extract the requested log infos
log_info = [extract_data(line) for line in log]

# Pretty print the first 10 lines of log info
print_table(log_info[:10])

# Write log info into a nice little .csv file.
with open("log_info.csv","w") as f:
    writer = csv.writer(f, delimiter=";",lineterminator='\n')
    writer.writerow(["wer", "wann", "was"])
    writer.writerows(log_info)