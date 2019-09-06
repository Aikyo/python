l1 = [175.0, 68.0, 139.0]
l2 = [('20190831154623-1013-TAR验证',), ('20190831160905-2019-C型架验证',), ('20190831173253-1008-TAR验证',)]
l3 = [x for x in range(len(l1))]

import matplotlib.pyplot as plt
import pylab as mpl

plt.bar(l3, l1)
plt.show()
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False
plt.title('dd')
for a, b in zip(l3, l1):
    plt.text(a, b + 0.001, '%d' % b, ha='center', va='bottom', fontsize=9)
plt.savefig("./data/%s.png" % 'test')
plt.cla()





