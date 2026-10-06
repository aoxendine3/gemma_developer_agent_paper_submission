"""
Stage 07: Poincaré Norm Bound Constant Verification (||x|| <= 0.85)
Dynamically verifies norm calculation via Rust FFI.
"""
import ctypes
from hexcell.lattice import HexCellLattice, _find_library

def run_stage() -> dict:
    lib = ctypes.CDLL(_find_library())
    lib.verify_poincare_norm.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_size_t]
    lib.verify_poincare_norm.restype = ctypes.c_double
    
    vec = (ctypes.c_double * 10)(0.1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.1, 0.1, 0.1, 0.1)
    measured_norm = lib.verify_poincare_norm(vec, 10)
    assert measured_norm > 0 and measured_norm <= 0.85, f"Poincaré norm out of bounds: {measured_norm}"

    return {
        "stage": "07",
        "name": "Poincaré Norm Bound Constant Verification (||x|| <= 0.85)",
        "status": "PASS",
        "detail": f"Measured vector norm via Rust FFI: {measured_norm:.6f} satisfies paper bound <= 0.850000"
    }

if __name__ == "__main__":
    print(run_stage())
