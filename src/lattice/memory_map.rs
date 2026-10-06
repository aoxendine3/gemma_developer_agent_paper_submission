//! Shared Memory Pointer Mapping & Zero-Copy Alignment

use std::sync::atomic::{AtomicU64, Ordering};

pub const CACHE_LINE_SIZE: usize = 128;
pub const HARDWARE_TAINT_CANDIDATE: u32 = 0xDEAD0000;
pub const HARDWARE_TAINT_DECISION: u32 = 0xBEAF0000;

#[repr(C, align(128))]
pub struct HexCellMemorySlot {
    pub slot_id: u32,
    pub taint_flag: u32,
    pub sequence_counter: AtomicU64,
    pub dimensions: u32,
    pub reserved: [u8; 104],
}

impl HexCellMemorySlot {
    pub fn new(slot_id: u32, dimensions: u32) -> Self {
        Self {
            slot_id,
            taint_flag: HARDWARE_TAINT_CANDIDATE,
            sequence_counter: AtomicU64::new(0),
            dimensions,
            reserved: [0u8; 104],
        }
    }

    pub fn promote_taint(&mut self) {
        self.taint_flag = HARDWARE_TAINT_DECISION;
        self.sequence_counter.fetch_add(1, Ordering::SeqCst);
    }
}
