"""
Stage 01: Sub-Millisecond State Transition Benchmark
Executes REAL dynamic micro-benchmarks timing FFI synchronization latency.
"""
import time
from hexcell.lattice import HexCellLattice


def run_stage() -> dict:
    iterations = 1000
    with HexCellLattice(dimensions=18432) as lattice:
        start_ns = time.perf_counter_ns()
        for _ in range(iterations):
            lattice.synchronize()
        total_ms = (time.perf_counter_ns() - start_ns) / 1e6

    avg_latency_ms = total_ms / iterations
    assert avg_latency_ms < 0.300, f"Avg latency {avg_latency_ms:.6f} ms exceeded 0.300 ms SLO limit"

    return {
        "stage": "01",
        "name": "Sub-Millisecond State Transition Benchmark",
        "status": "PASS",
        "detail": f"Empirically measured avg FFI sync latency: {avg_latency_ms:.6f} ms over {iterations} calls (<0.300 ms SLO limit)"
    }


if __name__ == "__main__":
    print(run_stage())
