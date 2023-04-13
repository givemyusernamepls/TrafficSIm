import networkx as nx
from scipy.spatial import distance

# create subgraphs:
R_70 = nx.MultiDiGraph()
R_50 = nx.MultiDiGraph()
O_50 = nx.MultiDiGraph()
O_30 = nx.MultiDiGraph()
Y_50 = nx.MultiDiGraph()
Y_30 = nx.MultiDiGraph()
G_50 = nx.MultiDiGraph()
G_30 = nx.MultiDiGraph()
B = nx.MultiDiGraph()
P = nx.MultiDiGraph()

# give speed limit to each individual subgraph:
lim_30 = 8.3333
lim_50 = 13.8889
lim_70 = 19.4444

# list of nodes and their coordinates:
ort_1 = {'R1':(230, 210), 'R2':(300, 200), 'R3':(350, 190), 'R4':(410, 180), 'R5':(490, 120), 'R6':(500, 80), 'R7':(520, 60), 'R8':(570, 20), 'R9':(590, 340), 'R10':(660, 280),
       'O1':(0, 0), 'O2':(40,40), 'O3':(110, 100), 'O4':(130, 120), 'O5':(150, 140), 'O6':(190, 180), 'O7':(260, 240), 'O8':(280, 260), 'O9':(280, 320), 'O10':(310, 330),
       'O11':(360, 350), 'O12':(370, 390), 'O13':(370, 420), 'O14':(380, 440), 'O15':(380, 470), 'O16':(390, 510), 'O17':(350, 220), 'O18':(400, 230), 'O19':(430, 220), 'O20':(460, 230),
       'O21':(490, 240), 'O22':(530, 250), 'O23':(540, 270), 'O24':(560, 300), 'O25':(620, 400), 'O26':(650, 440), 'O27':(480, 110), 'O28':(620, 100), 'O29':(690, 90), 'O30':(440, 20),
       'O31':(500, 0), 'O32':(650, 50),
       'Y1':(0, 150), 'Y2':(20, 150), 'Y3':(30, 120), 'Y4':(30, 90), 'Y5':(30, 60), 'Y6':(120, 90), 'Y7':(140, 110), 'Y8':(200, 70), 'Y9':(200, 120), 'Y10':(110, 240),
       'Y11':(130, 240), 'Y12':(180, 250), 'Y13':(180, 420), 'Y14':(200, 380), 'Y15':(250, 350), 'Y16':(320, 260), 'Y17':(340, 260), 'Y18':(400, 270), 'Y19':(420, 280), 'Y20':(440, 280),
       'Y21':(480, 290), 'Y22':(490, 260), 'Y23':(380, 350), 'Y24':(420, 350), 'Y25':(470, 370), 'Y26':(490, 380), 'Y27':(530, 390), 'Y28':(540, 410), 'Y29':(520, 420), 'Y30':(510, 450),
       'Y31':(500, 480), 'Y32':(470, 480), 'Y33':(430, 470), 'Y34':(330, 150), 'Y35':(580, 240), 'Y36':(620, 120), 'Y37':(660, 160),
       'G1':(10, 60), 'G2':(10, 90), 'G3':(10, 110), 'G4':(50, 90), 'G5':(50, 120), 'G6':(70, 90),'G7':(60, 120), 'G8':(60, 150), 'G9':(90, 150), 'G10':(110, 150),
       'G11':(140, 150), 'G12':(160, 170), 'G13':(80, 200), 'G14':(110, 200), 'G15':(130, 200), 'G16':(160, 200), 'G17':(170, 120), 'G18':(140, 80), 'G19':(160, 230), 'G20':(180, 220),
       'G21':(140, 370), 'G22':(280, 440), 'G23':(320, 460), 'G24':(280, 360), 'G25':(300, 370), 'G26':(340, 390), 'G27':(310, 300), 'G28':(320, 280), 'G29':(350, 310), 'G30':(370, 310),
       'G31':(390, 310), 'G32':(400, 300), 'G33':(420, 320), 'G34':(430, 320), 'G35':(420, 340), 'G36':(430, 390), 'G37':(430, 410), 'G38':(430, 430), 'G39':(430, 500), 'G40':(440, 430),
       'G41':(450, 450), 'G42':(470, 430), 'G43':(480, 420), 'G44':(490, 360), 'G45':(490, 340), 'G46':(490, 310), 'G47':(580, 430), 'G48':(540, 370), 'G49':(550, 350), 'G50':(520, 280),
       'G51':(330, 210), 'G52':(400, 160), 'G53':(490, 210),
       'B1':(280, 390), 'B2':(290, 410), 'B3':(290, 430), 'B4':(400, 430), 'B5':(270, 280), 'B6':(390, 380), 'B7':(440, 460), 'B8':(450, 390), 'B9':(470, 390), 'B10':(580, 410),
       'B11':(410, 320), 'B12':(510, 360), 'B13':(510, 340), 'B14':(530, 330), 'B15':(510, 300),
       'P1':(200, 230), 'P2':(270, 370), 'P3':(260, 450), 'P4':(290, 470), 'P5':(400, 410), 'P6':(510, 350)}

ort = {}
for key in ort_1:
    value = ort_1[key]
    coord = (5 * value[0], -5 * value[1])
    ort[key] = coord

