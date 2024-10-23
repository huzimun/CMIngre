
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import json
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, messagebox, simpledialog
from knowledge_graph import food_tree
import traceback
from clustering import kmeans, init_feature, WaitingWindow

def get_existed_label(label_tree):
    # label_tree: hierarchical tree
    global EXISTED_LABEL
    if label_tree:
        cur_level_keys = list(label_tree.keys())
        for cur_key in cur_level_keys:
            EXISTED_LABEL.add(cur_key)
            get_existed_label(label_tree[cur_key])
    else:
        pass

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\build\assets\frame0")

# 加载已经标记好的食材树
TREE_FILE = r'.\输入输出\全部数据\tree.json'
with open(TREE_FILE, 'r', encoding='utf-8') as f:
    INFOS = json.load(f)
# 将已经标记好的食材进行汇总，用集合EXISTED_LABEL表示，用于非重复标记判断
EXISTED_LABEL = set()
get_existed_label(INFOS)
# 加载未标记的食材文件
IN_FILE = r'.\输入输出\全部数据\in_person0.json'  # 该文件以64为batch_size
SAVE_IN_FILE = r'.\输入输出\全部数据\in_person0.json'  # 用于保存未标记的数据
with open(IN_FILE, 'r', encoding='utf-8') as f:
    LABEL = json.load(f)
LABEL = set(LABEL["in"])  # 用于表示仍未标记的食材, 0, 1表示第0个人的工作
LABEL = LABEL ^ (LABEL & EXISTED_LABEL)  # 先取二者交集，然后去除未标记中已经被标记好的节点
LABEL_LIST = list(LABEL)  # 用于保存食材数据的有序性，用于文本聚类展示
SELECT_LABEL = set()  # 用于表示选取拟准备标记的食材，放入标注食材缓存区, set属性防止重复选取
SELECT_NODE = dict()  # 用于表示拟删除的食材树节点，放入删除节点缓存区
CUR_LEVEL_KNOWLEDGE = []  # 用于表示食材树当前的级别
CUR_PAGE = 0   # 用于表示未标记食材中，需要展示的第几页数据
NUM_PER_ROW = 8  # 用于表示可视化主要区域每一行放多少个按钮块
NUM_PER_PAGE = 64  # 用于表示可视化主要区域每一页放多少个按钮块
NUM_PER_ROW_CACHE = 2  # 用于表示缓存区每一行放多少个按钮快
CUR_LABEL_NUM = len(LABEL)  # 用于表示当前仍未标注的食材数量
CUR_TREE = food_tree(INFOS)  # 用于表示当前食材树
PAD_X, PAD_Y = 15, 6  # 用于表示每一个食材块间的间隔
INPUT_NODES = set()  # 用于标记用户自己创建的类别
SAVE_TREE_FILE = r'.\输入输出\全部数据\tree.json'  # 用于保存食材树
ALL_INGREDIENT = r'.\输入输出\全部数据\in_min5.json'  # 加载所有食材数据，用于文本聚类
ALL_FEATURE = r'.\输入输出\全部数据\in_feature.npy'  # 加载所有食材数据特征，用于文本聚类
init_feature(ALL_INGREDIENT, ALL_FEATURE)  # 在文本聚类函数里链接每一个食材和对应的特征，便于文本特征选择

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_tree(keys:list):
    # visualize the food tree using labeled ingredient
    global CUR_LEVEL_KNOWLEDGE
    print(f"show level: {keys}")
    CUR_LEVEL_KNOWLEDGE = keys  # 记录当前所处树的层级，叶子节点层级不记录
    # 展示下一级数据时，将上一级数据清空
    for widget in entry_4.grid_slaves():
        widget.grid_forget()
    cur_dict = CUR_TREE.tree
    for key in keys:
        cur_dict = cur_dict[key]
    cur_level = list(cur_dict.keys())
    text_width = entry_4.winfo_width()
    cur_row = 0
    cur_column = 0
    cur_width = 0
    for i, name in enumerate(cur_level):
        button = Button(entry_4, text=name, command=lambda name=name: show_tree(keys + [name]))
        if cur_width + button.winfo_reqwidth() + PAD_X*2 < text_width - 80:
            button.grid(row=cur_row, column=cur_column, padx=PAD_X, pady=PAD_Y)
            cur_width += button.winfo_reqwidth() + PAD_X*2
        else:
            cur_row += 1
            cur_column = 0
            button.grid(row=cur_row, column=cur_column, padx=PAD_X, pady=PAD_Y)
            cur_width = button.winfo_reqwidth() + PAD_X*2
        cur_column += 1

