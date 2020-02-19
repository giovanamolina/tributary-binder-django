import tributary.streaming as ts


class TestAPI:
    def test_api(self):
        assert hasattr(ts.StreamingNode, '__add__')
        assert hasattr(ts.StreamingNode, '__add__')
        assert hasattr(ts.StreamingNode, '__radd__')
        assert hasattr(ts.StreamingNode, '__sub__')
        assert hasattr(ts.StreamingNode, '__rsub__')
        assert hasattr(ts.StreamingNode, '__mul__')
        assert hasattr(ts.StreamingNode, '__rmul__')
        assert hasattr(ts.StreamingNode, '__div__')
        assert hasattr(ts.StreamingNode, '__rdiv__')
        assert hasattr(ts.StreamingNode, '__truediv__')
        assert hasattr(ts.StreamingNode, '__rtruediv__')
        assert hasattr(ts.StreamingNode, '__pow__')
        assert hasattr(ts.StreamingNode, '__rpow__')
        assert hasattr(ts.StreamingNode, '__mod__')
        assert hasattr(ts.StreamingNode, '__rmod__')
        assert hasattr(ts.StreamingNode, '__and__')
        assert hasattr(ts.StreamingNode, '__or__')
        assert hasattr(ts.StreamingNode, '__invert__')
        assert hasattr(ts.StreamingNode, '__bool__')
        assert hasattr(ts.StreamingNode, 'int')
        assert hasattr(ts.StreamingNode, 'float')
        assert hasattr(ts.StreamingNode, '__str__')
        assert hasattr(ts.StreamingNode, '__lt__')
        assert hasattr(ts.StreamingNode, '__le__')
        assert hasattr(ts.StreamingNode, '__gt__')
        assert hasattr(ts.StreamingNode, '__ge__')
        assert hasattr(ts.StreamingNode, '__eq__')
        assert hasattr(ts.StreamingNode, '__ne__')
        assert hasattr(ts.StreamingNode, '__neg__')
        assert hasattr(ts.StreamingNode, '__len__')
        assert hasattr(ts.StreamingNode, 'log')
        assert hasattr(ts.StreamingNode, 'sin')
        assert hasattr(ts.StreamingNode, 'cos')
        assert hasattr(ts.StreamingNode, 'tan')
        assert hasattr(ts.StreamingNode, 'asin')
        assert hasattr(ts.StreamingNode, 'acos')
        assert hasattr(ts.StreamingNode, 'atan')
        assert hasattr(ts.StreamingNode, 'abs')
        assert hasattr(ts.StreamingNode, 'sqrt')
        assert hasattr(ts.StreamingNode, 'exp')
        assert hasattr(ts.StreamingNode, 'erf')

        assert hasattr(ts.StreamingNode, 'delay')
        # assert hasattr(ts.StreamingNode, 'state')
        assert hasattr(ts.StreamingNode, 'apply')
        assert hasattr(ts.StreamingNode, 'window')
        assert hasattr(ts.StreamingNode, 'unroll')
        assert hasattr(ts.StreamingNode, 'unrollDataFrame')
        assert hasattr(ts.StreamingNode, 'merge')
        assert hasattr(ts.StreamingNode, 'listMerge')
        assert hasattr(ts.StreamingNode, 'dictMerge')
        assert hasattr(ts.StreamingNode, 'reduce')

        assert hasattr(ts.StreamingNode, 'graph')
        assert hasattr(ts.StreamingNode, 'pprint')
        assert hasattr(ts.StreamingNode, 'graphviz')
        assert hasattr(ts.StreamingNode, 'print')
        assert hasattr(ts.StreamingNode, 'perspective')

        assert hasattr(ts.StreamingNode, 'rollingCount')
        assert hasattr(ts.StreamingNode, 'rollingSum')
        assert hasattr(ts.StreamingNode, 'rollingCount')
        assert hasattr(ts.StreamingNode, 'rollingMin')
        assert hasattr(ts.StreamingNode, 'rollingMax')
        assert hasattr(ts.StreamingNode, 'rollingAverage')
