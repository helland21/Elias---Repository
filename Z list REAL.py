def all_z_words(wordlist : list) -> list:
    """Produce list of words form the input that contain 'z'."""
    zlist = [] #start with an empty list
    for wd in wordlist:
        if 'z' in wd:
            zlist = [wd] + zlist # add wd to the beginning of zlist
    return zlist
#Teste funksjonen:
print(all_z_words(['zoom', 'zoo', 'flaske', 'tv']))   
