//! Lock-Free Double Buffering Ring Engine

use std::sync::atomic::{AtomicBool, Ordering};

pub struct LockFreeRingBuffer {
    active_index: AtomicBool,
}

impl LockFreeRingBuffer {
    pub fn new() -> Self {
        Self {
            active_index: AtomicBool::new(false),
        }
    }

    pub fn swap_buffers(&self) -> bool {
        let current = self.active_index.load(Ordering::Acquire);
        self.active_index.store(!current, Ordering::Release);
        !current
    }
}