# list of edges with weight:
strecken_R_50 = [('R1', 'R2', distance.euclidean(ort['R1'], ort['R2'])/lim_50), ('R2', 'R1', distance.euclidean(ort['R2'], ort['R1'])/lim_50), ('R3', 'R2', distance.euclidean(ort['R3'], ort['R2'])/lim_50), ('R2', 'R3', distance.euclidean(ort['R2'], ort['R3'])/lim_50), ('R3', 'R4', distance.euclidean(ort['R3'], ort['R4'])/lim_50), ('R4', 'R3', distance.euclidean(ort['R4'], ort['R3'])/lim_50), ('R5', 'R4', distance.euclidean(ort['R5'], ort['R4'])/lim_50), ('R4', 'R5', distance.euclidean(ort['R4'], ort['R5'])/lim_50),
                 ('R5', 'R6', distance.euclidean(ort['R5'], ort['R6'])/lim_50), ('R6', 'R5', distance.euclidean(ort['R6'], ort['R5'])/lim_50), ('R6', 'R7', distance.euclidean(ort['R6'], ort['R7'])/lim_50), ('R7', 'R6', distance.euclidean(ort['R7'], ort['R6'])/lim_50), ('R7', 'R8', distance.euclidean(ort['R7'], ort['R8'])/lim_50), ('R8', 'R7', distance.euclidean(ort['R8'], ort['R7'])/lim_50)]

strecken_R_70 = [('R9', 'R10', distance.euclidean(ort['R9'], ort['R10'])/lim_70), ('R10', 'R9', distance.euclidean(ort['R10'], ort['R9'])/lim_70)]

strecken_O_50 = [('O1', 'O2', distance.euclidean(ort['O1'], ort['O2'])/lim_50), ('O2', 'O1', distance.euclidean(ort['O2'], ort['O1'])/lim_50), ('O9', 'O10', distance.euclidean(ort['O9'], ort['O10'])/lim_50), ('O10', 'O9', distance.euclidean(ort['O10'], ort['O9'])/lim_50), ('O10', 'O11', distance.euclidean(ort['O10'], ort['O11'])/lim_50), ('O11', 'O10', distance.euclidean(ort['O11'], ort['O10'])/lim_50), ('O12', 'O11', distance.euclidean(ort['O12'], ort['O11'])/lim_50), ('O11', 'O12', distance.euclidean(ort['O11'], ort['O12'])/lim_50), ('O12', 'O13', distance.euclidean(ort['O12'], ort['O13'])/lim_50),
                 ('O13', 'O12', distance.euclidean(ort['O13'], ort['O12'])/lim_50), ('O13', 'O14', distance.euclidean(ort['O13'], ort['O14'])/lim_50), ('O14', 'O13', distance.euclidean(ort['O14'], ort['O13'])/lim_50), ('O15', 'O14', distance.euclidean(ort['O15'], ort['O14'])/lim_50), ('O14', 'O15', distance.euclidean(ort['O14'], ort['O15'])/lim_50), ('O15', 'O16', distance.euclidean(ort['O15'], ort['O16'])/lim_50), ('O16', 'O15', distance.euclidean(ort['O16'], ort['O15'])/lim_50), ('R5', 'O27', distance.euclidean(ort['R5'], ort['O27'])/lim_50), ('O27', 'R5', distance.euclidean(ort['O27'], ort['R5'])/lim_50),
                 ('O27', 'O28', distance.euclidean(ort['O27'], ort['O28'])/lim_50), ('O28', 'O27', distance.euclidean(ort['O28'], ort['O27'])/lim_50), ('O29', 'O28', distance.euclidean(ort['O29'], ort['O28'])/lim_50), ('O28', 'O29', distance.euclidean(ort['O28'], ort['O29'])/lim_50), ('R6', 'O32', distance.euclidean(ort['R6'], ort['O32'])/lim_50), ('O32', 'R6', distance.euclidean(ort['O32'], ort['R6'])/lim_50), ('O30', 'R6', distance.euclidean(ort['O30'], ort['R6'])/lim_50), ('R6', 'O30', distance.euclidean(ort['R6'], ort['O30'])/lim_50), ('R7', 'O31', distance.euclidean(ort['R7'], ort['O31'])/lim_50),
                 ('O31', 'R7', distance.euclidean(ort['O31'], ort['R7'])/lim_50), ('O19', 'O20', distance.euclidean(ort['O19'], ort['O20'])/lim_50), ('O20', 'O19', distance.euclidean(ort['O20'], ort['O19'])/lim_50), ('O20', 'O21', distance.euclidean(ort['O20'], ort['O21'])/lim_50), ('O21', 'O20', distance.euclidean(ort['O21'], ort['O20'])/lim_50), ('O21', 'O22', distance.euclidean(ort['O21'], ort['O22'])/lim_50), ('O22', 'O21', distance.euclidean(ort['O22'], ort['O21'])/lim_50), ('O22', 'O23', distance.euclidean(ort['O22'], ort['O23'])/lim_50), ('O23', 'O22', distance.euclidean(ort['O23'], ort['O22'])/lim_50),
                 ('O23', 'O24', distance.euclidean(ort['O23'], ort['O24'])/lim_50), ('O24', 'O23', distance.euclidean(ort['O24'], ort['O23'])/lim_50), ('O24', 'R9', distance.euclidean(ort['O24'], ort['R9'])/lim_50), ('R9', 'O24', distance.euclidean(ort['R9'], ort['O24'])/lim_50), ('R9', 'O25', distance.euclidean(ort['R9'], ort['O25'])/lim_50), ('O25', 'R9', distance.euclidean(ort['O25'], ort['R9'])/lim_50), ('O25', 'O26', distance.euclidean(ort['O25'], ort['O26'])/lim_50), ('O26', 'O25', distance.euclidean(ort['O26'], ort['O25'])/lim_50)]

