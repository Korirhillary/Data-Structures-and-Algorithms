def is_balanced(expression):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False

    return not stack

# Sample usage
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  
print(is_balanced(expression2))


def remove_duplicates(sequence):
    seen = set()
    result = []

    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

# Sample usage
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]

import string

def word_frequency(sentence):
    words = sentence.lower().translate(str.maketrans('', '', string.punctuation)).split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

# Sample usage
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)


