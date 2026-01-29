![](images/bcac3d0da9aae994051d2632c28df56fd3d432aede43627edd4ff8a8a38773b4.jpg)

计算机科学  
Computer Science  
ISSN 1002-137X,CN 50-1075/TP

# 《计算机科学》网络首发论文

题目：  
作者：  
网络首发日期：  
引用格式：基于滚动 MLP 特征提取的红外与可见光图像融合跨模态对比表示网络闫志林，聂仁灿  
2024-11-22  
闫志林，聂仁灿．基于滚动 MLP 特征提取的红外与可见光图像融合跨模态对比表示网络[J/OL]．计算机科学.  
https://link.cnki.net/urlid/50.1075.TP.20241122.1415.023

![](images/c4943618c2b887db413b902b7a19afeb025c5a0e7cc4263cca027ab335775e05.jpg)

网络首发：在编辑部工作流程中，稿件从录用到出版要经历录用定稿、排版定稿、整期汇编定稿等阶段。录用定稿指内容已经确定，且通过同行评议、主编终审同意刊用的稿件。排版定稿指录用定稿按照期刊特定版式（包括网络呈现版式）排版后的稿件，可暂不确定出版年、卷、期和页码。整期汇编定稿指出版年、卷、期、页码均已确定的印刷或数字出版的整期汇编稿件。录用定稿网络首发稿件内容必须符合《出版管理条例》和《期刊出版管理规定》的有关规定；学术研究成果具有创新性、科学性和先进性，符合编辑部对刊文的录用要求，不存在学术不端行为及其他侵权行为；稿件内容应基本符合国家有关书刊编辑、出版的技术标准，正确使用和统一规范语言文字、符号、数字、外文字母、法定计量单位及地图标注等。为确保录用定稿网络首发的严肃性，录用定稿一经发布，不得修改论文题目、作者、机构名称和学术内容，只可基于编辑规范进行少量文字的修改。

出版确认：纸质期刊编辑部通过与《中国学术期刊（光盘版）》电子杂志社有限公司签约，在《中国学术期刊（网络版）》出版传播平台上创办与纸质期刊内容一致的网络版，以单篇或整期出版形式，在印刷出版之前刊发论文的录用定稿、排版定稿、整期汇编定稿。因为《中国学术期刊（网络版）》是国家新闻出版广电总局批准的网络连续型出版物（ISSN 2096-4188，CN 11-6037/Z），所以签约期刊的网络版上网络首发论文视为正式出版。

# 基于滚动 MLP 特征提取的红外与可见光图像融合跨模态对比表示网络

闫志林 聂仁灿云南大学信息学院 昆明 650500（yanzhilin@stu.ynu.edu.cn）

摘 要 目前红外与可见光图像融合中，数据集缺乏真实融合图像来对最终融合图像所需要两种模态重要的差异信息进行引导。现有的融合方法大多数只考虑到源图像的权衡和交互，忽略了融合图像在融合过程中的作用。融合图像中的重要信息可以对源图像的差异信息进行约束，因此提出了一种对比表示(ContrastiveRepresentation Network, CRN)网络来更好地引导融合图像所需源图像中重要信息的提取；同时提高融合图像重建的质量可以进一步加强对源图像重要特征信息的引导。重建图像的质量与提取特征相关，现有的特征提取方法中，CNN 在全局特征的捕获上表现欠佳，而 Transformer 的计算复杂度高，局部特征的学习能力较差。在此基础上引入了一种结合MLP 的CNN 模块D2 Block，通过对不同方向上的特征映射进行滚动操作，有效提取并融合局部特征和远程依赖关系。该方法在多个公共数据集上的大量定性和定量实验证明，与其他先进方法相比取得较好的结果。

关键词：图像融合；对比表示学习；特征提取；深度学习；自编码器

中图法分类号  TP391

# Rolling MLP Feature Extraction Based Cross-modality Contrastive Representation Network for Infrared and Visible Image

YAN Zhilin ，NIE Rencan

School of Information Science and Engineering, Yunnan University, Kunming 650500, China

Abstract  At present, in the fusion of infrared and visible image, the data set lacks the real fusion image to guide the important difference information of the two modes required for the final fusion image. Most of the existing fusion methods only consider the tradeoff and interaction of the source image, ignoring the role of the fusion image in the fusion process. The important information in the fusion image can constrain the difference information of the source image. Therefore, a Contrastive Representation Network (CRN) is propose to better guide the extraction of important information in the source image required by the fused image. At the same time, improving the quality of fusion image reconstruction can further strengthen the guidance of important feature information of source image. The quality of the reconstructed image is related to the extracted features. Among existing feature extraction methods, CNN has poor performance in capturing global features, while Transformer has high computational complexity and poor learning ability of local features. On this basis, a CNN module D2 Block combined with MLP is introduced, which can effectively extract and fuse local features and remote dependencies by rolling feature mappings in different directions. A large number of qualitative and quantitative experiments on several public data sets show that the proposed method achieves better results than other advanced methods.

Keywords  Image fusion, Contrastive representation learning, Feature extraction, Deep learning, Autoencoder

# 1 引言

当前受硬件设备的限制和拍摄环境因素的影响，单模态传感器得到的图像往往无法全面描述整个场景。通过图像融合技术可以整合不同模态图像的优势，从源图像中提取出最有意义的差异信息，并将其融合成融合图像。融合后的图像在减少数据冗余的同时也促进后续应用，具有很大的应用前景。在图像融合领域，红外和可见光图像融合是应用最广泛的图像融合技术[1]。其融合算法广泛应用于自动驾驶、军事行动、目标检测[2], [3]和监控领域[4]。

