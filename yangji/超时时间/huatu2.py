l1 = [[175.0, 68.0, 139.0],[111,80,120]]
l2 = [[('20190831154623-1013-TAR验证',), ('20190831160905-2019-C型架验证',), ('20190831173253-1008-TAR验证',)],[('20190831154623-1013-TAR验证',), ('20190831160905-2019-C型架验证',), ('20190831173253-1008-TAR验证',)]]


import pandas as pd

data = pd.DataFrame({'time':l1,'material':l2})
print(data)
i = 0

def draw(data):
    global i
    import matplotlib.pyplot as plt
    import pylab as mpl
    l3 = data['material']
    # l3 = [x[0].split('-')[-1] for x in l3]
    l3 = [x[0] for x in l3]
    l1 = data['time']
    print(l3,l1)
    plt.bar(l3, l1,width=0.5)
    # plt.show()
    mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title('dd')
    for a, b in zip(l3, l1):
        plt.text(a, b + 0.001, '%d' % b, ha='center', va='bottom', fontsize=9)
    plt.savefig("./data/%sppp.png" % i)
    i += 1
    plt.cla()


data.apply(draw,axis=1)

















