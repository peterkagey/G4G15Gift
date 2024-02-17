import urllib.request
from tinydb import TinyDB, Query

class OEISBFile():
  DB = TinyDB('/Users/peter/Programming/MathArt/AxiDrawV3/G4G/OEIS_parsing/db.json')

  def __init__(self, a_number):
    self.a_number = a_number
    n = str(self.a_number).zfill(6)
    self.a_number_string = f"A{n}"

  def lookup_sequence(self):
    def is_valid(line):
      return line.strip() and not line.strip().startswith('#')
    lookup = self.DB.get(Query().id == self.a_number_string)
    if lookup == None:
      url = f"https://oeis.org/{self.a_number_string}/b{self.a_number_string[1:]}.txt"
      with urllib.request.urlopen(url) as response:
        response_string = response.read().decode('utf-8')
      values = [int(line.split()[1]) for line in response_string.split('\n') if is_valid(line)]
      self.DB.insert({'id': self.a_number_string, 'value':values})
      return values
    else:
      return lookup['value']
