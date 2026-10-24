''' Write a program to implement strStr(haystack: str, needle: str) -> int using KMP and a Randomizer class with
getRandom() -> int for stream sampling, accepting text/pattern strings or stream data and returning
indices or sampled elements.'''

import random
# KMP String Matching
def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0

    # Build LPS array
    lps = [0] * len(needle)
    length = 0
    i = 1

    while i < len(needle):
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    # Search pattern in text
    i = 0
    j = 0

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1

            if j == len(needle):
                return i - j

        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

    return -1
# Random Stream Sampling
class Randomizer:
    def __init__(self, stream):
        self.stream = iter(stream)
        self.selected = None
        self.count = 0

        # Reservoir sampling: keep one random item
        for item in self.stream:
            self.count += 1

            if random.randrange(self.count) == 0:
                self.selected = item

    def getRandom(self) -> int:
        if self.count == 0:
            raise ValueError("Stream is empty")

        return self.selected
# Main Program
haystack = "hello"
needle = "ll"

print("Haystack:", haystack)
print("Needle:", needle)
print("KMP Index:", strStr(haystack, needle))

stream = [10, 20, 30, 40, 50]
r = Randomizer(stream)

print("Random Sample:", r.getRandom())

