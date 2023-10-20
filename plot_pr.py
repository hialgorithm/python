# # coding:utf-8
# import matplotlib
# # matplotlib.use("Agg")
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.metrics import precision_recall_curve
#
# plt.figure(1)  # 创建图表1
# plt.title(r"E:\pycharm\code\github\yolov5-master\runs\train\exp45\results.csv")  # give plot a title
# plt.xlabel('Recall')  # make axis labels
# plt.ylabel('Precision')
#
# # y_true和y_scores分别是gt label和predict score
# y_true = np.array([0, 0, 1, 1])
# y_scores = np.array([0.1, 0.4, 0.35, 0.8])
# precision, recall, thresholds = precision_recall_curve(y_true, y_scores)
# plt.figure(1)
# plt.plot(precision, recall)
# plt.show()
# # plt.savefig('p-r.png')

# import matplotlib
# import pickle
# import matplotlib.pyplot as plt
#
#
# def draw_single_pr_curve(pkl_file_path):
#     # 若在图中添加中文，可加入下面两行
#     # plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
#     # plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#     # 有中文出现的情况，需要u'内容'
#     pkl_file = open(pkl_file_path, 'rb')
#     pr_curve_data = pickle.load(pkl_file)
#
#     recall = pr_curve_data['rec']
#     precision = pr_curve_data['prec']
#
#     plt.xlabel('recall')
#     plt.ylabel('precision')
#     plt.plot(recall, precision)
#     plt.show()
#
#
# your_pkl_file_path = r"E:\pycharm\code\github\yolov5-master\runs\train\exp15\results.csv"
# draw_single_pr_curve(your_pkl_file_path)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def clean_column_names(df):
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace('\s+', '_', regex=True)


ori=pd.read_csv(r"E:\pycharm\code\github\yolov5-master\runs\train\exp15\results.csv")
ori_weights=pd.read_csv(r"E:\pycharm\code\github\yolov5-master\runs\train\exp23\results.csv")

clean_column_names(ori)
clean_column_names(ori_weights)

pd.set_option('display.width',100)
pd.set_option('display.max_columns',None)

ori_precision=ori['metrics/precision']
ori_weights_precision=ori_weights['metrics/precision']

ori_recall=ori['metrics/recall']
ori_weights_recall=ori_weights['metrics/recall']

ori_map=ori['metrics/mAP_0.5']
ori_weights_map=ori['metrics/mAP_0.5']

epoch=161

plt.subplot(1, 3, 1)
plt.plot(ori_precision,label='ori')
plt.plot(ori_weights_precision,label='ori_weight')
plt.xlabel("Epoch")
plt.ylabel("Precision")
plt.legend()
# plt.show()

# plt.figure()
plt.subplot(1, 3, 2)
plt.plot(ori_recall,label='ori')
plt.plot(ori_weights_recall,label='ori_weight')
plt.xlabel("Epoch")
plt.ylabel("Recall")
plt.legend()
# plt.show()

# plt.figure()
plt.subplot(1, 3, 3)
plt.plot(ori_map,label='ori')
plt.plot(ori_weights_map,label='ori_weight')
plt.xlabel("Epoch")
plt.ylabel("Map")
plt.legend()
plt.show()
print(ori_map)