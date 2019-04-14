"""
SleepWeb
Projeto desenvolvido para o Programa de Pós-Graduação em Computação Aplicada
Universidade de Passo Fundo - 2018/2019

@author Matheus Hernandes
@since 13/04/2019
"""
import asyncio
from service.readfile import ReadFileService


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ReadFileService().run())
    loop.run_until_complete(ReadFileService().save())
    loop.close()
