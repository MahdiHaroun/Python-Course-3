def doubleStuff(a_list):
    """ Return a new list in which contains doubles of the elements in a_list. """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

things = [2, 5, 9]
print(things)
things = doubleStuff(things)
print(things)

#****************************************************

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

def f (st) : 
    return st.upper() 
abbrevs_upper = map ( f , abbrevs) 
abbrevs_upper_list = list(abbrevs_upper)
print(abbrevs_upper_list)

#****************************************************