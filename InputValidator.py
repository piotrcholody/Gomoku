class InputValidator:
    @staticmethod
    def is_size_valid(value):
        return isinstance(value, int) and (value > 2 and value <= 20)

    @staticmethod
    def is_position_valid(size, x, y):
        return isinstance(x, int) and isinstance(y, int) and (x >= 0 and x < size) and (y >= 0 and y < size)
