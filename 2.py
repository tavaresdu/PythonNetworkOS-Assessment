import subprocess
document = input('Digite o nome (com o caminho, se necessário) do arquivo de texto: ')
subprocess.Popen(['notepad', document])
