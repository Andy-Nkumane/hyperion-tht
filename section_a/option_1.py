def group_anagrams(strings):
    results = {}
    for string in strings:
        sorted_anagram = "".join(sorted(string))
        if sorted_anagram in results:
            results[sorted_anagram].append(string)
        else:
            results[sorted_anagram] = [string]
    return list(results.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
