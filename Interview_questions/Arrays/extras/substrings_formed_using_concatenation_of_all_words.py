def form_substring_using_concatenation(words, complete_string):
        def permutations(words):
            result = []

            if len(words) == 1:
                return [words[:]]

            for i in range(len(words)):
                n = words.pop(0)
                perms = permutations(words)
                for perm in perms:
                    perm.append(n)
                result.extend(perms)
                words.append(n)

            return result

        all_permutations = permutations(words)
        output = []
        for words in all_permutations:
            complete_string = ""
            for word in words:
                complete_string += word
            if complete_string in string:
                index = string.index(complete_string)
                if not index in output:
                    output.append(index)
                
        return output

# string = "wordgoodgoodgoodbestword"
# words = ["word","good","best","good"]
# print(form_substring_using_concatenation(words, string))

def form_string_using_concatenation(words, string):
    if len(words) == 1 and words[0] in string:
        return [0]

    word_length = len(words[0])
    ans = []

    for i in range(len(string) - word_length):
        hash_map = {}
        for word in words:
            if word in hash_map:
                hash_map[word] += 1
            else:
                hash_map[word] = 1
        
        left = i
        right = i + word_length
        sub_string = string[left:right]

        while (sub_string in hash_map) and hash_map[sub_string] > 0:
            hash_map[sub_string] = hash_map[sub_string] - 1
            if not list(filter(lambda i: i > 0, hash_map.values())):
                ans.append(i)
                break
            left = right
            right = left + word_length
            sub_string = string[left:right]

    return ans

string = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
print(form_string_using_concatenation(words, string))
