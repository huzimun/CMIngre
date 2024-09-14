from transformers import AutoTokenizer, AutoModel
import json
import numpy as np
from sklearn.cluster import KMeans
import collections
# import asyncio  # 异步加载文本预训练模型
import tkinter as tk

ALL_DICT = {}

class WaitingWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("等待")
        self.geometry("200x100")
        tk.Label(self, text="正在聚类，请稍后...").pack(expand=True)

def get_data(data_path):
    # data_path = r'.\输入输出\全部数据\in_min5.json'
    with open(data_path, 'r', encoding='utf-8') as f:
        infos = json.load(f)
    sort_labels = sorted(infos.items(), key=lambda x:-x[1])
    inputs_name = [sort_labels[i][0] for i in range(len(sort_labels))]
    return inputs_name

def text_feature(data):
    global ALL_DICT
    Tokenizer = AutoTokenizer.from_pretrained("hfl/chinese-xlnet-mid")
    Model = AutoModel.from_pretrained("hfl/chinese-xlnet-mid")

    batch_size = 128
    iterations = int(np.ceil(len(data) / batch_size))
    for i in range(iterations):  #
        inputs = Tokenizer(data[i * batch_size:min((i + 1) * batch_size, len(data))], return_tensors="pt",
                           padding=True)
        feature = Model(**inputs)
        feature = feature.last_hidden_state[:, 0, :].detach().numpy()
        if i == 0:
            features = feature[:]
        else:
            features = np.concatenate((features, feature), axis=0)

    return features


def kmeans(data):
    global ALL_DICT
    features = np.zeros([len(data), 768])
    for i, dd in enumerate(data):
        features[i] = ALL_DICT[dd]
    clf = KMeans(n_clusters=len(data)//10)
    y = clf.fit_predict(features)
    save_dict = collections.defaultdict(list)
    for i, cluster in enumerate(y):
        save_dict[str(cluster)].append(data[i])
    save_dict = sorted(save_dict.items(), key=lambda x: -len(x[1]))
    final_data = []
    for name in save_dict:
        final_data = final_data + name[1]
    return final_data

def init_feature(in_path, feature_path):
    global ALL_DICT
    ingredients = get_data(in_path)
    features = np.load(feature_path)
    for ingre, feature in zip(ingredients, features):
        ALL_DICT[ingre] = feature

if __name__ == '__main__':
    data_path = r'.\knowledge\输入输出\全部数据\in_min5.json'
    data = get_data(data_path)
    ALL_DICT = {}
    features = text_feature(data)
    feature_path = r'.\knowledge\输入输出\全部数据\in_feature.npy'
    np.save(feature_path, features)

    person_num = 2  # 定义标注人数量
    total_need_label_num = len(data)  # 需要标注的总数量
    interval = int(total_need_label_num // person_num)  # 每个人需要标注的数量
    in_task = {}
    for i, name in enumerate(data):
        if i // interval not in in_task:
            in_task[i // interval] = [name]
        else:
            in_task[i // interval].append(name)
    for pp in range(person_num):
        in_person_pp = {"in":in_task[pp]}
        in_person_task = fr'.\knowledge\输入输出\全部数据\in_person{pp}.json'
        with open(in_person_task, 'w', encoding='utf-8') as f:
            json.dump(in_person_pp, f, ensure_ascii=False, indent=4)
    # kmeans(data)
