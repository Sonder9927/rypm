use pyo3::prelude::*;

/// Prints a message.
#[pyfunction]
pub fn halo() -> PyResult<String> {
    Ok("Hello rypm from rust!".into())
}

/// Add function.
#[pyfunction]
pub fn add(left: usize, right: usize) -> usize {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}
