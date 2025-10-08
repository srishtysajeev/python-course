"""
Create a generator function called custom_range(start, end, step) that behaves like Python’s built-in range() but uses yield to produce values one at a time.
"""
import re
# def range_gen(start, stop, step):
#      x = start 
#      while x < stop:
#           yield x
#           x += step
#           pass 
#      return 

# for num in range_gen(2, 10, 2):
#     print(num)



def sentence_splitter(sentences): 
    x = 0
    sent_len = len(sentences)

    while x < sent_len: 
        yield sentences[x]
        x += 1

def word_tokenizer(sentence_gen): 
    for sentence in sentence_gen: 
        word_list = sentence.split(" ")
        for word in word_list:
            yield word
    # the above yields the sentences 
   # word_list = sentence_gen.split(" ") # split doesn't work on a generator
    # for word in word_list:

    #     yield word 

def word_cleaner(word_gen):
    for word in word_gen:
        #clean = [letter for letter in word if letter is re.sub(r'[^\w\s]', '', letter)]
        
        new_word = word.lower()
        clean = re.sub(r'[^\w\s]', '', new_word)
        yield clean
    
sentences = [
    "Hello world!",
    "Generators are powerful.",
    "Let's build a pipeline."
]

g = sentence_splitter(sentences)
g2 = word_tokenizer(g)
g3 = word_cleaner(g2)
for n in g3:      #  powers() instantiates a new generator
    print(n, end="\n")