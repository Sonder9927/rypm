use pyo3::prelude::*;

use halo;

/// A Python module implemented in Rust.
#[pymodule]
fn _librypm(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(halo::halo, m)?)?;
    m.add_function(wrap_pyfunction!(halo::add, m)?)?;
    Ok(())
}