近几十年来，人们提出了许多图像融合方法，大致分为两类:传统方法和基于深度学习的方法。传统方法包括显著性方法[5, 6]、多尺度变换方法[7-9]、神经网络方法[10, 11]、稀疏表示方法[12, 13]、子空间方法[14]等。虽然上述算法在某些场景下往往能取得较好的融合效果，但仍然存在一些问题:1)许多传统算法对不同源图像的特征提取使用相同的变换，没有考虑源图像的固有特征;2)目前的融合规则大多是手工设计的，这些融合规则变得更加复杂，并且有一定的实现难度和计算成本约束。

随着深度学习的不断发展，研究人员提出了一些基于深度学习的图像融合算法，例如，基于卷积神经网络(CNN)的方法，基于自编码器(AE)的方法，基于生成对抗网络(GAN)的方法，以及基于 Transformer 的方法等。SDNet[15]和 U2Fusion[16]被设计为统一的图像融合框架，解决了基于 CNN 的不同融合任务的问题。通过优良的网络结构和精心设计的损失函数，取得了良好的效果。DenseFuse[17]和 IFCNN[18]是典型的基于 AE 的方法。采用元素相加、拼接等融合规则将提取的特征进行融合。最后根据融合后的特征重构融合后的图像。SSL-WAEIE[19]关注模态间交互，采用逐像素差分来定义互补信息，并使用减法运算来获得互补信息。UNFusion[20]的编码器和解码器架

![](images/f0346ed45697d67bbf7b2e8bf57d4df9ee62492f89d553c5a9f49dc53fd8e94a.jpg)  
图 1 图像融合的示意图  
Fig. 1 Schematic illustration of image fusion.

构考虑到多尺度特征，并采用密集跳跃连接的方式，重用不同层和尺度的所有中间特征来完成融合。考虑到图像融合缺乏标签的特性，基于GAN 的方法不受损失函数的约束，因此将其引入图像融合。例如，GANMcC[21]提出在融合过程中，红外图像中的纹理和可见光图像中的对比度信息作为辅助信息同样不能忽视，并使用特定内容损失作为生成器来解决这一问题。DDcGAN[22]将源图像发送给生成器，然后将融合后的图像和源图像发送给判别器进行比较。SDDGAN[23]有两个鉴别器，设计了一个信息量鉴别器来生成融合的权重。在损失函数的指导下,融合图像能够获得源图像中丰富的纹理细节和重要的热目标。SwinFusion[24]是图像融合领域第一个清楚展示全局信息的研究，指出全局信息在图像融合中至关重要。SwinFuse[25]的整体结构基于 AE 的框架，在编码器中引入Transformer 来提取全 局特 征。DATFuse[26]利用双注意残差模块来实现重要特征提取，还设计了一个 Transformer 模块用于全局互补特征的保存。SeAFusion[27]考虑到融合最终为了高级视觉任务的完成，与下游任务的模块级联通过语义损失引导语义损失回流，提升在下游任务上的性能。

本质上来说，红外图像和可见光图像分别是对同一场景单个模态差异信息的描述。在融合的过程中，简单的提取两个模态的特征再将其融合重建出融合图像会引入一些多余信息造

![](images/0f15b16434ee47a0a724cd83899ccfdc91b13ebf7e080fd90bb4fd6c5f2ee12b.jpg)  
图 2 宽度方向的滚动操作说明

direction

成信息的冗余，影响最终融合图像的质量。现有的融合方法主要关注的是源图像两种模态间的交互，很少考虑到融合图像对于源图像的作用。同时在全局与局部特征的提取上，采取的基本是 CNN 和 Trasformer 的结合。He 等[28]在2020 年提出 Siamese 模型，在不需要负样本、大批量和动量编码器的条件下最大化一幅图像两个增强之间的相似性，学习到图像更有意义的表示。根据红外与可见光图像描述同一场景光谱与空间细节差异信息不同表示的特性，提出了一种对比表示网络(Contrastive RepresentationNetwork, CRN)，输入网络的融合图像与源图像间的相似性得以最大化。

CRN 利用融合图像中所需的重要信息作为约束，源图像中的有用信息得到更好的表示，最终得到了更优的融合图像。针对现有 CNN,Transformer 在全局与局部特征提取中存在的问题，提出了一种结合 MLP 的 CNN 模型 D2 Block。具体来说，D2 Block 的核心是 Rolling-MLP(R-MLP)模块，该模块负责学习整个图像在单一方向上的长距离依赖关系。通过对不同方向的 R-MLP 模 块 进 行 控 制 和 组 合 ， 形 成Orthogonal Rolling-MLP(OR-MLP)和 DoubleOrthogonal Rolling-MLP(DOR-MLP)模块，以捕获多方向的远程依赖关系，从而有效地提取融合了局部特征和全局依赖关系。我们选取一些代表性融合方法与本文方法作比较，如图 1所示。可以

![](images/81ba177eb44fc7934db83e7725e68b17c758dce2cb6d1cc987a769fd2a1a4fce.jpg)  
Fig. 2 Illustration of the Rolling operation in width   
图 3 控制组合不同方向的 R-MLP 示意图  
Fig. 3 Schematic diagram of R-MLP in different directions of control combination

看出三种基于深度学习的方法都得到了良好的融合效果，但本文的方法展示了更优异的效果。SDNet 和 SDDGAN 缺乏全局特征提取能力，引入 了 过 多 的 红 外 信 息 。SwinFusion 引 入Transformer 后这些问题得到一定缓解，但对比度信息有一定程度的削弱，同时纹理细节方面有丢失（房屋附近的树枝）。只有本文提出的方法很好的融合了红外图像中的对比度信息和可见图像中的纹理细节。

本文主要贡献如下：

(1)提出了一种基于滚动 MLP 特征提取的红外与可见光图像融合跨模态对比表示网络,利用生成融合图像与源图像的交互来解决真实融合图像缺失的问题。

(2)引入对比学习来处理两个模态间的差异性信息，从而得到更好的特征表示用于下游任务。

