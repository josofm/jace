from bs4 import BeautifulSoup

from jace.commons.parsers.ligamagic_parser import LigaMagicParser
from jace.page_files.save_files import save_file

def html_soup(body):
    return BeautifulSoup(body, "html.parser")


class Parser:
    def __init__(self, body, name, card):
        save_file(name, card, body)
        self.body = html_soup(body)
        self.name = name
        self.card = card

    def call_correct_file(self, name):
        if name == "ligamagic":
            return LigaMagicParser(self.body)


