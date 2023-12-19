import polars as pl

list_pl =  [[i, 0, 'test'] for i in range(200)]
df = pl.DataFrame(list_pl, ['id', 'mes', 'name'])

inf = lambda x : x > 100

s = inf(df['id'])

print(df)
print(s)