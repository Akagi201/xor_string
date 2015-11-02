# xor_string

![PyPI downloads](https://img.shields.io/pypi/dm/xor_string.svg) ![PyPI version](https://img.shields.io/pypi/v/xor_string.svg) ![PyPI python version](https://img.shields.io/pypi/pyversions/xor_string.svg)

Python doesn't support (natively) XOR on everything else than int, and this is annoying.

```
>>> 'hello' ^ 'world'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ^: 'str' and 'str'
```

Fortunately, Python has the (amazing) itertools module.

## unit tests
* `nosetests -v`

## Explanations

For those who are not familiar with python:

* cycle(key) returns an iterator that produces an infinite concatenation of key's content
* izip(a, b) returns an iterator that aggregates elements from each of the iterables. It stops on the shortest input sequence (here, our message, since cycle(key) is infinite
* ord(a) and chr(57) return (respectively) the integer representing the given char and the char represented by the given integer.
* ''.join() (roughly) concatenate every items of the list passed in argument in a string
