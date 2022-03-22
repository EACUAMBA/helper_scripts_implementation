import os
import os.path as path
import pathlib
from zipfile import ZipFile
from datetime import date
import shutil

strData = date.today().strftime("%d-%m-%Y")
origen = pathlib.Path().resolve()
caminho = pathlib.Path().resolve()
destino = os.path.join(caminho, "arquivos_processados_aos_" + strData);
def moveArquivo(arquivo):
    shutil.move(arquivo, destino)

def comprimeArquivo(caminho):
    dirs = os.listdir(caminho)
    dirs = map(lambda v: os.path.join(caminho, v), dirs)
    for fileOrDir in dirs:
        if(path.isfile(fileOrDir) and fileOrDir.endswith(".exe") or fileOrDir.endswith(".msi")):
            print('Zipando o ficheiro:', fileOrDir)
            ziper = ZipFile((fileOrDir + "-" + strData + ".zip"), 'w')
            ziper.write(fileOrDir, path.basename(fileOrDir));
            ziper.close()
            moveArquivo(fileOrDir)
        if(path.isdir(fileOrDir) and str(fileOrDir).find("arquivos_processados_aos") == -1):
            print("\n*Directorio: ", fileOrDir)
            print(comprimeArquivo(fileOrDir)) 
    return "\n*Compressão dos arquivos do directorio \"" + str(caminho) + "\" finalizado.\n"
    
if(not os.path.exists(destino)):
    os.makedirs(destino)
    
comprimeArquivo(caminho)