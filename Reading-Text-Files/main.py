# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from ctypes.wintypes import WORD
from string import punctuation


def read_file_content(filename):
      # [assignment] Add your code here
    print('The count of the message is calculated as thus:\n ')

    formatted_list = []
    with open('Downloads\Reading-Text-Files\Reading-Text-Files\story.txt', 'r') as letter:
        content = letter.read()
        #letter.close()
    for words in content.split():
        formatter = words.maketrans('','',punctuation)
        words = words.translate(formatter)
        formatted_list.append(words)
    return formatted_list
            
def count_words():
  # [assignment] Add your code here
  text = read_file_content('story.txt')
  word_count = {}
  for key in text:
      word_count[key] = word_count.get(key,0) + 1
  return word_count

print(count_words())

  #  return {"as": 10, "would": 20}