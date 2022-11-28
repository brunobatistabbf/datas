import process
from process import Process
import random

i = 0
p1 = Process("p1", "W", "P")
p2 = Process("p2", "W", "P")
process = (p1, p2)
buffer: bytearray()
Full = 0
Empty = 3
Mutex = 1

while (i < 10):
    processos = random.choice(process)
    if (processos.name == "p1"):
        print("Em Execução")
        processos.state = "E"

        if (Full < 4):
            if (Empty != 0):
                Empty = -1
                print("Down Empty")

            if (Mutex != 0):
                print("Down Mutex")
                Mutex = -1

            print("Dados Adicionados Com Sucesso!!!")
            print("--------------------------------")
            Mutex = +1
            processos.state = "P"
            print("Transição P")

    if (processos.name == "p2"):
        processos.state = "E"
        if (Full != 0):
            Full = -1
            print("FULL " + str(Full))
            if (Mutex != 0):
                print("Mutex")
                Mutex = -1

            print("Dado Retira com Sucesso!!!")
            Mutex = -1
            process.state = "P"
            print("Transição de Estado para P")

i =+1
