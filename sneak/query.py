class ListQueryResult(object):

    class query:
        select_related = True
        where = False

    def __init__(self, value):
        self.value = value

    def count(self):
        return len(self)

    def iterator(self):
        for v in self.value:
            yield v

    def _clone(self):
        return type(self)(list(self.value))

    def __len__(self):
        return len(self.value)

    def __getitem__(self, s):
        if isinstance(s, slice):
            return self.value.__getitem__(s)
        else:
            return self.value[s]
