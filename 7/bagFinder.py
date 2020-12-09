import pandas as pd
import networkx as nx

df = pd.read_csv('bags.txt', names=['s'], delimiter="|") # No real delimeter here. Just using this for easy reading.
df['color'] = df['s'].map(lambda x: x.split('bags')[0].strip())
df['rules'] = df['s'].map(lambda x: [] if 'no other bags' in x else [r.replace(".", "").replace(' bags', '').replace(' bag', '').strip().split(' ', 1)[1] for r in x.split('contain')[1].split(',')])
df['rules'] = df.apply(lambda row: [(row['s'].split(rule)[0].strip().split(' ')[-1], rule) for rule in row['rules']], axis=1)
pd.set_option("display.max_rows", None, "display.max_columns", None)

G = nx.DiGraph()
for index, row in df.iterrows():
    G.add_node(row['color'])

for index, row in df.iterrows():
    # print(row['rules'])
    for count, color in row['rules']:
        G.add_edge(row['color'], color, count=count)

# print(G.nodes())
print(G.in_edges('shiny gold'))
# print(G.in_edges('plaid purple'))


# # Part 1
# to_do = {'shiny gold'}
# done = set()
# while len(to_do) > 0:
#     # print(to_do)
#     item = to_do.pop()
#     done.add(item)
#     for source, sink in G.in_edges(item):
#         if source not in done:
#             to_do.add(source)
#
# print(len(done)-1)

# Part 2
def get_bag_count(G, item):
    sum = 0
    print(G.in_edges(item))
    for source, sink, d in G.out_edges(item, data=True):
        print(source + sink + str(d))
        sum += int(d['count'])*(get_bag_count(G, sink) + 1)
    return sum


print(get_bag_count(G, 'shiny gold'))
