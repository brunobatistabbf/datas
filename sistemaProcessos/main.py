import random
from processos import process
def main(null=None):
    process(10)
    tempoExecucao = [10000, 5000, 7000, 3000, 3000, 8000, 2000, 5000, 4000, 10000]
    tabelaProcessos = []
    j = 0;

    for i in tempoExecucao:
        process[j] = process(j, 0, 0, null, 0, 0, i)
        j = j + 1

    while(True):
        for process in process:
            entradaSaida = 0
            print("Executando")
            tabelaProcessos.__add__(process)

            if(process.TP < process.limiteTP):
                process.TP +=1;
                process.CP = process.TP + 1;
            else:
                print("Pronto")
                process.EP = "PRONTO"
                break

            if random.randint(100) + 1 <= 5:
                if(process.EP == "BLOQUEADO"):
                    if(random.randint(100) + 1 <= 30):
                        print(">>>>>>PRONTO")
                        process.EP = "PRONTO"
                        tabelaProcessos.__add__(process)
                entradaSaida = entradaSaida + 1
                operacaoEntradaSaida(process)
                tabelaProcessos.__add__(process)
        if(entradaSaida != 0):
            print("PRONTO")
            process.EP = "PRONTO"
            tabelaProcessos.__add__(process)
        if(process.EP == "EXECUTANDO"):
            print("BLOQUEADO")
            process.EP = "BLOQUEADO"

        print("%-5s", "PID")
        print("%10s", "TP")
        print("%10s", "CP")
        print("%12s", "EP")
        print("%5s", "NES")
        print("%7s%n", "N_CPU")
        print("%-5s", str(process.PID))
        print("%10s", str(process.TP))
        print("%10s", str(process.CP))
        print("%12s", str(process.EP))
        print("%5s", str(process.NES))
        print("%7s%n", str(process.N_CPU))

        if(verificador(process)):
            break



def verificador(process:bytearray):
    decide = True
    for process in process:
            if(process.TP < process.limiteTP):
                decide = False
                break;

    return decide;


def operacaoEntradaSaida(process):
    process.NES =+ 1
    print("BLOQUEADO")
    process.EP = "BLOQUEADO"
    return True;

if __name__ == '__main__':
    main()