"""
Rathilang to BF translator
@author ymll
"""


class RathilangTranslator():
    def __init__(self):
        self.bf_2_rathi_dictionary = {
            '+': 'jiren',
            '-': 'bakar',
            '[': 'allstack',
            ']': 'developer',
            '>': 'rathi',
            '<': 'aashutosh',
            ',': 'abeteri',
            '.': 'pitega'
        }
        self.rathi_2_bf_dictionary = {v: k for k, v in self.bf_2_rathi_dictionary.items()}

    def rathi_2_bf(self, rathi_code):
        out = ''
        try:
            for c in rathi_code:
                out += self.rathi_2_bf_dictionary[c]
        except KeyError as e:
            raise Exception('No baka no!') from e
        return out

    def bf_2_rathi(self, bf_code):
        out = ''
        for c in bf_code:
            try:
                out += self.bf_2_rathi_dictionary[c] + ' '
            except KeyError as e:
                pass
        return out


if __name__ == '__main__':
    bf_code = '++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+.+++++++..+++.<<++.>----.>----------.+++++++++++++++++.---.<<+.<++++++++++.'
    t = RathilangTranslator()
    rathi_code = t.bf_2_rathi(bf_code)
    print(rathi_code)