strecken_O_30 = [('O2', 'O3', distance.euclidean(ort['O2'], ort['O3'])/lim_30), ('O3', 'O2', distance.euclidean(ort['O3'], ort['O2'])/lim_30), ('O4', 'O3', distance.euclidean(ort['O4'], ort['O3'])/lim_30), ('O3', 'O4', distance.euclidean(ort['O3'], ort['O4'])/lim_30), ('O4', 'O5', distance.euclidean(ort['O4'], ort['O5'])/lim_30), ('O5', 'O4', distance.euclidean(ort['O5'], ort['O4'])/lim_30), ('O5', 'O6', distance.euclidean(ort['O5'], ort['O6'])/lim_30), ('O6', 'O5', distance.euclidean(ort['O6'], ort['O5'])/lim_30), ('O6', 'R1', distance.euclidean(ort['O6'], ort['R1'])/lim_30), ('R1', 'O6', distance.euclidean(ort['R1'], ort['O6'])/lim_30),
                 ('R1', 'O7', distance.euclidean(ort['R1'], ort['O7'])/lim_30), ('O7', 'R1', distance.euclidean(ort['O7'], ort['R1'])/lim_30), ('O7', 'O8', distance.euclidean(ort['O7'], ort['O8'])/lim_30), ('O8', 'O7', distance.euclidean(ort['O8'], ort['O7'])/lim_30), ('O8', 'O9', distance.euclidean(ort['O8'], ort['O9'])/lim_30), ('O9', 'O8', distance.euclidean(ort['O9'], ort['O8'])/lim_30), ('R3', 'O17', distance.euclidean(ort['R3'], ort['O17'])/lim_30), ('O17', 'R3', distance.euclidean(ort['O17'], ort['R3'])/lim_30), ('O17', 'O18', distance.euclidean(ort['O17'], ort['O18'])/lim_30), ('O18', 'O17', distance.euclidean(ort['O18'], ort['O17'])/lim_30),
                 ('O18', 'O19', distance.euclidean(ort['O18'], ort['O19'])/lim_30), ('O19', 'O18', distance.euclidean(ort['O19'], ort['O18'])/lim_30)]

strecken_Y_50 = [('Y1', 'Y2', distance.euclidean(ort['Y1'], ort['Y2'])/lim_50), ('Y2', 'Y1', distance.euclidean(ort['Y2'], ort['Y1'])/lim_50), ('Y3', 'Y2', distance.euclidean(ort['Y3'], ort['Y2'])/lim_50), ('Y2', 'Y3', distance.euclidean(ort['Y2'], ort['Y3'])/lim_50), ('Y3', 'Y4', distance.euclidean(ort['Y3'], ort['Y4'])/lim_50), ('Y4', 'Y3', distance.euclidean(ort['Y4'], ort['Y3'])/lim_50), ('Y4', 'Y5', distance.euclidean(ort['Y4'], ort['Y5'])/lim_50), ('Y5', 'Y4', distance.euclidean(ort['Y5'], ort['Y4'])/lim_50), ('Y5', 'O2', distance.euclidean(ort['Y5'], ort['O2'])/lim_50), ('O2', 'Y5', distance.euclidean(ort['O2'], ort['Y5'])/lim_50),
                 ('Y13', 'Y14', distance.euclidean(ort['Y13'], ort['Y14'])/lim_50), ('Y14', 'Y13', distance.euclidean(ort['Y14'], ort['Y13'])/lim_50), ('Y15', 'Y14', distance.euclidean(ort['Y15'], ort['Y14'])/lim_50), ('Y14', 'Y15', distance.euclidean(ort['Y14'], ort['Y15'])/lim_50), ('Y15', 'O9', distance.euclidean(ort['Y15'], ort['O9'])/lim_50), ('O9', 'Y15', distance.euclidean(ort['O9'], ort['Y15'])/lim_50), ('R2', 'Y16', distance.euclidean(ort['R2'], ort['Y16'])/lim_50), ('Y16', 'R2', distance.euclidean(ort['Y16'], ort['R2'])/lim_50), ('Y16', 'Y17', distance.euclidean(ort['Y16'], ort['Y17'])/lim_50), ('Y17', 'Y16', distance.euclidean(ort['Y17'], ort['Y16'])/lim_50),
                 ('Y17', 'Y18', distance.euclidean(ort['Y17'], ort['Y18'])/lim_50), ('Y18', 'Y17', distance.euclidean(ort['Y18'], ort['Y17'])/lim_50), ('Y18', 'Y19', distance.euclidean(ort['Y18'], ort['Y19'])/lim_50), ('Y19', 'Y18', distance.euclidean(ort['Y19'], ort['Y18'])/lim_50), ('Y19', 'Y20', distance.euclidean(ort['Y19'], ort['Y20'])/lim_50), ('Y20', 'Y19', distance.euclidean(ort['Y20'], ort['Y19'])/lim_50), ('Y20', 'Y21', distance.euclidean(ort['Y20'], ort['Y21'])/lim_50), ('Y21', 'Y20', distance.euclidean(ort['Y21'], ort['Y20'])/lim_50), ('O11', 'Y23', distance.euclidean(ort['O11'], ort['Y23'])/lim_50), ('Y23', 'O11', distance.euclidean(ort['Y23'], ort['O11'])/lim_50),
                 ('Y23', 'Y24', distance.euclidean(ort['Y23'], ort['Y24'])/lim_50), ('Y24', 'Y23', distance.euclidean(ort['Y24'], ort['Y23'])/lim_50), ('Y24', 'Y25', distance.euclidean(ort['Y24'], ort['Y25'])/lim_50), ('Y25', 'Y24', distance.euclidean(ort['Y25'], ort['Y24'])/lim_50), ('Y25', 'Y26', distance.euclidean(ort['Y25'], ort['Y26'])/lim_50), ('Y26', 'Y25', distance.euclidean(ort['Y26'], ort['Y25'])/lim_50), ('Y26', 'Y27', distance.euclidean(ort['Y26'], ort['Y27'])/lim_50), ('Y27', 'Y26', distance.euclidean(ort['Y27'], ort['Y26'])/lim_50), ('Y28', 'Y29', distance.euclidean(ort['Y28'], ort['Y29'])/lim_50), ('Y29', 'Y28', distance.euclidean(ort['Y29'], ort['Y28'])/lim_50),
                 ('Y29', 'Y30', distance.euclidean(ort['Y29'], ort['Y30'])/lim_50), ('Y30', 'Y29', distance.euclidean(ort['Y30'], ort['Y29'])/lim_50), ('Y30', 'Y31', distance.euclidean(ort['Y30'], ort['Y31'])/lim_50), ('Y31', 'Y30', distance.euclidean(ort['Y31'], ort['Y30'])/lim_50), ('Y32', 'Y31', distance.euclidean(ort['Y32'], ort['Y31'])/lim_50), ('Y31', 'Y32', distance.euclidean(ort['Y31'], ort['Y32'])/lim_50), ('Y32', 'Y33', distance.euclidean(ort['Y32'], ort['Y33'])/lim_50), ('Y33', 'Y32', distance.euclidean(ort['Y33'], ort['Y32'])/lim_50), ('Y33', 'O15', distance.euclidean(ort['Y33'], ort['O15'])/lim_50), ('O15', 'Y33', distance.euclidean(ort['O15'], ort['Y33'])/lim_50),
                 ('Y36', 'R5', distance.euclidean(ort['Y36'], ort['R5'])/lim_50), ('R5', 'Y36', distance.euclidean(ort['R5'], ort['Y36'])/lim_50), ('O28', 'Y36', distance.euclidean(ort['O28'], ort['Y36'])/lim_50), ('Y36', 'O28', distance.euclidean(ort['Y36'], ort['O28'])/lim_50), ('Y36', 'Y37', distance.euclidean(ort['Y36'], ort['Y37'])/lim_50), ('Y37', 'Y36', distance.euclidean(ort['Y37'], ort['Y36'])/lim_50)]

