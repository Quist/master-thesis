import re
from tabulate import tabulate

class Result(object):
    pass

def write_latex_table(results, path):
    data = []

    for result in results:
        data.append([result.name, "%s ms" % result.results[0].mean, "%s ms" % result.results[1].mean, "%s ms" % result.results[2].mean])

    latex_table = tabulate(data, headers=["Protocol","1 byte", "2500 bytes", "100 000 bytes"], tablefmt="latex")

    print("Writing to file %s%s" %(path, "result.tex"))
    latex_file = open(path + "result.tex", 'w')
    latex_file.write(latex_table)


def parse_result(path):

    result = Result()
    with open(path) as f:
        content = f.readlines()

        if content[0] == 'timeout\n':
            result.mean = "-"
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
    print("Parsing path %s" % path)
    plotfile = open(path + "result.plot", 'w')
    plotfile.write("%-10s%-10s%-10s%-10s\n" % ("Bytes", "Default", "HTTP", "AMQP"))

    results = []
    results.append(parse_protocol(path + "default/", "Default", "default"))
    results.append(parse_protocol(path + "http/", "HTTP", "http"))
    results.append(parse_protocol(path + "amqp/", "AMQP", "amqp"))

    tests = ["1 Byte", "2500 Bytes", "100000 Bytes"]

    for i in range(0,3):
        plotdata = "%-16s %-12s %-16s%-8s\n" %( "\"%s\"" % tests[i], results[0].results[i].mean, results[1].results[i].mean, results[2].results[i].mean)
        plotfile.write(plotdata)

    write_latex_table(results, path)


parse_size_results("cnr/size/")
parse_size_results("edge/size/")
parse_size_results("function_tests/size/")
parse_size_results("los/size/")
parse_size_results("satellite/size/")
parse_size_results("wifi1/size/")
parse_size_results("wifi2/size/")
