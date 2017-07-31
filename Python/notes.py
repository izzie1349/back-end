import re

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print('searching for pattern {}'.format(pat))
        print(re.findall(pat, phrase))
        print('\n')

test_phrase = 'this is a string! but has punctuation. how can we remove?'

test_patterns = ['[^!.?]+']

multi_re_find(test_patterns, test_phrase)
