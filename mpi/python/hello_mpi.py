from mpi4py import MPI

# Get the global communicator
comm = MPI.COMM_WORLD

# Get the total number of processes and the rank of the current process
world_size = comm.Get_size()
my_rank = comm.Get_rank()

print(f"Hello World from process {my_rank} of {world_size}")

