import tributary.lazy as tl


class TestAPI:
    def test_api(self):
        assert hasattr(tl.LazyNode, '__add__')
        assert hasattr(tl.LazyNode, '__add__')
        assert hasattr(tl.LazyNode, '__radd__')
        assert hasattr(tl.LazyNode, '__sub__')
        assert hasattr(tl.LazyNode, '__rsub__')
        assert hasattr(tl.LazyNode, '__mul__')
        assert hasattr(tl.LazyNode, '__rmul__')
        assert hasattr(tl.LazyNode, '__div__')
        assert hasattr(tl.LazyNode, '__rdiv__')
        assert hasattr(tl.LazyNode, '__truediv__')
        assert hasattr(tl.LazyNode, '__rtruediv__')
        assert hasattr(tl.LazyNode, '__pow__')
        assert hasattr(tl.LazyNode, '__rpow__')
        assert hasattr(tl.LazyNode, '__mod__')
        assert hasattr(tl.LazyNode, '__rmod__')
        assert hasattr(tl.LazyNode, 'sum')
        assert hasattr(tl.LazyNode, 'average')
        assert hasattr(tl.LazyNode, 'invert')
        assert hasattr(tl.LazyNode, '__and__')
        assert hasattr(tl.LazyNode, '__or__')
        assert hasattr(tl.LazyNode, '__invert__')
        assert hasattr(tl.LazyNode, '__bool__')
        assert hasattr(tl.LazyNode, 'int')
        assert hasattr(tl.LazyNode, 'float')
        assert hasattr(tl.LazyNode, '__str__')
        assert hasattr(tl.LazyNode, '__lt__')
        assert hasattr(tl.LazyNode, '__le__')
        assert hasattr(tl.LazyNode, '__gt__')
        assert hasattr(tl.LazyNode, '__ge__')
        assert hasattr(tl.LazyNode, '__eq__')
        assert hasattr(tl.LazyNode, '__ne__')
        assert hasattr(tl.LazyNode, '__neg__')
        assert hasattr(tl.LazyNode, '__len__')
        assert hasattr(tl.LazyNode, 'log')
        assert hasattr(tl.LazyNode, 'sin')
        assert hasattr(tl.LazyNode, 'cos')
        assert hasattr(tl.LazyNode, 'tan')
        assert hasattr(tl.LazyNode, 'asin')
        assert hasattr(tl.LazyNode, 'acos')
        assert hasattr(tl.LazyNode, 'atan')
        assert hasattr(tl.LazyNode, 'abs')
        assert hasattr(tl.LazyNode, 'sqrt')
        assert hasattr(tl.LazyNode, 'exp')
        assert hasattr(tl.LazyNode, 'erf')
        assert hasattr(tl.LazyNode, 'round')
        assert hasattr(tl.LazyNode, 'floor')
        assert hasattr(tl.LazyNode, 'ceil')

        # assert hasattr(tl.LazyNode, 'delay')
        # assert hasattr(tl.LazyNode, 'state')
        # assert hasattr(tl.LazyNode, 'apply')
        # assert hasattr(tl.LazyNode, 'window')
        # assert hasattr(tl.LazyNode, 'unroll')
        # assert hasattr(tl.LazyNode, 'unrollDataFrame')
        # assert hasattr(tl.LazyNode, 'merge')
        # assert hasattr(tl.LazyNode, 'listMerge')
        # assert hasattr(tl.LazyNode, 'dictMerge')
        # assert hasattr(tl.LazyNode, 'map')
        # assert hasattr(tl.LazyNode, 'reduce')

        assert hasattr(tl.LazyNode, 'graph')
        # assert hasattr(tl.LazyNode, 'pprint')
        assert hasattr(tl.LazyNode, 'graphviz')
        assert hasattr(tl.LazyNode, 'dagre')
        assert hasattr(tl.LazyNode, 'print')
        assert hasattr(tl.LazyNode, 'if_')

    def test_api_lazy_specific(self):
        '''apis specific to lazy nodes'''
        # expiration/interval functions
        assert hasattr(tl.LazyNode, 'expire')
        assert hasattr(tl.LazyNode, 'interval')
