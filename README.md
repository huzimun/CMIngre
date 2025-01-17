<!DOCTYPE html>
<html>
<table align="center" border="0" cellpadding="0" cellspacing="0">
    <tbody>
    <tr valign="middle">
        <td width="100%">
            <center>
                <h1 style="font-size:2em;padding-top:1em;">Toward Chinese Food Understanding: a Cross-Modal Ingredient-Level Benchmark</h1>
                <h4>
                    <font>Lanjun Wang<sup>1</sup>&nbsp;&nbsp;&nbsp;&nbsp;</font>
                    <font>Chenyu Zhang<sup>1</sup>&nbsp;&nbsp;&nbsp;&nbsp;</font>
                    <font>An-An Liu<sup>1</sup>&nbsp;&nbsp;&nbsp;&nbsp;</font>
                    <font>Bo Yang<sup>1</sup>&nbsp;&nbsp;&nbsp;&nbsp;</font>
                    <font>Mingwang Hu<sup>1</sup>&nbsp;&nbsp;&nbsp;&nbsp;</font>
                    <font>Xinran Qiao<sup>1</sup>&nbsp;&nbsp;&nbsp;&nbsp;</font>
                    <font>Lei Wang<sup>2</sup>&nbsp;&nbsp;&nbsp;&nbsp;</font>
                    <font>Jianlin He<sup>2</sup>&nbsp;&nbsp;&nbsp;&nbsp;</font>
                    <font>Qiang Liu<sup>2</sup>&nbsp;&nbsp;&nbsp;&nbsp;</font>
                </h4>
                <p><sup>1</sup>Tianjin University&nbsp;<sup>2</sup>Meituan Group</p>
    </tbody>
