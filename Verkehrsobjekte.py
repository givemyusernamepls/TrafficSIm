#Main- und Map-Code für die einzelnen Verkehrsobjekte
"""
#Kreuzung Main
sim.create_road(ort, strecken_I, lim_30, 0)

#Kreuzung Map
ort_1 = {'1':(-10,40), '2':(-40,40), '3':(-40,10) ,'4':(-40,70), '5':(-70,40)}

ort = {}
for key in ort_1:
    value = ort_1[key]
    coord = (5 * value[0], -5 * value[1])
    ort[key] = coord
lim_30 = 8.3333
lim_50 = 13.8889
lim_70 = 19.4444


I = nx.MultiDiGraph()
strecken_I = [('1', '2', distance.euclidean(ort['1'], ort['2']) / lim_30),
              ('2', '1', distance.euclidean(ort['1'], ort['2']) / lim_30),
              ('3', '2', distance.euclidean(ort['3'], ort['2']) / lim_30),
              ('2', '3', distance.euclidean(ort['3'], ort['2']) / lim_30),
              ('4', '2', distance.euclidean(ort['4'], ort['2']) / lim_30),
              ('2', '4', distance.euclidean(ort['4'], ort['2']) / lim_30),
              ('5', '2', distance.euclidean(ort['5'], ort['2']) / lim_30),
              ('2', '5', distance.euclidean(ort['5'], ort['2']) / lim_30)]

I.add_weighted_edges_from(strecken_I)
nx.set_node_attributes(I, ort, 'pos')
starts = ['1', '3','4','5']
ends = starts
"""

"""
#Ampel Main
sim.create_road(ort, strecken_B, lim_30, 0)
sim.create_road(ort, strecken_A, lim_30, 1)
sim.create_road(ort, strecken_C, lim_30, 1)
sim.create_road(ort, strecken_D, lim_30, 0)
sim.create_signal('2')

#Ampel Map
ort_1 = {'1':(-10,40), '2':(-40,40), '3':(-40,10) ,'4':(-40,70), '5':(-70,40)}

ort = {}
for key in ort_1:
    value = ort_1[key]
    coord = (5 * value[0], -5 * value[1])
    ort[key] = coord

lim_30 = 8.3333

A = nx.MultiDiGraph()
B = nx.MultiDiGraph()
C = nx.MultiDiGraph()
D = nx.MultiDiGraph()

strecken_A = [('1', '2', distance.euclidean(ort['1'], ort['2']) / lim_30),
              ('2', '1', distance.euclidean(ort['1'], ort['2']) / lim_30)]
strecken_C = [('5', '2', distance.euclidean(ort['5'], ort['2']) / lim_30),
              ('2', '5', distance.euclidean(ort['5'], ort['2']) / lim_30)]
strecken_B = [('3', '2', distance.euclidean(ort['3'], ort['2']) / lim_30),
              ('2', '3', distance.euclidean(ort['3'], ort['2']) / lim_30)]
strecken_D = [('4', '2', distance.euclidean(ort['4'], ort['2']) / lim_30),
              ('2', '4', distance.euclidean(ort['4'], ort['2']) / lim_30)]
A.add_weighted_edges_from(strecken_A)
nx.set_node_attributes(A, ort, 'pos')
B.add_weighted_edges_from(strecken_B)
nx.set_node_attributes(B, ort, 'pos')
C.add_weighted_edges_from(strecken_C)
nx.set_node_attributes(C, ort, 'pos')
D.add_weighted_edges_from(strecken_D)
nx.set_node_attributes(B, ort, 'pos')

K = nx.compose(A,B)
J = nx.compose(C,K)
I = nx.compose(J,D)

starts = ['1','3','4','5']
ends = starts
"""

"""
#Kreisel Main
sim.create_road(ort, strecken_K, lim_30, 0)
sim.create_road(ort, strecken_S, lim_30, 1)

#Kreisel Map
ort_1 = {'K1':(-30,33), 'K2':(-33,36), 'K3':(-36,33), 'K4':(-33,30), 'S1':(-0,33), 'S2':(-33,66), 'S3':(-66,33), 'S4':(-33,0)}
ort = {}
for key in ort_1:
    value = ort_1[key]
    coord = (5 * value[0], -5 * value[1])
    ort[key] = coord

lim_30 = 8.3333
lim_50 = 13.8889
lim_70 = 19.4444

S = nx.MultiDiGraph()
K = nx.MultiDiGraph()
strecken_S = [('S1', 'K1', distance.euclidean(ort['S1'], ort['K1']) / lim_30),
              ('K1', 'S1', distance.euclidean(ort['S1'], ort['K1']) / lim_30),
              ('S2', 'K2', distance.euclidean(ort['S2'], ort['K2']) / lim_30),
              ('K2', 'S2', distance.euclidean(ort['S2'], ort['K2']) / lim_30),
              ('S3', 'K3', distance.euclidean(ort['S3'], ort['K3']) / lim_30),
              ('K3', 'S3', distance.euclidean(ort['S3'], ort['K3']) / lim_30),
              ('S4', 'K4', distance.euclidean(ort['S4'], ort['K4']) / lim_30),
              ('K4', 'S4', distance.euclidean(ort['S4'], ort['K4']) / lim_30)]

strecken_K = [('K1', 'K2', distance.euclidean(ort['K1'], ort['K2']) / lim_30),
              ('K2', 'K3', distance.euclidean(ort['K3'], ort['K2']) / lim_30),
              ('K3', 'K4', distance.euclidean(ort['K3'], ort['K4']) / lim_30),
              ('K4', 'K1', distance.euclidean(ort['K1'], ort['K4']) / lim_30)]

K.add_weighted_edges_from(strecken_K)
nx.set_node_attributes(K, ort, 'pos')
S.add_weighted_edges_from(strecken_S)
nx.set_node_attributes(S, ort, 'pos')

I = nx.compose(K,S)

starts = ['S1', 'S2', 'S3' ,'S4']
ends = starts
"""