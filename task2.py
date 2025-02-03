from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not strings or not isinstance(strings, list) or not all(isinstance(string, str) for string in strings):
            raise TypeError(f"Illegal argument for findLongestCommonWord: 'strings' must be a non-empty list of strings")
        
        for string in strings:
            self.put(string)

        prefix = ''
        current = self.root

        while len(current.children) == 1 and not current.is_end_of_word:
            char = next(iter(current.children))
            prefix += char
            current = current.children[char]

        return prefix

if __name__ == "__main__":
    # Тести
    print('Asserting longest prefix in ["flower", "flow", "flowerpot"] to be "flow"')
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flowerpot"]
    assert trie.find_longest_common_word(strings) == "flow"
    print('   - Pass\n')

    print('Asserting longest prefix in ["flower", "flow", "flight"] to be "fl"')
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"
    print('   - Pass\n')

    print('Asserting longest prefix in ["interspecies", "interstellar", "interstate"] to be "inters"')
    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"
    print('   - Pass\n')

    print('Asserting longest prefix in ["dog", "racecar", "car"] to be ""')
    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
    print('   - Pass\n')

    print('Asserting longest prefix in [] to be ""')
    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == ""
    print('   - Pass\n')
# end if
