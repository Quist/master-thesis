import re
from tabulate import tabulate

class Result(object):
    pass

def write_latex_table(results, path):
    data = []

    for result in results:
        data.append([result.name, result.results[0].mean, result.results[1].mean, result.results[2].mean])

    latex_table = tabulate(data, headers=["Protocol","1 byte", "2500 bytes", "100 000 bytes"], tablefmt="latex")

    latex_file = open(path + "result.tex", 'w')
    latex_file.write(latex_table)


def parse_result(path):

    result = Result()
    with open(path) as f:
        content = f.readlines()

        if content[0] == 'timeout\n':
            pass
        else :
            result.n = re.findall("\d+", content[0])[0]
            result.mean = int(round(float(re.findall("\d+\.\d+", content[2])[0])))
            result.deviation = int(round(float(re.findall("\d+\.\d+", content[3])[0])))
            result.variance = int(round(float(re.findall("\d+\.\d+", content[4])[0])))
            result.min = int(round(float(re.findall("\d+\.\d+", content[5])[0])))
            result.max = int(round(float(re.findall("\d+\.\d+", content[6])[0])))
            result.median = int(round(float(re.findall("\d+\.\d+", content[7])[0])))
            result.size = int(round(float(re.findall("\d+", content[8])[0])))

    return result

def parse_protocol(path, printname, target):
    results = []
    results.append(parse_result(path +"1/%s.result"  %target))
    results.append(parse_result(path +"2500/%s.result" %target))
    results.append(parse_result(path +"100000/%s.result" % target))

    result = Result()
    result.name = printname
    result.results = results

    return result



def parse_size_results(path) :
    plotfile = open(path + "result.plot", 'w')
    plotfile.write("Protocol\t\t\"1 byte\"\t\"2500 bytes\"\t \"100000 bytes\"\n")

    results = []
    results.append(parse_protocol(path + "default/", "Default", "default"))
    results.append(parse_protocol(path + "http/", "HTTP", "http"))

    for result in results:
        plotdata = "%-16s %-12d %-16d%-8d\n" %(result.name, result.results[0].mean, result.results[1].mean, result.results[2].mean)
        plotfile.write(plotdata)

    write_latex_table(results)


parse_size_results("cnr/size/")
parse_size_results("function_tests/size/")
