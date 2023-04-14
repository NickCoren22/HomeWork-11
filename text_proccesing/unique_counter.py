story = 'DOWN THE RABBIT HOLE. Alice had sat on the bank by her sis-ter till she was tired.'\
        'Once or twice she had looked at the book her sis-ter held in her hand,'\
        'but there were no pict-ures in it, "and what is the use of a book," thought Alice,'\
        '"with-out pict-ures?" She asked her-self as well as she could,'\
        'for the hot day made her feel quite dull, if it would be worth while'\
        'to get up and pick some dai-sies to make a chain.'\
        'Just then a white rab-bit with pink eyes ran close by her.'


def unique_words(text):
        text = text.lower()\
                .replace(".", "")\
                .replace(",", "")\
                .replace("?", "")\
                .replace("\"", "")\
                .replace("-", "")
        words_list = text.split(" ")
        words = set(words_list)
        result = {}
        for item in words:
            numbers  = words_list.count(item)
            result[item] = numbers
        return result


print(unique_words(story))
