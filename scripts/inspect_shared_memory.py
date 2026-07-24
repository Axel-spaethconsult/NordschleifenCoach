"""
Inspect the ACC shared memory structure.
"""

from pprint import pprint

from nordschleifen_coach.infrastructure.acc.shared_memory.reader import (
    AccSharedMemoryReader,
)

reader = AccSharedMemoryReader()

snapshot = reader.read()

print(type(snapshot))
print()

try:
    pprint(vars(snapshot))
except TypeError:
    print(dir(snapshot))