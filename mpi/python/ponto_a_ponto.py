import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Este exemplo espera pelo menos 2 processos (mpiexec -n 2 python script.py)
if rank == 0:
    # Processo 0 cria os dados (um array NumPy)
    data = np.arange(10, dtype=np.float64)
    print(f"Processo 0: Enviando dados {data}")
    # Envia o array diretamente para o processo 1 (dest=1)
    comm.Send(data, dest=1, tag=11)

elif rank == 1:
    # Processo 1 aloca espaço na memória para receber os dados
    data = np.empty(10, dtype=np.float64)
    # Recebe os dados vindos do processo 0 (source=0)
    comm.Recv(data, source=0, tag=11)
    print(f"Processo 1: Dados recebidos com sucesso: {data}")