strecken_Y_30 = [('Y10', 'Y11', distance.euclidean(ort['Y10'], ort['Y11'])/lim_30), ('Y11', 'Y10', distance.euclidean(ort['Y11'], ort['Y10'])/lim_30), ('Y12', 'Y11', distance.euclidean(ort['Y12'], ort['Y11'])/lim_30), ('Y11', 'Y12', distance.euclidean(ort['Y11'], ort['Y12'])/lim_30), ('O8', 'Y12', distance.euclidean(ort['O8'], ort['Y12'])/lim_30), ('O3', 'Y6', distance.euclidean(ort['O3'], ort['Y6'])/lim_30), ('Y6', 'O3', distance.euclidean(ort['Y6'], ort['O3'])/lim_30), ('Y6', 'Y7', distance.euclidean(ort['Y6'], ort['Y7'])/lim_30), ('Y7', 'Y6', distance.euclidean(ort['Y7'], ort['Y6'])/lim_30), ('Y7', 'O4', distance.euclidean(ort['Y7'], ort['O4'])/lim_30),
                 ('O6', 'Y9', distance.euclidean(ort['O6'], ort['Y9'])/lim_30), ('Y9', 'O6', distance.euclidean(ort['Y9'], ort['O6'])/lim_30), ('Y8', 'Y9', distance.euclidean(ort['Y8'], ort['Y9'])/lim_30), ('Y9', 'Y8', distance.euclidean(ort['Y9'], ort['Y8'])/lim_30), ('R2', 'Y34', distance.euclidean(ort['R2'], ort['Y34'])/lim_30), ('Y34', 'R2', distance.euclidean(ort['Y34'], ort['R2'])/lim_30), ('Y34', 'R3', distance.euclidean(ort['Y34'], ort['R3'])/lim_30), ('Y22', 'Y21', distance.euclidean(ort['Y22'], ort['Y21'])/lim_30), ('Y21', 'Y22', distance.euclidean(ort['Y21'], ort['Y22'])/lim_30), ('O21', 'Y22', distance.euclidean(ort['O21'], ort['Y22'])/lim_30),
                 ('Y22', 'O21', distance.euclidean(ort['Y22'], ort['O21'])/lim_30), ('O22', 'Y35', distance.euclidean(ort['O22'], ort['Y35'])/lim_30), ('Y35', 'O22', distance.euclidean(ort['Y35'], ort['O22'])/lim_30), ('R9', 'Y28', distance.euclidean(ort['R9'], ort['Y28'])/lim_30)]

strecken_G_50 = [('G8', 'Y2', distance.euclidean(ort['G8'], ort['Y2'])/lim_50), ('O15', 'G23', distance.euclidean(ort['O15'], ort['G23'])/lim_50), ('G23', 'O15', distance.euclidean(ort['G23'], ort['O15'])/lim_50), ('G23', 'G22', distance.euclidean(ort['G23'], ort['G22'])/lim_50), ('G22', 'G23', distance.euclidean(ort['G22'], ort['G23'])/lim_50), ('Y14', 'G22', distance.euclidean(ort['Y14'], ort['G22'])/lim_50), ('G22', 'Y14', distance.euclidean(ort['G22'], ort['Y14'])/lim_50), ('Y14', 'G21', distance.euclidean(ort['Y14'], ort['G21'])/lim_50), ('G21', 'Y14', distance.euclidean(ort['G21'], ort['Y14'])/lim_50), ('G46', 'Y21', distance.euclidean(ort['G46'], ort['Y21'])/lim_50),
                 ('Y21', 'G46', distance.euclidean(ort['Y21'], ort['G46'])/lim_50), ('G45', 'G46', distance.euclidean(ort['G45'], ort['G46'])/lim_50), ('G46', 'G45', distance.euclidean(ort['G46'], ort['G45'])/lim_50), ('G44', 'G45', distance.euclidean(ort['G44'], ort['G45'])/lim_50), ('G45', 'G44', distance.euclidean(ort['G45'], ort['G44'])/lim_50), ('G44', 'Y26', distance.euclidean(ort['G44'], ort['Y26'])/lim_50), ('Y26', 'G44', distance.euclidean(ort['Y26'], ort['G44'])/lim_50), ('Y24', 'G36', distance.euclidean(ort['Y24'], ort['G36'])/lim_50), ('G36', 'Y24', distance.euclidean(ort['G36'], ort['Y24'])/lim_50), ('G36', 'G37', distance.euclidean(ort['G36'], ort['G37'])/lim_50),
                 ('G37', 'G36', distance.euclidean(ort['G37'], ort['G36'])/lim_50), ('G37', 'G38', distance.euclidean(ort['G37'], ort['G38'])/lim_50), ('G38', 'G37', distance.euclidean(ort['G38'], ort['G37'])/lim_50), ('G38', 'Y33', distance.euclidean(ort['G38'], ort['Y33'])/lim_50), ('Y33', 'G38', distance.euclidean(ort['Y33'], ort['G38'])/lim_50), ('Y33', 'G39', distance.euclidean(ort['Y33'], ort['G39'])/lim_50), ('G39', 'Y33', distance.euclidean(ort['G39'], ort['Y33'])/lim_50)]

