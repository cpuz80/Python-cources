import Lection3Module as mymod

PAIRS = [
    ('pears','mars'),
    ('learning','quit'),
    ('птица','песок'),
    ('собака', 'собаководы'),
    ('длинношеее','короткошерстное'),
    ]

for s,t in PAIRS:
    print(s,t, mymod.funcld(s,t))

