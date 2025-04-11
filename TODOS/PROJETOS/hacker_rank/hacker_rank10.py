def swap_case(s):
        ss = ""
        for letter in s:
            if letter.islower():
                ss += letter.upper()
            elif letter.isupper():
                ss += letter.lower()
            else:
                ss += letter      
        return ss
