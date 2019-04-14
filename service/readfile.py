"""
SleepWeb
Projeto desenvolvido para o Programa de Pós-Graduação em Computação Aplicada
Universidade de Passo Fundo - 2018/2019

@author Matheus Hernandes
@since 13/04/2019
"""
from time import sleep


class ReadFileService:
    """
    Controller defined to read video files
    """
    async def run(self):
        print("input read")
        sleep(5)
        return self

    async def save(self):
        print("output write")
        return self

