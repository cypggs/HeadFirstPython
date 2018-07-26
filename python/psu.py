import psutil
def println(str):
    print str
    print

    
println(psutil.cpu_times())
println(psutil.cpu_times().user)

mem = psutil.virtual_memory()
println(mem)
println(mem.total)

partitions = psutil.disk_partitions()
println(partitions)
println(partitions[1])
println(psutil.disk_usage('/'))


println(psutil.net_io_counters())
println(psutil.net_io_counters(pernic=True))


println(psutil.users())
println(psutil.boot_time())

ps = psutil.pids()
println(ps)
p = psutil.Process(1)
println(p.name())
println(p.exe())
println(p.status())
println(p.memory_percent())

#https://pypi.python.org/pypi/psutil

