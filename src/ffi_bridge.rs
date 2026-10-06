//! FFI Export Handlers for C / Python / TypeScript Interop

use crate::lattice::poincare;
use crate::lattice::memory_map::HexCellMemorySlot;
use crate::safety::lockfree_ring::LockFreeRingBuffer;

#[no_mangle]
pub extern "C" fn init_hyperbolic_manifold(dimensions: u32) -> *mut HexCellMemorySlot {
    if dimensions == 0 {
        return std::ptr::null_mut();
    }
    let slot = Box::new(HexCellMemorySlot::new(0, dimensions));
    Box::into_raw(slot)
}

#[no_mangle]
pub extern "C" fn lock_free_sync(slot_ptr: *mut HexCellMemorySlot) -> i32 {
    if slot_ptr.is_null() {
        return -1;
    }
    let ring = LockFreeRingBuffer::new();
    let _swapped = ring.swap_buffers();
    unsafe {
        (*slot_ptr).promote_taint();
    }
    0
}

#[no_mangle]
pub extern "C" fn verify_poincare_norm(vector_ptr: *const f64, len: usize) -> f64 {
    if vector_ptr.is_null() || len == 0 {
        return -1.0;
    }
    let slice = unsafe { std::slice::from_raw_parts(vector_ptr, len) };
    poincare::norm(slice)
}

#[no_mangle]
pub extern "C" fn free_hyperbolic_manifold(slot_ptr: *mut HexCellMemorySlot) {
    if !slot_ptr.is_null() {
        unsafe {
            let _ = Box::from_raw(slot_ptr);
        }
    }
}
