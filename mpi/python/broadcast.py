import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Aloca o array em todos os processos
data = np.empty(5, dtype=np.int32)

if rank == 0:
    # Apenas o processo raiz preenche o array com dados
    data = np.array([1, 2, 3, 4, 5], dtype=np.int32)
    print(f"Processo Raiz (0): Transmitindo dados originais: {data}")

# Todos os processos chamam o Bcast. 
# O processo root=0 envia, e os demais (rank != 0) atualizam seu array 'data'
comm.Bcast(data, root=0)

# Imprime o resultado em todos os processos para verificar o recebimento
print(f"Processo {rank}: Recebeu o broadcast de 'data': {data}")

