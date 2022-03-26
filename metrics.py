import sys
import psutil
import os

def cpu():
    print("CPU")
    print("---")
    print("\n")
    print("cores")
    print("-")
    number_of_cores = os.cpu_count()
    print(number_of_cores)
    print("-")
    print("\n")
    print("load average")
    print("------------")
    load1, load5, load15 = os.getloadavg()
    print("  1   5   15")
    print("---- ---- ----")
    print(f"{load1}  {load5} {load15}")
    print("\n")
    print("times")
    times = psutil.cpu_times()
    print(" user   nice  system    idle   iowait  irq   softirq  steal  guest guest_nice")
    print("-- ------ ------ --------- ------ ------- ----- --------- ----- ----- ------------")

    for c in range(number_of_cores):
            values = str(c) + "   "
            for t in times:
                    values += str(t) + "   "
            values += "\n"
            print(values)
            values = ""

    print("\n")
    print("utilization")
    print("-----------")
    utilization = psutil.cpu_percent(percpu=True)
    line = ""
    per_cpu_utilization = ""
    cpu_i = 0
    numbers = ""
    for u in utilization:
            numbers += "  " + str(cpu_i)
            line += "---- "
            per_cpu_utilization += str(u) + " "
            cpu_i += 1

    print(numbers)
    print(line)
    print(u)


def mem():
    print("MEMORY")
    print("------")
    print("\n")
    print("virtual memory")
    print("--------------")
    print("---------  ----------")
    mem = psutil.virtual_memory()
    variables = ['total', 'available', 'percent', 'used', 'free', 'active', 'inactive', 'buffers', 'cached', 'shared', 'slab']
    v = 0
    for m in mem:
            print(f"{variables[v]}     {m}")
            v += 1
    print("---------  ----------")
    print("\n")
    print("swap")
    print("-------  ----------")
    swap_mem = psutil.swap_memory()
    variables = ['total', 'used', 'free', 'percent', 'sin', 'sout']
    v = 0
    for sm in swap_mem:
            print(f"{variables[v]}      {sm}")
            v += 1
    print("-------  ----------")


def main(argument):
    if argument == "cpu":
            cpu()
    elif argument == "mem":
            mem()
    else:
            print("input is wrong")

if __name__ == "__main__":
    main(sys.argv[1])