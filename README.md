# Pickle Wrapper

pickleUtils:
	Provide a simple facade to the package 'pickle'

## Usage

Example usage:

```python
from picklewrapper.pickleutils import PickleUtils

pu = PickleUtils('mypickefile')

pu.pickle_write([obj1, obj2, obj3])

return_list = pu.pickle_read()

# For example, we can loop through the three objects we just stored
for obj in return_list:
	do_something(obj)

```