</table>

 <div id="container">
    <div>
        <h2>Content</h2>
        <p class="cont">
            <big>
            <ul>
            <li><a href="#intro">Introduction</a></li>
            <li><a href="#dataset">CMIngre Dataset</a></li>
            <li><a href="#task">Task</a></li>
            <li><a href="#citation">Citation</a></li>
            </ul>
            </big>
        </p>
    </div>
    <div id="intro">
        <h2>I. Introduction</h2>
        <p>
            <big>
            This is the supplementary material for the paper "Toward Chinese Food Understanding: a Cross-Modal Ingredient-Level Benchmark" <a href="https://ieeexplore.ieee.org/document/10496846">[link]</a>.
            The web intends to release the proposed dataset <b>CMIngre</b> and introduce related tasks.
            </big> 
        </p>
    </div>
    <div id="dataset">
        <h2>II. CMIngre Dataset</h2>
        <big>
        CMIngre consists of 8,001 food images with 429 ingredient labels from three sources, where 1,719 from dishes, 2,330 from recipes, and 3,952 from user-generated content (UGC). In <a href='#data_sources'>Sec. II-A</a>, we introduce the three data sources of CMIngre. In <a href='#ontology'>Sec. II-B</a>, we introduce the ingredient ontology <a href="https://www.chinanutri.cn/fgbz/fgbzhybz/201707/t20170721_148433.html">[link]</a> for refining ingredient labels. In <a href='#tool'>Sec. II-C</a>, we introduce two visualization tools for classifying and fusing ingredient labels. In <a href='#comparision'>Sec. II-D</a>, we compare CMIngre with existing food datasets. In <a href='#download'>Sec. II-E</a>, we provide a download method of CMIngre. 
        </big>
            <h3 id='data_sources'>A. Data Sources</h3>
                <big>
                <p>
                To gather a comprehensive collection of food images, we explore three types of image-text pairings:
                <ul>
                    <li>Dish Images. As depicted in <a href="#annotation">Figure 1</a>, second row, this category includes images of dishes paired with their names. The text in this type provides the most succinct description compared to the others.</li>
                    <li>Recipe Images. Shown in <a href="#annotation">Figure 1</a>, third row, these data consist of recipe images accompanied by detailed recipe text. These images are of higher quality and are more informatively described than those in the other two categories.</li>
                    <li>User-Generated Content (UGC). This type, illustrated in the last row of <a href="#annotation">Figure 1</a>, involves images taken by users and their accompanying comments. As the user-generated content lacks constraint, both images and text descriptions often include elements irrelevant to food, such as restaurant ambiance or tableware. </li>
                </ul>
                In <a href="#annotation">Figure 1</a>, we extract ingredient labels from both text annotation and image annotation.
                    <div style="text-align: center;" id="annotation">
                        <br>
                        <img src="./annotation.png" alt="annotations" width="50%" height="50%">
                        <div>
                        Figure 1. Food images in CMIngre comes from three sources, where UGC refers to the user-generated content such as the user comment.
                        </div>
                    </div>
                </p>
                </big>
            <h3 id='ontology'>B. Ingredient Ontology</h3>
                <big>
                <p>
                Since some ingredient labels of different names referring to the same ingredient, for example, "松花蛋–preserved egg" and "皮蛋–preserved egg", we utilize an ingredient ontology from the People’s Republic of China health industry standard <a href="https://www.chinanutri.cn/fgbz/fgbzhybz/201707/t20170721_148433.html">[link]</a> to compare and combine the ingredient labels. In <a href="#ontology">Figure 2</a>, we show the complete sub-tree under the super-class (i.e. the second level) "Dried beans and products", where the leaf nodes are ingredient labels after cleaning up and the non-leaf nodes are from the standard.
                <div style="text-align: center;" id="ontology">
                        <br>
                        <img src="./tree_example.png" alt="The ontology used to clean labels in CMIngre" width="50%" height="50%">
                        <div>
                        Figure 2. The ontology used to clean labels in CMIngre. In this figure, we show the complete sub-tree under the super-class (i.e. the second level) "Dried beans and products". The leaf nodes are ingredient labels after cleaning up and the non-leaf nodes are from the standard.
                        </div>
                </div>
                </p>
                </big>
            <h3 id='tool'>C. Visualization Tools</h3>
                <big>
                <p>
                In order to categorize ingredient labels into the ingredient ontology, we have designed a classification tool (provided in the "Label_Classification" folder). Then, we have developed a fusing tool (provided in the "Label_Fusion" folder) to merge ingredients with identical semantics under the same parent node in the ingredient ontology.
                </p>
                </big>
            <h3 id='comparision'>D. Comparison with Existing Food Datasets</h3>
                <big>
                <div>We compare CMIngre with other food related datasets in <a href="#table1">Table 1</a>. It can be observed that existing food-related datasets mainly focus on the food recognition task, which aims to recognize the food category within the image. Although few datasets do provide annotations for food bounding boxes, their objective is to locate the entire dish, not the free-form ingredients. In contrast, Recipe 1M offers ingredient annotations for each food image. However, due to the absence of location annotations for these fine-grained ingredients, they only implicitly model the associations between entire food images and corresponding ingredients, limiting the model performance. Consequently, we introduce CMIngre, aimed at enhancing the understanding of Chinese food by ingredient detection and retrieval tasks.</div>
                <table id="table1" style="text-align: center;">
                    <br>
                    <div style="text-align: left;">Table 1. The statistical comparison between existing food-related datasets and CMIngre.<div>
                    <br>
                    <tr style="border-top: 1px solid;border-bottom: 1px solid;">
                        <th style="text-align: center;">Dataset</th>
                        <th style="text-align: center;">Task</th>
                        <th style="text-align: center;">Image Number</th>
                        <th style="text-align: center;">Annotation Category</th>
                        <th style="text-align: center;">Number of Annotation Category</th>
                        <th style="text-align: center;">BBox</th>
                    </tr>
                    <tr>
                        <td><a href='https://ieeexplore.ieee.org/document/9878168'>ChileanFood64</a></td>
                        <td>Food Recognition</td>
                        <td>11,504</td>
                        <td>Food</td>
                        <td>64</td>
                        <td>&#10003;</td>
                    </tr>
                    <tr>
                        <td><a href='https://link.springer.com/chapter/10.1007/978-3-319-16199-0_1'>UECFood256</a></td>
                        <td>Food Recognition</td>
                        <td>29,774</td>
                        <td>Food</td>
                        <td>256</td>
                        <td>&#10003;</td>
                    </tr>
                    <tr>
                        <td><a href='https://ieeexplore.ieee.org/document/7776769'>UNIMIB2016</a></td>
                        <td>Food Recognition</td>
                        <td>1,027</td>
                        <td>Food</td>
                        <td>73</td>
                        <td>&#10003;</td>
                    </tr>
                    <tr>
                        <td><a href='http://123.57.42.89/FoodComputing-Dataset/ISIA-Food500.html'>ISIA Food-500</a></td>
                        <td>Food Recognition</td>
                        <td>1,027</td>
                        <td>Food</td>
                        <td>73</td>
                        <td>&#10005;</td>
                    </tr>
                    <tr>
                        <td><a href='https://ieeexplore.ieee.org/document/10019590'>Food2K</a></td>
                        <td>Food Recognition</td>
                        <td>1,036,564</td>
                        <td>Food</td>
                        <td>2,000</td>
                        <td>&#10005;</td>
                    </tr>
                    <tr>
                        <td><a href='https://dl.acm.org/doi/abs/10.1145/3397271.3401244'>Recipe 1M</a></td>
                        <td>Recipe Retrieval</td>
                        <td>1,029,720</td>
                        <td>Recipe</td>
                        <td>1,047</td>
                        <td>&#10005;</td>
                    </tr>
                    <tr style="border-bottom: 1px solid;">
                        <td>CMIngre</td>
                        <td>Ingredient Detection &amp; Retrieval</td>
                        <td>8,001</td>
                        <td>Ingredient</td>
                        <td>429</td>
                        <td>&#10003;</td>
                    </tr>
                </table>
                </big>
            <h3 id='download'>E. Download</h3>
                <big>
                <div>
                    You can download CMIngre dataset from HuggingFace <a href='https://huggingface.co/datasets/huzimu/CMIngre'>[Dataset Card]</a>.
                </div>                
                </big>
    </div>
    <div id="task">
        <h2>III. Task</h2>
        <p>
            <big>
            Our dataset involves two tasks, i.e. ingredient detection and cross-modal ingredient retrieval.
            <ul>
                <li>Ingredient detection focuses on identifying the ingredients and providing precise location information within the image. As shown in <a href="#detection">Figure 3</a>, we locate and identify the ingredients in food images from dish, recipe, and UGC.
                <div style="text-align: center;" id="detection">
                    <br>
                    <div class="image-container">
                        <!-- <img src="./custom_image_caiming_36.png" alt="custom_image_caiming_36.png" style="width: 400px;height: 300px;margin: 3px;">
                        <img src="./custom_image_caipu_56.png" alt="custom_image_caipu_56.png" style="width: 300px;height: 300px;margin: 3px;">
                        <img src="./custom_image_ugc_268.png" alt="custom_image_ugc_268.png" style="width: 250px;height: 300px;margin: 3px;"> -->
                        <img src="./food_detection.png" alt="ingredient detection" width="80%" height="80%">
                    </div>
                    <div style="text-align: center;">
                        Figure 3. The ingredient detection visualization of theree food images from dish, recipe, and UGC.
                    </div>
                </div>
                </li>
                <li>Cross-modal ingredient retrieval aims to investigate the intricate relationship between the image and the composition of ingredients. We visualize top-5 retrieval results by randomly sampling a query object from dish, recipe, and UGC in the test set. As shown in <a href="#img2ingre">Figure 4</a>, the corresponding ingredient composition appears in the first index position of the retrieval list with the highest matching similarity. Similarly, as shown in <a href="#ingre2img">Figure 5</a>, the corresponding image appears in the first index position of the retrieval list with the highest matching similarity.
                <div style="text-align: center;" id="img2ingre">
                    <br>
                    <img src="./white_image_to_ingredient.png" alt="image to ingredient" width="50%" height="50%">
                    <div>
                    Figure 4. The top-5 retrieval visualization of three random query images from dish, recipe, and UGC.
                    </div>
                </div>
                <div style="text-align: center;" id="ingre2img">
                    <br>
                    <img src="./white_ingre_to_image.png" alt="ingredient to image" width="50%" height="50%">
                    <div>
                    Figure 5. The top-5 retrieval visualization of three query ingredient composition from different sources.
                    </div>
                </div>
                </li>
            </ul>
            </big>
        </p>
    </div>
    <div id="citation">
        <h2>IV. Citation</h2>
        <big>
        <b>BibTeX<b>:<br>
        <code> 
            @inproceedings{li2023photomaker,<br>
            &nbsp;&nbsp;title={Toward Chinese Food Understanding: a Cross-Modal Ingredient-Level Benchmark},<br>
            &nbsp;&nbsp;author={Wang, Lanjun and Zhang, Chenyu and Liu, An-An and Yang, Bo and Hu, Mingwang and Qiao, Xinran and Wang, Lei and He, Jianlin and Liu, Qiang},<br>
            &nbsp;&nbsp;booktitle={IEEE Transactions on Multimedia},<br>
            &nbsp;&nbsp;year={2024},<br>
            &nbsp;&nbsp;publisher={IEEE}<br>
            } 
        </code> 
        </big>
    </div>
</div>

</html>