from typing import Iterable

from rest_framework import serializers


class NotContainWords:
    def __init__(self, words: Iterable[str]):
        self.words = set(words)

    def __call__(self, value):
        words = set(value.lower().split())
        intersection = words & self.words
        if intersection:
            raise serializers.ValidationError(
                "This field should not contain the words: %s." % ", ".join(intersection)
            )
