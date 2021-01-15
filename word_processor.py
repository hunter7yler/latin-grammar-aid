#nouns
# first = a, ae, ae, am, a, ae, amus, is, as, is
# second_m = us, i, o, um, o, i, orum, is, os, is
# second_n = um, i, o, um, o, a, orum, is, a, is
# third_mf = '', is, i, em, e, '', um, ibus, es, ibus
# third_ni = '', is, i, '', e, ia, ium, ibus, ia, ibus
# third_n = '', is, i, '', e, a, um, ibus, a, ibus

#verbs
# first = o, as, at, amus, atis, ant, are
# second = eo, es, et, emus, etis, ent, ere
# third = o, is, it, imus, itis, unt, ere
# fourth = o, s, t, mus, tis, unt


class Noun():
    def __init__(self):
        self.gender
        self.declension
        self.root
        self.forms

class Verb():
    def __init__(self):
        self.tense
        self.conjugation
        self.root
        self.forms