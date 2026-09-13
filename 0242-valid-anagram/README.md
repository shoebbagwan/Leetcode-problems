## Valid Anagram

**Problem:** Check if string `t` is an anagram of string `s` (same characters, same frequencies, different order).

**Approach:** Two strings are anagrams only if they're the same length and have identical character counts. Build a frequency dictionary from `s`, then walk through `t` decrementing counts — removing a key once it hits zero. If a character in `t` is missing from the count, they can't be anagrams. At the end, an empty dictionary means every character matched exactly.

**Complexity:** Time O(n), Space O(k) — where k is the number of distinct characters.