strecken_G_30 = [('G3', 'Y3', distance.euclidean(ort['G3'], ort['Y3'])/lim_30), ('Y3', 'G3', distance.euclidean(ort['Y3'], ort['G3'])/lim_30), ('G2', 'Y4', distance.euclidean(ort['G2'], ort['Y4'])/lim_30), ('Y4', 'G2', distance.euclidean(ort['Y4'], ort['G2'])/lim_30), ('G1', 'Y5', distance.euclidean(ort['G1'], ort['Y5'])/lim_30), ('Y5', 'G1', distance.euclidean(ort['Y5'], ort['G1'])/lim_30), ('G4', 'Y4', distance.euclidean(ort['G4'], ort['Y4'])/lim_30), ('Y4', 'G4', distance.euclidean(ort['Y4'], ort['G4'])/lim_30), ('G5', 'Y3', distance.euclidean(ort['G5'], ort['Y3'])/lim_30), ('Y3', 'G5', distance.euclidean(ort['Y3'], ort['G5'])/lim_30), ('G18', 'Y6', distance.euclidean(ort['G18'], ort['Y6'])/lim_30),
                 ('Y6', 'G18', distance.euclidean(ort['Y6'], ort['G18'])/lim_30), ('G17', 'Y7', distance.euclidean(ort['G17'], ort['Y7'])/lim_30), ('Y7', 'G17', distance.euclidean(ort['Y7'], ort['G17'])/lim_30), ('G17', 'Y9', distance.euclidean(ort['G17'], ort['Y9'])/lim_30), ('Y9', 'G17', distance.euclidean(ort['Y9'], ort['G17'])/lim_30), ('G4', 'G6', distance.euclidean(ort['G4'], ort['G6'])/lim_30), ('G6', 'G4', distance.euclidean(ort['G6'], ort['G4'])/lim_30), ('G5', 'G7', distance.euclidean(ort['G5'], ort['G7'])/lim_30), ('G7', 'G5', distance.euclidean(ort['G7'], ort['G5'])/lim_30), ('G12', 'G11', distance.euclidean(ort['G12'], ort['G11'])/lim_30), ('O6', 'G12', distance.euclidean(ort['O6'], ort['G12'])/lim_30),
                 ('G11', 'G10', distance.euclidean(ort['G11'], ort['G10'])/lim_30), ('G10', 'G9', distance.euclidean(ort['G10'], ort['G9'])/lim_30), ('G9', 'G8', distance.euclidean(ort['G9'], ort['G8'])/lim_30), ('R1', 'G20', distance.euclidean(ort['R1'], ort['G20'])/lim_30), ('G13', 'G14', distance.euclidean(ort['G13'], ort['G14'])/lim_30), ('G14', 'G13', distance.euclidean(ort['G14'], ort['G13'])/lim_30), ('G14', 'G15', distance.euclidean(ort['G14'], ort['G15'])/lim_30), ('G15', 'G14', distance.euclidean(ort['G15'], ort['G14'])/lim_30), ('G15', 'G16', distance.euclidean(ort['G15'], ort['G16'])/lim_30), ('G16', 'G15', distance.euclidean(ort['G16'], ort['G15'])/lim_30), ('Y12', 'O7', distance.euclidean(ort['Y12'], ort['O7'])/lim_30),
                 ('Y11', 'G19', distance.euclidean(ort['Y11'], ort['G19'])/lim_30), ('G19', 'Y11', distance.euclidean(ort['G19'], ort['Y11'])/lim_30), ('G19', 'G20', distance.euclidean(ort['G19'], ort['G20'])/lim_30), ('G20', 'G19', distance.euclidean(ort['G20'], ort['G19'])/lim_30), ('Y15', 'G24', distance.euclidean(ort['Y15'], ort['G24'])/lim_30), ('G24', 'G25', distance.euclidean(ort['G24'], ort['G25'])/lim_30), ('G25', 'O10', distance.euclidean(ort['G25'], ort['O10'])/lim_30), ('G26', 'G25', distance.euclidean(ort['G26'], ort['G25'])/lim_30), ('O10', 'G27', distance.euclidean(ort['O10'], ort['G27'])/lim_30), ('G27', 'O10', distance.euclidean(ort['G27'], ort['O10'])/lim_30), ('G28', 'Y16', distance.euclidean(ort['G28'], ort['Y16'])/lim_30),
                 ('Y16', 'G28', distance.euclidean(ort['Y16'], ort['G28'])/lim_30), ('Y17', 'G51', distance.euclidean(ort['Y17'], ort['G51'])/lim_30), ('G51', 'Y17', distance.euclidean(ort['G51'], ort['Y17'])/lim_30), ('O17', 'G51', distance.euclidean(ort['O17'], ort['G51'])/lim_30), ('G51', 'O17', distance.euclidean(ort['G51'], ort['O17'])/lim_30), ('G52', 'R4', distance.euclidean(ort['G52'], ort['R4'])/lim_30), ('R4', 'G52', distance.euclidean(ort['R4'], ort['G52'])/lim_30), ('R4', 'O19', distance.euclidean(ort['R4'], ort['O19'])/lim_30), ('O19', 'R4', distance.euclidean(ort['O19'], ort['R4'])/lim_30), ('O19', 'Y19', distance.euclidean(ort['O19'], ort['Y19'])/lim_30), ('Y19', 'O19', distance.euclidean(ort['Y19'], ort['O19'])/lim_30),
                 ('Y19', 'G33', distance.euclidean(ort['Y19'], ort['G33'])/lim_30), ('G33', 'Y19', distance.euclidean(ort['G33'], ort['Y19'])/lim_30), ('G33', 'G35', distance.euclidean(ort['G33'], ort['G35'])/lim_30), ('G35', 'G33', distance.euclidean(ort['G35'], ort['G33'])/lim_30), ('Y23', 'G30', distance.euclidean(ort['Y23'], ort['G30'])/lim_30), ('G30', 'Y23', distance.euclidean(ort['G30'], ort['Y23'])/lim_30), ('G29', 'G30', distance.euclidean(ort['G29'], ort['G30'])/lim_30), ('G30', 'G29', distance.euclidean(ort['G30'], ort['G29'])/lim_30), ('G30', 'G31', distance.euclidean(ort['G30'], ort['G31'])/lim_30), ('G31', 'G30', distance.euclidean(ort['G31'], ort['G30'])/lim_30), ('G32', 'Y18', distance.euclidean(ort['G32'], ort['Y18'])/lim_30),
                 ('Y18', 'G32', distance.euclidean(ort['Y18'], ort['G32'])/lim_30), ('Y18', 'O18', distance.euclidean(ort['Y18'], ort['O18'])/lim_30), ('O18', 'Y18', distance.euclidean(ort['O18'], ort['Y18'])/lim_30), ('O20', 'Y20', distance.euclidean(ort['O20'], ort['Y20'])/lim_30), ('G34', 'Y20', distance.euclidean(ort['G34'], ort['Y20'])/lim_30), ('Y20', 'G34', distance.euclidean(ort['Y20'], ort['G34'])/lim_30), ('G37', 'G40', distance.euclidean(ort['G37'], ort['G40'])/lim_30), ('G40', 'G41', distance.euclidean(ort['G40'], ort['G41'])/lim_30), ('G41', 'Y32', distance.euclidean(ort['G41'], ort['Y32'])/lim_30), ('Y26', 'G43', distance.euclidean(ort['Y26'], ort['G43'])/lim_30), ('G42', 'G43', distance.euclidean(ort['G42'], ort['G43'])/lim_30),
                 ('G43', 'G42', distance.euclidean(ort['G43'], ort['G42'])/lim_30), ('G42', 'Y31', distance.euclidean(ort['G42'], ort['Y31'])/lim_30), ('Y31', 'G42', distance.euclidean(ort['Y31'], ort['G42'])/lim_30), ('G53', 'O21', distance.euclidean(ort['G53'], ort['O21'])/lim_30), ('O21', 'G53', distance.euclidean(ort['O21'], ort['G53'])/lim_30), ('Y22', 'G50', distance.euclidean(ort['Y22'], ort['G50'])/lim_30), ('G50', 'Y22', distance.euclidean(ort['G50'], ort['Y22'])/lim_30), ('G50', 'O23', distance.euclidean(ort['G50'], ort['O23'])/lim_30), ('O23', 'G50', distance.euclidean(ort['O23'], ort['G50'])/lim_30), ('O25', 'G47', distance.euclidean(ort['O25'], ort['G47'])/lim_30), ('G47', 'O25', distance.euclidean(ort['G47'], ort['O25'])/lim_30),
                 ('G47', 'Y28', distance.euclidean(ort['G47'], ort['Y28'])/lim_30), ('Y28', 'G47', distance.euclidean(ort['Y28'], ort['G47'])/lim_30), ('Y28', 'Y27', distance.euclidean(ort['Y28'], ort['Y27'])/lim_30), ('Y27', 'Y28', distance.euclidean(ort['Y27'], ort['Y28'])/lim_30), ('G48', 'Y27', distance.euclidean(ort['G48'], ort['Y27'])/lim_30), ('Y27', 'G48', distance.euclidean(ort['Y27'], ort['G48'])/lim_30), ('G48', 'G49', distance.euclidean(ort['G48'], ort['G49'])/lim_30), ('G49', 'G48', distance.euclidean(ort['G49'], ort['G48'])/lim_30), ('G49', 'R9', distance.euclidean(ort['G49'], ort['R9'])/lim_30), ('R9', 'G49', distance.euclidean(ort['R9'], ort['G49'])/lim_30)]

