import Lection3Module as MyMod
pairs = [
    ('pears','mars'),
    ('learning','quit'),
    ('птица','песок'),
    ('собака', 'собаководы'),
    ('длинношеее','короткошерстное'),
    ]
for s,t in pairs:
    print(s,t, MyMod.FuncLD(s,t))

