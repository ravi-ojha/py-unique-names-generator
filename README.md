# py-unique-names-generator
Generate unique and memorable name strings


## Prerequisites

Python 3.6 or greater.

## Installation

```sh
$ pip install unique-names-generator
```

## Usage

```python
In [1]: from unique_names_generator import get_random_name

In [2]: get_random_name()
Out[2]: 'Pink Dragon'

```

### Parameters

#### `combo` - List of lists

The package comes with a bunch of random names as lists. By default, we use a `color` and `animal` to generate a random name.
Other lists are `ADJECTIVES`, `ANIMALS`, `COLORS`, `COUNTRIES`, `LANGUAGES`, `NAMES`, `STAR_WARS`.

```python
In [1]: from unique_names_generator import get_random_name
In [2]: from unique_names_generator.data import ADJECTIVES, STAR_WARS

In [3]: get_random_name(combo=[ADJECTIVES, STAR_WARS])
Out[3]: 'Furious Yoda'

```

#### `separator` - A string, default is blank space ` `


```python
In [1]: from unique_names_generator import get_random_name
In [2]: from unique_names_generator.data import ADJECTIVES, NAMES

In [69]: get_random_name(combo=[ADJECTIVES, NAMES], separator="_")
Out[69]: 'Fun_Antonie'
```

#### `style` - A string, one of capital|lowercase|uppercase.


```python
In [1]: from unique_names_generator import get_random_name
In [2]: from unique_names_generator.data import ADJECTIVES, NAMES

In [3]: get_random_name(separator="-", style="lowercase")
Out[3]: 'crimson-cat'

```

And, you can pass your own list of words. But let's face it, then this package would just be a function which randomly chooses a word from a list of strings. So its better to keep adding to the list here or fork it for your own use.
