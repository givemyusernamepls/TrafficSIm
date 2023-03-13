import networkx as nx
from scipy.spatial import distance

G = nx.MultiDiGraph()
H = nx.MultiDiGraph()
K = nx.MultiDiGraph()
G_speed_lim = 13.8889
H_speed_lim = 13.8889
K_speed_lim = 13.8889
ort = {1:(-100, 0), 2:(0, 0), 3:(0, -100), 4:(0, 100),5:(100, 0)}
strecken_G = [(1, 2, (distance.euclidean(ort[1], ort[2])/G_speed_lim))]
strecken_H = [(3, 2, (distance.euclidean(ort[3], ort[2])/H_speed_lim)), (2, 4, (distance.euclidean(ort[2], ort[4])/H_speed_lim))]
strecken_K = [(5, 2, (distance.euclidean(ort[5], ort[2])/K_speed_lim))]
G.add_weighted_edges_from(strecken_G)
nx.set_node_attributes(G, ort, "pos")
H.add_weighted_edges_from(strecken_H)
nx.set_node_attributes(H, ort, "pos")
H.add_weighted_edges_from(strecken_K)
nx.set_node_attributes(K, ort, "pos")
J = nx.compose(G, H)
I = nx.compose(J, K)
strecken_I = strecken_G + strecken_H + strecken_K
