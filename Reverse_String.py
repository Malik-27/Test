sdef reverse_words(s):
    
    words = s.split()
    
    rev_words = words[::-1]
    
    return ' '.join(rev_words)


reverse_words('The greatest victory is that which requires no battle')