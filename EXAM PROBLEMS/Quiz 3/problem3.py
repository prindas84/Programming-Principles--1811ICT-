lst = [["five", "twelve", "seventeen", "two", "eight", "seventeen"], 
["twenty", "fourteen", "eleven", "seven", "seventeen", "five", "two", "ten", "four", "twelve", "eleven"], 
["two", "nineteen", "seventeen", "ten", "seventeen", "nineteen", "seven", "four", "fifteen", "two"], 
["seventeen", "fifteen", "nineteen", "eleven", "twelve", "ten", "nineteen", "one", "two", "three", "six", "eighteen"]]

def build_dict(ls):
    
    word_count = {}

    for word_list in ls:
        for word in word_list:
            word_count[word] = word_count.get(word, 0) + 1
    
    return word_count


word_dict = build_dict(lst)

print("Seventeen occurs", word_dict['seventeen'], "times")
