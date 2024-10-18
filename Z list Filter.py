def all_z_words_filter(wordlist: list) -> list:
    """Produce list of words form the input that contain 'z'."""
    return list(filter(lambda wd: 'z' in wd.lower(), wordlist))

def test_all_z_words_filter():
    assert all_z_words_filter(['zoom', 'zoo', 'flaske', 'tv']) == ["zoom", "zoo"]

#Teste funksjonen:
print(all_z_words_filter(['zoom', 'zoo', 'flaske', 'tv']))   
