# 士 字 位 圯 文

THESIS FOR MASTER＇S DEGREE作 者 ： 解正旭指导教师 ： 张学东 教授学 科 ： 软件工程答辩 日期 ： 2 0 1 8 年 1 月 9 日分类号 TP399 密    级 公开U D C 单位代码 10146学 号 1 5 2 0 8 3 5 0 0 1 8 3

![](images/498e9fc77b33e646645cf7c0e9f157438a3d92a1ed3f431a3ece5f428d3fe506.jpg)

硕士学位论文基于 PCA+SVM 纸币红外特征鉴伪算法研究

研究生姓名：解正旭

指导教师 ：  张学东  教授 工作单位   :     辽宁科技大学  
指导教师 ： 工作单位 ：  
论文提交日期 ： 2018 年 1 月 11 日 答辩日期 ：   2018 年 1 月 9 日  
学位授予日期 ： 授予单位 ：   辽宁科技大学  
论文评阅人 ：  张学东  教授 工作单位 ：  辽宁科技大学  
论文评阅人 ： 工作单位 ：  
答辩委员会主席 ：  杨鸿雁  教授 工作单位 ： 鞍山师范学院

# Research on Infrared Feature Authentication and Counterfeiting Algorithm Based on PCA $+$ SVM Paper Currency

by

(Majoring in Software Engineering)

Supervisor: Prof. Zhang Xuedong

January 11，2018

# 中 文 摘 要

纸币识别是当今社会一个重要的课题，也是现代的流行的深度学习和人工智能一个重要的领域。目前，纸币的识别已经研究有很长的时间了，近年来，随着经济的发展，纸币的真伪已经影响到我们的日常生活，大部分的企业都实行了数字化和智能化，银行的纸币清分机实现了一体化的过程。但是，清分机存在着一定的准确性，易受外界因素和抗污染能力的影响。本文进行对纸币预处理过后进行鉴伪的研究和分析，进而对纸币的红外特征和真假币分类进行优化。对以前的纸币处理算法实行优化，得到了很好的识别效果。最后进行仿真试验，并对实验验证的结果进行分析。

本文应用的纸币是第五版人民币鉴伪样本图像，在进行对纸币识别之前，要做好对纸币预处理工作。为了提高的纸币识别率，在对纸币的预处理过后，在纸币的增强方面进行Gabor 滤波处理，得到处理的纸币图像。然后进行纸币的红外识别工作，本文使用主成分分析法(PCA)算法对纸币的鉴伪识别，实行纸币的维数降维，利用欧氏距离作为纸币之间的距离的计算，最后使用纸币的最大的距离作为真假币的判断阈值，纸币的识别率有所提高，但是假币的错判率不好。针对这样的情况，在后面的论文中利用了 $\mathrm { P C A + S V M }$ 的算法的结合，进行对 SVM 的核函数和惩罚因子的优化。最后处理纸币的特征量和处理的时间有所减少，其中更重要的是对SVM 参数的优化后对纸币的识别率有所提高，同时假币的错判率大幅度的下降，可以在一定意义上满足市场的要求，对我国的纸币研究有着很好的借鉴作用和参考价值。

关键词: 图像处理; Gabor 处理; 伪币识别; $\mathbf { P C A + S V M }$

# ABSTRACT

Banknote recognition is an important issue in today's society and an important area of modern popular deep learning and artificial intelligence. At present, the identification of banknotes has been studied for a long time. In recent years, along with economic development, the authenticity of banknotes has affected our daily life. Most of the enterprises have implemented digital and intelligent banknotes The extension of the realization of the integration process. However, there is a certain accuracy of the sorter, susceptible to external factors and anti-pollution ability. This article carries on the research and analysis of the authenticity verification after the paper currency pretreatment, and then optimizes the paper currency's infrared characteristic and the true and the false currency classification. The previous banknote processing algorithm optimization, has been very good recognition. Finally, simulation test is carried out, and the result of experiment verification is analyzed.

The paper currency used in this article is the fifth version of the RMB counterfeit sample image, before carrying out the identification of banknotes, we should do a good job on banknotes pretreatment. In order to improve the banknote recognition rate, Gabor filter processing is performed on the enhancement of the banknote after the preprocessing of the banknote to obtain the processed banknote image. Then the banknote infrared identification work is carried out. In this paper, PCA algorithm is used to identify the banknotes, the dimensionality reduction of the banknotes is carried out, the Euclidean distance is used as the calculation of the distance between the banknotes, The maximum distance as the true and false currency judgment threshold, the recognition rate of banknotes has increased, but the miscarriage of justice is not good. In view of such situation, in the following paper, the combination of $\mathrm { P C A } + \mathrm { S V M }$ algorithm is used to optimize the kernel function and penalty factor of SVM. Finally, the characteristic amount of the banknotes to be processed and the processing time are reduced. More importantly, the recognition rate of the banknotes after the optimization of the SVM parameters is improved. Meanwhile, the misclassification rate of the counterfeit currency is greatly reduced, and in a certain sense Meet the requirements of the market, China's paper currency research has a good reference and reference value.

Key words: Image processing, Gabor processing, Counterfeit currency identification, PCA+SVM

# 目    录

独创性声明.

关于论文使用授权的说明.   
中 文 摘 要. i  
ABSTRACT . ii  
1.绪论. .  
1.1 课题研究背景和意义 .  
1.2 纸币清分机的概述 .  
1.3 纸币识别技术概要. .  
1.4 论文研究的内容和章节安排 ..  
2.图像预处理. ..  
2.1 纸币图像去噪 .  
2.1.1 均值滤波 .  
2.1.2 自适应滤波 .  
2.1.3 中值滤波 .  
2.2 图像分割 . .  
2.2.1 图像的边缘分割技术 .  
2.2.2 图像阈值分割 . .  
2.2.3 图像的归一化 . . 1  
3.纸币 Gabor 滤波处理. . 2  
3.1 纹理的描述 . 2  
3.1.1 自相关函数 . 2  
3.1.2 等灰度游程长度. .. 3  
3.2 纸币 Gabor 滤波处理 . 4  
3.2.1 Gabor 滤波器 .. 5  
3.2.2 纸币图像 Gabor 增强 . .. 6  
3.3 纸币 Gabor 处理 .. 8  
4.基于 PCA 纸币红外光鉴伪. . 0  
4.1 PCA 特征提取 .. 0  
4.1.1 PCA 无监督学习 . 0  
4.1.2 PCA 算法基本原理 .. 1  
4.2 特征向量的处理和投影 . 4  
4.2.1 奇异性分解 . 4  
4.2.2 特征值的提取方法 . 4  
4.2.3 图像特征的表征. . 5  
4.3 纸币鉴伪和分类 . 6  
4.3.1 纸币判别距离的方法 .. 7  
4.3.2 纸币的阈值判定. .. 8  
4.3.3 实验结果分析 . 9  
5.基于 PCA 和 SVM 纸币红外鉴伪. . 3  
5.1 支持向量机 3  
5.1.1 线性可分的类算法 3  
5.1.2 线性不可分的分类算法 6  
5.1.3 核函数的分类算法 8  
5.2 支持向量机分类策略 9  
5.2.1 一对一投票策略 0  
5.2.2 一对多策略 . 0  
5.2.3 二叉树分类策略 1  
5.3 $\mathsf { P C A + S V M }$ 系统实现 2  
5.3.1 SVM 分类器的构造 2  
5.3.2 纸币 MATLAB 实验设计与实现 . 3  
5.4 实验结果分析. 6  
5.4.1 $P C A + S V M$ 结果分析 6  
5.4.2 两种算法的比较 7  
6.总结和展望. 9  
6.1 论文总结 9  
6.2 展望 9  
参考文献. 1  
致谢. 5  
作者简介. 6

# 1.绪论

# 1.1 课题研究背景和意义

在人类的发展的历史中，我国也进行纸币的交换，据历史记载，纸币最早的时期是在北宋期间，称之为“娇子”。那个时候的纸币就是现在纸币的基本雏形。人民币的制造技术上也逐渐的成熟起来，无论在纸的质量上，还是在技术上都有着很大的提升。在购买设备的市场份额来看，日本的光荣品牌是购买量是最大的，因为它的性价比是最好的，也是国内银行首选。但是国内的生产商以辽宁聚龙，中超信达，广电运通等，也占领了一定的市场的份额，而且这几年也有上升的趋势，同时也得到国内银行的认可，由于这几年地方银行的兴起，不少的小的制造商也开始对这些银行进行出售，使得银行市场呈现互相竞争，共同进步的现象。

随着信息时代的到来，人们虽然用支付宝和微信付款的多了，但是基于我国的国情，国家的发展不平衡，特别在县级以下的地区，因为没有人用太多的网，纸币的流通一定的层面上还是处于一个非常重要的地位。而且，国家在颁布实施惠农的政策时，用ATM 提款机愈加的方便。所以，在进行货币之间的流通的过程中，遍布在我们的生活里，它是物与物之间的一个工具，也是一个国家和个人的财富和权力的象征。纸币本身就是一个有着名族特色的艺术品，代表我们国家的政治、经济、文化的审美标准。

图像处理技术就是在使用的纸币在传感器进行对图像的采集，然后对于这个纸币的信息进行分析，得到需求的那样。如果，只是考虑纸币的图像之类的话，在处理的纸币可见光的情况下，进行红外光，紫外光的纸币处理。

由于可见光对纸币识别的要求不是特别的挑剔，然而，也有它自身的缺陷，随着纸币的印刷的技术日益更新，假币的仿真技术也是存出不穷，使得以前的技术不是特别适合现在纸币的鉴伪了，在纸币识别的进步发展中，已经有了红外，紫外的方法等，鉴于考虑性价比方面，本文采取红外光进行对人民币识别工作。纸币在市场上流通的时候，监管部门是无法干预的，导致在这个过程犯罪率最高。在当今的飞速发展的互联网中，信息建设以及数据管理已不存在技术难点，不需要很高的成本，可以有很好可靠性纸币技术，在一定的意义上，需要建立一个好的体系，对国家的金融安全起着很重要的作用。纸币的识别技术给金融安全有着不可低估的作用，从研究的课题方面来说，这个是一个值得探索的，并且也有很大的价值所在。以下是纸币的不稳定的因素，从而影响对人民币图像处理的分析。

（1）纸币介质的不稳定性： 纸币图像的分析是以纸张为材料进行纸币的印刷，在自然的环境中容易受到破坏。如空气热度、大气湿度等，流通的过程中会出现折皱、磨破、乱画的作用下，将产生对纸币的污染。

（2）纸币图像差异性：纸币在印刷总是存在误差，不同版本的纸币的图像差异特别的大。同时，纸币的图像在构建的时候，是特别的精细，纸币图案都有不同的纹理图像组成的。特别在边缘的位置，尤其的千变万化，这种纹理在低分辨率下，表现的极其不稳定。

纸币不仅有着特别的结构特色，而且具有不稳定性，许多的研究者都在研究这个问题。可以对纸币图像进行纹理增强处理，希望可以让此类方法可以提高纸币的识别率。在不降低的效率的情况下，纸币的处理，纸币的特征提取，纸币的真假鉴伪是对纸币在图像处理的过程中不可分割的三个部分[1-4]。

# 1.2 纸币清分机的概述

![](images/1bd0fcb4a9914dd2dd726993162c0bea3d9514baf1bd06d6a528906697774f0c.jpg)  
图1.1 纸币清分机系统Fig. 1.1 Notes Sorter System

纸币清分机是一个具有高科技的机器，纸币清分机缓解了人工的劳动力，提高效率，这个应用的技术贯彻了纸币的发行-流通-收回-销毁一体化。经过我们国家的努力，目前国内的国产的清分机从无到有，从简单的到复杂的继而最后变成一体化的设备，达到国际上的要求。从目前的形势看，技术层面的比较成熟，特别在面值上，准确度和速度上都可以达到市场的要求。对于纸币的新旧，污损的技术还是没有达到国际上的要求对于一个一体化的清分机来说，主要包括图像采集，纸币处理，主控和机械操控等。其流程如下图所示，纸币由入钞口进入，首先完成采集图像信息工作，然后进行纸币进行预处理，最后将得到的图像信息进行传送到图像处理 CPU 和磁性检测，最后得到的数据和结果进行显示和真假币进行分类输出，其中在这个识别的过程中，可以使用键盘对系统的控制操作。其中图像的预处理和图像的鉴伪作为论文研究的重要的部分[5-8]。

# 1.3 纸币识别技术概要

清分机的重要技术就是对纸币图像鉴别[9-13]。其中图像的识别技术可以分为四个步骤:纸币预处理，纸币边缘分割，纸币特征提取和纸币真假分类。

图像的预处理：这个过程是进行识别前期最重要的一环，也是相对来讲比较关键的一步，它的目的是提高纸币的识别率，对获取图像的信息进行预处理，淡化的信息中噪音。当图像信息特别少的时候，还需要的对图像局部增强，矫正处理，边缘分割等，这样就可以更好的对纸币特征进行识别。目前常用的预处理方法中，去燥的方法分别有中值滤波。增强的算法有直方图均匀化，亮度增强，锐化等。

图像的分割：为了获取纸币物体的整体轮廓，还要对整个图像进行分割，也就是定位和分离不同物体。在这个过程中输入图像，这个原图像叫做元图像。目前流行的图像分割算法有三种，分别是边缘分割算法，区域图像边缘算法和自定义的分割算法。

图像的特征提取：这个是图像处理最关键的部分，在识别物体被分割的基础上，提取图像的特征向量，并对这个数据实施计算，得到数据的结果后进行分类。

图像的分类：按照提取的纸币特征值，运用模式识别的方式实施分类，确定真假币。以便对图像一些重要的信息就行说明和演示，这个过程对特征提取过后相关信息进行处理，输出的是类别的种类。

对于纸币清分机的其他功能，下面是差的两种功能，下面对一下的两种功能进行探讨。第一种方法是点算技术，就是使用对射式红外传感器进行处理。当纸币经过处理的核心部分的时候，将这些信息进行转换为脉冲信号，最后进行对纸币张数计算功能。第二种鉴伪技术，由于人民币的制造技术的提高，假钞的制造也存出不穷。机器要识别所有的假币，以前的方法已经不能够满足了。如对纸币进行红外光识别，只可以对没有红外光的假币进行鉴别，然而对有红光的假币就没有好的效果了。只有通过红外光水印真假辨别，才能判别是否是真钞。这样就要求清分机的鉴别能力需要更多的识别真钞[14-15]。正常的鉴伪识别有以下的几种类型：

紫外荧光鉴伪是最好识别真假币的措施，其次纸币在紫外光下可以展现一些隐含在不发光的物质表面可见光的物理特征 真币采用是不同的纸张，在紫光的照射下，不会有一定的荧光效果。通常的假币不会具备这个条件，会在纸币的上面发生一些反应。所以，在具有紫色光下机器是可以对纸币荧光量是可以辨别真假币。这种方法在民间特别的常用，好多都有荧光灯，使用起来特别的方便。对于有无荧光反应的假钞，这是一种比较好的方法。

纸币在可见光下可以看到不同的色差，但是当纸币在外红线的照射下呈现出两种不同的颜色，由的物理知识得知，暗的一面就是吸收了光照，才得到的暗的现象。红外光很难仿制，而且也不受印刷的影响，是当前性价比最高的识别真假币最好的方法。

利用磁性的油墨对纸币检测目前在世界上也是比较流行的一个方法，国家的人民币也适用于这个方法。灵敏的磁性感应器可以快速的捕捉到上面的磁信号。而且，人民币了同时还增加磁性的安全线，同时每个纸币种类的磁码排列都是不同的。假的纸币制造手艺限制了目前还不可以达到这个要求，因此，每个真币磁性的分布是基本固定的。

# 1.4 论文研究的内容和章节安排

纸币的真假识别是本文的研究重点，对之前的纸币的识别率进行优化提升。在这样的基础上，提出了一种高效识别率的方法。利用主成分分析法（PrincipalComponent Analysis ，PCA）与支持向量机（Support Vector Machine，SVM）的理论进行着手。利用 $\mathrm { P C A + S V M }$ 的纸币红外特征鉴伪方法，用的 Matlab 编程软件进行对人民币的算法的测试和仿真实验。纸币的识别有以下几个部分：红外光图像采集和图像处理阶段，纸币的特征空间构造提取的阶段，分类器的确定以及待识别纸币的鉴伪。

第一章内容是纸币的研究背景和意义，在考虑国内外的现状的情况下，说明我们国家在纸币研究方面需要做的东西，对纸币的清分机的描述和纸币识别历史的描述。

