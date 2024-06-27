def read_in_file(input_file, output_file):
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        for line_num, line in enumerate(in_file, start=1):
            out_file.write(f'{line_num}: {line}')


inputfile = 'text.txt'
outputfile = 'output.txt'

read_in_file(inputfile, outputfile)
