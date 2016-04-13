import argparse

def write_header(outfile) :
    with open("./table_header.tex") as f:
         out = f.readlines()
         "".join(out)
         outfile.write("".join(out))

def write_line(line, outfile):
    splitted = line.split("\"")
    testname = splitted[1]
    testname = testname.replace("&", "\\&")

    results = splitted[2].split()

    outfile.write("%-32s" % testname)
    for result in results:
        outfile.write("& %-15s" % result)
    outfile.write("\\\\\n")


parser = argparse.ArgumentParser(description='Convert .dat file to latex table')
parser.add_argument('-o', metavar="outputfile",
                   help='output file', required='true')
parser.add_argument('input',
                   help='input file')
args = parser.parse_args()

input_file = args.input
output_file = args.o

outfile = open(output_file, 'w')

write_header(outfile)

with open(input_file) as f:
    content = f.readlines()
    for line in content[1:]:
        write_line(line, outfile)

outfile.write("\end{tabular}")
