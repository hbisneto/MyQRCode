import os
import pyqrcode
import png
from pyqrcode import QRCode
from datetime import date

AnoAtual = date.today().year
SoftwareName = "MyQRCode"
Version = "1.0"
CopyrightName = "Heitor Bisneto."
SystemLocation = os.getcwd()
QRFolder = SystemLocation + '/QR Base/'

MyURL = []

print("="*80)
print(f'[{SoftwareName}] - Em Execução...')
print("="*80)
print("Nome:", SoftwareName)
print("Versão:", Version)
print("Criado por:", CopyrightName)

if AnoAtual == 2021:
    print("Copyright ©", AnoAtual, "|", CopyrightName, "All rights reserved.")
else:
    print("Copyright © 2021 -", AnoAtual, "|", CopyrightName, "All rights reserved.")
print()

class cd:
    def __init__(Self, NewPath):
        Self.NewPath = os.path.expanduser(NewPath)

    def __enter__(Self):
        Self.SavedPath = os.getcwd()
        os.chdir(Self.NewPath)

    def __exit__(Self, Etype, Value, Traceback):
        os.chdir(Self.SavedPath)

def SystemCheck():
    try:
        print("="*80)
        print(f'>> Verificação de arquivos do sistema {SoftwareName} <<')
        print("="*80)
        print(f'>> Verificando pasta: "{QRFolder}"...')
        os.mkdir(QRFolder)
        print(f'>> Pasta "{QRFolder}" criada')
    except OSError:
        print()

def App():
    SystemCheck()
    print("="*80)
    print(f'>> [{SoftwareName}] - Menu <<')
    print("="*80)
    print(f'>> 1. http://')
    print(f'>> 2. https://')
    print("="*80)
    Protocolo = int(input(">> Escolha o tipo de protocolo: "))

    if Protocolo == 1:
        MyURL.append("http://")
        Endereco = str(input(f'>> Digite o endereço (Sem {MyURL[Protocolo-1]}): '))
        MyURL.append(Endereco)
    elif Protocolo == 2:
        MyURL.append("https://")
        Endereco = str(input(f'>> Digite o endereço (Sem {MyURL[Protocolo-2]}): '))
        MyURL.append(Endereco)
    else:
        print(f'>> Escolha não disponível')

    FullURL = MyURL[0]+MyURL[1]

    print("="*80)
    print(f'>> [{SoftwareName}] - A URL está correta? <<')
    print("="*80)
    print(f'>> URL Digitada: {FullURL}')
    print("="*80)
    print(f'>> 1. SIM <<')
    print(f'>> 2. Não')
    Confirm = int(input(">> Digite a opção desejada: "))

    if Confirm == 1:
        Nome = str(input(">> Digite um nome para o arquivo: "))
        Extensao = '.png'
        Escala = int(input(">> Digite o valor da escala do arquivo [1-100]: "))
        with cd(QRFolder):
            Processo = pyqrcode.create(FullURL)
            Processo.png(f'{Nome}{Extensao}', scale = Escala)
    else:
        print(">> Execute o programa novamente")

App()