(3)与目前 13 种先进融合方法相比，本文算法在定性、定量实验以及下游目标检测中展示了优异的性能。

# 2 R-MLP 模块

Liu 等[29]提出了一种结合 MLP 的 CNN 模型 Rolling-Unet 用于医学图像分割。给定空间分辨率为 $H \times W$ ，通道数为 $C$ 的特征矩阵

![](images/752547435cd7a52a38097a71fa1580c9c5711a124d1e9932d1d73ab226fd732a.jpg)  
图 4 网络整体结构

![](images/ae66256a8de7ee53c99f3296fa228e7c5c6822b8d8ffccec6588142a880ba6b4.jpg)  
图 5 D2 模块结构  
Fig. 5 Structure of the D2 Block

$\pmb { x } \in \pmb { H } \times \pmb { W } \times \pmb { C }$ ，其中 $\pmb { h } _ { i } ( \pmb { i } \in [ 1 , H ] )$ 表示高度，𝒘𝒋(𝒋 ∈[1, 𝑊])表示宽度， $\pmb { c } _ { k } ( \pmb { k } \in [ 1 , C ] )$ 表示通道数。我们沿同一方向对特征矩阵中各通道层的特征映射进行滚动操作，如图2 所示(以宽度方向为例)。滚动操作包括两个步骤:移动和裁剪。首先，对通道索引为 $\scriptstyle \mathbf { c } _ { k }$ 的特征映射移动 $\mathcal { k }$ 步，然后以通道索引为 $\pmb { c _ { 0 } }$ 的特征映射为参考，将其他特征映射的多余部分裁剪为缺失部分。最后，在每个空间位置索引 $( \pmb { h } _ { i } , \pmb { w } _ { j } )$ 上执行一个权重共享的通道投影来编码远程依赖。在图 2 中我们可以看到原始特征矩阵在固定的空间索引 $( h _ { i } , w _ { j } )$ 下只有一个宽度 $\pmb { w } _ { j }$ 特征。但在宽度方向上施加滚动操作后，不同的通道具有不同的宽度特征。当$C { \ge } W$ 时，我们可以对整个图像的宽度特征进行编码，可以理解为全局的、单向的、线性的感受野。当 $C < W$ 时，这个线性感受野是非全局的。同样，R-MLP 也可以在高度方向上捕获远程依赖。通过核心的 R-MLP 模块负责学习整个图像在单一方向上的远程依赖关系。然后通过对不同方向的 R-MLP 模块进行控制和组合，如图 3 所示，可以捕获多方向的远程依赖关系。

![](images/ed3ca4ff1212266d69fa7b6f41d44cda897a0a65a96c088105cb700d6c5af088.jpg)  
Fig. 4 The overall structure of the network   
图 6 DOR-MLP 的详细结构  
Fig. 6 Detail structure of the DOR -MLP

# 3 滚动 MLP 对比表示网络

# 3.1 网络结构

本文的网络结构如图 4 所示，红外和可见光图像作为输入，先经过参数共享的编码器升至对比表示网络所需的通道数，再通过映射头和预测头将其映射到 CRN 的特征空间中，同时解码器 1 将红外与可见光特征进行通道级联并得到 CRN 所需的通道数再将其送入 CRN。在对比损失的约束下，融合图像与源图像中所需的重要信息相互靠近，减少了融合过程中重要信息的丢失，从而引入了更多源图像中的重要信息。最后解码器 2 将融合后的特征多级解码重构得出融合图像。在特征提取阶段，我们利用 CNN 和 MLP 结合的办法，更好地捕获了整幅图像的局部和全局的特征，并采取残差连接进一步加强了特征提取能力。

![](images/134c9c7ce4f3511633da7deaed8527f62f6ef52b68206de809baf763b69c1d72.jpg)  
图 7 TNO、MSRS 和 M3FD 数据集的融合结果比较（从上到下：TNO、MSRS 和 M3FD）  
Fig. 7 Comparison of fusion results of TNO, MSRS and M3FD datasets(from top to bottom: TNO, MSRS and

M3FD)

# 3.2 特征提取阶段

本文的特征提取模块如图 4 所示，由两个ResBlock 与两个 D2 Block 经残差连接构成。ResBlock 用来缓解梯度消失或爆炸问题，其残差映射由两个卷积层组成，用于提取特征。恒等映射由一个核大小为 $1 \times 1$ 的卷积层组成，用于调整输入和输出维数并保持其一致性，如图 4 所示。D2 Block 具体结构见图 5， 由 DOR-MLP 和DSC 组成，分别用来提取图像的全局和局部信息。DOR-MLP 模块如图 6 所示，用来捕获二维空间中沿四个方向的全局线性远程依赖关系，但缺乏局部上下文信息。深度可分离卷积(DSC)参数少，计算成本低，与 DOR-MLP 兼容。因此我们采用DSC 来更好地整合本地信息和全局依赖关系。本文中的 R-MLP 等价于 CNN 中的标准 $1 \times 1$ 卷积，允许不同通道之间的特征交互。DOR-MLP 与 DSC 采用并行连接，然后将它们的输出进行通道级联，最后使用 通 道 混 合(Channel-mixing, CM)来 融 合特 征并将通道恢复到 $\mathbf { \Psi } _ { c }$ 。D2 模块由此形成，参见公式(1)。

