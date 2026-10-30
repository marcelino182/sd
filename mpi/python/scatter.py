import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Cada processo vai receber um pedaço contendo 2 elementos
sendbuf = None
recvbuf = np.empty(2, dtype=np.int32)

if rank == 0:
    # O processo raiz cria o array completo
    # O tamanho total deve ser (número de processos * tamanho do pedaço)
    sendbuf = np.arange(size * 2, dtype=np.int32)
    print(f"Processo Raiz (0): Array original para dividir: {sendbuf}")

# Divide o sendbuf igualmente e envia uma parte para o recvbuf de cada rank
comm.Scatter(sendbuf, recvbuf, root=0)

print(f"Processo {rank}: Recebeu o pedaço {recvbuf}")

