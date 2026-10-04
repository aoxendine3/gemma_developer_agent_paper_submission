# HexCell Memory Lattice Python Bindings
import ctypes
import os

class HexCellLattice:
    def __init__(self, dimensions=18432):
        self.dimensions = dimensions
        self.lib = ctypes.CDLL(os.path.abspath("libcontext_bridge.dylib"))
        
        self.lib.init_hyperbolic_manifold.argtypes = [ctypes.c_size_t]
        self.lib.init_hyperbolic_manifold.restype = ctypes.c_void_p
        
        self.buffer = self.lib.init_hyperbolic_manifold(self.dimensions)
        
    def synchronize(self):
        self.lib.lock_free_sync(self.buffer)
