#nouns

d_dict = {}
d_dict['1f'] = ['a', 'ae', 'ae', 'am', 'a', 'ae', 'amus', 'is', 'as', 'is']
d_dict['2m'] = ['us', 'i', 'o', 'um', 'o', 'i', 'orum', 'is', 'os', 'is']
d_dict['2n'] = ['um', 'i', 'o', 'um', 'o', 'a', 'orum', 'is', 'a', 'is']
d_dict['3m'] = ['', 'is', 'i', 'em', 'e', '', 'um', 'ibus', 'es', 'ibus']
d_dict['3f'] = ['', 'is', 'i', 'em', 'e', '', 'um', 'ibus', 'es', 'ibus']
d_dict['3n'] = ['', 'is', 'i', '', 'e', 'a', 'um', 'ibus', 'a', 'ibus']
d_dict['5m'] = ['es', 'ei', 'ei', 'em', 'e', 'es', 'erum', 'ebus', 'es', 'ebus']
d_dict['5f'] = ['es', 'ei', 'ei', 'em', 'e', 'es', 'erum', 'ebus', 'es', 'ebus']

#verbs
c_dict = {}
c_dict['0'] = ['', '', '', '', '', '', ''] #irregulars
c_dict['1'] = ['o', 'as', 'at', 'amus', 'atis', 'ant']
c_dict['2'] = ['eo', 'es', 'et', 'emus', 'etis', 'ent']
c_dict['3'] = ['o', 'is', 'it', 'imus', 'itis', 'unt']
c_dict['4'] = ['o', 's', 't', 'mus', 'tis', 'unt']

class Word():
    def __init__(self, root, cat, gpos, add):
        if gpos == 'v':
            self.pos = 'Verb'
        else:
            self.pos = 'Noun'
        if self.pos == 'Noun':
            self.gender = gpos
        self.root = root
        self.cat = cat
        if self.pos == 'Verb':
            self.tense = add[0]
            add = add[1:]
        self.add = add
        self.gen_forms()

    def gen_forms(self):
        ending_set = []
        if self.pos == 'Noun':
            ending_set = d_dict[self.cat + self.gender]
        if self.pos == 'Verb':
            ending_set = c_dict[self.cat]
        while len(self.add) < len(ending_set):
            self.add.append('')
        self.forms = []
        for i in range(len(ending_set)):
            if self.add[i] != '':
                self.forms.append(self.add[i])
            else:
                self.forms.append(self.root + ending_set[i])


#skipped loquor, loqueris in 2.1
#skipped velle, vult

