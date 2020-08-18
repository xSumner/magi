#encoding = utf-8
"""
@version:??
@author: xq
@contact:xiaoq_xiaoq@163.com
@file: test.py
@time: 2017/10/18 14:29
"""
import pandas as pd
import matplotlib.pyplot as plt
from  sklearn.cluster import KMeans
from matplotlib.font_manager import FontProperties
class clusterApi(object):
    def __init__(self,data):
        self.data = data
        # self.font = FontProperties(fname='C:/Windows/Fonts/msyh.ttf')#设置中文字体
    def initData(self):
        '''
        数据预处理,统一数据格式
        :return: 固定格式的数据
        '''
        initdata = pd.DataFrame(self.data)
        scatterData = initdata[['Id', 'lat', 'lng']]
        return scatterData
    def k_meansUp(self):
        pointsData = self.initData()#要分类的数据
        plt.figure()
        plt.subplot(331)#绘制子图
        lats = pointsData.lat
        lngs =pointsData.lng
        # plt.title(u'样本',fontproperties=self.font)#设置图的标题
        plt.title('sample')#设置图的标题
        plt.scatter(lngs, lats,s=3)#绘制样本图
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'b']#画图颜色
        markers = ['o', 's', 'D', 'v', '^', 'p', '*', '+']#画图形状
        testsK = [2, 3, 4, 5, 8]#k值的取值
        subplot_counter = 1#子图的位置
        for t in testsK:
            subplot_counter += 1
            plt.subplot(3, 2, subplot_counter)
            kmeans_model = KMeans(n_clusters=t).fit(pointsData)
            for i, l in enumerate(kmeans_model.labels_):
                plt.plot(lngs[i], lats[i],markersize=2,color=colors[l],marker=markers[l], ls='None')
                plt.title(u'K = %s' %t)
        plt.show()
def main():
    #测试数据
    stopList= [{'Id': '50001','lat': 28.571906,'lng': 112.337788},
               {'Id': '50001','lat': 28.573678,'lng': 112.381103},
               { 'Id': '50001','lat': 28.571915,'lng': 112.337533},
               { 'Id': '50001','lat': 28.573978,'lng': 112.35765},
                { 'Id': '50001','lat': 28.572656,'lng': 112.3366},
               {'Id': '50001', 'lat': 28.578011, 'lng': 112.330688},
               {'Id': '50001', 'lat': 28.572228, 'lng': 112.335841},
               {'Id': '50001', 'lat': 28.57849, 'lng': 112.3338},
               {'Id': '50001', 'lat': 28.57239, 'lng': 112.336491},
               {'Id': '50001', 'lat': 28.577943, 'lng': 112.330995},
               {'Id': '50001', 'lat': 28.571921, 'lng': 112.337783},
               {'Id': '50001', 'lat': 28.572401, 'lng': 112.3359},
               {'Id': '50001', 'lat': 28.569629, 'lng': 112.34005},
               {'Id': '50001', 'lat': 28.588048, 'lng': 112.337783},
               {'Id': '50001', 'lat': 28.572035, 'lng': 112.335683},
               {'Id': '50001', 'lat': 28.560938, 'lng': 112.378183},
               {'Id': '50001', 'lat': 28.544781, 'lng': 112.494936},
               {'Id': '50001', 'lat': 28.572296, 'lng': 112.336288},
               {'Id': '50001', 'lat': 28.571951, 'lng': 112.337806},
               {'Id': '50001', 'lat': 28.571551, 'lng': 112.32685}]
    print('共有%d个点'%len(stopList))
    clustertest = clusterApi(stopList)#实例化
    clustertest.k_meansUp()#聚类画图
if __name__ == '__main__':
    main()