第二章是对纸币预处理,首先对纸币的处理的技术进行简单的描述，预处理的经历图像灰度化，图像去噪，图像的分割。去掉纸币图像的噪音和杂质，更好的为后面的识别和鉴伪更好的作用。

第三章是纸币的 Gabor 滤波的图像增强，介绍了纹理的原理，Gabor 滤波器的原理,目的是对纸币的增强。

第四章是 PCA 的红外纸币识别，介绍了无监督的学习，对于无监督学习的纸币识别的优势。后面介绍 PCA 的处理纸币的基本的流程，纸币的阈值和距离的优化处理，最后对纸币的分类。

第五章是 $\mathrm { P C A } { + } \mathrm { S V M }$ 的红外纸币的识别，考虑PCA 纸币识别的缺点，采用将他们两个进行结合的方法。经过 Gabor 滤波增强处理，而后进行 PCA 的变换和降维处理,提取纸币的特征。通过支持向量机的办法实行最终的分类，利用这个分类器最后进行真假币的鉴伪[57]。经过数据仿真，验证这个系统的有效性。

第六章是总结和展望，介绍纸币需要改正和对未来纸币研究的展望。

# 2.图像预处理

图像处理是计算机学科和其他学科的交叉部分。之间牵涉了许多的专业知识，图像的处理原理就是将图像信号转换为数字信号。然后对这个数字图像信号进行处理，达到需要的那样，如分割，获取信息，进行识别的过程[16-18]。

在论文过程中，首先要完成对纸币图像的预处理，完成纸币的灰度化，去燥，图像分割，图像的Gabor 滤波增强，具体的流程如下:

![](images/ffb9900668b500b298d99c4656613a6b609b4c05291c72c5bb1bda983ddb48b1.jpg)  
图 2.1 纸币预处理的流程图  
Fig. 2.1 Flow chart of banknote preprocessing

图 2.1 所示的流程主要包括以下的两个部分：清分机在采集纸币图像放入它们自己存储空间。本文对采集得到的纸币图像的进行预处理，完成这个结果需要许多的前期工作的准备。在对图像进行预处理过程中，得到纸币尽量最好。但是，在实际的采集过程中，受到外界的光照程度，纸币的新旧状况的影响，很难达到的要求，所以需要对纸币进行预处理，让他更符合实验的要求。这其中包括纸币的灰度化，去噪，增强。预处理结束后，就可以对纸币提取的信息就行分类和识别，取得红外特征进行纸币的真伪鉴别。最后得到想要处理的结果，预处理的结果很大程度上影响到纸币识别成效。

# 2.1 纸币图像去噪

在进行图像的处理的过程中，当输入的图像存在噪音情况下，对实验的结果特别有影响。要对图像进行滤波处理，一般的噪音来自采集和传输的过程，图像的噪音分别为加性噪声和乘性噪声两种[19-20]。

# 2.1.1 均值滤波

均值滤波复原包含算术滤波和几何滤波。坐标点 $\left( x , y \right)$ ，大小是 $\mathrm { ~ m ~ } { * \mathrm { ~ n ~ } }$ 的矩形窗口表示为 $S _ { x y }$ ，算术滤波平均值是窗口 $S _ { x y }$ 中噪音图像 $g ( s , t )$ 的平均值。

$$
f ( x , y ) = \frac { 1 } { m n } \sum _ { ( s , t ) \in s _ { x y } } g ( s , t )
$$

几何的均值的表达式为:

$$
f ( x , y ) = \left[ \prod _ { ( x , y ) \in s _ { x y } } g ( s , t ) \right] ^ { \frac { 1 } { m n } }
$$

# 2.1.2 自适应滤波

在 MATLAB 的图像算法中，wiener2 函数可以对图像噪音进行自适应滤除。wiener2 函数根据图像局部的方差来调整滤波的输出。当局部方差大的时候，滤波器的平滑效果较弱，反之，滤波器的平滑效果强。wiener2 函数采用的算法首先需要估算像素的局部矩阵和方差。

$$
\mu = \frac { 1 } { M N } \sum _ { n _ { 1 } , n _ { 2 } \in \beta } a ( n _ { 1 } , n _ { 2 } )
$$

$$
\sigma ^ { 2 } = { \frac { 1 } { M N } } \sum _ { n _ { 1 } , n _ { 2 } \in \beta } a ^ { 2 } \left( n _ { 1 } , n _ { 2 } \right) - \mu ^ { 2 }
$$

$\beta$ 表示点的 $M ^ { * } N$ 领域， ${ a } ( \mathbf { n } _ { 1 } , \mathbf { n } _ { 2 } )$ 表示的坐标为 $( \boldsymbol { \mathrm { n } } _ { 1 } , \boldsymbol { \mathrm { n } } _ { 2 } )$ ，点的像素灰度值。然后每一个像素的利用 wiener2 滤波器预计出灰度值。

$$
{ \mathsf { b } } \big ( n _ { 1 } , n _ { 2 } \big ) = \mu + \frac { \delta ^ { 2 } - \nu ^ { 2 } } { \delta ^ { 2 } } \big ( a ( n _ { 1 } , n _ { 2 } ) - \mu \big )
$$

其中， $v ^ { 2 }$ 表示图像的方差，从上面的表达式可以看出，wiener2 是可以自动调节的滤波方法，当 $\delta ^ { 2 }$ 大的时候，滤波的作用差，反之作用好。

# 2.1.3 中值滤波

中值滤波技术是一种不错的去噪方法，它可以在特殊的条件下克制一些线性的滤波噪声带来隐患。而且它可以不需要运算就可以得到图像的统计特征。这样运用的更便利。与加权的平滑滤波不同，将领域中的像素按灰度级排序，取其两边的中值作为输出像素值。它的长处在于可以在克服随机噪声的同时不使边沿含糊，然而对于那些图像层次特别锐化图像不适合采用中值滤波。

若S为像素 $( x _ { 0 } , y _ { 0 } )$ 的领域集合，包含 $( x _ { 0 } , y _ { 0 } )$ ，(x,y)是S中的元素， $f \left( x , y \right)$ 是(x,y)该点的灰度值，|𝑆|是集合S中元素的个数，Sort 表示排序，则对 $( \mathrm { x } _ { 0 } , \mathrm { y } _ { 0 } )$ 进行平滑表示为:

$$
f ^ { \prime } ( x _ { 0 } , y _ { 0 } ) { = } { [ \begin{array} { l } { } \\ { S o r t \ f ( x , y ) } \\ { ( x , y ) \in S } \end{array} ] } { \frac { ] _ { | S | + 1 } } { 2 } }
$$

在图像任意一点坐标为 $( \mathrm { x } , \mathrm { y } )$ ，大小为 $\mathbf { m } \times \mathbf { n }$ 的图像中，中值滤波就是选取 $S _ { x y }$ 中被干扰图像 $g ( s , t )$ 的中值，公式可以表示为:

$$
f \left( x , y \right) = M e d i a n { \left[ g \left( s , t \right) \right] }
$$

![](images/99acba95de21f8cf4d7578ba56c701f5f44d8bf347d1c7a4424f8e056001c89b.jpg)  
图 2.2 三种滤波的纸币图  
Figure 2.2 Three kinds of filter banknotes chart

通过对纸币去噪的效果来看，中值滤波对椒盐的噪音的处理效果特别的好。原因是椒盐只是在画面的部分点的图上，根据对中值滤波处理的结果来看，通过数据排序的方法来说。将图像中未被污染的点代替噪音点值概率比较大。因此噪声的处理特别的好，同时画面的边缘也显示的特别清晰。因此，通过数据的比较，对于椒盐密度小时，尤其是孤立噪音点，用中值滤波效果是最好的。

# 2.2 图像分割

图像分割就是利用分割算法将图像与边界进行区分的方法。以达到需要的那部分图像，而任何相邻区域之间其性质具有明显的区别。图像分割在很多图像处理方面和牵涉到不同类型的图像。把图像分割成不同的区域，并且每个区域包含着一定的特征。对要求的部分进行分割就可以提高目标图像的精确度，无关紧要的就可以放弃了。

# 2.2.1 图像的边缘分割技术

边缘检测就是对图像的边界处进行处理，显然通常边缘地带的图像的灰度值是有一定的差异性。因此这个情况下边缘是相对清晰的。可以在这样的情况下进行分割提取边界的信息，这样就可以把图像的局部特征表示出来，如灰度值和纹理值的突变等，通常得到的图像边缘信息是特别有用，在实际的运用中有着广泛的作用。

一般的分割算法有 Sobel 算子、Prewitt 算子、Robert 算子。通过这些算子对图像进行分割，就可以获得图像的边缘。

（1）Robert 算子

对于图像边缘处的灰度值进行水平方向和垂直方向进行梯度算子的计算，即：

$$
\nabla f = \left( f \left( x , y \right) - \left( x - 1 , y \right) , f \left( x , y \right) - f \left( x , y - 1 \right) \right)
$$

在进行边缘的计算的时候，对于边界上每一个的像素值计算的值进行求绝对值，而后通过阈值的判定，得到 Robert 算子实现为：

$$
R { \big ( } x , y { \big ) } = { \sqrt { \left[ f \left( i , j \right) - f \left( i + 1 , j + 1 \right) \right] ^ { 2 } + \left[ f \left( i , j + 1 \right) - f \left( i + 1 , j \right) \right] ^ { 2 } } }
$$

Robert 算子有下面的两个模块组成:

$$
\begin{array} { r } { \left[ \begin{array} { l l } { 1 } & { 0 } \\ { 0 } & { - 1 } \end{array} \right] ~ \left[ \begin{array} { l l } { 0 } & { 1 } \\ { - 1 } & { 0 } \end{array} \right] } \end{array}
$$

（2）Prewitt 算子

Prewitt 算子既可以检测边缘界还克制噪声的影响，因而对灰度和噪声较多的图像处理比较好。Prewitt 算子的大小 $3 \times 3$ ，如图所示。

$$
{ \left[ \begin{array} { l l l } { - 1 } & { - 1 } & { - 1 } \\ { 0 } & { 0 } & { 0 } \\ { 1 } & { 1 } & { 1 } \end{array} \right] } \quad { \left[ \begin{array} { l l l } { - 1 } & { 0 } & { 1 } \\ { - 1 } & { 0 } & { 1 } \\ { - 1 } & { 0 } & { 1 } \end{array} \right] }
$$

(3)Sobel算子

Sobel 算子矩阵维度和 Prewitt 算子是相同的，都是 $3 \times 3$ 。Sobel 算子的矩阵如下所示。

$$
{ \left[ \begin{array} { l l l } { - 1 } & { 0 } & { 1 } \\ { - 2 } & { 0 } & { 2 } \\ { - 1 } & { 0 } & { 1 } \end{array} \right] } \quad { \left[ \begin{array} { l l l } { - 1 } & { - 2 } & { - 1 } \\ { 0 } & { 0 } & { 0 } \\ { 1 } & { 2 } & { 1 } \end{array} \right] }
$$

下图为以上的 3 个算法处理的图像

![](images/fc70f5352068137b45788c8610e2d7416b6696556c76764cdf2f339a5ab2074f.jpg)  
图 2.5 三种不同算子纸币分割图  
Fig 2.5 three different operator banknotes segmentation diagram

使用了三个不同的分割算法进行对纸币的边界进行分割，得到三个不同的分割图。显然纸币的Roberts 算法和Prewitt 算法对纸币的边缘有着一定的效果，但是纸币的图像失真太大，不符合实验的要求。Sobel 算法实现对边缘和图像质量得到很好的效果，因此，本实验对纸币采用了这个算法。

# 2.2.2 图像阈值分割

阈值分割[21-25]是建立在区域分割基础上提出来的，它对物体与物体所在的边界有较强对比度，因操作简单直观，因此，在图像分割中有着很好的应用。这个分割的思想是把灰度级进行等级的划分，之后进行设定的阈值进行对边缘的灰度进行划分，该方法最常用的就是 Ostu 的阈值分割。

这个算法就是在进行对图像处理后得到的直方图，对这个进行常用的最小二乘法进行公式的推导，最后得到最优的分割值。利用这个原理将最优的值进行分割成两个部分，是这个两个部分的方差最大的，这样就达到分割的效果。

假设图像的灰度值为 $f \left( x , y \right)$ ，灰度级的范围为 $L$ ，假如灰度级 $i$ 的所在像素总和为 $f _ { i }$ ，则第 $i$ 级所对应的概率为：

$$
p \left( i \right) = \frac { f _ { i } } { M \times N }
$$

其中 i=1,2,…,L-1

$$
\sum _ { 0 } ^ { L - 1 } p \big ( i \big ) = 1
$$

按照图像的灰度值将 $t$ 划分为两个部分，即纸币的边缘作为 $C _ { 0 }$ 和纸币图像为$C _ { 1 }$ 。 $C _ { 0 }$ 的灰度级为 $0 { \sim } t { - } I$ ， $C _ { 1 }$ 的灰度级为 $_ { t \sim L - 1 }$ 。 $C _ { 0 }$ 部分出现的概率为：

$$
\omega _ { \scriptscriptstyle 0 } = \sum _ { \mathrm { i } = 0 } ^ { { t - 1 } } p \big ( i \big )
$$

$C _ { 1 }$ 部分的出现的概率为：

$$
\omega _ { \scriptscriptstyle 1 } = \sum _ { \mathrm { i } = t } ^ { { \cal L } - 1 } p \big ( i \big )
$$

其中 $\omega _ { 0 } + \omega _ { 1 } { = } 1$

$C _ { 0 }$ 部分的平均灰度值为：

$$
\mu _ { \scriptscriptstyle 0 } \left( { \mathrm { t } } \right) = \sum _ { i = 0 } ^ { t - 1 } i \ast \frac { p \left( i \right) } { \omega _ { \scriptscriptstyle 0 } }
$$

$C _ { 1 }$ 部分的平均度值为：

$$
\mu _ { 1 } = \sum _ { \mathrm { i } = t } ^ { L - 1 } i * \frac { p \left( i \right) } { \omega _ { 1 } }
$$

纸币图像的总平均值为：

$$
\mu { = } \sum _ { i { = 0 } } ^ { L - 1 } i p \big ( i \big )
$$

纸币图像周围介质的类间方差为：

$$
\begin{array} { r } { \delta ^ { 2 } \left( k \right) = \omega _ { 0 } \left( \mu - \mu _ { 0 } \right) ^ { 2 } + \omega _ { 1 } \left( \mu - \mu _ { 1 } \right) ^ { 2 } } \end{array}
$$

设 $k$ 的取值范围为 $0 { \sim } L { \cdot } I , 0 { \sim } L { \cdot } I$ 计算每个 $k$ 值类间方差，使得 $\delta ^ { 2 } ( k )$ 最大值的对应的 $k$ 值就是所要求的最优阈值。

![](images/a73f66430972f171dcf08b23bf7ab649d977045a4d20030c1b756babf04d9cf8.jpg)  
图 2.6 纸币原图和O   算法分割图

Fig 2.6 Banknotes and Ostu algorithm segmentation diagram

# 2.2.3 图像的归一化

纸币图像的归一化[52-54]就是经过函数的处理，将原图像转换相应的统一规范模式。图像归一化思想就是:对图像的数据进行仿射变换后的，确定变换的函数参数，最后利用这个参数对原始的图像进行规范化。函数里的图像数据有的情况下要求是浮点型才可以，而图像数灰度值都在 0-255 范围中。因此要对图像进行归一化，转化为到0-1 之间。下面是归一化纸币前后图像。

![](images/8315cdfdd0b7be4b8185a821e4821533ffd5fe5a8461c4cfc227407beb7ef3d0.jpg)  
图 2.7 纸币原图和归一化图像  
Fig 2.7 Original banknotes and normalized images

# 3.纸币 Gabor 滤波处理

Gabor 滤波变换原理就是对图像进行傅立叶变换的措施，同时也可以看作一个带通的滤波器。它在图像增强[26-27]方面有着很好的运用，Gabor 滤波器在时域和频域分辨方面都有着很好的应用，更好的显示图像的信息。Gabor 核函数对图像的局部光照和图像的对比度具有一定的鲁棒性，同时Gabor[29-32]可以在不同的方向上显示灰度的信息。

# 3.1 纹理的描述

