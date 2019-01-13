"""Class for handling the training instances."""


class Instance:
    """Class for handling the training instances."""

    def __init__(self, truth=False):
        """Fill default values."""
        self.truth = truth
        self.idx = [None, 'idx']
        self.time = [None, 'time']
        self.n_ppl = [None, 'n_ppl']
        self.decision = [None, 'decision']

    def fill(self, data):
        """Fill real values."""
        self._fill(data, self.idx)
        self._fill(data, self.time)
        self._fill(data, self.n_ppl)
        if self.truth:
            self._fill(data, self.decision)

    def _join_features(self):
        data = []
        header = []
        self._add_feature(data, header, self.idx)
        self._add_feature(data, header, self.time)
        self._add_feature(data, header, self.n_ppl)
        if self.truth:
            self._add_feature(data, header, self.decision)
        return data, header

    def _fill(self, data, value):
        value[0] = data[value[1]]

    def _add_feature(self, data, header, value):
        data.append(value[0])
        header.append(value[1])

    def header(self):
        """Return header."""
        return ','.join(self._join_features()[1])

    def csv(self):
        """Return values in csv format."""
        data, _ = self._join_features()
        return ','.join(map(str, data))
