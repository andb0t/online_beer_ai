"""Class for handling the training instances."""
import datetime


class Instance:
    """Class for handling the training instances."""

    def __init__(self, truth):
        """Fill default values."""
        self.truth = truth
        self.idx = 0
        self.time = datetime.datetime.now().hour
        self.n_ppl = None
        self.decision = None

    def fill(self, data):
        """Fill real values."""
        self.idx = data['idx']
        self.time = data['time']
        self.n_ppl = data['n_ppl']
        if self.truth:
            self.decision = data['decision']

    def _join_features(self):
        data = [self.idx]
        header = ['idx']
        # time
        header.append('time')
        data.append(self.time)
        # n_ppl
        header.append('n_ppl')
        data.append(self.n_ppl)
        # decision
        if self.truth:
            header.append('decision')
            data.append(self.decision)
        # return
        return data, header

    def header(self):
        """Return header."""
        return ','.join(self._join_features()[1])

    def csv(self):
        """Return values in csv format."""
        data, _ = self._join_features()
        return ','.join(map(str, data))
