import json

from .score import Score


class HighScores:
    """This class manages a list of high scores, including serialization/deserialization and persistence using JSON"""

    # Maximum number of scores to keep
    NUMBER_OF_SCORES_TO_KEEP = 15

    def __init__(self, filename="scores.json"):
        """
        Initialize values.

        The scores are loaded from the file provided as argument, using JSON format.
        """
        self._current = 0
        self._scores = list()
        self._filename = filename
        try:
            with open(self._filename, "r") as fp:
                data = json.load(fp)
        except FileNotFoundError:
            data = dict()

        for json_score in data:
            score = Score(
                name=json_score["name"],
                score=json_score["score"],
                timestamp=json_score["timestamp"],
            )
            self.add(score)

    def add(self, other):
        """Add a score to the list of scores, and truncate it if necessary"""
        if not isinstance(other, Score):
            raise TypeError("Object must be a score instance.")

        self._scores.append(other)

        # We keep the scores sorted (highest score first)
        self._scores.sort(reverse=True)

        # Truncate the list if necessary
        if len(self._scores) > self.NUMBER_OF_SCORES_TO_KEEP:
            self._scores = self._scores[: self.NUMBER_OF_SCORES_TO_KEEP]

    def save(self):
        """Save all Score instances in a single file as JSON"""
        data = [score.json() for score in self._scores]
        with open(self._filename, "w") as fp:
            json.dump(data, fp)

    def by_name(self, name):
        """Helper function: returns a list of score for a specific player name. The case must match!"""
        return [score for score in self._scores if score.name == name]

    @property
    def scores(self):
        """Getter for the scores private attribute"""
        return self._scores

    @property
    def best(self):
        """Helpful attribute: returns the best score in the list"""
        if not self._scores:
            return None

        return self._scores[0]

    @property
    def lowest(self):
        """Helpful attribute: returns the worst score in the list (== the score to beat to enter the high scores)"""
        if not self._scores:
            # If there are no scores yet - we make up a fake score
            # Any score will be above -1
            # !!! We are breaking encapsulation when doing this
            fake_score = Score("FakeScore", 0, 0)
            fake_score._score = -1
            return fake_score

        return self._scores[-1]

    def __len__(self):
        """Utility function to get the number of high scores"""
        return len(self._scores)

    def __iter__(self):
        """Magic method: allows to use the instance as an iterable"""
        self._current = 0
        return self

    def __next__(self):
        """Magic iterator method: return the elements in the iterable one by one"""
        if self._current < len(self):
            self._current += 1
            return self._scores[self._current - 1]

        raise StopIteration

    def __str__(self):
        """String representation of the instance"""
        return f"<HighScores ({len(self)} scores)>"
