import networkx as nx
from scipy.spatial import distance

# create subgraphs:
G = nx.MultiDiGraph()
H = nx.MultiDiGraph()
K = nx.MultiDiGraph()
Kreis = nx.MultiDiGraph()

# give speed limit to each individual subgraph:
G_speed_lim = 13.8889
H_speed_lim = 13.8889
K_speed_lim = 13.8889
Kreis_speed_lim = 13.8889

# list of nodes and their coordinates:
ort = {1:(-150, 0), 2:(0, 0), 3:(0, -150), 4:(0, 150), 5:(150, 0), 6:(25, 0), 7:(0, -25), 8:(0, 25), 9:(-25, 0)}

# list of edges with weight:
#strecken_G = [(1, 2, (distance.euclidean(ort[1], ort[2])/G_speed_lim)), (2, 1, (distance.euclidean(ort[2], ort[1])/G_speed_lim))]
#strecken_H = [(3, 2, (distance.euclidean(ort[3], ort[2])/H_speed_lim)), (2, 4, (distance.euclidean(ort[2], ort[4])/H_speed_lim)), (2, 3, (distance.euclidean(ort[2], ort[3])/H_speed_lim)), (4, 2, (distance.euclidean(ort[4], ort[2])/H_speed_lim))]
#strecken_K = [(5, 2, (distance.euclidean(ort[5], ort[2])/K_speed_lim)), (2, 5, (distance.euclidean(ort[2], ort[5])/K_speed_lim))]
strecken_G = [(1, 9, (distance.euclidean(ort[1], ort[9])/G_speed_lim)), (9, 1, (distance.euclidean(ort[9], ort[1])/G_speed_lim))]
strecken_H = [(3, 7, (distance.euclidean(ort[3], ort[7])/H_speed_lim)), (8, 4, (distance.euclidean(ort[8], ort[4])/H_speed_lim)), (7, 3, (distance.euclidean(ort[7], ort[3])/H_speed_lim)), (4, 8, (distance.euclidean(ort[4], ort[8])/H_speed_lim))]
strecken_K = [(5, 6, (distance.euclidean(ort[5], ort[6])/K_speed_lim)), (6, 5, (distance.euclidean(ort[6], ort[5])/K_speed_lim))]
strecken_Kreis = [(6, 7, (distance.euclidean(ort[6], ort[7])/Kreis_speed_lim)), (7, 9, (distance.euclidean(ort[7], ort[9])/Kreis_speed_lim)), (9, 8, (distance.euclidean(ort[9], ort[8])/Kreis_speed_lim)), (8, 6, (distance.euclidean(ort[8], ort[6])/Kreis_speed_lim))]

# add edges to corrwsponding subgraph:
G.add_weighted_edges_from(strecken_G)
nx.set_node_attributes(G, ort, "pos")
H.add_weighted_edges_from(strecken_H)
nx.set_node_attributes(H, ort, "pos")
K.add_weighted_edges_from(strecken_K)
nx.set_node_attributes(K, ort, "pos")
Kreis.add_weighted_edges_from(strecken_Kreis)
nx.set_node_attributes(Kreis, ort, "pos")

# combine all subgraphs to one graph:
J = nx.compose(G, H)
J_1 = nx.compose(J, Kreis)
I = nx.compose(J_1, K)
strecken_I = strecken_G + strecken_H + strecken_K + strecken_Kreis

# set start and endpoints:
starts = [1, 3, 4, 5]
ends = starts