纹理[28]是反应图像的重要特性，它的定义一般来说是出现在局部模式和它们之间的排列规则，是图像灰度级的或者颜色的某种规律性的变化，被认为是变化和统计相关的。毕竟，纹理是一种特征，与形状不同，它的定义不是提别的清晰。与特征的提取不同，纹理很少用到边缘检测，由于边缘检测对全体的亮度级的要求有点高。目前对纹理可以得到一些有用的信息，就如手掌的指纹一样，可以在某个层次上代表一个人的身份信息。

# 3.1.1 自相关函数

下图的两个图是分布规律相同的而圆的带带有不同组成的图像，在这两张的粗细的纹理图中放入一个相同大小的透明片，并按照相同的方向和速度进行移动$\Delta \mathbf { x }$ 。令 $S _ { \mathrm { { L } } }$ 表示尺寸较大的园的重叠的面积， $S _ { \mathrm { R } }$ 表示尺寸小的重叠的面积。

可以看出 $S _ { \mathrm { R } }$ 比 $S _ { \mathrm { { L } } }$ 下降的速度快，粗糙的比例与局部结构的空间复杂周期有关。周期小，纹理就细。反之亦然。假定图像为 $f ( x , y )$ ，它的自相关函数的公式如下：

$$
R \left( \varepsilon , \eta , j , k \right) = \frac { \displaystyle \sum _ { x = j - w } ^ { j + w } \sum _ { y = k - w } ^ { k + w } f \left( x , y \right) f \left( x - \varepsilon , y - \eta \right) } { \displaystyle \sum _ { x = j - w } ^ { j + w } \sum _ { y = k - w } ^ { k + w } \left[ f \left( x , y \right) \right] ^ { 2 } }
$$

![](images/41aec55558dc68e95f5b377defd14ab038d0774fbc34e4a04cc4f41c583695aa.jpg)  
Fig 3.1 Thickness map and the overlapping area of the shift relationship

# 3.1.2 等灰度游程长度

灰度的游程长度定义是在某 $\nu$ 方向上连续，共线是具备一样灰度级的像素个数。一般的规律来说，在粗纹理所在的灰度长因子值大，而在细纹理的里，短游程灰度长因子数目比较多。所以，通常使用灰度游程长度进行分析一般用在线性纹理中。假设某个计算灰度的游程矩阵为 $N ^ { ( \theta ) }$ ，其第 $\mathbf { \Delta } _ { a }$ 行,第 $b$ 列的元素 $n _ { a b }$ 体现图像中在 $\nu$ 方向上灰度为 $a$ ,游程长度为 $b$ 的灰度频率的总次数。

就可以构造在 $\nu$ 方向上 $4 { \times } 4$ 的灰度游程矩阵 $N ^ { ( \theta ) }$ ，如下图所示，从而由灰度矩阵得到纹理特征的度量。

![](images/1187bfa5cd4fade7c2eae09d7600228178dd50a72b6b6fff4f8a8ceea7a0c8e9.jpg)  
图 3.1 粗细纹理图和重叠面积的平移关系  
图 3.2 图像灰度和灰度等级分布Fig 3.2 Image gray and gray level distribution

![](images/d3ea052cd6d23b6b441a5e5246d91bb695c1513b31ea4c106b893b3ce1a80dde.jpg)  
图 3.3 四个方向的游程矩阵  
Fig 3.3 Four directions of the runner matrix

通常可以将图像中任意一点在 $\nu$ 方向上游程长度为 $b$ 的情况发生的概率为$f ( a , b )$ ，由 $f ( a , b )$ 可以比较好的纹理特征的参数。

（1）长游程加重法：

$$
L R E = \sum _ { a , b } b ^ { 2 } f ( a , b ) / \sum _ { a , b } f ( a , b )
$$

由公式可以得到，当游程长时， $L R E$ 大。

（2）灰度值分布：

$$
G L D = \sum _ { a } \Biggl [ \sum _ { b } f ( a , b ) \Biggr ] ^ { 2 } / \sum _ { a , b } f ( a , b )
$$

由公式可以得到，当灰度游程等分布时， $G L D$ 最小；假设某些图像灰度出现多，灰度较匀称，则 $G L D$ 大。

（3）游程比：

$$
R P G = \sum _ { a , b } f \left( a , b \right) / M ^ { 2 }
$$

$M ^ { 2 }$ —像素总数

# 3.2 纸币 Gabor 滤波处理

视觉系统把视网膜的图像分解成许多的滤波后的图像加以识别的，呈现的每幅图像的频率,方向的变化范围较窄。就是在滤波的图像的在一个窄的频带和方向的范围内进行划分。在这个的启发下，在模拟人类的视觉中，将频率和方向结合在一起，调谐到一个比较小的范围内进行分析。Gabor 滤波器具备自相似性，所以可以很好的形容对应空间次数，空间地方及位置选择性的某段信息。同时对图像的边缘的信息提别的灵敏，并且图像对光照的变化不是很灵敏，但是光照的变化有着很好的适应性。本文中使用 Gabor 滤波器来增强纸币图像，增强预处理的纸币图片。

# 3.2.1 Gabor 滤波器

Gabor 滤波是在 1940 年期间提出一个处理图像的思想，后来在对图像处理的应用中，有着很好的效果。在实际的运用中，当的图像在时域里，平稳信号变化趋于平和，非平稳并不是那么的稳定，也许会不断进行变换，传统的变换运用傅立叶的变换，但是傅立叶是全局，效果并不好。利用Gabor 进行对信号进行分割成等距离的，在实行傅立叶变换，这样使得效果变得更好，此方法就是加个$f \left( t \right)$ 窗口函数，进行处理。

设函数 $f$ 为具体的函数，则Gabor变换为:

$$
G _ { f } \left( a , b , \omega \right) = \int _ { - \infty } ^ { + \infty } f \left( t \right) g _ { a } ^ { \ast } \left( t - t _ { 0 } \right) e ^ { - i \omega t } d t
$$

其中， $g _ { a } \left( t \right) = \frac { 1 } { 2 \sqrt { \pi a } } e x p \Biggl ( - \frac { t ^ { 2 } } { 4 a } \Biggr )$ 为高斯函数，别名为窗函数。

由于 $a > 0 , b > 0$ ， $g _ { a } ^ { * } ( t )$ 是 $g _ { a } ( t )$ 共轭函数。 $g _ { a } ( t - t _ { 0 } )$ 是一种局部化的“窗函数”。其中，参数 $t _ { 0 }$ 用与平移移动窗口，以便于覆盖整个区域。

$$
f \left( t \right) = \frac { 1 } { 2 \pi } \int _ { - \infty } ^ { + \infty } \int _ { - \infty } ^ { + \infty } G _ { f } \left( a , b , \omega \right) g _ { a } \left( t - t _ { 0 } \right) e ^ { i \omega t } d \omega d b
$$

Gabor 中的 $g \left( t \right)$ 为一个窗函数有两个缘由：一是窗函数的 Fourier 逆变换同时也是窗口函数的部分化，同时显示频域局部化;二是 Gabor 变换最好的窗口函数是 Fourier 变换。其目标就是在 Gabor 滤波解决过后，才有真正的意义上解决时间与频率问题。就是利用 Gabor 变换得到了时域局部化的目标。它可以在整体的基础上提供全部的信息而且又可以提供任意的局部时间。

（1）离散Gabor 变换的一般求法首先选取核函数：

$$
g ( t ) = \left( \frac { \sqrt { 2 } } { T } \right) ^ { 2 } e ^ { - \pi \left( \frac { t } { T } \right) ^ { 2 } }
$$

其对应的对偶函数为：

$$
\gamma ( t ) = \left( \frac { 1 } { \sqrt { 2 } T } \right) ^ { \frac { 1 } { 2 } } \left( \frac { K _ { 0 } } { \pi } \right) ^ { - \frac { 3 } { 2 } } e ^ { \pi \left( \frac { t } { T } \right) ^ { 2 } } \sum _ { \frac { n + 1 } { 2 } > \frac { 1 } { T } } \left( - 1 \right) ^ { n } e ^ { - \pi \left( \frac { n + 1 } { 2 } \right) ^ { 2 } }
$$

再进行离散Gabor 弱变换处理：

$$
G _ { m n } = \int _ { - \infty } ^ { + \infty } \varphi \left( t \right) g ^ { \ast } \left( t - m T \right) e ^ { - j n \omega t } d t = \int _ { - \infty } ^ { + \infty } \varphi \left( t \right) g _ { m n } ^ { \ast } \left( t \right) d t
$$

公式 3.9 中 $\varphi ( t )$ 函数表达形式如下：

$$
\varphi ( t ) = \sum _ { m = - \infty } ^ { + \infty } \sum _ { n = - \infty } ^ { + \infty } G _ { m n } \gamma \left( t - m T \right) e ^ { - j n \omega t }
$$

其中， $g _ { m n } = g \left( t - m T \right) e ^ { - j n \omega t } , \gamma \left( t \right)$ 是 $g \left( t \right)$ 的对偶函数，两者之间都是双正交关系。Gabor 滤波纸币图像如下：

![](images/e9614ad3935cae5052af0b6a38c00d96e3fb6bbf77852fdaff277950a44f8965.jpg)  
图 3.4 纸币转换滤波和Gabor 滤波图像  
Fig 3.4 Banknote conversion filter and Gabor filter image

（2）二维Gabor 函数数学表达

复数表达：