$$
D 2 ( X ) = C M ( C o n c a t [ D O R ( X ) , D S C ( X ) ]
$$

# 3.3 对比表示网络(CRN)

CRN 由投影 MLP 和预测 MLP 两部分组成，如图 3 所示。映射 MLP 和预测 MLP 分别用 $g ( \cdot )$ 和h(∙)表示。

# 3.3.1 映射 MLP

在 CRN 中，减少红外与可见光图像两种模态的差异就是缩小特征空间中两个向量的距离。 $g$ 的作用是将编码器得到的特征向量映射到特征空间，表示为：

$$
\pmb { z _ { 1 } } \triangleq g ( f ( I _ { i r } ) )
$$

$$
\pmb { z _ { 2 } } \triangleq g ( f ( I _ { v i } ) )
$$

# (3)

# 表 1 不同方法在 MSRS、M3FD 与 TNO 数据集的定量结果

Table1 Average quantitative results on MSRS, M3FD and TNO for different methods   

<html><body><table><tr><td rowspan="2">Datasets Metric</td><td colspan="4">MSRS datasets</td><td colspan="4">M3FD datasets</td><td colspan="4">TNO datasets</td></tr><tr><td>VIFP</td><td>Qy</td><td>QABF</td><td>NMI</td><td>VIFP</td><td>Qy</td><td>QABF</td><td>NMI</td><td>VIFP</td><td>Qy</td><td>QABF</td><td>NMI</td></tr><tr><td>DATFuse</td><td>0.4511</td><td>0.8608</td><td>0.6394</td><td>0.6000</td><td>0.3222</td><td>0.8777</td><td>0.4935</td><td>0.6239</td><td>0.3398</td><td>0.7035</td><td>0.3665</td><td>0.4705</td></tr><tr><td>LRRNet</td><td>0.2220</td><td>0.4121</td><td>0.2674</td><td>0.3383</td><td>0.2232</td><td>0.5675</td><td>0.2732</td><td>0.4572</td><td>0.2423</td><td>0.6153</td><td>0.3369</td><td>0.3268</td></tr><tr><td>LDRepFM</td><td>0.4261</td><td>0.5977</td><td>0.4852</td><td>0.4846</td><td>0.4285</td><td>0.7215</td><td>0.5404</td><td>0.5389</td><td>0.3646</td><td>0.7410</td><td>0.4382</td><td>0.4313</td></tr><tr><td>SeAFusion</td><td>0.4874</td><td>0.8952</td><td>0.6653</td><td>0.5917</td><td>0.2927</td><td>0.6550</td><td>0.5067</td><td>0.4435</td><td>0.3031</td><td>0.7155</td><td>0.4226</td><td>0.3803</td></tr><tr><td>SSL-WAEIE</td><td>0.4487</td><td>0.8901</td><td>0.6219</td><td>0.6054</td><td>0.3726</td><td>0.8610</td><td>0.5259</td><td>0.6402</td><td>0.4262</td><td>0.8323</td><td>0.5157</td><td>0.5646</td></tr><tr><td>SwinFuse</td><td>0.1768</td><td>0.2915</td><td>0.1753</td><td>0.3306</td><td>0.3905</td><td>0.7253</td><td>0.5384</td><td>0.4459</td><td>0.3334</td><td>0.7103</td><td>0.4163</td><td>0.3614</td></tr><tr><td>SwinFusion</td><td>0.3565</td><td>0.7866</td><td>0.6029</td><td>0.3660</td><td>0.2994</td><td>0.6529</td><td>0.5188</td><td>0.5293</td><td>0.3746</td><td>0.8576</td><td>0.5209</td><td>0.4873</td></tr><tr><td>U2Fusion</td><td>0.2649</td><td>0.5689</td><td>0.4076</td><td>0.3425</td><td>0.3422</td><td>0.7530</td><td>0.5573</td><td>0.3993</td><td>0.3029</td><td>0.7148</td><td>0.4264</td><td>0.2792</td></tr><tr><td>UNFusion</td><td>0.4728</td><td>0.8883</td><td>0.6513</td><td>0.6366</td><td>0.3901</td><td>0.8747</td><td>0.5514</td><td>0.5866</td><td>0.4506</td><td>0.8618</td><td>0.5364</td><td>0.5423</td></tr><tr><td>SDDGAN</td><td>0.3325</td><td>0.6032</td><td>0.3757</td><td>0.3666</td><td>0.2905</td><td>0.6483</td><td>0.3508</td><td>0.4555</td><td>0.2779</td><td>0.6599</td><td>0.3323</td><td>0.3253</td></tr><tr><td>SDNet</td><td>0.2474</td><td>0.5539</td><td>0.3726</td><td>0.3063</td><td>0.2915</td><td>0.7358</td><td>0.5294</td><td>0.4677</td><td>0.2884</td><td>0.7230</td><td>0.4270</td><td>0.3296</td></tr><tr><td>GF</td><td>0.3850</td><td>0.7952</td><td>0.5828</td><td>0.4057</td><td>0.2828</td><td>0.6526</td><td>0.4553</td><td>0.4137</td><td>0.2660</td><td>0.6588</td><td>0.3849</td><td>0.3178</td></tr><tr><td>GANMcC</td><td>0.3137</td><td>0.6291</td><td>0.3298</td><td>0.3866</td><td>0.2734</td><td>0.6251</td><td>0.3199</td><td>0.4122</td><td>0.2707</td><td>0.6369</td><td>0.3119</td><td>0.3212</td></tr><tr><td>Ours</td><td>0.4967</td><td>0.9327</td><td>0.6834</td><td>0.9342</td><td>0.4287</td><td>0.9008</td><td>0.5541</td><td>1.0161</td><td>0.5274</td><td>0.8795</td><td>0.5601</td><td>0.9613</td></tr></table></body></html>

$$
z _ { 3 } \triangleq g ( f ( I _ { f } ) )
$$

这里 $\pmb { z _ { 1 } }$ ， $\pmb { z } _ { 2 }$ ， $\pmb { z _ { 3 } }$ 代表红外图像 $I _ { i r }$ 、可见光图像$I _ { v i }$ 和融合图像 $I _ { f }$ 通过 $g$ 映射到特征空间的特征向量。

# 3.3.2 预测 MLP

两种模态的图像包含许多无效特征，最终会影响重要信息的引入，导致融合结果的恶化。为了减少两种模态信息的冗余， $h$ 将一种模态的输出与另一种模态的输出相匹配，表示为：

其中， ${ \pmb p } _ { 1 }$ ，𝒑𝟐 ${ \pmb p } _ { 3 }$ 代表 $\pmb { z _ { 1 } }$ ，𝒛𝟐， 𝒛𝟑在经过预测MLP 后输出的特征向量。

# 3.4 损失函数

本文损失函数由对比损失和亮度损失两部分组成，如式(4)所示：

$$
{ \cal L } = { \cal L } _ { f s l } + \alpha { \cal L } _ { i n t }
$$

其中， $\boldsymbol { L _ { f s l } }$ 为对比损失， $L _ { i n t }$ 为亮度损失， $\alpha$ 为权重系数。

# 3.4.1 对称损失

本文将对称损失 $L _ { f s l }$ 分为红外 $L _ { f s l 1 }$ 与可见光$L _ { f s l 2 }$ 两部分，分别来约束融合图像引入更多红外和可见光图像的重要信息，具体见公式(9)：

$$
{ \cal L } _ { f s l } = { \cal L } _ { f s l 1 } + { \cal L } _ { f s l 2 }
$$

其中， $\boldsymbol { L _ { f s l 1 } }$ 和 $L _ { f s l 2 }$ 分别表示红外和可见光的对称损失。具体表示为：

$$
\begin{array} { r } { L _ { f s l 1 } = \frac { 1 } { 2 } D ( \pmb { p _ { 1 } } , \pmb { z _ { 3 } } ) ) + \frac { 1 } { 2 } D ( \pmb { p _ { 3 } } , \pmb { z _ { 1 } } ) } \\ { L _ { f s l 2 } = \frac { 1 } { 2 } D ( \pmb { p _ { 2 } } , \pmb { z _ { 3 } } ) ) + \frac { 1 } { 2 } D ( \pmb { p _ { 3 } } , \pmb { z _ { 2 } } ) } \end{array}
$$

