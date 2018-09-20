import psutil
for p in psutil.process_iter():
    try:
        print('Nome='+p.name(), "|", 'CPU='+str(p.cpu_percent(interval=0.2))+'%', "|", 'Mem='+str(p.memory_percent())+'%')
    except psutil.NoSuchProcess:
        pass
