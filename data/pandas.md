# Pandas Documentation

## Installation

```bash
pip install pandas
```

## Series
```python
import pandas as pd
s = pd.Series([1, 3, 5, 7])
print(s)
```

## DataFrame
```python
data = {'A': [1, 2], 'B': [3, 4]}
df = pd.DataFrame(data)
print(df)
```

## Reading/Writing CSV
```python
df = pd.read_csv('data.csv')
df.to_csv('output.csv', index=False)
```

## Selection and Filtering
```python
print(df['A'])
print(df[df['A'] > 1])
```

## Aggregations
```python
print(df.sum())
print(df.mean())
```

## References
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Pandas User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html)