其中， $D ( \cdot )$ 是距离函数，我们选取的是负余弦相似度：

$$
\begin{array} { r } { D \big ( \pmb { p } _ { i } , s t o p g r a d ( \pmb { z } _ { j } ) \big ) = - \frac { \pmb { p } _ { i } } { | | \pmb { p } _ { i } | | _ { 2 } } \cdot \frac { \pmb { z } _ { j } } { | | \pmb { z } _ { j } | | _ { 2 } } } \end{array}
$$

其中，stopgrad (∙ )所指的是停止梯度传播操作。|| ∙ ||2 为 $l _ { 2 }$ 范数。最小值为-1。负余弦相似度相当于最小化两个归一化向量的 MSE（均方误差）。它的值越小，在特征空间中两个特征向量的值越近。

# 3.4.2 亮度损失

为了保证融合图像的最优亮度分布，我们进一步引入了亮度损失 $L _ { i n t }$ ，如下：

$$
\begin{array} { r } { L _ { i n t } = \frac { 1 } { H W } | | I _ { f } - m a x ( I _ { i r } , I _ { v i } ) | | _ { 1 } } \end{array}
$$

其中， $H$ 和 $W$ 分别代表输入图像的长和宽。𝑚𝑎𝑥(∙)代表逐像素的最大选择。

# 4 实验

本章首先介绍实验的具体设置细节，数据集的介绍和评价指标。然后为了验证我们方法的有效性，将我们的方法与当前 13 种先进方法做了对比实验。消融实验和参数分析进一步验证了网络设计的合理性。另外通过目标检测实验，我们证实我们的网络显著提高了下游任务的性能。

# 4.1 实验设置及细节

我们所提出的方法是在 PyTorch 框架部署的，所有的实验是在 GPU NVIDIA GeForce RTX 3090上完成的，训练过程中所有的batch size设置为1，式(8)中的 $\alpha$ 设置为125。在我们选取的13 种先进方法中，包括一种传统方法： $\mathrm { G F } ^ { [ 3 0 ] }$ ，两种基于 AE的方法：SSL-WAEIE[19]，UNFusion[20]，两种基于GAN 的方法：GANMcC[21]，SDDGAN[23]，四种基于 CNN 的 方 法 ：SDNet[15]，U2Fusion[16]，LDRepFM[31]， 三 种 基 于 transformer 的 方 法 ：SwinFusion[24]，SwinFuse[25]，DATFuse[26]， 一 种基于表示学习的方法：LRRNet[32]，一种考虑高级视觉任务的方法：SeAFusion[27]。值得一提的是，为了证明我们的方法在多个数据集的泛化性能，我们选择了200 对MSRS 数据集中的图像作为训练集，然后从 MSRS, M3FD 和 TNO 数据集中随机选取了361、300 和40 对图像作为测试集直接测试。

# 4.2 评价指标

仅凭视觉效果评价的结果受环境影响，不同人对同一结果的直观感受存在差异。因此本文使用 4 个评估指标用于衡量融合结果,分别是基于信息论的评价指标：归一 化互信息(NMI)[33]，基于结构相似性的指标：结构相似性指数 $( \mathrm { Q } \mathrm { Y } ) _ { \hphantom { [ 3 4 ] } } ^ { [ 3 4 ] } ;$ ,基于源图像与生成图像的指标：基于梯度的融合度量$( \mathrm { Q } ^ { \mathrm { A B F } } ) ^ { [ 3 5 ] }$ ，基于人类视觉感知的指标： 像 素 级 视觉 信 息 保 真 度 (VIFP)[36]。NMI 是一个基于信息理论的度量，来评估 $\cdot _ { I _ { f } }$ 中包含源图像中的信息量。$\mathrm { Q _ { Y } }$ 反映的是源图像与 $I _ { f }$ 的结果相似程度，能够表示出结构信息的保持度。QABF反映了𝐼 中包含源图像梯度转移的程度。VIFP 则是从视觉信息的一致性和保持度上来衡量 $I _ { f }$ 的质量。上述指标都是值越大，表示融合效果越好。

