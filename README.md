# Interpolation

A python package containing classes for (linear and bilinear) interpolation

The API is optimized for reusing the same table many times.

If `extrapolate` is `True` then a linear extrapolation will be performed using the edge segment.  If
it is false, then a `ValueError` will be raised.

## Examples

### Linear

```python
from interpolation import LinearInterpolation

table = LinearInterpolation(
    x_index=(1, 2, 3),
    values=(10, 20, 30),
    extrapolate=False)

assert table(1.5) == 15
assert table(2.5) == 25

```

### Bilinear

```python
from interpolation import BilinearInterpolation

table = BilinearInterpolation(
    x_index=(1, 2, 3),
    y_index=(1, 2, 3),
    values=((110, 120, 130),
            (210, 220, 230),
            (310, 320, 330)),
    extrapolate=True)

assert table(1, 1) == 110
assert table(2.5, 2.5) == 275
```
