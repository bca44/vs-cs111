class Link:

    empty = ()

    def __init__(self, first, rest=empty):
        """
        define a link with first and rest
        link must be empty or contain Link obj
        """
        assert rest is Link.empty or isinstance(
            rest, Link), "Link does not follow proper structure."
        self.first = first
        self.rest = rest

    def __repr__(self):
        """
        return a machine-readable representation of Link
        in format of "Link(first, rest)"
        """
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        """
        return a human-readable representation of Link
        in format of "<rest first>"
        """
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

    def __len__(self):
        """
        return the length of Link
        """
        return 1 + len(self.rest)
