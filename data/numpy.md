# NumPy Documentation

## Installation

```bash
pip install numpy
```

## Creating Arrays
```python
import numpy as np
a = np.array([1, 2, 3])
print(a)
```

## Matrices
```python
matrix = np.array([[1, 2], [3, 4]])
print(matrix)
```

## Operations
```python
b = np.array([4, 5, 6])
print(a + b)
print(a * 2)
print(np.dot(a, b))
```

## Indexing and Slicing
```python
print(a[0])
print(a[1:3])
```

## Reshaping
```python
c = np.arange(6)
print(c.reshape(2, 3))
```

## Random Numbers
```python
rand = np.random.rand(2, 3)
print(rand)
```

## References
- [NumPy Documentation](https://numpy.org/doc/)
- [NumPy User Guide](https://numpy.org/doc/stable/user/)
