def print_lines_in_file(inputfile, outputfile):
    with open(inputfile, 'r', encoding='utf-8') as input, open(outputfile, 'w', encoding='utf-8') as output:
        for line_num, content in enumerate(input, start=1):
            output.write(f"{line_num}: {content}")

inp = 'text.txt'
outp = 'output_last.txt'
print_lines_in_file(inp, outp)