import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Cada processo cria um array local com dados diferentes baseados no seu rank
# Exemplo para 3 processos: Rank 0 ->, Rank 1 ->, Rank 2 -> [2, 3]
local_data = np.array([rank, rank + 1], dtype=np.int32)
print(f"Processo {rank}: Dados locais para redução: {local_data}")

# O processo raiz precisa de um buffer para armazenar o resultado final
result = None
if rank == 0:
    result = np.empty(2, dtype=np.int32)

# Todos os processos enviam seus 'local_data'. 
# O MPI soma os valores posição por posição (MPI.SUM) e salva em 'result' no root=0
comm.Reduce(local_data, result, op=MPI.SUM, root=0)

if rank == 0:
    print(f"\nProcesso Raiz (0): Resultado final da soma global: {result}")

