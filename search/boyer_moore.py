def boyer_moore_search(text, pattern):
    def get_bad_character_shift(term):
        skip = {}

        for i in range(len(term) - 1):
            skip[term[i]] = len(term) - i - 1
        
        return skip

    def get_good_suffix_shift(term):
        skip = {}
        buffer = ""
        
        for i in range(len(term)):
            buffer = term[i] + buffer
            skip[len(buffer)] = find_suffix_position(buffer, term)
        
        return skip

    def find_suffix_position(buffer, term):
        for i in range(len(term) - 1, -1, -1):
            if term[i:].endswith(buffer):
                return len(term) - i - len(buffer)

        return len(term)

    def get_full_shift(term):
        skip = {}
        buffer = ""

        for i in range(len(term)):
            buffer = term[i] + buffer
            skip[len(buffer)] = find_full_position(buffer, term)
        
        return skip

    def find_full_position(buffer, term):
        for i in range(len(term) - 1, -1, -1):
            if term[i:] == buffer:
                return len(term) - i - len(buffer)

        return len(term)

    bad_character_shift = get_bad_character_shift(pattern)
    good_suffix_shift = get_good_suffix_shift(pattern)
    full_shift = get_full_shift(pattern)

    i = 0
    
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            return i
        else:
            char_shift = bad_character_shift.get(text[i + j], len(pattern))
            if j + 1 < len(pattern):
                suffix_shift = good_suffix_shift[len(pattern) - j - 1]
                full_shift_val = full_shift[len(pattern) - j - 1]
                i += max(char_shift, suffix_shift, full_shift_val)
            else:
                i += char_shift
    return -1