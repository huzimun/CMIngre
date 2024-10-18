# Introduction of Food Ingredient Label Classification Program
[Read in Chinese](./食材分类小程序介绍.md)
## Interface Display
<div style="text-align: center;">
<img src=".\cover.png" alt="Classification Cover"  width="80%" height="80%">
</div>

## Function

The main function of this program is to classify the food ingredient labels in the dataset into the corresponding category nodes of the food tree.

## Unclassified Ingredient Labels

Select labels that appear in at least 5 images from all ingredient label data (located in ".\输入输出\全部数据\all_in.csv"), resulting in 517 ingredient labels.

Two people classify the food labels, with each person having approximately 260 labels (located in “.\输入输出\全部数据\in_person0.json” and “.\输入输出\全部数据\in_person1.json”, respectively). The path of input file can be modified in gui.py。

## Input and Output

- All ingredient labels: located in “.\输入输出\全部数据\in_min5.json”;
- All ingredient features: located in “.\输入输出\全部数据\in_feature.npy”;
- Uncategorized ingredient labels: located in “.\输入输出\全部数据\in_person0.json” and “.\输入输出\全部数据\in_person1.json”;
- Food tree with categorized ingredient labels: located in “.\输入输出\全部数据\tree.json”.

## Running
```
python gui.py
```

## Enviroment

1. sklearn: Used for text clustering
2. [tkinter](https://github.com/ParthJadhav/Tkinter-Designer): for gui visualization

## Function Display

| Function Name             | Function             |
| ------------------- | --------------------|
| 首页 (Home Page)    | Return to the visualization homepage of uncategorized ingredients, displaying the first 64 tags          |
| 上一页 (Last Page)  | Return to the ingredient label on the previous page. If the current page is the homepage, return a warning   |
| 下一页 (Next Page)       | Return the ingredient label to the next page. If the current page is the last page, return a warning   |
| 根节点 (Root Node)        | Return the root node of the categorized food tree  |
| 下一级 (Next Level)        | Return the next level of the food tree       |
| 上一级 (Last Level)       | Return the previous level of the food tree       |
| Click Uncategorized Ingredient   | Put uncategorized ingredient into “标记食材缓存区” (categorized Ingredient Area)|
| Click Leaf Node of Food Tree | Enter next level nodes under the current node    |
| 删除节点缓存区 (Delete Ingredients in Cache Area)  | Put the parrent node of current node into “删除节点缓存区” (Removing Nodes Cache Area), then click “删除节点” (Delete Node) and you can delete this node and its sub-tree. $\textcolor{red}{Note that you would better do not delete non-leaf nodes or it is irrevocable. You would better only delete leaf nodes.}$       |
| 标记节点 (Label Node)     | Put ingredients of “标记食材缓存区” (categorized Ingredient Area) into current level of the ingredient tree and delete corresponding ingredients from uncategorized ingredients area. $\textcolor{red}{Note that, when adding multiple nodes, they must belong to the same parent node of the ingredient tree. The program will automatically call the current node in the visualization area of the food tree as the inserted parent node. }$ |
| 删除节点 (Delete Node)    | Delete the leaf nodes in the “删除节点缓存区” (Delete Ingredients in Cache Area) and place them in the uncategorized ingredient area. $\textcolor{red}{After deleting the corresponding node, the food tree will default to returning the previous node of the current node for visualization}$                             |
| 添加新节点 (Add New Node)   | Some ingredients may not belong to the specified category, or it may be considered that some ingredients should have a more detailed classification. You can add a new node by adding a new node button under the current node of the food tree.     |
| 保存数据  (Save Data)      | Save data in real-time.             |
| PS             | The program can only be terminated by closing the UI interface. Otherwise, the food tree with partially categorized data that has not been saved will not be saved and will only be closed normally. Finally, the program will automatically save the categorized food tree.         |

## Other

- Each page contains 64 ingredients, which is one batch. The labeling of each batch takes about 2 hours, mainly because there are a large number of ingredients that the labeling personnel do not recognize.
- There are two files for annotating the final result, one is the annotated ingredient tree, and the other is the unlabeled ingredient (for ingredients with vague and ambiguous names that cannot be determined, they can be placed in **其他 (Other)** categories).
- Note that everyone's subjective level is different, so it is necessary to label the ingredients twice.
- Duration: approximately 1 day.