def next_tree():
    # visualize the next level ingredient
    cur_dict = CUR_TREE.tree
    for key in CUR_LEVEL_KNOWLEDGE:
        cur_dict = cur_dict[key]
    if cur_dict:
        show_tree(CUR_LEVEL_KNOWLEDGE + [list(cur_dict.keys())[0]])
    else:
        messagebox.showinfo("提示", "已经是食材树最低级别了")

def prior_tree():
    # visualize the prior level ingredient
    global CUR_LEVEL_KNOWLEDGE
    if CUR_LEVEL_KNOWLEDGE:
        CUR_LEVEL_KNOWLEDGE = CUR_LEVEL_KNOWLEDGE[:-1]
        show_tree(CUR_LEVEL_KNOWLEDGE)
    else:
        messagebox.showinfo("提示", "已经是食材树最高级别了")

def show_label(page=0):
    # visual the unlabeled data
    global CUR_PAGE
    print(f"show labels: the {page}th page")
    CUR_PAGE = page
    # 展示下一级数据时，将上一级数据清空
    for widget in entry_1.grid_slaves():
        widget.grid_forget()
    
    labels = LABEL_LIST[page * NUM_PER_PAGE: min((page + 1) * NUM_PER_PAGE, CUR_LABEL_NUM)]
    for i in range(len(labels)):
        label = labels[i]
        button = Button(entry_1, text=label, command=lambda label=label: record_select_ingredient(label))
        button.grid(row=i//NUM_PER_ROW, column=i%NUM_PER_ROW, padx=PAD_X, pady=PAD_Y)

def next_label():
    # visual the next-page labels
    if CUR_PAGE * NUM_PER_PAGE >= CUR_LABEL_NUM:
        messagebox.showinfo("提示", "已经是标签最后一页了")
    else:
        show_label(page=CUR_PAGE+1)

def prior_label():
    # visual the prior-page labels
    if CUR_PAGE == 0:
        messagebox.showinfo("提示", "已经是标签首页了")
    else:
        show_label(page=CUR_PAGE-1)

def record_select_ingredient(name):
    global SELECT_LABEL
    if name in SELECT_LABEL:
        log_txt = rf"{name}已经在标记食材缓存区，请勿重复添加"
        print(log_txt)
        messagebox.showinfo("提示", log_txt)
    else:
        SELECT_LABEL.add(name)
        print(f"将{name}放入标记缓冲区")
        show_label_cache()

def show_label_cache():
    global SELECT_LABEL
    # 展示数据时，将上一次数据清空
    print("更新标签缓存")
    for widget in entry_2.grid_slaves():
        widget.grid_forget()
    for i, name in enumerate(SELECT_LABEL):
        button = Button(entry_2, text=name, command=lambda name=name: delete_label_cache(name))
        button.grid(row=i // NUM_PER_ROW_CACHE, column=i % NUM_PER_ROW_CACHE, padx=PAD_X, pady=PAD_Y)

def delete_label_cache(delete_name:str):
    global SELECT_LABEL
    SELECT_LABEL.remove(delete_name)
    print(f"在标记缓冲区将{delete_name}移除")
    show_label_cache()

def add_node():
    # add the selected label into the selected tree
    # after adding the label, should delete the label in LABEL
    global SELECT_LABEL, EXISTED_LABEL, CUR_LABEL_NUM
    if SELECT_LABEL:
        existed_labels = []
        for label in SELECT_LABEL:
            if label in EXISTED_LABEL:
                existed_labels.append(label)
        if existed_labels:
            messagebox.showinfo("提示", f"标签{existed_labels}已经被划分完毕，无需重新划分\n"
                                      f"如需重新划分，请先删除该节点")
        else:
            try:
                # 记录已经标注好的标签，同时在所有未标注标签里删除该标签
                for label in SELECT_LABEL:
                    CUR_TREE.add_node(val=label, fathers=CUR_LEVEL_KNOWLEDGE)
                    EXISTED_LABEL.add(label)
                    LABEL.remove(label)
                    CUR_LABEL_NUM -= 1
                SELECT_LABEL = set()  # 清空缓存食材区
                update_label_list()
                show_label_cache()
                show_label()
                show_tree(keys=CUR_LEVEL_KNOWLEDGE)
            except Exception as e:
                log_txt = f"A error was happened in add_node function\n: {traceback.format_exc()}"
                print(log_txt)
                messagebox.showinfo("提示", log_txt)
    else:
        messagebox.showinfo("提示", "请先选择至少一个食材")

def update_label_list():
    # 在未标记数据存在变动时，LABEL集合数据可以直接通过remove,add来删除或添加数据
    # 然而，LABEL_LIST由于要保持有序性，必须遍历所有数据才能达到更新的目的
    global LABEL_LIST, LABEL
    cur_label_list_set = set(LABEL_LIST)
    diff_data = cur_label_list_set ^ LABEL
    i,j = 0,0  # 双指针，i指针指向需要存放的元素，j指针指向需要更换的元素
    while j < len(LABEL_LIST):
        # 如果差异数据，在原始列表，却不在更新列表中，说明该数据需要被删除
        # 被删除即是，第j个元素不赋给第i个元素，j同时+1继续遍历
        if LABEL_LIST[j] in diff_data and LABEL_LIST[j] not in LABEL:
            diff_data.remove(LABEL_LIST[j])  # 删除所有的需被删除数据后，diff中保存的就是需要被添加的数据
        else:
            LABEL_LIST[i] = LABEL_LIST[j]  #
            i += 1
        j += 1
    LABEL_LIST = LABEL_LIST[:i] + list(diff_data)

def record_delete_node_cache():
    global SELECT_NODE
    if CUR_LEVEL_KNOWLEDGE[-1] in SELECT_NODE:
        log_txt = rf"{CUR_LEVEL_KNOWLEDGE[-1]}已经在删除节点缓存区，请勿重复添加"
        print(log_txt)
        messagebox.showinfo("提示", log_txt)
    else:
        SELECT_NODE[CUR_LEVEL_KNOWLEDGE[-1]] = CUR_LEVEL_KNOWLEDGE[:-1]
        print(f"将{CUR_LEVEL_KNOWLEDGE[-1]}加入删除缓冲区")
        show_node_cache()

def show_node_cache():
    global SELECT_NODE
    # 展示数据时，将上一次数据清空
    for widget in entry_3.grid_slaves():
        widget.grid_forget()
    for i, name in enumerate(SELECT_NODE.keys()):
        button = Button(entry_3, text=name, command=lambda name=name: delete_node_cache(name))
        button.grid(row=i // NUM_PER_ROW_CACHE, column=i % NUM_PER_ROW_CACHE, padx=PAD_X, pady=PAD_Y)

def delete_node_cache(delete_name):
    global SELECT_NODE
    del SELECT_NODE[delete_name]
    print(f"将{delete_name}移除删除节点缓冲区")
    show_node_cache()


def delete_node():
    # 该函数通过SELECT_NODE变量来删除食材树节点
    global EXISTED_LABEL, SELECT_LABEL, SELECT_NODE, CUR_LABEL_NUM
    if SELECT_NODE:
        try:
            # 注意！！！
            # 删除节点有三大注意事项
            # 1. 删除的节点必须是同一父节点下的同一级别的子节点
            # 2. 删除节点前必须将节点放入删除节点缓存区，即进入删除节点下的空子节点，然后点击缓存区将该节点加入缓存区
            # 3. 点击删除节点按钮的同时，食材树可视化页面必须为删除节点这一级
            for node, path in SELECT_NODE.items():
                CUR_TREE.delete_node(val=node, fathers=path)
                print(f"在食材树中删除{node}食材")
                if node not in INPUT_NODES:
                    LABEL.add(node)  # 删除的数据如果为用户标记的新节点，则未标记节点不加入该节点
                    EXISTED_LABEL.remove(node)
                    CUR_LABEL_NUM += 1
                else:
                    INPUT_NODES.remove(node)  # 如果为用户标记节点，则在标记节点集合中删除该节点
            CUR_LEVEL_KNOWLEDGE.pop()  # 返回当前可视化父层级
            SELECT_NODE = dict()  # 初始化删除节点缓存
            update_label_list()  # 更新未标记数据数组
            show_node_cache()
            show_label()
            show_tree(keys=CUR_LEVEL_KNOWLEDGE)
        except Exception as e:
            log_txt = f"A error was happened in delete_node function\n: {traceback.format_exc()}"
            print(log_txt)
            messagebox.showinfo("提示", log_txt)

    else:
        messagebox.showinfo("提示", "请先选择至少一个叶子节点")

def input_node():
    # 弹出输入对话框
    user_input = simpledialog.askstring("Input", "请输入需要创建的类别:")
    # 在后台接收用户输入
    if user_input:
        # 在这里可以对用户输入进行处理
        print("User input:", user_input)
        # 在这里处理输入的字符串
        try:
            CUR_TREE.add_node(val=user_input, fathers=CUR_LEVEL_KNOWLEDGE)
            # 记录已经标注好的标签，同时在所有未标注标签里删除该标签
            INPUT_NODES.add(user_input)  # 将用户输入的节点记录
            EXISTED_LABEL.add(user_input)  # 将用户输入的节点放入食材树
            show_tree(keys=CUR_LEVEL_KNOWLEDGE)
        except Exception as e:
            log_txt = f"A error was happened in input_node function\n: {traceback.format_exc()}"
            print(log_txt)
            messagebox.showinfo("提示", log_txt)
    else:
        print("User cancelled the dialog")


def save_file():
    # 随时保存标记好的数据
    try:
        assert set(LABEL_LIST) == LABEL
    except:
        log_txt = "未标记数据集合和数组不统一，请检查集合更新代码"
        print(log_txt)
        messagebox.showinfo("提示", log_txt)
    save_unlabeled_data = LABEL_LIST  # 剩下仍未标注的食材数据
    save_food_tree = CUR_TREE.tree  # 已经标注的食材字典
    with open(SAVE_IN_FILE, 'w', encoding="utf-8") as f:
        json.dump({"in": save_unlabeled_data}, f, ensure_ascii=False)
    with open(SAVE_TREE_FILE, 'w', encoding="utf-8") as f:
        json.dump(save_food_tree, f, ensure_ascii=False, indent=4)
    log_txt = "保存数据成功"
    print(log_txt)
    messagebox.showinfo("提示", log_txt)

def text_cluster():
    global LABEL, window, LABEL_LIST
    # 加载等待页面
    wait_window = WaitingWindow(window)
    wait_window.transient(window)
    wait_window.grab_set()
    # 执行文本聚类
    try:
        LABEL_LIST = kmeans(LABEL_LIST)
        # print(LABEL_LIST)
    except Exception as e:
        log_txt = f"{e} is not in the original ingredient set"
        print(log_txt)
        messagebox.showinfo("提示", log_txt)
    # 关闭等待页面
    wait_window.destroy()
    # 更新未标记标签
    show_label()

if __name__ == "__main__":
    window = Tk()
    window.geometry("1440x1024")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=1024,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: prior_tree(),
        relief="flat"
    )
    button_1.place(
        x=460.0,
        y=522.0,
        width=140.0,
        height=44.8803825378418
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_tree([]),
        relief="flat"
    )
    button_2.place(
        x=249.0,
        y=522.0,
        width=140.0,
        height=44.8803825378418
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: add_node(),
        relief="flat"
    )
    button_3.place(
        x=1259.0,
        y=701.0,
        width=140.0,
        height=44.88038635253906
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: input_node(),
        relief="flat"
    )
    button_4.place(
        x=1259.0,
        y=620.0,
        width=140.0,
        height=44.88038635253906
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: text_cluster(),
        relief="flat"
    )
    button_5.place(
        x=1259.0,
        y=311.0,
        width=140.0,
        height=44.88038635253906
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_label(),
        relief="flat"
    )
    button_6.place(
        x=263.0,
        y=104.0,
        width=140.0,
        height=45.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    button_7.place(
        x=43.0,
        y=223.0,
        width=29.0,
        height=209.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_8 clicked"),
        relief="flat"
    )
    button_8.place(
        x=43.0,
        y=697.0,
        width=29.0,
        height=209.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: prior_label(),
        relief="flat"
    )
    button_9.place(
        x=475.0,
        y=104.0,
        width=140.0,
        height=44.88037109375
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: next_label(),
        relief="flat"
    )
    button_10.place(
        x=680.0,
        y=104.0,
        width=140.0,
        height=44.88037109375
    )

    button_image_11 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: delete_node(),
        relief="flat"
    )
    button_11.place(
        x=1259.0,
        y=786.0,
        width=140.0,
        height=44.88037109375
    )

    button_image_12 = PhotoImage(
        file=relative_to_assets("button_12.png"))
    button_12 = Button(
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: save_file(),
        relief="flat"
    )
    button_12.place(
        x=1259.0,
        y=867.0,
        width=140.0,
        height=44.88037109375
    )

    button_image_13 = PhotoImage(
        file=relative_to_assets("button_13.png"))
    button_13 = Button(
        image=button_image_13,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: next_tree(),
        relief="flat"
    )
    button_13.place(
        x=659.0,
        y=522.0,
        width=140.0,
        height=44.8803825378418
    )

    canvas.create_rectangle(
        42.0,
        89.0,
        1381.0,
        90.0,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        1235.0,
        89.0,
        1236.0,
        1009.0005493164062,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        126.0,
        511.0,
        1238.0,
        515.0272476673126,
        fill="#000000",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        559.0,
        330.5,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=127.0,
        y=163.0,
        width=864.0,
        height=333.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        1113.5,
        330.5,
        image=entry_image_2
    )
    entry_2 = Text(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=1007.0,
        y=163.0,
        width=213.0,
        height=333.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        1113.5,
        769.0,
        image=entry_image_3
    )
    entry_3 = Text(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=1007.0,
        y=572.0,
        width=213.0,
        height=392.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        559.0,
        769.0,
        image=entry_image_4
    )
    entry_4 = Text(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=127.0,
        y=572.0,
        width=864.0,
        height=392.0
    )

    canvas.create_rectangle(
        130.0,
        24.0,
        1249.0,
        77.0,
        fill="#D74040",
        outline="")

    canvas.create_text(
        451.0,
        31.0,
        anchor="nw",
        text="食材数据标签重新划分小程序v1.0",
        fill="#FFFFFF",
        font=("Inter", 32 * -1)
    )

    button_image_14 = PhotoImage(
        file=relative_to_assets("button_14.png"))
    button_14 = Button(
        image=button_image_14,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_14 clicked"),
        relief="flat"
    )
    button_14.place(
        x=1007.0,
        y=104.0,
        width=213.0,
        height=45.0
    )

    button_image_15 = PhotoImage(
        file=relative_to_assets("button_15.png"))
    button_15 = Button(
        image=button_image_15,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: record_delete_node_cache(),
        relief="flat"
    )
    button_15.place(
        x=1007.0,
        y=522.0,
        width=213.0,
        height=45.0
    )
    window.resizable(False, False)
    window.mainloop()

    save_file()



