from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, suffix) -> int:
        if not suffix or not isinstance(suffix, str):
            raise TypeError(f"Illegal argument for countWordsWithSuffix: 'suffix' must be a non-empty string")
        
        count = 0
        for word in self.keys():
            if word.endswith(suffix):
                count += 1
        return count

    def has_prefix(self, prefix) -> bool:
        if not prefix or not isinstance(prefix, str):
            raise TypeError(f"Illegal argument for hasPrefix: 'prefix' must be a non-empty string")
        
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    # Доданий метод для перерахунку всіх слів
    def keys(self):
        result = []
        self._collect_keys(self.root, "", result)
        return result
    
    def _collect_keys(self, node, prefix, result):
        if node.is_end_of_word:
            result.append(prefix)
        for char, next_node in node.children.items():
            self._collect_keys(next_node, prefix + char, result)

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    print(f'Asserting count_words_with_suffix("e") == 1   # apple')
    assert trie.count_words_with_suffix("e") == 1  # apple
    print('   - Pass\n')

    print(f'Asserting count_words_with_suffix("ion") == 1   # application')
    assert trie.count_words_with_suffix("ion") == 1  # application
    print('   - Pass\n')

    print(f'Asserting count_words_with_suffix("a") == 1   # banana')
    assert trie.count_words_with_suffix("a") == 1  # banana
    print('   - Pass\n')

    print(f'Asserting count_words_with_suffix("at") == 1   # cat')
    assert trie.count_words_with_suffix("at") == 1  # cat
    print('   - Pass\n')

    # Перевірка наявності префікса
    print('Asserting has_prefix("app") == True  # apple, application ')
    assert trie.has_prefix("app") == True  # apple, application
    print('    - Pass\n')

    print('Asserting has_prefix("bat") == False')
    assert trie.has_prefix("bat") == False
    print('    - Pass\n')

    print('Asserting has_prefix("ban") == True  # banana ')
    assert trie.has_prefix("ban") == True  # banana
    print('    - Pass\n')

    print('Asserting has_prefix("ca") == True  # cat ')
    assert trie.has_prefix("ca") == True  # cat
    print('    - Pass\n')
# end if
