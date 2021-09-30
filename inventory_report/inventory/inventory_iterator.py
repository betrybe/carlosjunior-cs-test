from collections.abc import Iterator


class InventoryIterator(Iterator):
    @classmethod
    def __init__(self, iterable):
        self.iterable = iterable
        self.position = 0

    def __next__(self):
        try:
            each_product = self.iterable[self.position]
        except IndexError:
            raise StopIteration()
        else:
            self.position += 1
            return each_product