# 4.3 结果分析

我们随机选取了 MSRS, M3FD 和 TNO 数据集中的部分代表性场景的图像融合结果在图7 中展示。为了更清晰的展示实验结果的差别，我们对纹理细节信息放大用红框标记，同时热辐射信息做了伪彩处理放大用绿框标记。另外，在三个数据集上与其他对比方法的指标结果如表1 所示，第一和第二结果分别用红色和蓝色字体标记。

从图 7 中可以清晰地看出，在 TNO 数据集中，LRRNet, SDNet, U2Fusion, SwinFuse, SDDGAN,GANMcC 和 GF 中有不同程度的光谱污染，

DATFuse、LDRepFM 中的显著目标信息受到削弱。在 MSRS 数据集中光照充足的环境下，SSL-WAEIE, SwinFusion, UNFusion 和 LDRepFM 中的对比度信息有不同程度的退化，LRRNet, SwinFusion,SDNet, U2Fusion, SwinFuse 和 GANMcC 在可见光纹理的保留方面受到不同程度的干扰。在 M3FD数据集的夜间场景中，SwinFusion, SwinFuse 和SDDGAN 引入了不同程度的噪声污染。LRRNet,SSL-WAEIE, SDNet 和 SwinFuse 放大的可见光纹理细节均有一定程度的退化。

从表1 中可知，我们的方法在三个数据集上的指标表现优异，除了 U2Fusion 在 M3FD 数据集上的 $\mathbf { Q } ^ { \mathrm { A B F } }$ 略高于本文方法，在所有数据集上的其他指标本文方法都位列第一位。只有我们的方法考虑了𝐼 与源图像间的交互，最高的 NMI 表示本文方法得到的𝐼𝑓包含了最多的源图像信息，表明CRN 极大增强了𝐼 与源图像间的交互。最高的VIFP 反映了表示本文方法得到的 $I _ { f }$ 在视觉效果上极大符合人眼的要求，结合图7 的定性分析分析，可以得出我们的方法在视觉信息的保持度方面表现最优。 $\mathrm { Q } _ { \mathrm { Y } }$ 最高则代表 D2 Block 在特征提取方面展示了良好的性能，很好的保持源图像中的结构信息。

综上所述，本文方法很好地保留了图像的纹理细节和显著性目标信息。在定性分析中拥有良好的视觉效果，同时在边缘梯度信息和与源图像的信息交互上效果显著。

表2 不同参数的平均指标  
Table 2 Average metrics of different parameters   

<html><body><table><tr><td rowspan="2">Parameters</td><td colspan="4">Metrics</td></tr><tr><td>VIFP</td><td>Qy</td><td>QABF</td><td>NMI</td></tr><tr><td>125</td><td>0.4967</td><td>0.9327</td><td>0.6834</td><td>0.9342</td></tr><tr><td>150</td><td>0.5092</td><td>0.9169</td><td>0.6845</td><td>0.9059</td></tr><tr><td>175</td><td>0.4988</td><td>0.9052</td><td>0.6675</td><td>0.8451</td></tr><tr><td>200</td><td>0.5043</td><td>0.9306</td><td>0.6846</td><td>0.8973</td></tr><tr><td>225</td><td>0.5014</td><td>0.8862</td><td>0.6692</td><td>0.8919</td></tr></table></body></html>

# 4.4 参数分析

为了证明式(8)中 $\alpha$ 设置的合理性以及在损失函数中不同设置造成的影响，我们设置了不同的 $\alpha$ 值进行了实验。通过实验结果来选择 $\alpha$ 最后的参数设置。表 2 列出了不同值 $\alpha$ 下的融合性能。可以看出在所有参数设置中我们的方法在 $\alpha = 1 2 5$ 时，QY和

NMI 指标位列第一，代表此参数设置下 $\dot { I } _ { f }$ 保留了最多的结构信息且与源图像的交互达到最大，此时NMI 与最低值相差接近 $10 \%$ ，而 VIFP 和 $\mathbf { Q } ^ { \mathrm { A B F } }$ 与其他参数设置下相差无几，因此我们最终选择 $\alpha$ 设置为 125。

# 4.5 消融实验分析

为了证明所设计网络结构和损失函数的有效性，本文在 MSRS 数据集上针对对应网络结构和损失函数做了消融实验。我们分别去除了特征提取阶段的 D2Block 以及对比损失 $L _ { f s l }$ ，结果如表 3所示。可以看出，去除 D2 Block 后 $\mathrm { Q } _ { \mathrm { Y } }$ 和 $\mathbf { Q } ^ { \mathrm { A B F } }$ 大幅下降，代表包含 DOR-MLP 的 D2 Block 很好的提取了全局和局部特征。 $I _ { f }$ 很好保留了源图像中的梯度和结构信息。而去除 CRN 所有指标都大幅下降，证明 $I _ { f }$ 在整个融合过程中的重要性。输入CRN 的图像相似性最大化，减少了无效信息的引入，最终 $I _ { f }$ 所需的重要信息得到加强。我们所提出的方法除了 VIFP 略低于消融的版本，在其他各项指标上都表现出更优的效果。由此可见，我们的方法更好地引入了梯度信息，并加强了与源图像的交互。

表3 MSRS 数据集上网络结构和损失函数的消融实验 Table 3 Ablation study of network structures and loss functions   

<html><body><table><tr><td rowspan="2">Version</td><td></td><td colspan="3">Metrics</td></tr><tr><td>VIFP</td><td>Qy</td><td>QABF</td><td>NMI</td></tr><tr><td>No D2Block</td><td>0.5016</td><td>0.9054</td><td>0.6713</td><td>0.9169</td></tr><tr><td>No Lfst</td><td>0.4998</td><td>0.9002</td><td>0.6732</td><td>0.8749</td></tr><tr><td>Ours</td><td>0.4967</td><td>0.9327</td><td>0.6834</td><td>0.9342</td></tr></table></body></html>