strecken_B = [('G6', 'G7', distance.euclidean(ort['G6'], ort['G7'])/lim_30), ('G7', 'G6', distance.euclidean(ort['G7'], ort['G6'])/lim_30), ('G5', 'G4', distance.euclidean(ort['G5'], ort['G4'])/lim_30), ('G8', 'G7', distance.euclidean(ort['G8'], ort['G7'])/lim_30), ('G9', 'G13', distance.euclidean(ort['G9'], ort['G13'])/lim_30), ('G13', 'G9', distance.euclidean(ort['G13'], ort['G9'])/lim_30), ('G10', 'G14', distance.euclidean(ort['G10'], ort['G14'])/lim_30), ('G14', 'G10', distance.euclidean(ort['G14'], ort['G10'])/lim_30), ('G14', 'Y10', distance.euclidean(ort['G14'], ort['Y10'])/lim_30), ('Y10', 'G14', distance.euclidean(ort['Y10'], ort['G14'])/lim_30), ('O5', 'G11', distance.euclidean(ort['O5'], ort['G11'])/lim_30),
              ('G11', 'O5', distance.euclidean(ort['G11'], ort['O5'])/lim_30), ('G11', 'G15', distance.euclidean(ort['G11'], ort['G15'])/lim_30), ('G15', 'G11', distance.euclidean(ort['G15'], ort['G11'])/lim_30), ('G15', 'Y11', distance.euclidean(ort['G15'], ort['Y11'])/lim_30), ('Y11', 'G15', distance.euclidean(ort['Y11'], ort['G15'])/lim_30), ('G16', 'G12', distance.euclidean(ort['G16'], ort['G12'])/lim_30), ('G12', 'G16', distance.euclidean(ort['G12'], ort['G16'])/lim_30), ('G16', 'G19', distance.euclidean(ort['G16'], ort['G19'])/lim_30), ('G19', 'G16', distance.euclidean(ort['G19'], ort['G16'])/lim_30), ('O6', 'G20', distance.euclidean(ort['O6'], ort['G20'])/lim_30), ('G20', 'O6', distance.euclidean(ort['G20'], ort['O6'])/lim_30),
              ('G20', 'Y12', distance.euclidean(ort['G20'], ort['Y12'])/lim_30), ('Y12', 'G20', distance.euclidean(ort['Y12'], ort['G20'])/lim_30), ('O8', 'B5', distance.euclidean(ort['O8'], ort['B5'])/lim_30), ('B5', 'O8', distance.euclidean(ort['B5'], ort['O8'])/lim_30), ('Y14', 'B1', distance.euclidean(ort['Y14'], ort['B1'])/lim_30), ('G44', 'G35', distance.euclidean(ort['G44'], ort['G35'])/lim_30), ('G26', 'B1', distance.euclidean(ort['G26'], ort['B1'])/lim_30), ('B1', 'G26', distance.euclidean(ort['B1'], ort['G26'])/lim_30), ('B1', 'B2', distance.euclidean(ort['B1'], ort['B2'])/lim_30), ('B2', 'B1', distance.euclidean(ort['B2'], ort['B1'])/lim_30), ('B2', 'B3', distance.euclidean(ort['B2'], ort['B3'])/lim_30),
              ('B3', 'B2', distance.euclidean(ort['B3'], ort['B2'])/lim_30), ('B3', 'G22', distance.euclidean(ort['B3'], ort['G22'])/lim_30), ('G22', 'B3', distance.euclidean(ort['G22'], ort['B3'])/lim_30), ('B3', 'O13', distance.euclidean(ort['B3'], ort['O13'])/lim_30), ('O13', 'B3', distance.euclidean(ort['O13'], ort['B3'])/lim_30), ('O12', 'B6', distance.euclidean(ort['O12'], ort['B6'])/lim_30), ('B6', 'O12', distance.euclidean(ort['B6'], ort['O12'])/lim_30), ('O14', 'B4', distance.euclidean(ort['O14'], ort['B4'])/lim_30), ('B4', 'O14', distance.euclidean(ort['B4'], ort['O14'])/lim_30), ('B4', 'G38', distance.euclidean(ort['B4'], ort['G38'])/lim_30), ('G38', 'B4', distance.euclidean(ort['G38'], ort['B4'])/lim_30),
              ('G41', 'B7', distance.euclidean(ort['G41'], ort['B7'])/lim_30), ('B7', 'G41', distance.euclidean(ort['B7'], ort['G41'])/lim_30), ('G43', 'G37', distance.euclidean(ort['G43'], ort['G37'])/lim_30), ('G43', 'Y29', distance.euclidean(ort['G43'], ort['Y29'])/lim_30), ('G42', 'G40', distance.euclidean(ort['G42'], ort['G40'])/lim_30), ('G42', 'Y30', distance.euclidean(ort['G42'], ort['Y30'])/lim_30), ('Y30', 'G42', distance.euclidean(ort['Y30'], ort['G42'])/lim_30), ('G36', 'B8', distance.euclidean(ort['G36'], ort['B8'])/lim_30), ('B8', 'G36', distance.euclidean(ort['B8'], ort['G36'])/lim_30), ('B9', 'Y25', distance.euclidean(ort['B9'], ort['Y25'])/lim_30), ('Y25', 'B9', distance.euclidean(ort['Y25'], ort['B9'])/lim_30),
              ('B11', 'G33', distance.euclidean(ort['B11'], ort['G33'])/lim_30), ('G33', 'B11', distance.euclidean(ort['G33'], ort['B11'])/lim_30), ('G33', 'G34', distance.euclidean(ort['G33'], ort['G34'])/lim_30), ('G34', 'G33', distance.euclidean(ort['G34'], ort['G33'])/lim_30), ('G34', 'G45', distance.euclidean(ort['G34'], ort['G45'])/lim_30), ('G45', 'G34', distance.euclidean(ort['G45'], ort['G34'])/lim_30), ('G45', 'B13', distance.euclidean(ort['G45'], ort['B13'])/lim_30), ('B13', 'G45', distance.euclidean(ort['B13'], ort['G45'])/lim_30), ('B13', 'G49', distance.euclidean(ort['B13'], ort['G49'])/lim_30), ('G49', 'B13', distance.euclidean(ort['G49'], ort['B13'])/lim_30), ('B12', 'G48', distance.euclidean(ort['B12'], ort['G48'])/lim_30),
              ('G48', 'B12', distance.euclidean(ort['G48'], ort['B12'])/lim_30), ('B12', 'G44', distance.euclidean(ort['B12'], ort['G44'])/lim_30), ('G44', 'B12', distance.euclidean(ort['G44'], ort['B12'])/lim_30), ('G46', 'B14', distance.euclidean(ort['G46'], ort['B14'])/lim_30), ('B14', 'G46', distance.euclidean(ort['B14'], ort['G46'])/lim_30), ('B14', 'O24', distance.euclidean(ort['B14'], ort['O24'])/lim_30), ('O24', 'B14', distance.euclidean(ort['O24'], ort['B14'])/lim_30), ('B15', 'G50', distance.euclidean(ort['B15'], ort['G50'])/lim_30), ('G50', 'B15', distance.euclidean(ort['G50'], ort['B15'])/lim_30), ('B10', 'G47', distance.euclidean(ort['B10'], ort['G47'])/lim_30), ('G47', 'B10', distance.euclidean(ort['G47'], ort['B10'])/lim_30)]

