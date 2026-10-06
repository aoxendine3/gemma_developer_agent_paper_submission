# HexCell Memory Lattice Python Bindings
import ctypes
import os
import sys

def _find_library():
    # 1. Check direct current directory / relative paths
    candidates = [
        os.path.abspath("libcontext_bridge.dylib"),
        os.path.abspath("libcontext_bridge.so"),
        os.path.join(os.path.dirname(__file__), "..", "target", "release", "libcontext_bridge.dylib"),
        os.path.join(os.path.dirname(__file__), "..", "target", "release", "libcontext_bridge.so"),
        os.path.join(os.path.dirname(__file__), "..", "target", "debug", "libcontext_bridge.dylib"),
        os.path.join(os.path.dirname(__file__), "..", "target", "debug", "libcontext_bridge.so"),
    ]
    for candidate in candidates:
        if os.path.exists(candidate):
            return candidate
    return "libcontext_bridge.dylib"

class HexCellLattice:
    def __init__(self, dimensions=18432, lib_path=None):
        self.dimensions = dimensions
        target_lib = lib_path or _find_library()
        
        try:
            self.lib = ctypes.CDLL(target_lib)
        except OSError as e:
            raise RuntimeError(
                f"Failed to load dynamic library '{target_lib}'. "
                "Ensure you have run 'cargo build --release' inside the repository."
            ) from e

        # FFI Function Declarations
        self.lib.init_hyperbolic_manifold.argtypes = [ctypes.c_size_t]
        self.lib.init_hyperbolic_manifold.restype = ctypes.c_void_p
        
        self.lib.lock_free_sync.argtypes = [ctypes.c_void_p]
        self.lib.lock_free_sync.restype = ctypes.c_int
        
        if hasattr(self.lib, 'free_hyperbolic_manifold'):
            self.lib.free_hyperbolic_manifold.argtypes = [ctypes.c_void_p]
            self.lib.free_hyperbolic_manifold.restype = ctypes.c_int

        self.buffer = self.lib.init_hyperbolic_manifold(self.dimensions)
        if not self.buffer:
            raise MemoryError("Failed to allocate Poincaré Hyper-Manifold memory buffer.")

    def synchronize(self):
        res = self.lib.lock_free_sync(self.buffer)
        if res != 0:
            raise RuntimeError(f"Lock-free atomic sync failed with error code: {res}")
        return True

    def close(self):
        if hasattr(self, 'buffer') and self.buffer:
            if hasattr(self.lib, 'free_hyperbolic_manifold'):
                self.lib.free_hyperbolic_manifold(self.buffer)
            self.buffer = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

if __name__ == "__main__":
    print("Testing HexCell Memory Lattice FFI Bridge...")
    lattice = HexCellLattice()
    lattice.synchronize()
    print("✅ HexCell 18,432-D Lock-Free Synchronization Verified!")
    lattice.close()
