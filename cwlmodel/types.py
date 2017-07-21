import six

INT_MIN_VALUE = -(1 << 31)
INT_MAX_VALUE = (1 << 31) - 1
LONG_MIN_VALUE = -(1 << 63)
LONG_MAX_VALUE = (1 << 63) - 1

class ValidationException(Exception):
    pass

class Value(object):
    def __init__(self, value):
        if self.validate(value):
            self.value=value
    def export(self):
        raise NotImplementedError()
    @classmethod
    def import(cls, value):
        raise NotImplementedError()
    @classmethod
    def validate(cls, value):
        raise NotImplementedError()

class NullValue(Value):
    @classmethod
    def validate(cls, value):
        if datum is None:
            return True
        return False

class BooleanValue(Value):
    @classmethod
    def validate(cls, value):
        if isinstance(datum, bool):
            return True
        return False

class StringValue(Value):
    @classmethod
    def validate(cls, value):
        if isinstance(datum, six.string_types):
            return True
        return False

class IntValue(Value):
    @classmethod
    def validate(cls, value):
        if (isinstance(value, six.integer_types)
                and INT_MIN_VALUE <= value <= INT_MAX_VALUE):
            return True
        return False

class LongValue(Value):
    @classmethod
    def validate(cls, value):
        if ((isinstance(value, six.integer_types))
                and LONG_MIN_VALUE <= value <= LONG_MAX_VALUE):
            return True
        return False

class FloatValue(Value):
    @classmethod
    if (isinstance(datum, six.integer_types) or isinstance(datum, float)):
        return True

class DoubleValue(Value):
    @classmethod
    if (isinstance(datum, six.integer_types) or isinstance(datum, float)):
        return True