$$
{ \bf g } { \bf ( } x , y , \lambda , \theta , \psi , \sigma , \gamma { \bf ) } = \exp \left( - \frac { x ^ { 2 } + \gamma ^ { 2 } y ^ { ' 2 } } { 2 \sigma ^ { 2 } } \right) \exp \left( i { \left( 2 \pi \frac { \dot { x _ { { + } } } } { \lambda } + \psi \right) } \right)
$$

实数部分：

$$
{ \bf g } { \bf ( } x , y , \lambda , \theta , \psi , \sigma , \gamma { \bf ) } = \exp \left( - { \frac { x ^ { 2 } + \gamma ^ { 2 } y ^ { ' 2 } } { 2 { \sigma } ^ { 2 } } } \right) \cos \left( 2 \pi { \frac { x ^ { ' } } { \lambda } } + \psi \right)
$$

虚数部分：

$$
g \left( x , \mathbf { y } , \lambda , \theta , \psi , \sigma , \gamma \right) = \exp \left( - \frac { { \dot { x ^ { 2 } } } + \gamma ^ { 2 } y ^ { ' 2 } } { 2 \sigma ^ { 2 } } \right) \sin \left( 2 \pi \frac { \dot { x ^ { } } } { \lambda } + \psi \right)
$$

其中， $x ^ { ' } = x \cos \theta + y \sin \theta$ 和 $y ^ { ' } = x \sin \theta + y \cos \theta$ 。

# 3.2.2 纸币图像 Gabor 增强

Gabor 小波处理就是在实际的操作中存在着大量的冗余的信息，保证处理的滤波的响应在显示的频谱上峰值可以互相接触，且不重叠。因此使用下面的办法就可以进行解决这个问题，让 $B _ { l }$ 和 $B _ { h }$ 为中心频率可以从低到高的范围，得到的中心频率是 $\left( B _ { 0 , \mathrm { m } } , C _ { 0 , \mathrm { m } } \right)$ ，它们对应的二维标准差 $\left( \sigma _ { { \scriptscriptstyle B } , m } , \sigma _ { { \scriptscriptstyle C } , m } \right)$ 的设计确保就是多通道的滤波。可以有下面的公式:

$$
D _ { c } = \tan \left( \frac { \pi } { 2 k } \right) \left[ B _ { h } - 2 \ln 2 \left( \frac { D _ { B } ^ { 2 } } { B _ { h } } \right) \right] \left[ 2 \ln 2 - \frac { \left( 2 \ln 2 \right) ^ { 2 } D _ { B } ^ { 2 } } { B _ { h } ^ { 2 } } \right] ^ { \frac { 1 } { 2 } }
$$

为了获取图像的不同的特征，在处理的过程中选取一个不是很长的 Gabor的滤波进行提取图像的特征。通常来说，当选择的滤波器越多，获得的信息就特别的丰富可以表示特征的存在和频率的范围。但是选取的过多就会增加计算量，这个方法是不可取的，要选取一些有价值的滤波器进行分析，确保要求，由低频到高频带宽变大。这是原始图像的高频分量较少，是为了纹理的每个指标的频率增大。在此滤波器的尺度区间是指数级的，可得：

$$
B _ { h } = a ^ { M - 1 } B _ { l }
$$

同时参数为：

$$
a = \left( \frac { B _ { h } } { B _ { l } } \right) ^ { \frac { 1 } { M - 1 } }
$$

下图为滤波器的中心的频率中心坐标为：

$$
B _ { 0 , m } = B _ { l } a ^ { m } \qquad \mathrm { m = 0 , 1 , . . . , } M - 1
$$

现在来计算滤波器参数 $\sigma _ { \mathrm { B , m } }$ ，令 $\mathbf { \Psi } _ { t }$ 为坐标上的半幅宽度，即最低的频率滤波器的椭圆的半径，则当 $\mathbf { m } { = } 0 , 1 , { \ldots } { \ldots } , M { - } 1$ ，对应每个椭圆的半径为 $\boldsymbol { a } ^ { \mathrm { m } } t$ ，可以得到：

$$
\begin{array} { c } { { B _ { _ h } - B _ { _ l } = t + 2 a t + 2 a ^ { 2 } t + . . . + 2 a ^ { M - 2 } t + a ^ { M - 1 } t } } \\ { { \displaystyle = \frac { a + 1 } { a - 1 } \Big ( a ^ { M - 1 } - 1 \Big ) t } } \end{array}
$$

设椭圆的半径为 $\mathbf { \Phi } _ { t }$ 所在的位置是滤波器高频最小波幅的一半，即它的方差是$2 \sqrt { \ln { 2 } }$ 倍，得到的最高的幅值是为：

$$
a ^ { M - 1 } t = \sigma _ { { } _ { B , M - 1 } } \sqrt { 2 \ln 2 }
$$

由上面的几个公式可以得出，消除 $t$ 可得：

$$
\sigma _ { B , M - 1 } = \frac { \bigl ( a - 1 \bigr ) B _ { h } } { \bigl ( a - 1 \bigr ) \sqrt { 2 \ln 2 } }
$$

每个滤波器的带宽呈指数增长，同时可以获得横坐标的滤波器方差为：

$$
\sigma _ { { } _ { B , m } } = \sigma _ { { } _ { B , M - 1 } } a ^ { m - M + 1 } \quad m = 0 , 1 , . . . , M - 1
$$

由每个纵坐标方向方差是 $\sigma _ { c , m }$ ，对于坐标 $L$ 个滤波的方向，其中的每个椭圆的夹角是 $2 \pi / L$ ，得到的直线方程为：

$$
C = C \tan \beta = B \tan \left( \pi / L \right)
$$

此时最高频率的椭圆方程为：

$$
\frac { \left( B - B _ { h } \right) ^ { 2 } } { 2 \ln { 2 \sigma _ { B , M - 1 } ^ { 2 } } } + \frac { C ^ { 2 } } { 2 \ln { 2 \sigma _ { C , M - 1 } ^ { 2 } } } = 1
$$

由上面的直线方程和椭圆方程可以得到一个关于 $B$ 的交点方程为：

$$
\left( B - B _ { h } \right) \sigma _ { c , M - 1 } ^ { 2 } + \left( \tan \frac { \pi } { L } \right) ^ { 2 } B ^ { 2 } \sigma _ { B , M - 1 } ^ { 2 } = 2 \ln 2 \sigma _ { c , M - 1 } ^ { 2 } \sigma _ { B , M - 1 } ^ { 2 }
$$

从上面的公式能够看出，直线和每一个椭圆有且只有一个交点，根据定理可得，一元二次方程的有且只有一个，即：

$$
\Big ( 2 B _ { h } \sigma _ { { \scriptscriptstyle C } , M - 1 } ^ { 2 } \Big ) ^ { 2 } - 4 \left( \sigma _ { { \scriptscriptstyle C } , M - 1 } ^ { 2 } + \left( \tan \frac { \pi } { L } \right) ^ { 2 } \sigma _ { B , M - 1 } ^ { 2 } \right) \left( B _ { h } ^ { 2 } \sigma _ { { \scriptscriptstyle M } - 1 } ^ { 2 } - 2 \ln 2 \sigma _ { B , M - 1 } ^ { 2 } \sigma _ { { \scriptscriptstyle C } , M - 1 } ^ { 2 } \right) = 0
$$

从上面的纵坐标的最高频率方差为：

$$
\sigma _ { C , M - 1 } = \tan \frac \pi L \sqrt { \frac { B _ { h } ^ { 2 } } { 2 \ln 2 } - \sigma _ { B , M - 1 } ^ { 2 } }
$$

则纵坐标的每个滤波的方差为：

$$
\sigma _ { c , m } = \sigma _ { c , M - 1 } a ^ { m - M + 1 } \quad m = 0 , 1 , 2 . . . . . , M - 1
$$

利用这个旋转方程，可以得图像每个方向的滤波器函数。在进行纸币图像增强的时候，主要目的就是增强需要的地方，尤其对那些感兴趣的问题细节特征需要增强，上面的滤波组进行尽可能减少冗余，在这个算法中，在这个基础上减少一些分量，这样就可以消除图像的主流成分对二维 Gabor 函数的影响，这个过程叫做是直流的补偿，使得二维 Gabor 滤波的变换不受灰度的影响，而且这个措施对图像的光照不敏感，经过我的实验的研究，这个算法可以对纸币细节的方面增强有着显著的作用。

# 3.3 纸币 Gabor 处理

本文纸币使用 Gabor 对纸币图像增强处理，首先对预处理纸币图像进行规格化，然后得到灰度值的均值和方差。，

归一化后的均值 $\scriptstyle M _ { 0 } = 8 0$ ，方差 $\mathrm { V a r } _ { 0 } { = } 2 0 0$ ，纸币图像的尺寸是 $1 1 2 \times 9 2$ ， $M$ 为原始图像均值，Var 为原始图像的方差。len 和 wid 分别为下的长度和宽度。下面对图像规格化 fpn 的计算：

$$
f p n = \left\{ \begin{array} { l l } { \displaystyle M _ { 0 } + \frac { M _ { 0 } + s q r t ( V a r _ { 0 } { } ^ { * } ( f p - M ) ) } { V a r } } & { f p > M } \\ { \displaystyle M _ { 0 } - \frac { M _ { 0 } + s q r t ( V a r _ { 0 } { } ^ { * } ( f p - M ) ) } { V a r } } & { f p \le M } \end{array} \right.
$$

其中 $f p$ 为对应纸币的直方图。

接下来纸币图像的 $x$ 和 $y$ 方向上梯度 $d x$ 和 $d y$ ，对文件夹的真币进行梯度计算。

$$
d x { \big ( } m , n { \big ) } = d x { \big ( } m , n { \big ) } + f p { \big ( } m + i - 2 , n + j - 2 { \big ) } * s o b e l x { \big ( } i , j { \big ) }
$$

$$
d y \left( m , n \right) = d y \left( m , n \right) + f p \left( m + i - 2 , n + j - 2 \right) * s o b e l y \left( x , y \right)
$$

其中 $m$ 和 $n$ 就是之间进行， $s o b e l x { = } [ - 1 , 0 , 1 ; - 2 , 0 , 2 ; - 1 , 0 , 1 ]$ ，其中 sobely=sobelx’，本论文中有四个个文件夹都放入纸币。对纸币进行分块进行 Gabor 处理，对每个纸币的块的方向进行处理，在这个处理的过程中把对应的弧度改成角度。最后对每张纸币进行7 个角度的采集信息。下面就是纸币一个角度Gabor 处理的结果图:

![](images/657f6ebfb28c9e059e8701eb04b779db253f9ce71370b3a78fe7c14149bad0b5.jpg)  
图 3.5 纸币图像灰度图和Gabor 滤波灰度图 Fig 3.5 Banknote image gray and Gabor filter grayscale

# 4.基于 PCA 纸币红外光鉴伪

PCA 是目前对图像特征提取最好的方法之一，最初的应用于人脸识别的领域中。早在1987 年Kirby 和Sirovich 二人为了解决人脸识别的维数过高的难题。他们引用了 PCA 算法。他们最后虽然没有引到人脸识别的领域，但他们二人将降维方法让许多爱好图像处理的学者的关注和探索。经过了多年的实验，在 1991年由Alex Pentland 和 Matthew Turk二人将PCA算法[33-37]很好应用于人脸识别中，人脸识别的领域得到很大的进步。

# 4.1 PCA 特征提取

本文利用 PCA 算法对纸币进行处理，纸币的信息大比较大，对纸币的处理的特征也是一个不错的方法。对纸币数据空间进行降维，提取具有代表性的特征向量。将这个方法应用到纸币识别领域，可以解决两个问题。一是具有判别能力获取的问题。利用 PCA 可以很好的提取需要的信息，它并不是随意的提取纸币的特征，而是有选择的提取。提取一些可以区分很大差别的类。二是解决处理的纸币信息量大，计算时间长的问题。该方法将高维的降维处理，实现了图像数据的压缩。同时利用了无监督的方法对纸币的特征的识别。以上为 PCA 在纸币的处理中的方法和优点，所以利用这个算法在一定意义上有一定的可行性。

# 4.1.1 PCA 无监督学习

无监督督学习[38-39]是事先不知道图像的分类标准，计算机通过对待图像样本进行分析，可以得到每一类图像的特征。通过统计分析的待分类图像具有识别能力特征系数，自主建立一个分类的原则。无监督学习和监督性学习在一定的意义上并没有明确的定义，并不可以从客观的角度辨别的监督者是特征提取者还是目标实验者。

一个好的无监督学习工作就是表示图像数据特征的“最佳”。这个好的特征可以有很多的表达方式，通常来说，在自身表现比本身更可以体现信息同时还受到一些限制的情况下，尽最大可能保存多的信息。有很多专家对无监督学习的进行定义，最后得到方法有 3 种分别是低维，稀疏和独立表示。低维表示将数据尽可能压缩在小的范围进行描述。稀疏就是将数据嵌入到大多数为零的矩阵中。它通常也有增加维数作用，目的是让更多的数据为零的信息不丢失，可以使得我的整体信息可以分布到整个坐标轴上。独立的表示的方法目的就是把数据分开来寻找数据的来源，使得最后的得到的维度可以相互得到独立。

# 4.1.2 PCA 算法基本原理

主成分析的方法在对纸币图像处理的过程中，不是直接的就利用原图的矩阵，它是用少量的若干个新的变量或者是原变量的线性组合代替原来的图像矩阵信息。这样就可以用一个新的矩阵信息代替以前的矩阵信息，同时得到的矩阵是互相正交的，这样就可以消除原始变量之间的重复信息。

假设一个图像的矩阵 $X = \left( X _ { 1 } , X _ { 2 } , . . . , X _ { \mathrm { { m } } } \right)$ ，有N 张随机训练的样本。每一张纸币的样本 $X _ { \mathrm { i } }$ 都有 $\mathfrak { n }$ 个元素或者特征，就如：

$$
X _ { i } = ( X _ { i , 1 } , X _ { i , 2 } , . . . , X _ { i , n } )
$$

通过这个特征的元素，对其定义一个列向量：

$$
L ( x ) = \left( X _ { 1 } , X _ { 2 } , . . . , X _ { m } \right) ^ { T }
$$

把一个矩阵 X 按列进行堆叠变换叫做向量化。

利用两个随机变量之间的线性依赖，经过协方差计算两个数据之间的是否存在关系。设 $\mathbf { \boldsymbol { x } }$ 表示一个随机的变量, $\boldsymbol { x } = ( x _ { 1 } , x _ { 2 } , . . . , x _ { N } ) ^ { T }$ ，这个向量 $\mathbf { \boldsymbol { x } }$ 的均值为：

$$
\mu { = } \frac { 1 } { N } \sum _ { i = 1 } ^ { N } x _ { i } ( i { = } 0 , 1 , 2 , . . . , N { - } 1 )
$$

求出样本的标准差，如下式：

$$
\sigma = \frac { 1 } { N } \sum _ { i = 1 } ^ { N } \bigl ( x _ { i } - \mu \bigr ) \bigl ( x _ { i } - \mu \bigr ) ^ { T } \quad ( i = 1 , 2 , . . . , N )
$$

对图像进行中心化：

$$
X _ { _ a } = { \frac { X - \mu } { \sigma } }
$$

$X$ 矩阵的协方差 $C$ 是定义为：

$$
\boldsymbol { C } = \sum _ { i = 1 } ^ { N } x _ { i } \boldsymbol { x } _ { i } ^ { T } = X _ { a } \boldsymbol { X } _ { a } ^ { T } \quad \left( i = 1 , 2 , . . . , N \right)
$$

这样获取的协方差的矩阵的维数是 $N { \times } N$ ，协方差给带来数据的重要的信息。比如，看到的值近似于零时，可以分类出一些不相关的特征。或低或高就是有一定的关联。对于矩阵进行区分，就可以进行放弃。PCA 通过协方差矩阵变成对角阵的方法继而变换数据，就是除了对角线的外全部归一为 0。在这样的情形下，数据之间没有什么依赖，选择一个阈值进行分组，这样就可以很清晰的将数据分开，与其他的特征的值无关联。其中有上面信息得到了一个重要的新信息，可以对数据进行分类或压缩。寻找一个变换 $\boldsymbol { Q }$ ，将定义的集合 $X$ 中的特征向量映射到集合 Y 的另一个的特征向量中。让 $Y$ 中的矩阵的协方差矩阵转换为对角阵。可以变换为线性的，定义为：

$$
C \ ( Y ) { = } C { \big ( } X { \big ) } Q ^ { T }
$$

由于协方差的矩阵是对称的，因此 $C ( Y ) ^ { \mathrm { { T } } } = Q C { ( X ) } ^ { \mathrm { { T } } }$ 。

为了根据 $X$ 的矩阵的特征，获取 $Y$ 的特征的协方差，可以替代以前的矩阵$C ( Y )$ 和 $C ( Y ) ^ { T }$ 得到 $C 1$ 。

$$
C 1 = Q C Q ^ { T }
$$

如上面的等式，可以寻找 $\boldsymbol { Q } , \boldsymbol { c }$ 是对角阵。这个过程在矩阵的过程中叫做矩阵对角化。考虑到 $\boldsymbol { Q } ^ { - 1 } = \boldsymbol { Q } ^ { T }$ ,可以达到 $\boldsymbol { Q } ^ { T } \boldsymbol { C } ( \boldsymbol { Y } ) ^ { T } = \boldsymbol { C } ( \boldsymbol { x } ) ^ { T }$ ,这个求得等式特别的有用，在数据压缩的过程中，利用 $C ( Y )$ 中重要的元素，可以得到近似的 $C ( X )$ 。考虑上面的变换，特征向量的维数存着一定的关系，当纸币维数从 30 到60 左右的时候，识别率有着显著的上升，中间以将等式写成下面的等式：

$$
\boldsymbol { C } \big ( \boldsymbol { X } \big ) \boldsymbol { Q } ^ { T } = \boldsymbol { Q } ^ { T } \boldsymbol { C } \big ( \boldsymbol { Y } \big )
$$

其中，协方差上对角线元素采用线性代数的表达符号，标记为 $\lambda$ ，带入上面的公式进行化解最后得到一个 $\boldsymbol { Q }$ ：

$$
C ( x ) w _ { i } = \lambda _ { i } w _ { i }
$$

$\mathbf { w } _ { i }$ 表示 $\boldsymbol { Q }$ 的第 $i$ 的 $\lambda _ { i }$ 是特征值， $\mathbf { w } _ { i }$ 是特征向量。由于 $\mathrm { \Delta y }$ 具有零均值特性，可以达到满足下式：

$$
\boldsymbol { C } \left( \boldsymbol { Y } \right) = \boldsymbol { Q } \boldsymbol { C } \left( \boldsymbol { X } \right) \boldsymbol { Q } ^ { T } = \boldsymbol { \Lambda } = d i a g ( \lambda _ { 1 } , \lambda _ { 2 } , . . . , \lambda _ { \scriptscriptstyle N } )
$$

通过的公式可以知道，利用 PCA 的方法既可以消除这些变量的关联的信息，同时能够保存原始大量有用的信息。可以看出矩阵的前后并没有很大的变化，然而特征向量之间的关系发生了很大的变化。这样就可以达到要求。不仅可以使原始信息不受损失，而且对高维的矩阵进行了降维，计算量大大的减少。但是就当前的一些信息进行筛选，让得到的数据在很大的程度上对我更有利。

![](images/39f4b06d984fa39ffccd2cab9b7e52b76e8a4db75be3b4f0cefa87f779daba45.jpg)  
图 4.1 特征点 PCA 的分类图Fig 4.1 Feature Points PCA classification map

上面就是两个特征点进行分析，通常用彩色图变成灰度图，然而，PCA 通常用于许多特征的数据。在的实际的应用中，它们的原理是相同的，但是根据求解高次，通常许多的特征数据进行分类，其中特征向量与矩阵或像素有关。例如，将图像的特征向量点进行分类，将矩阵排成列向量，通过 PCA 获取一组特征向量。为了实行分类，一个新的纸币图像根据 PCA 得到的变换计算出新的图像的矩阵，并与其它图像进行比较，它的优点就是在于 PCA 具有独立的特征。

# 4.2 特征向量的处理和投影

# 4.2.1 奇异性分解

利用 PCA 降维是最重要的是训练的样本最好的方差，求解最优的特征值和特征向量。可以对纸币的任何一张的纸币信息都可以用一列的向量表示出来。将训练的样本进行集合一起，共同构成需要的协方差矩阵。通过这个方法主要是为了计算矩阵 $X$ 和协方差 $c$ 特征值和特征的向量。但是协方差的维数特别的高，进行矩阵的求解泰国复杂，导致开发的软件内存占满，运算的时间长，在这样情况下，引入了奇异值分解[40-42]。

SVG 定理:假设有一个 $\mathbf { m } { \times } \mathbf { n }$ 的矩阵 $\mathrm { \Delta } \mathrm { X }$ ，矩阵之间存在 $U$ 与 $V$ 两个正交矩阵:

$$
\begin{array} { r } { \{ U = [ u _ { 1 } , u _ { 2 } , . . . , u _ { m } ] \quad U ^ { T } U = 1 } \\ { V = [ \nu _ { 1 } , \nu _ { 2 } , . . . , \nu _ { m } ] \quad V ^ { T } V = 1 } \end{array}
$$

得到的矩阵为:

$$
U ^ { T } A V = \left[ { \begin{array} { l l } { \sum r } & { 0 } \\ { 0 } & { 0 } \end{array} } \right]
$$

$$
\sum r = d i a g \left[ { \hat { \lambda } } _ { 1 } , { \hat { \lambda } } _ { 2 } , . . . , { \hat { \lambda } } _ { \mathrm { r } } \right] \quad { \hat { \lambda } } _ { 1 } \geq { \hat { \lambda } } _ { 2 } \geq . . . { \hat { \lambda } } _ { \mathrm { r } } \geq 0 , \quad U _ { i } - A A T ~ ; ~ V _ { i } - A T A
$$

由 SVG 定理可知， $\boldsymbol { A } \boldsymbol { A } ^ { T }$ 和 $A ^ { T } A$ 的特征向量存在对应关系:

$$
u _ { i } = \frac { 1 } { \lambda _ { i } } A \nu _ { i } \quad i = 1 , 2 , . . . , r - 1
$$

通过这个矩阵的求解可以实现AAT到 $\mathtt { A ^ { T } A }$ 特征向量的间接实现。

# 4.2.2 特征值的提取方法

在进行纸币的图像处理的过程中，一般纸币的数量没有纸币图像的维数的多，根据 SVG 定理，X的协方差矩阵 C1 的特征值和相应的特征向量就可以用矩阵${ \bf W } = { \bf X } ^ { \mathrm { T } } { \bf X }$ 获得，这样降低了维数，进而提高了预算的速度。

因为协方差矩阵的秩不是提别好，相应的特征向量也不好。但是这些信息包括大量图像的特征信息。但是矩阵后面的特征值也具有纸币图像的信息，为了解决信息的问题，将排在前面的特征向量与它相对应的特征向量映射到 PCA 的投影空间。这样就可以在最大的限度下保留纸币的最多信息。

经过 PCA 算法得到协方差，协方差的是依次递减的，从概率论的只是可以得出，方差越大，里面包含的信息就特别的大，依次得到的特征值信息也是递减的。采用了以下的几个方法。讨论下面的几个提取特征值得方法：

方法一：丢弃最后的 $3 5 \%$ 的特征向量

知道矩阵的特征向量的特征值的是按大小进行排列的，越往后的得到的有用的信息就越少，可以将这些信息进行丢弃。这样的信息丢失虽然降低图像的维度，但是有可能失去一些有用的信息。

方法二：丢弃了前面的三个向量

将全部的图像特征值进行从大到小排序，但是由于中方差是没有变化的。前几个的最大的特征值有时反应图像受到环境的因素的影响造成的影响。舍弃前面几个，可以有效的解决环境对影响的总体特征。这种方法的缺点容易丢失一些重要的信息。

方法三：按计算的复杂度进行维数的确定

这个方法不和其他的方法一样，是比较人性化的一面，可以对能具体的问题可以具体的对待。思想就是进行最后的留下的特征值的信息量与总信息的比值是z。通常是要求 $\mathrm { e { = } 9 0 \% { \sim } 9 9 \% }$ 之间取值，该方法的计算如下：

$$
z _ { i } = \frac { \displaystyle \sum _ { i = 1 } ^ { k } \lambda _ { i } } { \displaystyle \sum _ { i = 1 } ^ { m } \lambda _ { i } } \geq \mathbf { e }
$$

其中图像最后选取的特征值的个数， $m$ 为图像特征值总的个数，此式又为贡献率。一般要求 $z _ { \mathrm { i } }$ 取为 $9 9 \%$ ，即要求训练的样本在前 $\mathfrak { p }$ 个特征向量集合上投影量有 $9 9 \%$ 。

# 4.2.3 图像特征的表征

本算法采用预处理图像进行训练，采用的纸币进行识别的作用，将这些纸币图像先经过 PCA 进行处理，转换为的矩阵的形式，形成了样本的矩阵。则求得的训练的样本集为：

$$
X = \left( x _ { 1 } , x _ { 2 } , . . . , x _ { n } \right)
$$

特征提取的方法如下：

（1）纸币图像矩阵的平均值为：

$$
\overline { { X } } = \frac { 1 } { n } \sum _ { i = 1 } ^ { \mathrm { n } } x _ { i }
$$

（2）每个图像与总平均值的差值为：

$$
d _ { i } = x _ { 1 } - \overline { { X } } \quad ( i = 1 , 2 , . . . , n )
$$

（3）构造协方差的图像矩阵：

$$
H = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } d _ { i } d _ { i } ^ { T } = \frac { 1 } { n } A A ^ { T }
$$

其中 $A = \left( d _ { 1 } , d _ { 2 } , . . . , d _ { n } \right)$

$\textcircled{1}$ 求解特征矩阵 $\boldsymbol { A } \boldsymbol { A } ^ { T }$ 的特征值 $\lambda _ { \mathrm { i } }$ 与其对应的特征向量 $t _ { i }$ 。

$\textcircled{2}$ 将上面特征解的求得贡献率的取值方法，选取的 $\boldsymbol { A } \boldsymbol { A } ^ { T }$ 从大到小的特征值个数和贡献率，接下来求出原协方差矩阵的特征向量：

$$
u _ { i } = \frac { 1 } { \sqrt { \lambda _ { i } } } A \nu _ { i } \left( i = 1 , 2 , . . . , p \right)
$$

得到图像的空间为：

$$
U = ( u _ { 1 } , u _ { 2 } , . . . , u _ { p } )
$$

最后实现投影的界面为：

$$
W = U ^ { T } \ast d _ { i } = U ^ { T } \left( x _ { i } - \bar { X } \right) \ \left( i = 1 , 2 , 3 , . . . , n \right)
$$

根据上图，选取的贡献率为 $9 9 \%$ 对应的特征的个数为 $\scriptstyle { L = 4 0 }$ 保留样本的大部分的信息。

# 4.3 纸币鉴伪和分类

利用 PCA 算法对纸币的识别大体通过三个阶段，第一阶段对纸币进行目的性的学习，第二阶段使用心得纸币进行特征向量的投影，这个过程进行选取需要进行纸币鉴伪[55-56]的分类的阈值，第三阶段对待测试纸币进行识别。选取了 100张纸币像的图像，其中包括 75 张真币和25 张假币。

下图为纸币的处理的过程流程图:

![](images/de0315883eb3ddbe07bef90eb31439a8fc97d1d0ff32949b2e194f5969ca759b.jpg)  
图 4.2 纸币真假鉴伪流程图  
Fig 4.2 Banknote authenticity pseudo-flow chart

# 4.3.1 纸币判别距离的方法

利用第三个方法进行有效的丢弃的没有用的信息量，可以让最后的识别率可以有所提高，最后可以构造一个相对理想的最佳投影矩阵。一般的图像相似性的方法有两种:一种是计算维度图像之间的距离；另一种计算训练和测试图像的相似性。当使用空间距离进行真假币识别，都希望可以找到一个最佳的距离进行区分。当使用第二个方法的时候，希望纸币的图像尽量相似，使得的训练的图像最大程度上相似于真币图像，这样的训练图像好像起着一个模范。但是这个方法无论在训练的复杂度和效率都不是特别的理想，所以在论文中采用了空间的距离，利用这个方法可以更好的进行识别的工作。

下面是介绍几种常见的计算空间距离[58-59]的方法：

欧式距离（Euclidean distance）：

欧式距离是最简单的距离计算的方法，也是常用的计算空间距离的重要方法。计算的公式如下：

二维空间的两个点 $A ( x _ { 1 } , y _ { 1 } )$ 和 $B ( x _ { 2 } , y _ { 2 } )$ 欧式距离 d 为：

$$
d = { \sqrt { \left( x _ { 2 } - x _ { 1 } \right) ^ { 2 } - \left( y _ { 2 } - y _ { 1 } \right) ^ { 2 } } }
$$

这个计算的距离可以基于各个维度的距离值，这是距离可以每个维度有着相同的刻度级别。

曼哈顿距离（Manhattan distance）

这个名字一开始用来计算城市间的距离，最短的行车路线而来，是将许多维度上进行多个位置进行求和：

两个 $\mathbf { n }$ 维向量 $A { = } \left( x _ { 1 1 } , x _ { 1 2 } , { \ldots } , x _ { 1 n } \right)$ 与 $B = \left( x _ { 2 1 } , x _ { 2 2 } , . . . , x _ { 2 n } \right)$ 间欧氏距离 $d$ 为:

$$
d = \sum _ { k = 1 } ^ { n } \bigl | x _ { 2 k } - x _ { 1 k } \bigr |
$$

这样的距离一般不是直线，它就相当于直角三角形的两个直角边，而斜边的就是欧式距离。

马哈诺拉斯距离（Maharanos distance）

马氏距离是由印度统计学家马哈诺斯提出来的，表示矩阵数据的协方差矩阵。它是对于一些未知样本计算的方法，和欧式距离不一样就是对原始的数据进行。对于一个变量与尺度无关，即为独立于测量尺度。对于一个均值为 $\mu$ ，协方差矩阵为 $C$ 的变量x，此时的马氏距离 $d$ :

$$
d = { \sqrt { \left( x - \mu \right) ^ { T } C ^ { - 1 } \left( x - \mu \right) } }
$$

假设协方差矩阵为单位矩阵，那么计算的距离相似于欧式距离；同理协方差矩阵是对角阵的话，这也被称为规范化的马氏距离 $d$ 为:

$$
d = { \sqrt { \ \sum _ { i = 1 } ^ { m } { \frac { \left( x _ { i } - y _ { i } \right) ^ { 2 } } { \sigma _ { i } ^ { 2 } } } } }
$$

其中 $x _ { i }$ 和 $y _ { i }$ 两个服从同一分布并且协方差为对角矩阵， $\sigma _ { i }$ 为 $x _ { i }$ 的标准差

# 4.3.2 纸币的阈值判定

为了得到最佳的阈值，将训练集的纸币进行测试，首先进行处理，利用 PCA进行处理，取得每张纸币的特征值和特征向量，得到的分类阈值的具体方法如下：

（1）将测试的纸币图像X与训练集的总平均值μ̅进行做差，最后将差值投影到对应的投影的特征向量空间。我的最后得到的特征向量：

$$
\boldsymbol { W } ^ { X } = \boldsymbol { U } ^ { T } \left( \boldsymbol { X } - \overline { { \boldsymbol { \mu } } } \right)
$$

（2）阈值的定义为：

$$
\theta = \operatorname* { m a x } _ { j , k } \left\{ W _ { j } ^ { X } - W _ { k } \right\} \quad ( j , k = 1 , 2 , 3 , . . . . , n )
$$

其中的 j， $\mathbf { k }$ 就是不同纸币的名称，最后得到的θ就是纸币测试级图像与训练集的最大空间距离。在识别阶段，选取了 100 张纸币图像，选取了 75 张真币图像和25 张假币图像。识别的大体流程如下：

$\textcircled{1}$ 将待识别的纸币图像Y与训练的纸币图像的均值μ̅的差值投影到特征空间，得到的特征向量为：

$$
\boldsymbol { W } ^ { Y } = \boldsymbol { U } ^ { T } \left( \boldsymbol { Y } - \overline { { \boldsymbol { \mu } } } \right)
$$

$\textcircled{2}$ 利用马氏距离计算每张待识别的纸币图像与训练集样本的最大空间距离，

具体的表示和训练集的表示优点相似。具体的表示如下：

$$
\tau = \operatorname* { m a x } _ { j , k } \left\{ W _ { j } ^ { Y } - W _ { k } \right\} \quad \left( j , k = 1 , 2 , . . . , n \right)
$$

其中τ表示待识别的图像在的特征空间域训练集的样本的最大的空间距离，以下的规则进行对纸币进行真伪的识别：

如果 $\tau > \theta$ ，则待识别的纸币图像就是假币。  
如果 $\tau < \theta$ ，则待识别的纸币图像就是真币。

下图进行的处理的纸币识别的图像：

![](images/3bdfd0cb7ab172331cf7e770cea72e22be38226cfc76903a52c0d83808d1484a.jpg)  
图 4.3 实验的真假鉴别结果图

Fig 4.3 The authenticity of the experiment results of the identification

# 4.3.3 实验结果分析

本实验在纸币的研究中，从两个方面进行研究，得到最佳的值，第一个实验就是纸币识别率和特征向量的维数之间的关系；第二个实验就是纸币的错判率和纸币的样本维度之间的关系。

纸币识别率和特征向量的空间之间的关系。实验选取了 100 张真币进行训练的样本，阈值的计算同样进行计算的作为训练，得到的阈值，在进行处理的识别，选取75 张真币和25 张假币，我选取的特征向量的空间维数从 30 到80，下面为判断的阈值表和识别率，错判率的关系图。

表 4.1 纸币的特征向量和对应的阈值  
Tab 4.1 Paper currency feature vector and corresponding threshold   

<html><body><table><tr><td>纸币特征向量维数</td><td>纸币的判断阈值</td></tr><tr><td>40</td><td>0.885</td></tr><tr><td>50</td><td>1.137</td></tr><tr><td>60</td><td>1.243</td></tr><tr><td>70</td><td>1.487</td></tr><tr><td>80</td><td>1.505</td></tr><tr><td>90</td><td>1.698</td></tr></table></body></html>

从表 4.1 可以看出，纸币的不同的特征的维数在 PCA 的投影下的判断阈值，可以看出，随着特征维数的增加，判断阈值在不断的上升。

![](images/34e4d2598fd4d45621e0edeb753a2800f373be8b29327861f4c9c603173f32ad.jpg)  
图 4.4 纸币特征维数与识别率之间的关系

Fig 4.4 The relationship between banknote feature dimensions and recognition rate

从实验的结果可以看出，识别还是有点下降的趋势，但是总体还是上升的趋势，当到达60 的左右，识别达到最大值，随后识别下降，到了80 维的时候，纸币的识别率只可以维持在 $80 \%$ 。

![](images/469d792535373a7f69c563736ea3f9c4a34b00a1b19a6745a539f23de254ab55.jpg)  
图 4.5 纸币特征维数与错判率之间的关系  
Fig 4.5 Relationship between banknote feature dimension and misjudgment rate

同时假币的错判率随着维数变化。随着维数的增加，有着很显著的下降的趋势，在维数为 60 的时候，错判率为 $14 \%$ ，不过随后有些小波动，最后在随着维数的变化维持在 $14 \%$ 左右。

最后进行纸币的识别的阶段，采用纸币的维数为 60，这个状态下，纸币错判率也很低，综合上面的因素，最后的选取这个维度，我们选取的 100 张纸币，前75 张为真币，后面的 25 张为假币，下表为识别纸币的空间距离。

表 4.2 处理后纸币的空间距离  
Tab 4.2 Spatial Distances of Treated Banknotes   

<html><body><table><tr><td>序号</td><td colspan="8">空间距离</td></tr><tr><td>1-10</td><td>1.412</td><td>1.287</td><td>1.314</td><td>1.286</td><td>1.361</td><td>1.417</td><td>1.283</td><td>1.428</td></tr><tr><td>11-20</td><td>1.493</td><td>1.350</td><td>1.745</td><td>1.377</td><td>1.439</td><td>1.383</td><td>1.368</td><td>1.477</td></tr><tr><td>21-30</td><td>1.400</td><td>1.373</td><td>1.366</td><td>1.469</td><td>1.640</td><td>1.388</td><td>1.395</td><td>1.382</td></tr><tr><td>31-40</td><td>1.420</td><td>1.480</td><td>1.466</td><td>1.405</td><td>1.450</td><td>1.403</td><td>1.369</td><td>1.380</td></tr><tr><td>41-50</td><td>1.361</td><td>1.410</td><td>1.461</td><td>1.329</td><td>1.434</td><td>1.415</td><td>1.816</td><td>1.467</td></tr><tr><td>51-60</td><td>1.360</td><td>1.315</td><td>1.535</td><td>1.429</td><td>1.481</td><td>1.299</td><td>1.364</td><td>1.428</td></tr><tr><td>61-70</td><td>1.448</td><td>1.334</td><td>1.447</td><td>1.310</td><td>1.313</td><td>1.461</td><td>1.377</td><td>1.490</td></tr><tr><td>71-80</td><td>1.398</td><td>1.425</td><td>1.378</td><td>1.314</td><td>1.401</td><td>1.699</td><td>1.525</td><td>1.784</td></tr><tr><td>81-90</td><td>1.667</td><td>1.342</td><td>1.646</td><td>1.251</td><td>1.304</td><td>1.972</td><td>1.364</td><td>1.545</td></tr><tr><td>91-100</td><td>1.854</td><td>1.678</td><td>1.514</td><td>1.435</td><td>1.617</td><td>1.443</td><td>1.746</td><td>1.297</td></tr></table></body></html>

表 4.2 表明，采用无监督的学习方法的分类和PCA方法结合的对纸币进行真伪鉴别，对的纸币的真币识别率一般保持在 $90 \%$ ，用纸币的真币之间的最大的距离作为真假的真假币识别的最大阈值，但是假币的错判率的只有 $40 \%$ ，这个数值达不到的实验的要求。经过实验的数据能够看出，选取的阈值并不是特别的好，在一定的意义上影响的纸币的识别率，只保留了纸币的主特征大的值作为特征向量，这样的方法会在降维丢失了许多的重要信息。利用这个方法进行对纸币的特征进行提取，把纸币的样本集进行投影和测试集进行对比，对PCA方法是进行鉴伪，但是识别率很高，但是对纸币的错判率特别的高。达不到实际的运用中，在不考虑纸币图像自身的影响和类内的信息的关系，一定的意义上影响真假币的识别率，在后面的论文内容中利用 $\mathrm { P C A } + \mathrm { S V M }$ 的方法进行对PCA的算法进行优化。

# 5.基于 PCA 和 SVM 纸币红外鉴伪

在一般的情况下，使用的红外的识别纸币图像的维数提别的高，里面还有采集过程中的噪音信息。在这样的情况下进行图像处理的十分的麻烦，获取的特征体征信息往往达不到预想的那么好。在第四章已经通过无监督的学习分类的主成分的分析方法建立了纸币提取的特征空间，在这个过程中，简化了纸币图像的维数，提取纸币的红外的特征，实现纸币的鉴伪，这个过程仅仅把数据映射到要求的特征空间里，单独就是使用主要的特征代替了其他的分类。主成分分析只可以表现能力的特征，并不一定使得具有辨别的能力，因此下面使用支持向量的方法进行有效的分类方法。

# 5.1 支持向量机

SVM 是Cor e 和Vapnik于1995 年提出的，它在解决小样本数据中的非线性及高纬度模式中都有着许多的优点，可以广泛应用到分类的问题中去。以前的进行处理的样本数多，这样在一定的意义上，可能效果会不错。然而实际中样本实验的数据是不是提别的多，许多以前的方法达不到的需求。后来人们提出了新的支持向量机模式，随着信息技术的发展，这个方法已经得到很多专家的肯定并运用实际的运用中。SVM 是继 k-近邻，神经网络，贝叶斯等方法之后的一个好的样本的分类。伴随着 SVM 在语音识别的过程中的应用， $\mathrm { S V M } ^ { [ 4 3 - 4 6 ] }$ 是基于统计学的基础上实现分险最小化，获取最大的区分两类的超平面，使得 margin 最大与核技术的方法结合在一起，在实际的运用中表现为很好的泛化能力。SVM 就是寻觅一个最大的超平面的进行分类，使得样本尽可能的分开，且分类的距离最大。他们也避免了维数较大和过拟合的缺点，在对于纸币鉴别的分类的应用中，起着很好的作用。

# 5.1.1 线性可分的类算法

支持向量机最开始研究区分两个类的问题，寻找一个最佳的分类线，如下图显示的那样，能够找到一个最大的分类界面，这个分界面不仅把两个类正确的分开，同时要求他们两个类之间的间隔最大。这个称之为最优分类面。

![](images/004bf667512993d49a7518ad99ce32f276a208d421ef124a8e57396ae30a2eab.jpg)  
图 5.1 线性可分的分界面Fig 5.1 Linearly separable interface

如上图显示有空心圆和实心圆两个训练的样本，在这个平面上有着好多分界线，但是其中有三个斜线，其中中间的实线就是正确的分开两个类的分界线 $D$ ，左下角的虚线是实心圆的临界分界线 $D 1$ ，右上角是空心圆的临界分界线 $D 2$ 。其中 $D$ 到 $D 1$ 与 $D 2$ 之间的间隔是一样的， $D 1$ 和 D2 之间的距离就是两个样本之间的最大距离。上面的 $D$ 是二维空间的最佳的分类线，可以推广到高维的界面，称之为最优分类面，可以有统计学的可知，这个最优的界面就是最小化的结构风险。假设分类点如上图所示那样,样本集为 $\left\{ x _ { i } , y _ { i } \right\}$ 。

$i = 1 , 2 , . . . , n \quad \mathrm { x } \in \mathbf { R } ^ { d } \quad \mathrm { y } \in [ - 1 , 1 ]$ ， $\textrm { d }$ 维空间函数可以表示为：

$$
w \cdot x + b = 0
$$

这个直线把坐标的平面分成两个界面，把 $\mathrm { \Delta y }$ 对应的-1 和 1，确切的是按照 $x$ 得到推断点的决策函数：

$$
f ( x ) = \operatorname { s g n } ( w \cdot x + b )
$$

其中sgn 是符号函数

假设这个 2 维的特征向量， $\scriptstyle x = \left( x _ { 1 } , x _ { 2 } \right)$ ,其中 $b$ 为二外的 $w _ { 0 }$ 。

超平面的方程为：

$$
w _ { 0 } + w _ { 1 } x _ { 1 } + w _ { 2 } x _ { 2 } = 0
$$

坐标的左下方的方程为：

$$
w _ { 0 } + w _ { 1 } x _ { 1 } + w _ { 2 } x _ { 2 } < 0
$$

坐标的右上方的方程为：

$$
w _ { 0 } + w _ { 1 } x _ { 1 } + w _ { 2 } x _ { 2 } > 0
$$

调整这个 $w _ { 0 }$ ，使得超平面的边缘的两边：

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { w _ { 0 } + w _ { 1 } x _ { 1 } + w _ { 2 } x _ { 2 } \leq - 1 \quad y _ { i } = - 1 } \\ { w _ { 0 } + w _ { 1 } x _ { 1 } + w _ { 2 } x _ { 2 } \geq - 1 \quad y _ { i } = + 1 } \end{array} \right. } \end{array}
$$

由上的不等式可得：

$$
y _ { i } \left( w _ { 0 } + w _ { 1 } x _ { 1 } + w _ { 2 } x _ { 2 } \right) \geq 1 \quad \forall _ { i }
$$

此时坐落在边缘两边的超平面被称为“支持向量（support vector）”。

此时超平面和 $D 1$ 或 $D 2$ 之间的任意一点的距离为:

$$
\frac { 1 } { \left. w \right. }
$$

其中‖w‖是向量的范数

得到两个支持的直线的距离为 $2 / \left. w \right.$ ，相应的“间隔”为 $2 / \left. w \right.$ 。这个最大的距离的思想就是求解变量 $\boldsymbol { w }$ 和 $b$ 的最优化的问题。

$$
\operatorname* { m a x } _ { \mathrm { w , b } } = \frac { 2 } { w }
$$

对于所有的 $\mathrm { y _ { i } } = 1$ 的下标i,有 $\mathbf { w } \cdot \mathbf { x _ { i } } + \mathbf { b } \leq - 1$ 。

对于所有的 $\mathrm { y } _ { \mathrm { i } } = - 1$ 的下标i,有 $\mathbf { w } \cdot \mathbf { x _ { i } } + \mathbf { b } \geq 1$ 。

或者

$$
\operatorname* { m i n } _ { \boldsymbol { w } , \boldsymbol { b } } = \frac { 1 } { 2 } \big \| \boldsymbol { w } \big \| ^ { 2 }
$$

约束条件为：

$$
y _ { i } \left( w _ { 0 } + w _ { 1 } x _ { 1 } + w _ { 2 } x _ { 2 } \right) \geq 1 \quad i = 1 , 2 , . . . , n
$$

上面的最优化的问题是在 $R ^ { 2 }$ 上的一个特殊的问题推到出来的，其它的要求是最大化的两个支持直线形成的距离，这就是所谓的最大距离原则，有这个原则，与此对应 $w$ 和 $b$ 凸的二次规划的问题。

现在考虑实现最大的间隔的原则性的另一条的方法就是不直接求解最优化的问题，而是求解他们对偶问题的解决办法。为了解决这个问题，引入了Lagrange 函数。

$$
L { \big ( } w , \mathbf { b } , \mathbf { a } { \big ) } = { \frac { 1 } { 2 } } w ^ { 2 } - \sum _ { i = 1 } ^ { n } \alpha _ { i } { \big ( } y _ { i } { \big ( } w \cdot x _ { i } + b { \big ) } - 1 { \big ) }
$$

其中 $\alpha _ { \mathrm { i } } > 0 , \alpha = ( \alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { \mathrm { n } } ) ^ { \mathrm { T } }$ 为拉格朗日的乘子向量

下面分别对上面的公式 $w$ 和 $b$ 进行求偏导的原始问题的对偶问题，令这个等式为0，得出下面的最大值和约束条件如式5.13、式5.14:

$$
\operatorname* { m a x } _ { \boldsymbol { \alpha } } \big ( \boldsymbol { \alpha } \big ) = - \frac { 1 } { 2 } \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } y _ { i } y _ { j } \big ( x _ { i } \cdot x _ { j } \big ) \alpha _ { i } \alpha _ { j } + \sum _ { j = 1 } ^ { n } \alpha _ { j }
$$

$$
\sum _ { i = 1 } ^ { n } y _ { i } \alpha _ { i } = 0
$$

其中 $\alpha _ { \mathrm { i } } \geq 0 , \ \mathrm { i } = 1 , 2 , . . . , \mathtt { n }$

对于上面的问题，必有解 $\boldsymbol { \alpha } ^ { * } = \left( \alpha _ { 1 } ^ { * } , \alpha _ { 2 } ^ { * } , . . . , \alpha _ { \mathrm { { n } } } ^ { * } \right) ^ { \mathrm { T } }$ 。此时得到的最佳分类的向量进行训练的样本的线性组合为,求出的解 $\left( \boldsymbol { w } ^ { * } , \boldsymbol { b } ^ { * } \right)$ 为:

$$
\left\{ \begin{array} { c } { { w ^ { * } = \displaystyle \sum _ { i = 1 } ^ { n } \alpha _ { i } ^ { * } y _ { i } x _ { i } } } \\ { { \displaystyle b ^ { * } = y _ { j } - \sum _ { i = 1 } ^ { n } \alpha _ { i } ^ { * } y _ { i } x _ { i } \left( x _ { i } \cdot y _ { i } \right) } } \end{array} \right.
$$

构造分划超平面 $\boldsymbol { w } ^ { * } \cdot \mathbf { x } + \boldsymbol { b } ^ { * } = 0$ ，这样获得的决策函数为:

$$
f ( x ) = s g n { \bigl ( } w ^ { * } \cdot x + b ^ { * } { \bigr ) } = \sum _ { i = 1 } ^ { n } y _ { i } \alpha _ { i } ^ { * } \left( x _ { i } \cdot x \right) + b ^ { * }
$$

所得到的决策函数只依赖与训练集的对应的非负 $\alpha _ { i } ^ { * }$ 的训练点 $\left( x _ { i } , y _ { i } \right)$ ，而其他的训练都不起作用，这个 $x _ { i }$ 为支持向量，若 $\alpha ^ { * }$ 的分量 $\boldsymbol { \alpha } _ { i } ^ { * }$ 非零，否则 $\mathbf { x _ { i } }$ 为非支持向量。在这个的超平面的满足一下的两个原则:

（1）支持向量 $x _ { i }$ 满足 $\mathbf { y } _ { \mathrm { i } } f \left( \mathbf { x } _ { \mathrm { i } } \right) { = } { \mathbf { y } _ { \mathrm { i } } } \left( \mathbf { w } ^ { * } \cdot \mathbf { x } _ { \mathrm { i } } + \mathbf { b } ^ { * } \right) { = } 1$ ，支持向量表示的分类向量都在支持向量上。

（2）非支持向量 $x _ { i }$ 满足 $\mathbf { y } _ { \mathrm { i } } f \left( \mathbf { x } _ { \mathrm { i } } \right) - \mathbf { y } _ { \mathrm { i } } \left( \mathbf { w } ^ { * } \cdot \mathbf { x } _ { \mathrm { i } } + \mathbf { b } ^ { * } \right) { \geq } 1 \mathrm { . }$ 。

线性可分的情况下的模型的支持向量的复杂度是由个数决定的，并不是有矩阵的维数决定的，这样就不会产生矩阵的溢出的现象，SVM 算法训练的模型就是依靠求出的支持向量。即的一些非向量的点都不在的情况下，反复的进行训练，获取的模型和原本的基本一样。这个算法的应用的个数不可以太少，不然容易产生泛化。

# 5.1.2 线性不可分的分类算法

现实的问题好多问题的特征点分布并不是线性的，更多的是非线性的，用线性划分得不到预期的要求。如下图所示：

![](images/aef36505529a60ae86c82b81aa0d85b330580f0f5b57c1098984b8a915dd97d4.jpg)  
图 5.2 非线性不可分界面Fig 5.2 Non-linear inseparable interface

如上图所示，这个特征点进行区分，对这样的点进行分类，用直线是无法进行的区分，只可以曲线进行划分，用非线性分划代取代线性分划，但是需要求出这个曲线，需要寻找一个方法，就是用线性的直线的方法把“曲线”变成“直线”，方法就是利用变换 $\mathbf { X } = \Phi { \bigl ( } \mathbf { x } { \bigr ) }$ 。具体的分类算法步骤如下：

在线性不可分的情景下，可以添加一个 $\varepsilon _ { \mathrm { i } } \geq 0$ ，则对这个特征向量进行分类，他们之间的距离还是为 $\left\| \boldsymbol { w } \right\| / 2$ ，得到最初的原始问题的表达方式和约束条件如式5.17、式 5.18：

$$
\operatorname* { m i n } _ { \boldsymbol { w } , \boldsymbol { b } , \boldsymbol { \varepsilon } } = \frac { 1 } { 2 } \boldsymbol { w } ^ { 2 } + C \sum _ { i = 1 } ^ { n } \mathcal { E } _ { i }
$$

$$
y _ { i } \left( w \cdot x _ { i } + b \right) \geq 1 - \varepsilon _ { i } \quad i = 1 , 2 , . . . , n
$$

其中 $\mathfrak { E } _ { \mathrm { i } } \geq 0 \Im = 1 , 2 , . . . . , \mathfrak { n }$ ， $c$ 是常数，控制对样本的特征向量进行惩罚的水准，对 $C$ 的取值进行折中， $c$ 值越大，对应的分类惩处就越大。

就如前面的线性可分进行分析的话，引入了 Lagrange 函数。可以得到对应的对偶问题，最后的得到的最大值和约束条件为：

$$
\operatorname* { m a x } _ { \alpha } \left( \alpha \right) = - \frac { 1 } { 2 } \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } y _ { i } y _ { j } \left( \Phi \left( x _ { i } \right) \cdot \Phi \left( x _ { j } \right) \right) \alpha _ { i } \alpha _ { j } + \sum _ { j = 1 } ^ { n } \alpha _ { j }
$$

$$
\sum _ { i = 1 } ^ { n } y _ { i } \alpha _ { i } = 0 \quad i = 1 , 2 , . . . , n \quad 0 \leq \alpha _ { i } \leq C
$$

此时注意，当 $\sum _ { i = 1 } ^ { n } y _ { i } \alpha _ { i } = 0$ 与 $k - \alpha _ { i } = 0$ 不同时成立的时候，可以得到他们的解为：

$$
\boldsymbol { \alpha } ^ { * } = \left( \alpha _ { 1 } ^ { * } , \alpha _ { 2 , \ldots , } ^ { * } \alpha _ { n } ^ { * } \right) ^ { T }
$$

计算 $\boldsymbol { b } ^ { * }$ ,选取位于开区间 $\left( 0 , k \right)$ 中的分量 $\alpha ^ { * }$ 的分量 $\boldsymbol { \alpha } _ { j } ^ { * }$ ，求出下式为：

$$
\boldsymbol { b } ^ { * } = y _ { j } - \sum _ { i = 1 } ^ { n } \alpha _ { i } ^ { * } y _ { i } x _ { i } \left( \Phi ( x _ { i } ) \cdot \Phi \left( x _ { j } \right) \right)
$$

构造分划超平面 $\boldsymbol { w } ^ { * } \boldsymbol { \cdot } \boldsymbol { x } + \boldsymbol { b } ^ { * } = 0$ ，这样获取的决策函数为：

$$
f \left( \boldsymbol { x } \right) = s g n { \left( \boldsymbol { w } ^ { * } \cdot \boldsymbol { x } + \boldsymbol { b } ^ { * } \right) } = \operatorname { s g n } \left( \sum _ { i = 1 } ^ { n } y _ { i } \alpha _ { i } ^ { * } \left( \Phi { \left( \boldsymbol { x } _ { i } \right) } \cdot \Phi { \left( \boldsymbol { x } _ { j } \right) } \right) + \boldsymbol { b } ^ { * } \right)
$$

可以看出这个与前面的线性可区分只是里面的内积函数不同。

# 5.1.3 核函数的分类算法

支持向量机应用的成功就是有两个好的方法:第一是就是应用 SRM(风险最小化)技术计算出有最大间隔的最好的分类面，把低维不可区分的样本数据放入到高维空间里，使用核函数的方法非线性的方法，最后设计成最好的分解面。第二个就是现在的核函数方法。引用了核函数的，极大的提高学习机器的自学处理非线性的能力，高维的数据之间的内积是由的核函数进行完成的。通过映射需要$\Phi$ 确定往往需要有很高的技巧和相关的专业技术，同时这个 $\Phi$ 的计算是相当复杂的，再是就是这个 $\Phi$ 的映射是低维到高维的过程，计算量特别的大。用核函数只改变它们内积的运算，并没有增加这个算法的复杂度。下面的图就是在低维空间下线性不可分的样本点转换为高维空间的线性可分。

![](images/603a541f7c4d55cd9a085aca7ac5f88b0d4d669f1d8c7497f8c2abbe90ed2e20.jpg)  
图 5.3 非线性不可分转换为线性可分  
Fig 5.3 Non-linear conversion can be divided into linear separable

进行对称核函数的应用，需要一个 Mercer 的条件就可以代替内积的使用。如果可以找到一个 $K { \Big ( } x , x { \ ' } { \Big ) } = \Phi { \Big ( } x { \Big ) } \cdot \Phi { \Big ( } x { \Big ) }$ 的话，使得这个函数满足 Mercer 要求的条件，它就可以代替某个的内积。任意的对称函数 $K { \bigl ( } x , x ^ { ' } { \bigr ) }$ ，在空间的内积运算的提前的条件是，对于任意 $\mathcal { S } \big ( x \big ) \neq 0$ 且 $\iint \mathcal { G } ^ { 2 } \left( x \right) d x < \infty$ 。

$$
\hat { \iiint } \mathbf { K } { \left( \mathbf { x } , \mathbf { x } ^ { ' } \right) } \mathcal { \boldsymbol { A } } { \left( \mathbf { x } \right) } \mathcal { \boldsymbol { A } } { \left( \mathbf { x } ^ { ' } \right) } \mathbf { d x } \mathbf { d x } ^ { ' } > 0
$$

这个函数很重要，当采用函数 K，而不变换 $\Phi$ ，用K 代替可以得到效果一样的决策函数，称这个就是核函数。这样的措施获得的优化函数和约束条件如式5.25、式 5.26：

$$
H \left( \alpha \right) = \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { n } y _ { i } y _ { j } K \left( x _ { i } , x _ { j } \right) \alpha _ { i } \alpha _ { j } + \sum _ { j = 1 } ^ { n } \alpha _ { j }
$$

$$
\sum _ { i = 1 } ^ { n } y _ { i } \alpha _ { i } = 0 \quad n = 1 , 2 , 3 , . . . , n
$$

构造分划超平面 $\boldsymbol { w } ^ { * } \cdot \boldsymbol { x } + \boldsymbol { b } = 0$ ，这样获取的决策函数为：

$$
f \left( x \right) = s g n { \left( w ^ { * } \cdot x + b ^ { * } \right) } = s g n { \left( \sum _ { i = 1 } ^ { n } { y _ { i } } \alpha _ { i } ^ { * } K \left( x _ { i } , x \right) + b ^ { * } \right) }
$$

利用这个方法有以下的一些性质:

（1）问题规模的转化。问题是从训练集找那个找到一个决策函数，这里的$x , \ n$ 维向量。直接的途径是规模依赖于 $n$ 的原始的问题，当 $n$ 增加时，求解的计算量会增加，通常认为这个就是“维数灾难”，但是支持向量机需要求解的对偶问题的规模输入与输入的空间维数无关，这个方法在一定意义克服了维数灾难。

（2）核函数的使用。用 $k$ 代替变换的 $\Phi$ ，十分有效的从线性分划到非线性分划的过渡，只需要选取的核函数不但便利，而且可以简化运算。因为在高维的空间里计算内积的计算量比核函数的计算量大得多。

（3）稀疏性。从的决策函数来看，不是所有的点都有作用，求得对偶问题的解 $\alpha ^ { * }$ 的分量 $\alpha _ { i } ^ { * }$ 非零训练点对决策函数起着作用。换句话来说，只有支持向量的点对决策函数起着作用，而非支持向量对训练点决策函数没有作用，可以想象，当实验的训练的数目多的情况下，支持的向量的比重不大，大部分都是非支持的向量。

通常核函数需要满足 Mercer 条件还有以下几个:

线性核函数: $K \left( x , x ^ { ' } \right) = \left( x , x ^ { ' } \right) ,$ 。

多项式核函数: $K \left( x , x _ { i } \right) = \left[ \left( x , x _ { i } \right) + 1 \right] ^ { d }$ 。

高斯径向核函数: $K { \bigl ( } x , x _ { i } { \bigr ) } = e x p { \bigl ( } - x - x ^ { ' 2 } / \sigma ^ { 2 } { \bigr ) }$

# 5.2 支持向量机分类策略

这个策略是针对多分类的问题，通常有两个方法可以解决这个问题，一是解决多个类之间的优化问题，它可以进行一次性的解决 原始的一些问题，但是这个过程比较耗时。所以在实际的运用中用的比较少，二是解决二分类的问题，可以进行对数据分类，得到想要的效果。这个用法没有那么的复杂，常用的方法包括一对多和一对一的决策树等方式。在实行纸币的识别的过程中，实际的过程中就是二分类的问题，其中常见的分类方法策略[60]：一对多的最大响应策略，一对一的投票策略，二叉树分类法。这三个的方法在实际的运用都有着很好的作用，本文中的纸币识别使用一对一的投票策略解决了的问题。

# 5.2.1 一对一投票策略

在进行一对一的投票的使用中，组合这样的分类器很自然的用到投票的方法，获得票最多的就是新点所属的类。在进行测试的中，将测试的样本放到所有的分类器中判断，看他们属于什么哪个类别。记录这个输入样本的类别并进行判断，给输出的结果类别投上一票。通过所有的类别的数进行累加，得票数最高的就是需要新的类别。具体的如下图：

![](images/2a358558451b8744e27ab6b4d1e22c8548f13bb5497d8a3d7a1242fa88379596.jpg)  
图 5.4 一对一投票策略示意图Fig 5.4 One-to-one voting strategy diagram

这个方法计算方便，但是当训练得样本增大的时候，计算的效率会优点降低，得到的最优分界面。采用的分类规则就是符号的方式，也许出现多个类别指向同一个类别，只要在数据不是很大的情况下，效果还是不错的。

# 5.2.2 一对多策略

这个分类策略就是构造两个分类器，将前面的样本作为一个分类样本，剩下的样本作为另一个样本，这样使得每一类的数据都可以从其他的类别区别出来，这样进行处理就可以得到最大分类函数所对应的类。在分类中产生多个二类分类器，其中每一个分类器将自己的一类和其他类进行区分。具体的图示如下：

![](images/089c439c1bed4a305db4c4d9d033b75c59b32b1d7250a2ce67912032752e3ecc.jpg)  
图 5.5 一对多策略示意图

这个方法就是对于 $K$ 类的问题秩序求解二次规划的问题，即有 $K$ 个两类的分类器，因此它的速率较快。但是这个方法的缺点就是分离器的样本都需要参与，会导致训练的效率低下，又因为每一个一类和其他的类构造的超平面，正常的样本数目小于相对的数目，使得训练的样本分类的效率低下。改进的方法就是去掉符号的运算，用类别的投票的最大结果进行分类。

# 5.2.3 二叉树分类策略

对于一个N类的训练样本，需要 N-1 个支持向量机。第 1 个样本和其他的样本进行分类，并表示为 A，将剩下的样本进行分类，并表示为 B。最后将 A 类和B 类的样本进行训练，直到 N-1 个支持向量机作为 A 类，以第 N 类样本为 B类训练为N-1。具有实现的如下图:

![](images/66b25926359e4e181a4eb6d96029e69e1f6e66d2efebf85dee407ab6cd4f6a80.jpg)  
Fig 5.5 One-to-many strategy diagram   
图 5.6 二叉树分类策略示意图Fig 5.6 Binary tree classification strategy diagram

由上面的二叉树的分类图可以得到，在进行 k 类问题的时候，二叉树的方法就是在训练的只需要 K-1 个分类器，最后进行决策不使用遍历全部的分类器，最多经过 $\log _ { 2 } \mathsf { K }$ 个分类器，这样使得效率特别的高，但是当的某个节点产生错误的时候，那么在它的后续节点上产生了错误，最后影响了分类的精确度。

# 5.3 PCA+SVM 系统实现

# 5.3.1 SVM 分类器的构造

本文的采用纸币的分类算法，需要处理当前两个重要问题:一是择取核函数，二是确定核函数的参数以及错误代价 K 的最佳取值。

（1）由于的纸币的特征的是非线性的，要求引用核函数实行处理，由上面的多种核函数，其中应用最广泛的是高斯径向核函数，即常说的 RBF 函数，在实际运用中，无论是高维还是低维，大小样本的情况下，RBF 核函数有着很有用的作用，下面是选取了加州大学的尔湾分校数据库研究的三种职务数据集的在不同的核函数下的仿真实验，在的 MATLAB 的平台下，有如下的数据对比:

表 5.1 不同的核函数在不同的介质的正确分类率  
Tab 5.1 Correct classification rates of different kernels on different media   

<html><body><table><tr><td>正确的分类率(%)</td><td>玻璃识别数据</td><td>菖蒲植物数据</td><td>汽车评估数据</td></tr><tr><td>线性核函数</td><td>98.12</td><td>96,67</td><td>93.34</td></tr><tr><td>多项核函数</td><td>98.14</td><td>96.67</td><td>99.99</td></tr><tr><td>高斯径向基核函数</td><td>99.10</td><td>96.67</td><td>93.34</td></tr><tr><td>Sigmoid核函数</td><td>35.55</td><td>6.67</td><td>92.00</td></tr></table></body></html>

由上表可以看出，玻璃的识别分类线性，多项，高斯径向核函数效果不错，菖蒲和玻璃的核函数是一样的，汽车的分类率的效果都不错，由于选用不同的核函数，得到的效果是不同的，目前专家也没有统一的说法，考虑纸币的对核函数的敏感性和专家们的预测，最后采用了高斯径向的核函数。如下所示：

$$
\operatorname { K } { \Bigl ( } x , x { \Bigr ) } = e x p \left( - { \frac { \left| x - x \right| ^ { 2 } } { \gamma ^ { 2 } } } \right) \quad \gamma ^ { 2 } { \dot { \jmath } } _ { 5 } \bigcap { \vec { \Xi } } \equiv { \overrightarrow { \sf E K } } | { \vec { \Xi } } | { \vec { \mathcal { K } } } | | { \vec { \mathcal { K } } } | |
$$

（2）核函数的参数和惩罚因子

核函数选定以后，进行确定核函数的参数γ和惩罚因子 $c$ ，SVM 受到高斯和参数的γ的影响，核函数和所对应的映射函数及特征空间都是互相映射的，进行选择了核函数后，就相应的确定映射函数和特征向量的空间，在纸币的识别问题中，选取参数是至关重要的，使用的子空间是维数是影响最后得到分界面，决定达到最小的误差；同时影响着进行分类界面的误差。当特征空间的维数高时，进行求解的最优分界面是比较复杂的，要求经验的风险小而置信范围大，反之亦然。惩罚参数 $c$ 的影响在实现错分样本和算法的复杂之间的方法中。当选取 $c$ 的数据足够大时候，就要求样本准确的分类，每一个的子空间选择一个合适的 $c$ 使得推广的作用更好。通过实验的测试，最终取得惩罚因子 $c$ 为2，参数 $\gamma$ 为-2，这样核函数达到的效果最好。下图是错误率随这两个参数的影响的变化情况。

![](images/c7e7cf4f493ddd8717a167580b085c29d679239c98cadb7144e783181b61618b.jpg)  
图2错误率随γ的变化率

![](images/916096fb273d174d04d6f9d0db9333d2118d5a637520e70949f57c8dc8e12c70.jpg)  
图1错误率随C的变化率  
图 5.7 核函数参数和惩罚因子随错误率的变化图

Fig 5.7 Kernel function parameters and penalty factors with the error rate changes

本文中采用了结合 Gabor 滤波和 PCA 的方法进行纸币特征提取，而后使用SVM 对纸币特征进行分类。基于支持向量机的纸币分类的训练步骤和测试的步骤。练的阶段的基本步骤如下：

1.从纸币库读取纸币的图像，经过预处理过后，将纸币图像分为两个部分:训练样本和测试样本。2.利用Gabor滤波对训练样本进行图像增强，得到低频的纸币图像用于纸币的特征提取的图像。3.使用PCA算法计算纸币本身的特征值和特征向量，选取一些采用的方法剩下的特征值作为特征向量的特征子空间。4.把训练的纸币图像投影到对应的空间里，得到对应的特征向量。5.采用了径向基的核函数。利用LibSvm工具寻找合适的参数，并利用从样本的训练本中提取特征的向量。测试的阶段的步骤如下:$\textcircled{1}$ 输入进行测试的纸币图像样本图像。$\textcircled{2}$ 对测试的样本进行 Gabor 变换增强，然后把测试的图像投到对应的子空间里，得到纸币的特征向量。$\textcircled{3}$ 把特征向量输入设置的支持的向量中，采用二叉树分类策略进行特征的分类。最后进行投票的机制进行纸币的特征的识别。

# 5.3.2 纸币 MATLAB 实验设计与实现

对于纸币的复杂的情况下，采用之前预处理的过后的纸币图像，采用 PCA和SVM 算法[47-50]和相关的研究，进行纸币的训练，把纸币的结果放入训练的库中，利用 PCA 进行纸币的降维处理和纸币的特征提取，识别率很高，符合的要求。对纸币的训练和测试，分为以下的几个模块：

![](images/6910b022dd4727c3e5911815cde07357cfd204b262f6abdfeb00654540d56daa.jpg)  
图 5.8 纸币 GUI 设计模块图  
Fig 5.8 Banknote GUI design module diagram

上图是纸币识别的系统主界面图，有三个模块，分别是训练集的数据模块，这个模块是对纸币进行训练的。接下来对纸币的图像进行测试，选取的图像进行识别的阶段。最后是进行真假鉴伪模块。

![](images/e601d12d1c2d2d104bfb37ba4e50944e46917f2d2836992811d9f19ddb6ee2df.jpg)  
图 5.9 纸币 Gabor 预处理结果图Fig 5.9 Banknote Gabor pretreatment results

在进行纸币的训练图像，训练图像的模块安排是将训练的样本输入的系统中。首先进行纸币的灰度化，Gabor 滤波的处理后，对纸币进行 PCA 降维。在这个系统中，将特征向量降维到 50 维，然后将降维后的特征进行 SVM 训练，得到真假币的超平面。将降维后的纸币图像特征向量，对真假币进行分类，让后期的纸币进行真假币识别分类。

![](images/e581e2001ca8c3a0a319b41a1917abfa7ae999e5d7a562ef89653a411fec91cf.jpg)  
图 5.10 纸币真假鉴伪图像识别结果图

Fig 5.10 banknotes false authenticity image recognition results

# 5.4 实验结果分析

# 5.4.1 PCA+SVM 结果分析

进行对这个结合的算法进行研究，的进行两个实验，第一组实验是纸币的识别率和向量维度的之间的关系。第二组实验纸币的错判率和特征向量维度的关系。第三组实验选取的分类算法的比较图表。

表 5.2 特征向量维数和相对应的阈值  
Tab 5.2 Eigenvector dimensions and corresponding thresholds   

<html><body><table><tr><td>纸币特征向量维数</td><td>纸币的判断阈值</td></tr><tr><td>40</td><td>0.345</td></tr><tr><td>50</td><td>0.396</td></tr><tr><td>60</td><td>0.453</td></tr><tr><td>70</td><td>0.487</td></tr><tr><td>80</td><td>0.498</td></tr><tr><td>90</td><td>0.522</td></tr></table></body></html>

表 5.2 为利用 $\mathrm { P C A + S V M }$ 进行处理的纸币特征向量的维数与判断阈值之间的关系，由表可以得知，随着特征维数的增加，判断阈值也在不断增加，其次，就是这段阈值比之前的阈值小。

![](images/5caa52a53ce9e3c2e43d9df60c4e59470b757c8363b41d0afc31c3e446a0a7fa.jpg)  
图 5.11 纸币特征维数与识别率之间的关系  
Fig 5.11 The relationship between banknote feature dimensions and recognition rate

本实验选取 100 张纸币作为进行纸币的训练样本，上表为纸币在不同的维度的情况下的纸币的阈值，同样和 PCA 的方法是相同的测试方法，选取 75 张真币和 25 张假币，真币识别图为 30 维到 80 维的范围内，纸币的识别随着维度的改变识别率，可以看出在维数为 50 的时候，识别率最高为 $9 6 \%$ ，随着维数的变化，最后基本保持在 $93 \%$ 左右。

![](images/dc33ded19ccae6fe231419d105151ad90b680f4f9d518bbf330dded947f24a52.jpg)  
图 5.12 纸币识别率与特征向量维数的关系图

Fig 5.12 Banknotes recognition rate and the relationship between the number of eigenvectors

假币的错判率也是随着的变化，在维数为 50 左右的时候，达到最低为 $4 \%$ ，这样的效果基本达到对纸币的真假币识别。其次就是选取的二叉树分类策略算法，本身就有很高的识别纸币的识别率，同时判别的时间是最短的，运用了二叉树的优点，得到测试的纸币图像少于 N-1 个分类器就可以对纸币进行识别，因此，它的时间在一定的意义上最少的。

# 5.4.2 两种算法的比较

对纸币的进行两种不同方法进行比较，这两种对纸币的识别都有着很高的识别率，在对 PCA 的识别中，选取了不同的阈值，选取了真币和真币之间的最大的距离作为真假币的识别标准，但是对假币的错判率是有着很大的变化。采用的这个方法，有时只是考虑纸币类间的关系，从而忽视了纸币类间的关系，把类间的距离作为唯一的判别标准，有时会造成一些制造很真的假币的投影位置和我纸币是非常的接近，这也是假币的错判率这么高的直接原因。但是利用 $\mathrm { P C A } { + } \mathrm { S V M }$ 的方法[51]是，错判率得到了显著的下降，进行纸币的维数也下降了，选取的纸币的核函数和分类的策略算法可以更好的进行纸币的识别。得到的识别率增加了，假币的错判率也下降了。

表5.3 两种方法实验结果对比图  
Tab 5.3 Comparison of two methods experimental results   

<html><body><table><tr><td>方法</td><td>真币识别率</td><td>假币错判率</td><td>识别的速度</td></tr><tr><td>PCA</td><td>0.90</td><td>0.42</td><td>近似0.175s/张</td></tr><tr><td>PCA+SVM</td><td>0.95</td><td>0.12</td><td>近似0.083s/张</td></tr></table></body></html>

# 6.总结和展望

# 6.1 论文总结

纸币识别鉴伪识别是图像处理的一个重要研究范畴，纸币是一个国家的象征，对一个民族的经济安定起着重要的作用，保证的国家的稳定。不断的提高的纸币的技术，这个论文在这些纸币的识别的基础上，使用了 $\mathrm { P C A } { + } \mathrm { S V M }$ 结合的办法应用在纸币的领域中，经过实验的分析，这个方法基本达到的要求，对纸币的处理有着许多的处理的工作。研究的内容包括纸币图像的采集，图像的预处理，图像的 Gabor 处理，基于 $\mathrm { P C A + S V M }$ 的纸币红外光真伪的识别等。这个纸币的工作中 $\mathrm { P C A + S V M }$ 纸币的识别是的本文的核心的工作，对之间的特征向量的维数和分类的方法进行调节，寻找一个更好的优化的参数，下面是我进行的主要的工作：

（1）对纸币的图像采集和图像的预处理的工作:本文纸币的红外的图像采集的仪器是聚龙JL305 清分机，并将处理的纸币的图像进行图像的归一化，图像的分割，为以后的纸币的识别工作做好铺垫。（2）基于纸币的 Gabor 的预处理的工作，将前面预处理的纸币进行滤波处理，得到的纸币的进行后面的算法的研究。（3）基于 $\mathrm { P C A } { + } \mathrm { S V M }$ 的纸币的红外光的纸币的真伪的识别的工作，而且使用当前阶段这个算法比较成熟的算法，结合非监督的学习设计出这个算法。（4）对纸币的判断的阈值和 SVM 的分类算法选取。本文使用的欧式距离作为 PCA 作为纸币的判断的方法。采用识别阶段的最大距离进行判别的阈值，SVM 分类的算法一对一的分类算法，这个算法很好的降低算法复杂度，最后进行识别的工作。经过实验仿真和算法参数进行优化，提高纸币的识别率。经过对纸币的算法改进，最后得到的一组数据是:纸币的特征空间维数为 50-55 维，纸币的训练的样本的数目为 100 张，纸币的大小尺寸为 $1 1 2 \times 9 2$ ，在这样的参数调解下，基于 $\mathrm { P C A + S V M }$ 的纸币红外特征算法的识别率得到 $9 5 \%$ ,假币的错判率为0.12，识别的速度为 $0 . 0 8 3 ~ \mathrm { s } /$ 张。

# 6.2 展望

纸币识别是对图像处理一个方便的范围的扩充，虽然在图像处理的方向上做到了相当的成熟，但是还有许多的问题都没有进行解决，许多的看似成熟的算法还不够完善。许多纸币的真伪的识别还在不断的研究中，在实际的操作中， 还存在的差距，目前来看，纸币的识别技术的弊端有以下的几个方面：

$\textcircled{1}$ 纸币面额特征的差异

在进行纸币的建造中，很难保证每张纸币的一模一样，比如:纸币的纹理，图像的标志的图标都有一定的误差，这个对纸币的进行纹理的提取造成一定的误差，有时纸币的面额特征并没有消失，有时更产生新的特征，只有这样才可以对纸币进行Fenix 和识别，指出纸币的差异，同时也增加对纸币的进一步的认识。

$\textcircled{2}$ 纸币的预处理的图像

在进行纸币的识别的阶段，纸币的最后的结果的准确和对纸币的预处理的图像有着很大的关系。在对纸币的灰度图像提取受到外界的环境和噪音的影响，都会纸币图像特征提取产生误差，在对实验的提取中，可以发现一个大的问题，新纸币的灰度图像比旧的纸币灰度图像的识别率有着明显的上升趋势。

$\textcircled{3}$ 纸币样本数的局限

在进行纸币的训练的过程中，真币的数量勉强还可以，假币的数量有限，这也是对进行假币的错判率降不到 $10 \%$ 以下，为了让实验的识别率提高，尽量增加了假币的数量，让纸币的错判率和纸币的识别率有所改善。

$\textcircled{4}$ 对纸币的算法的变量进行优化

本文中利用 PCA 的算法的最大的距离有着一定的误差，真币的识别率确实挺高，但是假币的错判率特别的高，对纸币的鉴伪的算法是采用的无监督的方法，无监督学习大多数情况是指在不需要外界干涉下进行样本信息的提取。它通过边学习边进行分类，学习从图像中采样,从图像中进行去噪,寻找数据分布的特征或者是数据的相关进行分类。

$\textcircled{5}$ 进行多国纸币的鉴伪

这个论文纸币我们国家的人民币进行识别，得到一定好的效果，但是还有进行对纸币的识别推广到其他国家的纸币，以后进行对纸币的识别的算法进行不断的完善，优化，增加纸币的识别率。进行对纸币的识别推广到其他国家纸币识别的范畴。

参考文献  
[ 1 ] 郭艳平. 纸币币种和币值识别系统的研究.[硕士学位论文]. 南京, 南京航空航天大学, 2007.  
[ 2 ] 朱凯, 王正林. 精通 MATLAB 神经网络[M]. 北京: 电子工业出版社.2010.  
[ 3 ] Kruse F A, Lefkoff A B, Boardman J W, et al. The spectral image processing system(SIPS) interactive visualization and analysis of imaging spectrometer data[J]. RemoteSensing ofEnvironment, 1993, 44(1): 145-163.  
[ 4 ] 饶文碧, 陈旭辉, 徐锐.基于 $\mathbf { C } { + } { + }$ Builder 的图形图像处理方法[J]. 交通与计算机.2002(2):61-63.  
[ 5 ] 李庆峰. 基于图像处理的纸币清分系统关键算法研究[D].中国科学院研究生院（成都计算机应用研究所）,2006.  
[ 6 ] Gai S. New banknote defect detection algorithm using quaternion wavelet transform[J].Neurocomputing, 2016: 133-139.  
[ 7 ] 李国华. 基于 TMS320F2812 的小型纸币鉴伪/清分机. 电子技术. 2004,32(08): 355-358  
[ 8 ] 何卫国, 曹益平, 梁友生等. 基于DSP 实现的光电点钞系统数据处理方法研究. 光学技术.2004,28(04):312-317.  
[ 9 ] 曹贵强. 纸币识别及红外鉴伪技术的研究[D]. 辽宁科技大学,2014.  
[10] 马继刚. 新旧版第五套人民币防伪特征的比较研究[J]. 中国人民公安大学学报(自然科学版),2006,(01):46-51.  
[11] Zhang J, Meng X, Xu W, et al. Research on the Compression Algorithm of the InfraredThermal Image Sequence Based on Differential Evolution and Double Exponential DecayModel[J]. The Scientific World Journal, 2014: 601506-601506.  
[12] 索双富, 孙晋厚, 肖丽英. 点钞机鉴伪技术发展趋势[J]. 机械设计与制造. 2007(12):1992-201.  
[13] 李忠和. 第五套人民币两个版本的防伪特征比较[J]. 中国防伪报道,2015,(03):20-24.  
[14] 庞程, 基于流形学习的纸币图像分析方法研究[D]. 哈尔滨:哈尔滨工业大学，2013  
[15] 刘加峰, 刘松波, 唐降龙. 一种实时纸币识别方法的研究. 计算机研究与发展. 2003,40(7):1057-1061  
[16] 徐雪倩, 张凤生. 基于中值滤波和小波变换的织物图像预处理[J]. 青岛大学学报(工程技术版), 2011,26(01):19-22.  
[17] 李方震. 纸币多光谱图像采集及预处理技术研究与实现[D]. 华中科技大学,2015.  
[18] 蒋琳琼, 李余琪. 基于 ARM 和 T-Kernel 的纸币特征采集预处理系统[J]. 科技信息，2010，(09):428-429.  
[19] 杨柱中, 周激流, 郎方年. 基于分数阶微积分的噪声检测和图像去噪[J]. 中国图象图形学报,2014,19(10):1418-1429.  
[20] Lee Y, Rhee S. Wavelet-based Image Denoising with Optimal Filter[J]. Journal ofInformation Processing Systems, 2005, 1(1): 32-35.  
[21] 杨晓, 胡可杨, 汪烈军等. 基于布谷鸟优化的三维OTSU 图像分割算法[J]. 新疆大学学报(自然科学版),2017,34(04):452-458.  
[22] Sfikas G, Nikou C, Galatsanos N P, et al. Edge preserving spatially varying mixtures forimage segmentation[C]. computer vision and pattern recognition, 2008: 1-7.  
[23] 陈会斌, 郑永辉, 张磊. 基于改进分水岭算法的高分遥感影像分割方法研究[J]. 计算机与数字工程,2017,45(09):1853-1858.  
[24] Thakare P,A Study of Image Segmentation and Edge Detection Techniques [J]. InternationalJournalon Computer Science and Engineering 2011,3(2):899-904.  
[25] Lakshmi S, Sankaranarayanan DV.A study of Edge Detection Techniques for SegmentationComputing Approaches[J]. International Journal of Computer Applications, 2010: 7-10.  
[26] Pandit S M, Joshi G A. Image Enhancement: A Data Dependent Systems Approach[J].Journal of Engineering for Industry, 1994, 116(2): 247-252.  
[27] 聂超. 基于直方图的高效图像增强算法研究[D].杭州电子科技大学,2014.  
[28] 王龙. 图像纹理特征提取及分类研究[D].中国海洋大学,2014.  
[29] 李建萍, 付丽琴, 韩焱. 用于特征提取的Gabor 滤波器参数设计[J], 光学与光电技术，2010,8(3):79-83.  
[30] Abhishree T M, Latha J, Manikantan K, et al. Face Recognition Using Gabor Filter Based FeatureExtraction with Anisotropic Diffusion as a Pre-processing Technique[J]. ProcediaComputer Science, 2015: 312-321.  
[31] 徐红侠. 基于Gabor 和局域二值模式的人脸表情识别[D].南京理工大学,2008.  
[32] 林喜荣, 苏晓生, 王敏. Gabor 滤波器在指纹图像处理中的应用[J]. 仪器仪表学报, 2003,(02):183-186.  
[33] Gottumukkal R, Asari V K.An improved face recognition technique based on modular PCAapproach[J].Pattern Recognition Letters，2004，25（4）：429-436.  
[34] 陈伏兵, 杨静宇.分块 PCA 及其在人脸识别中的应用[J].计算机工程与设计, 2007，28（8）：1889-1893.  
[35] 尚硕. 基于 Gabor 小波和 2DPCA 方法的人脸表情识别算法[D].河北工业大学,2014.  
[36] Javed A. Face Recognition Based on Principal Component Analysis[J]. International JournalofImage, Graphics and Signal Processing. (IJIGSP), 2013, 5(2): 38.  
[37] He Lianghua. Multi-Dimension Principal Component Analysis based on face recognition[J]. TheJournal of New Industrialization, 2012, 2(1): 59-65.  
[38] 利强. 无监督学习框架下学习分类器系统聚类与主干网提取方法研究[D].苏州大学,2016.  
[39] 絮青, 宋书林, 沈源. 一种无监督学习的异常行为检测方法[J]. 光电工程,2014,41(03):43-48.  
[40] Jessup E R, Sorensen D C. A Parallel Algorithm for Computing the Singular ValueDecomposition of a Matrix[J]. SIAM Journal on Matrix Analysis and Applications, 1994,15(2): 530-548.  
[41] 曾作钦, 赵学智. 一种基于奇异值分解的奇异性检测新方法[J]. 沈阳工业大学学报, 2011,33(01):102-107.  
[42] 洪子泉, 杨静宇. 基于奇异性特征和统计模型的人像识别算法[J]. 计算机研究与发展.1994,31(3).  
[43] Lerong MA,Dandan SONG,Lejian LIAO,Jingang WANG. PSVM: a preference-enhanced SVMmodel using preference data for classification[J]. Science China(Information  Sciences),2017,(12):165-178.  
[44] 赵展, 夏旺, 闫利. 基于特征距离的多类 SVM 分类方法研究[J/OL]. 地理空间信息,2017,(11):84-87+7(2017-11-21).  
[45] Bazi Y, Melgani F. Toward an Optimal SVM Classification System for Hyperspectral RemoteSensing Images[J]. IEEE Transactions on Geoscience and Remote Sensing, 2006, 44(11):3374-3385.  
[46] 刘东启, 陈志坚, 徐银. 面向不平衡数据分类的复合SVM 算法研究[J/OL]. 计算机应用研究,2018, (04):(2017-04-01).  
[47] 于欣, 秦文华, 周崇波等. 基于改进的 PCA 和 SVM 的人脸识别方法[J]. 电子技术, 2015,44(08):57-59+50.Poh T C, Lani N F, Kin L W, et al. Multi-dimensional features reduction of PCA on SVMclassifierfor imaging surveillance application[C]. international conference on signal processing, 2008:92-197.  
[48] Jing C, Hou J. SVM and PCA based fault classification approaches for complicated industrialprocess[J]. Neurocomputing, 2015: 636-642.  
[49] 李太福, 胡胜, 魏正元等. 基于遗传优化的PCA-SVM 控制图模式识别[J]. 计算机应用研究,2012,29(12):4538-4541+4545.  
[50] 彭红星, 陈祥光, 徐巍. PCA 特征抽取与SVM 多类分类在传感器故障诊断中的应用[J]. 数据采集与处理,2010,25(01):111-116.  
[51] Abumostafa Y S, Psaltis D. Image Normalization by Complex Moments[J]. IEEE Transactions onPattern Analysis and Machine Intelligence, 1985, 7(1): 46-55.  
[52] 郭伟, 赵亦工, 谢振华, et al. 一种改进的红外图像归一化互相关匹配算法[J]. 2009, 38(01).  
[53] 孙劲光, 苗锡奎, 张语涵, et al. 图像归一化与伪 Zernike 矩的鲁棒水印算法研究[J]. 2010:1052-1054.  
[54] Xie J, Qin C, Liu T, et al. A new method to identify the authenticity of banknotes based On thetexture roughness[C]. robotics and biomimetics, 2009: 1268-1271.  
[55] Lohweg V, Schaede J G, Turke T, et al. Robust and reliable banknote authentification and print flawdetection with opto-acoustical sensor fusion methods[J]. Proceedings of SPIE, 2006.  
[56] 索双富, 孙晋厚, 肖丽英, et al. 点钞机鉴伪技术发展趋势[J]., 2007: 199-201.  
[57] Latane B, Liu J H, Nowak A, et al. Distance Matters: Physical Space and Social Impact[J].Personality and Social Psychology Bulletin, 1995, 21(8): 795-805.  
[58] 陈重阳. 空间距离的统一向量公式及应用[J]. 2005.  
[59] 刘冰. 多类 SVM 分类算法的研究和改进[J]. 2007.

# 致谢

在我的论文完成之际，我要特别感谢我的指导老师张学东教授的热情关怀和悉心指导，在我撰写论文的过程中，张学东教授倾注了大量的心血和汗水，无论在论文选题，构思和资料的收集方面，还是在论文的研究方法以及成文定稿方面，我都得到他的悉心细致的教诲和无私的帮助，特别是他广博的学识，沉厚的学术素养，严谨的治学精神和一丝不苟的工作作风给我做出了榜样，在此我表示我的真诚的感谢和深深的谢意。

感谢实验室里一起经历的同学，感谢他们对我论文上的帮助，在这个两年的生活里，大家和睦相处，相互帮助，度过一个难忘的研究生生活。同时我也感谢我的父母和亲人，感谢父母对我的养育之恩，感谢那些对我生活上的关心和支持。由他们对我的做我坚强的后盾，让我更好的向前进步。

![](images/9093fc22f8dfa50a8ebd4e27b44b6f21b7a7941ceb78939228b45ca39eeccecd.jpg)