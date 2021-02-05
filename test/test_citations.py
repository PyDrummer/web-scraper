from scraper import get_citations_needed_count, get_citations_needed_report

def test_live():
    actual = 'test'
    expected = 'test'
    assert actual == expected

url = 'https://en.wikipedia.org/wiki/List_of_Roman_deities'

def test_count():
    actual = get_citations_needed_count(url)
    expected = "The total citations needed is: 4"
    assert actual == expected

def test_report():
    actual = get_citations_needed_report(url)
    expected = 'Citation needed for: Divine male-female complements such as these, as well as the anthropomorphic influence of Greek mythology, contributed to a tendency in Latin literature to represent the gods as "married" couples or (as in the case of Venus and Mars) lovers.[citation needed] Citation needed for: Letum, personification of death.[citation needed] Citation needed for: Poena, goddess of punishment.[citation needed] Citation needed for: Venilia or Venelia, sea goddess, wife of Neptune or Faunus.[citation needed] '
    assert actual == expected