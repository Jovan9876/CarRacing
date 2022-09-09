from datetime import datetime


class Score:
    """
    The class has three private attributes:
       - name: string
       - score: integer
       - timestamp: float

    The timestamp represents the date of the score. It is transformed to a readable date in __str__.

    """

    def __init__(self, name, score, timestamp=None):
        """Initialize and check values"""
        if not name or type(name) is not str:
            raise ValueError("Provided name is incorrect.")

        try:
            score = int(score)
        except (TypeError, ValueError):
            raise ValueError("Score must be a positive integer.")

        # Scores cannot be negative
        if score < 0:
            raise ValueError("Score must be a positive integer.")

        self.name = name
        self._score = score

        # If no timestamp is provided, use the current time
        if timestamp is None:
            timestamp = datetime.now().timestamp()
        self._timestamp = timestamp

    def __lt__(self, other):
        """Allow comparisons / sorting with other Score objects, or number-like values"""
        try:
            return self._score < other._score
        except AttributeError:
            pass

        try:
            score = int(other)
            return self._score < score
        except (TypeError, ValueError):
            raise TypeError(
                "Can only compare with other Score instances or a number-like value."
            )

    def json(self):
        """Return a JSON representation of the instance"""
        data = {
            "name": self.name,
            "score": self._score,
            "timestamp": self._timestamp,
        }

        return data

    @property
    def time(self):
        """Human readable time from the timestamp"""
        dt = datetime.fromtimestamp(self._timestamp)
        return f"{dt:%d-%m-%Y %H:%M:%S}"

    @property
    def score(self):
        """Getter for the private attribute score"""
        return self._score

    def __str__(self):
        """Returns a string representation of the instance, including a human readable date"""
        human_date = datetime.fromtimestamp(self._timestamp)
        return f"<Score ({self.name}): {self._score} @ {human_date:%d-%m-%Y %H:%M:%S}>"


if __name__ == "__main__":
    s = Score("Tim", 1000)
    s2 = Score("John", 200)