表4 MSRS 数据集上361 幅图像的目标检测评价指标

on MSRS dataset   
Table 4 Object detection evaluation index of 361 images on   
MSRS dataset   

<html><body><table><tr><td colspan="4">MSkSdataset</td></tr><tr><td></td><td>Precision</td><td>Recall</td><td>mAP@[0.5:0.95]</td></tr><tr><td>DATFuse</td><td>0.921</td><td>0.814</td><td>0.589</td></tr><tr><td>LRRNet</td><td>0.888</td><td>0.787</td><td>0.557</td></tr><tr><td>LDRepFM</td><td>0.940</td><td>0.792</td><td>0.579</td></tr><tr><td>SeAFusion</td><td>0.860</td><td>0.848</td><td>0.583</td></tr><tr><td>SSL-WAEIE</td><td>0.922</td><td>0.780</td><td>0.516</td></tr><tr><td>SwinFuse</td><td>0.802</td><td>0.796</td><td>0.524</td></tr><tr><td>SwinFusion</td><td>0.892</td><td>0.840</td><td>0.564</td></tr><tr><td>U2Fusion</td><td>0.856</td><td>0.849</td><td>0.560</td></tr><tr><td>UNFusion</td><td>0.887</td><td>0.784</td><td>0.545</td></tr><tr><td>SDDGAN</td><td>0.927</td><td>0.793</td><td>0.560</td></tr><tr><td>SDNet</td><td>0.913</td><td>0.779</td><td>0.565</td></tr><tr><td>GF</td><td>0.784</td><td>0.750</td><td>0.496</td></tr><tr><td>GANMcC</td><td>0.855</td><td>0.874</td><td>0.587</td></tr><tr><td>Ours</td><td>0.944</td><td>0.804</td><td>0.608</td></tr></table></body></html>

# 4.6 目标检测实验分析

为了进一步验证本文提出网络得到融合图像的质量，我们选择了融合图像在下游任务目标检测中的性能来评估。本文使用在COCO 数据集上预训练的YOLOv7 来验证本文方法与其他对比方法的检测性能，并随机选择了 MSRS 数据集中的361 张图像做了手工标注。标注分为行人和车两个类别。

在表 4 中，我们可以看到目标检测的定量指标。Precision（精确率）指在正确预测目标与总的预测目标的比值。Recall（召回率）指正确预测目标与实际目标的比值。mAP（平均精度）则是目标检测中最重要的指标，代表着不同阈值下的平均精度值。从表 4 可以看出我们的方法在Precision与 mAP上均位列第一， 与其他方法相比，我们的方法性能更稳定。同时在对比方法中，SeAFusion 考虑了下游视觉任务并进行了初步探索。本文方法没有针对下游任务进行专门优化，但对于重要目标和所有类别的检测性能优于SeAFusion。证明我们的方法很好地保留源图像的差异信息，对于显著性目标和纹理细节做了有效的融合。

结束语 本文提出了一种基于滚动MLP 特征提取的红外与可见光图像融合跨模态对比表示网络。首先本文通过 MLP 与 CNN 的组合增强了网络的特征提取能力，有效地兼顾了图像的局部与全局特征。并且通过对比表示网络加强了融合图像与源图像的信息交互，更好地提取源图像中的重要信息，避免了一些冗余信息对最终的融合结果造成干扰。在公共数据集上的大量定量和定性实验得到的结果分析验证本文方法的性能优于最新的对比方法。本文实验使用的均为公开数据集，红外与可见光图像融合考虑的更多应用场景应该是复杂极端环境，同时图像融合的目标是提高下游任务的性能，更多应该考虑下游视觉任务的实际需求。未来应考虑将我们的工作应用到更多场景，整个图像融合的建模工作更多从高级视觉任务的需求出发。

# 参 考 文 献

[1] MA J, MA Y, LI C. Infrared and visible image fusion methods and applications: A survey [J]. Information fusion, 2019, 45: 153-78.   
[2] LI C, LIANG X, LU Y, et al. RGB-T object tracking: Benchmark and baseline [J]. Pattern Recognition, 2019, 96: 106977.   
[3] KRISTAN M, MATAS J, LEONARDIS A, et al. The seventh visual object tracking VOT2019 challenge results; proceedings of the Proceedings of the IEEE/CVF international conference on computer vision workshops, F, 2019 [C].   
[4] SHRINIDHI V, YADAV P, VENKATESWARAN N. IR and visible video fusion for surveillance; proceedings of the 2018 International conference on wireless communications, signal processing and networking (WiSPNET), F, 2018 [C]. IEEE.   
[5] BAVIRISETTI D P, DHULI R. Two-scale image fusion of visible and infrared images using saliency detection [J]. Infrared Physics & Technology, 2016, 76: 52-64.   
[6] ZHANG X, MA Y, FAN F, et al. Infrared and visible image fusion via saliency analysis and local edge-preserving multi-scale decomposition [J]. JOSA A, 2017, 34(8): 1400-10.   
[7] LI S, KANG X, HU J. Image fusion with guided filtering [J]. IEEE Transactions on Image processing, 2013, 22(7): 2864-75.   
[8] PAJARES G, DE LA CRUZ J M. A waveletbased image fusion tutorial [J]. Pattern recognition, 2004, 37(9): 1855-72.   
[9] ZHANG Z, BLUM R S. A categorization of multiscale-decomposition-based image fusion schemes with a performance study for a digital camera application [J]. Proceedings of the IEEE, 1999, 87(8): 1315-26.   
[10] KONG W, ZHANG L, LEI Y. Novel fusion method for visible light and infrared images based on NSST–SF–PCNN [J]. Infrared Physics & Technology, 2014, 65: 103-12.   
[11] XIANG T, YAN L, GAO R. A fusion algorithm for infrared and visible images based on adaptive dualchannel unit-linking PCNN in NSCT domain [J]. Infrared Physics & Technology, 2015, 69: 53-61.   
[12] YANG B, LI S. Visual attention guided image fusion with sparse representation [J]. Optik, 2014, 125(17): 4881-8.   
[13] LI S, YIN H, FANG L. Group-sparse representation with dictionary learning for medical image denoising and fusion [J]. IEEE Transactions on biomedical engineering, 2012, 59(12): 3450-9.   
[14] BAVIRISETTI D P, XIAO G, LIU G. Multisensor image fusion based on fourth order partial differential equations; proceedings of the 2017 20th International conference on information fusion (Fusion), F, 2017 [C]. IEEE.   
[15] ZHANG H, MA J. SDNet: A versatile squeezeand-decomposition network for real-time image fusion [J]. International Journal of Computer Vision, 2021, 129(10): 2761-85.   
[16] XU H, MA J, JIANG J, et al. U2Fusion: A unified unsupervised image fusion network [J]. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2020, 44(1): 502-18.   
[17] LI H, WU X-J. DenseFuse: A fusion approach to infrared and visible images [J]. IEEE Transactions on Image Processing, 2018, 28(5): 2614-23.   
[18] ZHANG Y, LIU Y, SUN P, et al. IFCNN: A general image fusion framework based on convolutional neural network [J]. Information Fusion, 2020, 54: 99-118.   
[19] ZHANG G, NIE R, CAO J. SSL-WAEIE: Selfsupervised learning with weighted auto-encoding and information exchange for infrared and visible image fusion [J]. IEEE/CAA Journal of Automatica Sinica, 2022, 9(9): 1694-7.