strecken_P = [('Y12', 'P1', distance.euclidean(ort['Y12'], ort['P1'])/lim_30), ('P1', 'Y12', distance.euclidean(ort['P1'], ort['Y12'])/lim_30), ('P2', 'G24', distance.euclidean(ort['P2'], ort['G24'])/lim_30), ('G24', 'P2', distance.euclidean(ort['G24'], ort['P2'])/lim_30), ('P2', 'B1', distance.euclidean(ort['P2'], ort['B1'])/lim_30), ('B1', 'P2', distance.euclidean(ort['B1'], ort['P2'])/lim_30), ('G22', 'P3', distance.euclidean(ort['G22'], ort['P3'])/lim_30), ('P3', 'G22', distance.euclidean(ort['P3'], ort['G22'])/lim_30), ('G22', 'P4', distance.euclidean(ort['G22'], ort['P4'])/lim_30), ('P4', 'G22', distance.euclidean(ort['P4'], ort['G22'])/lim_30), ('B4', 'P5', distance.euclidean(ort['B4'], ort['P5'])/lim_30),
              ('P5', 'B4', distance.euclidean(ort['P5'], ort['B4'])/lim_30), ('B12', 'P6', distance.euclidean(ort['B12'], ort['P6'])/lim_30), ('P6', 'B12', distance.euclidean(ort['P6'], ort['B12'])/lim_30), ('B13', 'P6', distance.euclidean(ort['B13'], ort['P6'])/lim_30), ('P6', 'B13', distance.euclidean(ort['P6'], ort['B13'])/lim_30)]

