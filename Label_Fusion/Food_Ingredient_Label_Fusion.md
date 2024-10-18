# Introduction of the Food Ingredient Label Fusion Program
[Read in Chinese](./食材标签融合小程序介绍.md)

## Interface Display

<div style="text-align: center;">
<img src=".\cover.png" alt="Fusion Cover"  width="80%" height="80%">
</div>

## Function Introduction

The main function of this program is to adjust the food ingredient labels annotated in the early stage. It has two major functions:

1. For food ingredient labels with fuzzy semantic labels, if it is impossible to determine their node (i.e. food category) in the food tree, it is necessary to find the corresponding image of the food ingredient label and manually determine whether to change or delete the label.
2. Manually merge food ingredient labels with similar semantics.

## Running
```
python fuse_label_gui.py
```
## Function of Buttons

1. **根节点（Root Node）**: Display the root node of the food tree.
2. **上一级（Higher Level）**: Display the higher level node of the food tree.
3. **下一级（Lower Level）**: Display the lower level node of the food tree.
4. **拟融合节点 (Nodes to be fused)**: Put the nodes to be fused into this cache area.
5. **融合 (Fusion)**: Perform Fusion operation on semantically similar labels in the cache area. The program will pop up a user input box, where the user inputs the name of the fused label and places it in the current display level of the left food tree. Note that **only leaf nodes can be fused**.
6. **撤销 (Rollback)**: Step back operation. <font color=red>**Only used to retract the previous fusion node operation**</font>. For other functions, it is necessary to perform a rollback.
7. **保存 (Save)**: Save data, there are two data that need to be saved: **Food tree** and **original label-fused label mapping dict**.

**Note that**: The Fusion operation is limited to leaf nodes, and the logic of the fusion operation is:

1. Click the '融合 (Fusion)' button to pop up an input box. The user inputs the fused label, and the program places the label into the current display level of the food tree. If the label already exists in the food tree, the put operation is not performed.

2. Delete the original nodes in the cache area in the food tree

Therefore, according to the above logic, **this program has multiple operation methods for label fusion**:

1. Ordinary leaf nodes fusion, the fused node becomes a new node in the food tree: select any two leaf nodes, click the fusion button, and enter a new node name added into the food tree;
2. Ordinary leaf nodes fusion, resulting in node that already exist in the food tree: select any two leaf nodes, click the fusion button, and enter the existing node name in the current level of the food tree;
3. Change the node name of a regular leaf node: select any leaf node, click the merge button, enter the new node name, and place it in the current level of the food tree.