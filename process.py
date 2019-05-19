from collections import Counter
import json

'''
Processes words_dictionary json by following rules
1. length should be between 4 and 8 chars long
2. Either should have words with repeated chars or unrepeated chars
'''

with open('dictionary_compact.json') as file:
    words = json.load(file)
cleaned_words={}
cleaned_words_unrep={}
for word,meaning in words.items():
    if len(word)>=3 and len(word)<=6:
        cleaned_words[word]=meaning


def dump_file(reverse_bool):
    for word,meaning in cleaned_words.items():
        counter_dict = Counter(word)
        #print(sorted(counter_dict.values(),reverse=True))
        for value in sorted(counter_dict.values(),reverse=reverse_bool):
            if value==1:
                print(word)
                cleaned_words_unrep[word]=meaning
                break
            break
    json_file = json.dumps(cleaned_words_unrep)

    with open('unrep_words_{}.json'.format(reverse_bool),'w') as file:
        file.write(json_file)

def get_meaning(word):
    return words[word]

dump_file(True)