# add edges to corresponding subgraph:
R_50.add_weighted_edges_from(strecken_R_50)
nx.set_node_attributes(R_50, ort, 'pos')
R_70.add_weighted_edges_from(strecken_R_70)
nx.set_node_attributes(R_70, ort, 'pos')
O_50.add_weighted_edges_from(strecken_O_50)
nx.set_node_attributes(O_50, ort, 'pos')
O_30.add_weighted_edges_from(strecken_O_30)
nx.set_node_attributes(O_30, ort, 'pos')
Y_50.add_weighted_edges_from(strecken_Y_50)
nx.set_node_attributes(Y_50, ort, 'pos')
Y_30.add_weighted_edges_from(strecken_Y_30)
nx.set_node_attributes(Y_30, ort, 'pos')
G_50.add_weighted_edges_from(strecken_G_50)
nx.set_node_attributes(G_50, ort, 'pos')
G_30.add_weighted_edges_from(strecken_G_30)
nx.set_node_attributes(G_30, ort, 'pos')
B.add_weighted_edges_from(strecken_B)
nx.set_node_attributes(B, ort, 'pos')
P.add_weighted_edges_from(strecken_P)
nx.set_node_attributes(P, ort, 'pos')

# combine all subgraphs to one graph:
Sub_1 = nx.compose(R_50, R_70)
Sub_2 = nx.compose(O_50, O_30)
Sub_3 = nx.compose(Y_30, Y_50)
Sub_4 = nx.compose(Sub_2, Sub_3)
Sub_5 = nx.compose(G_30, G_50)
Sub_6 = nx.compose(B, P)
Sub_7 = nx.compose(Sub_5, Sub_6)
Sub_8 = nx.compose(Sub_4, Sub_7)
I = nx.compose(Sub_8, Sub_1)

# set start and endpoints:
starts = ['O1', 'O1', 'O1', 'O1', 'O1', 'O1', 'O1', 'O1', 'O1', 'O1', 'G1', 'G2', 'G3', 'Y1', 'Y1', 'Y1', 'Y1', 'Y1', 'G6', 'G13', 'G16', 'Y10', 'G18', 'G17', 'Y8', 'P1', 'G21', 'G21', 'G21', 'G21', 'G21', 'Y13', 'Y13', 'Y13', 'Y13', 'Y13', 'Y13', 'Y13', 'Y13', 'Y13', 'Y13', 'P2', 'B2', 'P4', 'P3', 'P5',
          'O16', 'O16', 'O16', 'O16', 'O16', 'O16', 'O16', 'O16', 'O16', 'O16', 'G39', 'B7', 'G42', 'B10', 'B8', 'B9', 'O26', 'O26', 'O26', 'O26', 'O26', 'O26', 'O26', 'O26', 'O26', 'O26', 'P6', 'B14', 'B15', 'B11', 'G32', 'G31', 'G29', 'G27', 'G28', 'B5', 'G51', 'Y34', 'G52', 'G53', 'Y35', 'R10', 'R10', 'R10', 'R10', 'R10', 'R10',
          'R10', 'R10', 'R10', 'R10', 'Y37', 'O30', 'O30', 'O31', 'O31', 'O31', 'O29', 'O29', 'O29', 'O29', 'O29', 'R8', 'R8', 'R8', 'R8', 'R8', 'R8', 'R8', 'R8', 'R8', 'R8', 'O32', 'O32', 'O32', 'O32', 'O32', 'O32', 'O32', 'O32', 'O32', 'O32']
ends = starts
