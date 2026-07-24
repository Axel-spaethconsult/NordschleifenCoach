from pyaccsharedmemory import accSharedMemory


class AccSharedMemoryReader:
    def __init__(self) -> None:
        self._shared_memory = accSharedMemory()

    def read(self):
        return self._shared_memory.read_shared_memory()

    def close(self) -> None:
        self._shared_memory.close()