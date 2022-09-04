def longest_substring_without_repeating_characters(string):
    string_set = set()
    longest = 0
    left = 0

    for letter in string:
        while letter in string_set:
            string_set.remove(string[left])
            left += 1
        string_set.add(letter)
        longest = max(len(string_set), longest)

    return longest 

print(longest_substring_without_repeating_characters("abcabcbb"))