[20] WANG Z, WANG J, WU Y, et al. UNFusion: A unified multi-scale densely connected network for infrared and visible image fusion [J]. IEEE Transactions on Circuits and Systems for Video Technology, 2021, 32(6): 3360-74.

[21] MA J, ZHANG H, SHAO Z, et al. GANMcC: A generative adversarial network with multiclassification constraints for infrared and visible image fusion [J]. IEEE Transactions on Instrumentation and Measurement, 2020, 70: 1-14. [22] MA J, XU H, JIANG J, et al. DDcGAN: A dualdiscriminator conditional generative adversarial network for multi-resolution image fusion [J]. IEEE Transactions on Image Processing, 2020, 29: 4980-95. [23] ZHOU H, WU W, ZHANG Y, et al. Semanticsupervised infrared and visible image fusion via a dualdiscriminator generative adversarial network [J]. IEEE Transactions on Multimedia, 2021, 25: 635-48. [24] MA J, TANG L, FAN F, et al. SwinFusion: Cross-domain long-range learning for general image fusion via swin transformer [J]. IEEE/CAA Journal of Automatica Sinica, 2022, 9(7): 1200-17. [25] WANG Z, CHEN Y, SHAO W, et al. SwinFuse: A residual swin transformer fusion network for infrared and visible images [J]. IEEE Transactions on Instrumentation and Measurement, 2022, 71: 1-12. [26] TANG W, HE F, LIU Y, et al. DATFuse: Infrared and visible image fusion via dual attention transformer [J]. IEEE Transactions on Circuits and Systems for Video Technology, 2023, 33(7): 3159-72. [27] TANG L, YUAN J, MA J. Image fusion in the loop of high-level vision tasks: A semantic-aware realtime infrared and visible image fusion network [J]. Information Fusion, 2022, 82: 28-42.

[28] CHEN X, HE K. Exploring simple siamese representation learning; proceedings of the Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, F, 2021 [C].

[29] LIU Y, ZHU H, LIU M, et al. Rolling-Unet: Revitalizing MLP’s Ability to Efficiently Extract Long-Distance Dependencies for Medical Image Segmentation; proceedings of the Proceedings of the AAAI Conference on Artificial Intelligence, F, 2024 [C].   
[30] MA J, ZHOU Y. Infrared and visible image fusion via gradientlet filter [J]. Computer Vision and Image Understanding, 2020, 197: 103016.   
[31] LU M, JIANG M, KONG J, et al. LDRepFM: a real-time end-to-end visible and infrared image fusion model based on layer decomposition and reparameterization [J]. IEEE Transactions on Instrumentation and Measurement, 2023, 72: 1-12. [32] LI H, XU T, WU X-J, et al. Lrrnet: A novel representation learning guided fusion network for infrared and visible images [J]. IEEE transactions on pattern analysis and machine intelligence, 2023, 45(9): 11040-52.   
[33] NIE R, MA C, CAO J, et al. A total variation with joint norms for infrared and visible image fusion [J]. IEEE Transactions on Multimedia, 2021, 24: 1460-72. [34] LI S, HONG R, WU X. A novel similarity based quality metric for image fusion; proceedings of the 2008 International Conference on Audio, Language and Image Processing, F, 2008 [C]. IEEE.   
[35] XYDEAS C S, PETROVIC V. Objective image fusion performance measure [J]. Electronics letters, 2000, 36(4): 308-9.   
[36] HAN Y, CAI Y, CAO Y, et al. A new image fusion performance metric based on visual information fidelity [J]. Information fusion, 2013, 14(2): 127-35.

YAN Zhilin, born in 1998, postgraduate. His main research interests include deep learning and image fusion.

![](images/11c6e5096aaf40b74735762c85b694d262b5926b0c1eb0dfc5bada45711da7b3.jpg)

![](images/638978ceea5759ca747e5174dd47a2c8b03277a38996500134aa30ac4350743b.jpg)

NIE Rencan, born in 1982, Ph.D, professor, doctoral supervisor. His main research interests include neural networks, image processing and machine learning.

![](images/4effedba41e93d988106485d9eb1c70987372deb9aea91812ce7d00852d72ffb.jpg)