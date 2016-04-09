import re
from tabulate import tabulate

class Result(object):
    pass


def write_latex_table(results, path):
    data = []

    for result in results:
        data.append([result.name, "%s ms" % result.mean, result.deviation, result.variance, result.n])

    latex_table = tabulate(data, headers=["Test","Mean", "Std. Deviation", "Variance", "Test runs"], tablefmt="latex")

    latex_file = open(path + "result.tex", 'w')
    latex_file.write(latex_table)

def parse_results(target, printName) :
    print("Parsing file: %s " % target)

    result = Result()

    with open("%s.result" % target) as f:
        result.name = printName

        content = f.readlines()
        if content[0] == 'timeout\n':
            print("Timeout")
            result.n = 1
            result.mean = "0"
            result.deviation = "-"
            result.variance = "-"
        else :
            result.n = re.findall("\d+", content[0])[0]
            result.mean = int(round(float(re.findall("\d+\.\d+", content[2])[0])))
            result.deviation = int(round(float(re.findall("\d+\.\d+", content[3])[0])))
            result.variance = int(round(float(re.findall("\d+\.\d+", content[4])[0])))

    return result

def parse_result_set(path):
    plotfile = open(path + "result.plot", 'w')
    plotfile.write("Protocol\t\t\t\"Without Compression\"\t\"With Compression\"\n")

    results = []

    result = parse_results(path + "default/default", "Without proxy")
    plotdata = "%-16s %-24d%-8d\n" %("\"Without Proxy\"", result.mean, 0)
    plotfile.write(plotdata);
    results.append(result)

    result = parse_results(path + "http/http", "Proxy with HTTP")
    result_compressed = parse_results(path + "http/http_compression", "Proxy with HTTP & GZIP")
    plotdata = "%-16s %-24d%-8d\n" %("\"HTTP Proxy\"", result.mean, result_compressed.mean)
    plotfile.write(plotdata);
    results.append(result)
    results.append(result_compressed)

    result = parse_results(path + "amqp/amqp", "Proxy with AMQP")
    result_compressed = parse_results(path + "amqp/amqp_compression", "Proxy with AMQP & GZIP")
    plotdata = "%-16s %-24s%-8d\n" %("\"AMQP Proxy\"", result.mean, result_compressed.mean)
    plotfile.write(plotdata);
    results.append(result)
    results.append(result_compressed)

    result = parse_results(path + "coap/coap", "Proxy with CoAP")
    result_compressed = parse_results(path + "coap/coap_compression", "Proxy with CoAP & GZIP")
    plotdata = "%-16s %-24s%-8s\n" %("\"CoAP Proxy\"", result.mean, result_compressed.mean)
    plotfile.write(plotdata);
    results.append(result)
    results.append(result_compressed)

    write_latex_table(results, path)

parse_result_set("function_tests/rest/")
parse_result_set("satellite/rest/")
parse_result_set("satellite/nffi/")
parse_result_set("los/rest/")
parse_result_set("wifi1/rest/")
parse_result_set("wifi2/rest/")
parse_result_set("wifi2/nffi/")
parse_result_set("cnr/rest/")
parse_result_set("cnr/nffi/")
parse_result_set("edge/nffi/")
parse_result_set("edge/rest/")
