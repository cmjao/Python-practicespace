class OopsException(Exception):
    pass

# raise OopsException('Caught an oops')

try:
    raise OopsException('Caught an oops')
except OopsException as exc:
    print(exc)