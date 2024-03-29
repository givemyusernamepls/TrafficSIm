import matplotlib.pyplot as plt
import numpy as np

#Ampel
aa = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
ab = [200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
ac = [300, 300, 300, 300, 300, 300, 300, 300, 300, 300]
ad = [400, 400, 400, 400, 400, 400, 400, 400, 400, 400]
ae = [465, 452, 450, 460, 466, 452, 447, 461, 466, 462]
af = [500, 481, 500, 484, 484, 507, 480, 500, 495, 488]
ag = [519, 517, 519, 515, 522, 535, 528, 529, 524, 517]
ah = [549, 536, 546, 554, 547, 546, 549, 543, 544, 539]
ai = [569, 561, 577, 572, 559, 564, 568, 571, 564, 565]
aj = [611, 592, 611, 592, 587, 590, 591, 582, 593, 580]
ak = [603, 601, 598, 600, 613, 604, 598, 606, 607, 610]
al = [603, 612, 614, 616, 610, 608, 612, 599, 609, 616]
am = [616, 617, 606, 627, 616, 625, 618, 627, 625, 605]
an = [615, 605, 603, 617, 616, 611, 624, 613, 607, 605]
ao = [624, 608, 614, 618, 619, 631, 612, 606, 607, 625]


#kreisel
ka = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
kb = [200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
kc = [300, 300, 300, 300, 300, 300, 300, 300, 300, 300]
kd = [400, 400, 400, 400, 400, 400, 400, 400, 400, 400]
ke = [491, 490, 489, 480, 496, 499, 484, 491, 484, 496]
kf = [525, 532, 521, 532, 531, 533, 524, 536, 524, 528]
kg = [534, 550, 537, 542, 538, 549, 525, 524, 525, 538]
kh = [540, 553, 538, 547, 532, 536, 549, 522, 550, 556]
ki = [535, 529, 545, 557, 544, 549, 529, 537, 533, 536]
kj = [545, 555, 546, 542, 532, 541, 556, 530, 550, 556]
kk = [543, 542, 554, 560, 557, 542, 560, 542, 548, 558]
kl = [542, 560, 552, 549, 531, 535, 542, 562, 548, 532]
km = [547, 551, 535, 553, 554, 549, 556, 547, 552, 546]
kn = [554, 557, 569, 553, 532, 559, 575, 558, 562, 552]
ko = [540, 539, 540, 556, 542, 553, 558, 559, 543, 547]

#Kreuzung
za = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
zb = [200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
zc = [300, 300, 300, 300, 300, 300, 300, 300, 300, 300]
zd = [400, 400, 400, 400, 400, 400, 400, 400, 400, 400]
ze = [450, 427, 450, 445, 451, 425, 431, 439, 437, 438]
zf = [430, 442, 443, 429, 422, 451, 450, 433, 435, 443]
zg = [452, 451, 459, 421, 437, 450, 437, 442, 447, 435]
zh = [440, 452, 444, 446, 441, 440, 435, 445, 453, 461]
zi = [460, 446, 438, 467, 444, 431, 447, 434, 445, 457]
zj = [449, 423, 433, 453, 421, 428, 449, 427, 463, 441]
zk = [438, 440, 437, 439, 443, 425, 458, 429, 444, 444]
zl = [441, 445, 437, 451, 445, 460, 429, 440, 434, 442]
zm = [449, 447, 438, 449, 434, 446, 461, 444, 449, 441]
zn = [432, 441, 454, 445, 424, 456, 441, 460, 442, 449]
zo = [444, 425, 448, 452, 451, 432, 427, 449, 451, 432]


A = [np.mean(aa)/10, np.mean(ab)/10, np.mean(ac)/10, np.mean(ad)/10, np.mean(ae)/10, np.mean(af)/10, np.mean(ag)/10, np.mean(ah)/10, np.mean(ai)/10, np.mean(aj)/10, np.mean(ak)/10, np.mean(al)/10, np.mean(am)/10, np.mean(an)/10, np.mean(ao)/10]
K = [np.mean(ka)/10, np.mean(kb)/10, np.mean(kc)/10, np.mean(kd)/10, np.mean(ke)/10, np.mean(kf)/10, np.mean(kg)/10, np.mean(kh)/10, np.mean(ki)/10, np.mean(kj)/10, np.mean(kk)/10, np.mean(kl)/10, np.mean(km)/10, np.mean(kn)/10, np.mean(ko)/10]
Z = [np.mean(za)/10, np.mean(zb)/10, np.mean(zc)/10, np.mean(zd)/10, np.mean(ze)/10, np.mean(zf)/10, np.mean(zg)/10, np.mean(zh)/10, np.mean(zi)/10, np.mean(zj)/10, np.mean(zk)/10, np.mean(zl)/10, np.mean(zm)/10, np.mean(zn)/10, np.mean(zo)/10]
r = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]

plt.ylabel('tatsächliche "vehicle rate" gemittelt über 10 Minuten')
plt.xlabel('angegebene "vehicle rate" für den "vehicle generator"')
plt.suptitle('Kapazität der einzelnen Verkehrsobjekte abhängig von der "vehicle rate"')
plt.ylim(10, 70)
plt.plot(r, A, '.', color='blue', label='Ampel')
plt.plot(r, K, '.', color='red', label='Kreisverkehr')
plt.plot(r, Z, '.', color='green', label='Kreuzung')
plt.legend(loc='upper left')

plt.show()


#Berechnung des durchschnittlichen Maximalwerts
aa= np.mean([np.mean(al)/10, np.mean(am)/10, np.mean(an)/10, np.mean(ao)/10])
kk= np.mean([np.mean(kl)/10, np.mean(km)/10, np.mean(kn)/10, np.mean(ko)/10])
zz= np.mean([np.mean(zl)/10, np.mean(zm)/10, np.mean(zn)/10, np.mean(zo)/10])

print('ampel', aa)
print('kreisel', kk)
print('kreuzung', zz)
