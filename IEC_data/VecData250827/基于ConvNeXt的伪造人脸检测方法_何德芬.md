# 基于ConvNeXt的伪造人脸检测方法

# 何德芬　江　倩　金　鑫　冯　明　苗圣法　易华松

（云南大学软件学院　昆明　650504）  
（跨境网络空间安全教育部工程研究中心（云南大学）　昆明　650504）  
（291087273 $\textcircled{ a}$ q．com）

# Fake　Face　Detection　Method　Based　on　ConvNeXt

He　Defen，Jiang　Qian，Jin　Xin，Feng　Ming，Miao　Shengfa，and　Yi　Huasong（Schol　of　Software，Yunan　University，Kunming650504）（Enginering　Research　Center　of　Cyberspace，Yunan　University，Kunming650504）

Abstract　 The　fake　images　generated　by　dep　generative　models　are　becoming　increasingly realistic，surpasing　the　human　eye’s　ability　to　detect　them．These　models　have　become　new　tols for　ilegal　activities，such　as　fabricating　lies　and　creating　public　opinion．Although　curent researchers　have　proposed　many　detection　methods　to　detect　fake　images，their　generalization ability　is　typicaly　limited．To　adres　this　isue，we　proposed　a　fake　face　detection　method　based on　ConvNeXt．Firstly，we　ad　a　PSA（polarization　self－atention）module　after　the　second　and　third downsampling　modules　of　ConvNeXt，enhancing　the　network’s　spatial　and　chanel　atention performance．Secondly，a　RIB（rich　imformation　block）is　designed　at　the　end　of　ConvNeXt　to enrich　the　information　learned　by　the　network．The　information　is　procesed　through　this　module before　final　clasification．Furthermore，the　los　function　used　in　network　training　is　a　combination of　CrosEntropy　los　and　KL（Kulback－Leibler）divergence．Extensive　experiments　on　the　curent mainstream　fake　face　datasets　demonstrate　that　our　method　surpases　al　comparative　methods　in acuracy　and　generalization　on　the　F $^ { + + }$ C23dataset

Key　words　neural　network；dep　learning；fake　face；feature　extraction；fake　image　detection摘　要　由深度生成模型生成的虚假图像越发逼真，这些图像已经超越了人眼的识别能力．这种模型已成为编造谎言、制造舆论等非法活动的新工具．虽然当前研究者已经提出了很多检测方法检测伪造图像，但泛化能力普遍不高，因此，提出了一种基于 ConvNeXt的伪造人脸检测方法．首先在ConvNeXt的第2个和第3个下采样模块后添加极化自注意（polarization　self－atention，PSA）模块，使网络具有空间注意力和通道注意力的性能．其次在ConvNeXt的尾部设计一个信息富余模块（rich　imformation　block，RIB），以丰富网络学习到的信息，通过该模块对信息进行处理后再进行最终的分类．此外，网络训练使用的损失函数是交叉熵损失与 KL（Kulback－Leibler）散度的结合．在当前主流的伪造人脸数据集上作了大量的实验，实验结果表明该方法在F ＋＋高质量数据集上无论是准确率还是泛化性都超过所有对比方法

关键词　神经网络；深度学习；伪造人脸；特征提取；伪造图像检测

中图法分类号 TP391

# 1　概 述

随着深度伪造技术的发展，许多基于深度学习的伪造图像检测方法被广泛提出．当前研究者们根据伪造图像的不同类型从不同的角度对伪造图像检测进行了探索，提出了基于空间域和频率域等各具特色的检测方法．在这些方法中，结合图像的空间信息和频率信息已经成为最常用的方法

# 1．1 基于特殊伪造缺陷的检测方法

由于当前图像生成方法固有的缺陷，使伪造图像存在一些视觉痕迹或瑕疵，使用针对这些瑕疵设计的检测模型识别和检测这些痕迹，可以实现伪造图像检测，如基于视觉伪影的检测方法、基于生物特征的检测法等

在人脸伪造检测中，通常情况下人脸交换的伪造图像有2个来自不同源的图像合成，一个来自源图像，另一个来自目标图像．基于此，Sun等人［1］提出了一种基于源图像和目标图像之间纹理差异的网络，它由1个共享的编码器和2个解码器组成一些伪造方法是将生成的人脸添加到原始图像的人脸上，导致拼接边界不一致．为解决这个问题，Li等人［2］提出了一种人脸X射线表示方法——FaceX－ray，该方法通过计算面部 X射线，在训练过程中避免使用任何最先进的面部处理方法生成虚假图像，从而使得训练后的模型具有很好的泛化能力．Afchar等人［3］关注介观性质，提出了2个网络Meso－4和 MesoInception－4，它们的层数较少且只使用了卷积操作．彭舒凡等人［4］观察到生成的图像会存在伪影，于是构建了一种提取图像细粒度特征的检测网络．该网络通过多分支网络以充分学习图像的细粒度特征，并结合数据增强的方式提高模型对细粒度特征的鲁棒性．张亚等人［5］提出了一种专用于检测由生成式对抗网络（generativeadversarial　network，GAN）生成的图像网络，先使用高斯滤波器对图像预处理以获得图像的高频信息，后将处理后的图像输入到自动编码器提取特征

生物的生理特征都是独特且难以复制的，这种独特性为研究者提供了一个有利途径．Li等人［6］观察到生成的视频缺乏眨眼的视频帧，因此，先提取每只眼睛对应的区域，形成特定的序列，然后使用长期循环卷积网络（long－term　recurentconvolutional　networks，LRCN）模型量化视频中每一帧的眼睛睁开程度，以检测眼睛是否眨眼，从而判别图像真假．由于面部血液随心跳的波动，正常的心跳节奏会被深度伪造技术（DepFake）打乱甚至完全打乱，因而 Qi等人［7］通过监测肤色的最小周期性变化，设计了一种放大心律信号频率的双时注意力检测网络

# 1．2 基于深度学习的检测方法

基于深度学习的图像伪造检测方法在应对不断演进的图像伪造技术方面表现出卓越的潜力．这些方法利用卷积神经网络（convolutional　neuralnetwork，CNN）等深度学习架构，通过学习大量的真实和伪造图像，能够高效地捕捉图像中微妙的特征和痕迹

为寻找一种检测假照片的方法，Liu等人［8］通过对真脸和假脸的研究得到了2个重要的发现：一是假脸的纹理与真脸有本质区别；二是全局纹理统计对图像编辑具有更强的鲁棒性，可以迁移到不同的数据集．基于上述观察，他们提出 了Gram－Net，利用全局图像纹理表示实现图像检测，利用图像分割技术让网络模型先精确标记出图像中被篡改的部分．Zhao等人［9］提出了一种多注意力网络（multi－atention　network，MAT）．MAT利用多注意力模块和纹理增强模块生成多个注意力图并提取纹理特征．此外，在不同的模块提取到不同的特征图之后，嵌入了双分支注意力池化融合注意力图和纹理图．Luo等人［10］利用图像的空间信息提出了一种基于 Xception的双流网络模型．在此双流网络的一个分支中，使用空域富模型（spatial　rich　model，SRM）提取图像的高频信息，SRM 是数字隐写中常用的一种方法；在另一个分支中使用 Xception网络提取图像的低频纹理信息

真假图像之间的差异也可以在频域上体现出来．在基于频域的伪造检测中，通常需要先用离散傅里叶变换（discrete　Fourier　transform，DFT）和离散余弦变换（discrete　cosine　transform，DCT），将图像从空间域变换到频域．基于DFT，Dural 等人［11］提出了一种由2个主要块组成的检测网络，其中一种用于提取特征，另一种则用于区分图像的真伪．通过对真假图像进行傅里叶模数分析，黄珊珊等人［12］提出了一种基于图像频谱分析的方法．在基于光谱信息的伪造检测方法中，图像的相位谱往往被忽略，它可以保留图像的边缘和整体结构信息．因此，Liu等人［13］提出了一种新的空间相位浅层学习 （spatial　phase　shalow　learning，SPSL）方法．幅度和相位信息最早由 Wang等人［14］引入伪造图像检测领域中，对区分图像的高频和低频信息起到重要作用．Qian等人［15］根据图像频带对图像进行分割，然后计算分割后图像块的局部频率，最后根据得到的频率差值对图像进行分类．由于基于图像空域和频域提取的图像特征具有互补性，因此许多结合图像空域和频域的伪造图像检测方法相继被提出．Masi等人［16］提出了一种双分支循环网络，一个分支用于提取图像的空间信息，另一个分支用于使用高斯深度拉普拉斯算子增强频率．当前很多检测模型致力于模型设计，通常缺乏通用性，所以Deng等人［17］将EficientNet和Transformer级联，其中EficientNet作为特征提取器，Transformer作为分类器

深度学习网络已被用于图像取证，伪造图像检测方法的准确率也在逐渐升高，但是泛化性低是当前研究普遍存在的挑战．因此，本文以ConvNeXt［18］为基础网络，在此基础上进行改进优化，主要目的就是提高网络模型的泛化能力．该工作是在尽量保持网络准确率不下降的情况下提高网络的泛化性．先在ConvNeXt网络的第2个和第3个下采样模块后分别加1个空间金字塔注意力（spatial　pyramid　atention，SPA）块，以提高网络的通道学习能力和空间学习能力．其次在网络的尾部增加了本文设计的 RIB（rich　imformationblock）块对最后用于分类的信息作进一步特征提取．网络训练使用的损失函数是交叉熵损失和 KL（Kulback－Leibler）散度组合损失函数．在人脸数据集上的实验表明本文方法在高质量数据集上优于所有对比方法

# 2 基于ConvNeXt的检测方法设计

为了提高检测方法的泛化性，本文方法的主要目的就是在保证域内准确率不降低的情况下，提高域外的准确率．这一目标的背后蕴含着对机器学习模型更全面、更稳健的应用需求，特别是在面对多变和未知数据时传统模型的泛化性往往受到挑战．为了实现在特定领域内准确率的保持，本文注重在训练过程中随时关注网络在域内与域外的表现情况，确保方法在原有领域的性能水平不会受到削弱．这一步骤旨在构建一个坚实的基础，使模型能够在熟悉的环境中取得高准确率，为后续的泛化性提升奠定基础

# 2．1 网络模型结构

随着卷积神经网络在视觉领域的快速发展，Transformer［19］这一强大的模型在自然语言处理领域被提出．传统的卷积神经网络专注于图像的局部信息，而由于 Transformer加入了多头注意力，可以关注到图像的全局信息．Transformer在自然语言处理领域取得极大成功后，Dosovitskiy等人［20］将其应用到计算机视觉领域，提出了 ViT（vision　Transformer），自此，ViT很快超越了传统的卷积神经网络并成为主流．为探索 Transformer的内在机制，Liu等人［21］以 ResNet为探究的起点，逐步模仿Transformer改进网络，包括参数设置、激活函数的选择等方面．在此过程中，他们提出了ConvNeXt系列网络，其在可拓展性与精确度方面均超过了Transformer，且因为它是一个纯的卷积神经网络模型，所有其依然保留了卷积神经网络的简单与高效．在此工作中，ConvNext－Tiny（ConvNeXt系列网络中的一种）作为基础网络框架，通过对此网络的改进，使得其在伪造人脸检测任务中有更好的表现．最终的网络整体架构如图1所示：

![](images/99d15dab0a5f2ef54b29f74007f83c85992646671a6e36d6d68459419a22d3d6.jpg)  
图1　网络整体架构

# 2．2 PSA

卷积神经网络中的注意力机制在提高网络性能方面非常受欢迎，Liu等人［22］通过研究发现，在图像分类、目标检测、语义分割等任务中，通道注意力和空间注意力的组合与单一的通道注意力相比并没有显示出组合的优势．基于此，作者提出了一个即插即用的注意力机制——极化自注意力（polari－zation　self－atention，PSA）．PSA 有2种形式：一种是将通道注意力与空间注意力并行（如图2所示），另一种则是将通道注意力与空间注意力串行PSA采用了极化滤波，即在通道上的维度为输入通道数的一半，在空间维度上保持不变，这在一定程度上减少了维度降低带来的信息损失．在此网络中，如图1所示，在第2个和第3个下采样模块后加入PSA块，使得该网络同时具有提取图像空间信息和通道信息的能力

![](images/593e2b9552eed0749c315b35055049f6cf020d5acd5a93095d7ee9b33ca3f7dd.jpg)  
图2　并行PSA模块

# 2．3 RIB

一般地，平均池化适用于考虑图像整体特征的任务中，提取纹理特征适用于强调图像局部信息的任务中，在此任务中，将平均池化与卷积提取图像纹理特征功能相结合，本文提出的 RIB块使得网络既关注到图像的整体信息又关注到图像的局部信息．RIB块位于网络尾部，有利于网络前中段提取到的图像信息不被减弱．该模块的结构如图3所示，模块的输入分别进入到2个分流：一个分支是平均池化分流，平均池化的作用是在每个池化区域内取像素点的平均值作为输出，这有助于平滑图像、降低噪声，从而得到的特征图不易受图像局部变化的影响；另一个分支是纹理信息提取分流，以帮助理解图像的结构、组织和特征，从而实现对图像内容更深入的分析和理解．这也有助于提取图像的细微特征，使得网络对图像的纹理特征更加敏感．此外，RIB除了2个分支外，还加入了残差连接，使得网络不会因为加入了此操作而造成特征图信息的损失

![](images/322d9a354b4f20a71bc8c7d26b4e0d6c76c950daca3fd02365a529c95f21bbd4.jpg)  
图3　RIB模块结构

# 2．4 损失函数

交叉熵损失是一种用于度量2个概率分布之间差异的损失函数．在二分类问题中，它可以衡量模型输出的概率分布与实际标签的分布之间的差异．优化交叉熵有助于使模型更好地拟合训练数据，并提高分类准确性．KL散度同样也是衡量2个概率分布之间的相似性或差异性．在混合使用时，KL散度可以帮助模型更加关注正确类别的分类，促使模型更加专注于对正确类别的准确性

考虑到交叉熵损失和 KL散度的相关特性，在网络的训练过程中，将交叉熵损失和 KL散度结合作为损失函数，可以使模型更全面地学习特征，既关注准确分类又关注概率分布的一致性，从而提高模型对正负样本的区分能力．如式（1）所示，使用1个参数 $\partial$ 平衡两者.表1所示为不同 $\partial$ 下的AUC比较，最终选择0.2作为 $\partial$ 的值.

$$
C K - L o s s = C r o s s E n t r o \phi y L o s s + \partial \times
$$

$$
K L D i v L o s s = - \sum _ { i } \rlap { / } D ( x _ { i } ) \log q ( x _ { i } ) +
$$

$$
\partial \times \sum _ { i } { \phi \left( x _ { i } \right) } \log \biggl ( \frac { \not p \left( x _ { i } \right) } { q \left( x _ { i } \right) } \biggr ) =
$$

$$
\partial \times \sum _ { i } { p ( x _ { i } ) \log p ( x _ { i } ) } - ( 1 + \partial ) \times
$$

$$
\sum _ { i } ^ { } { p \left( { x _ { i } } \right) \log q \left( { x _ { i } } \right) } ,
$$

其中CrosEntropyLos 表示交叉熵损失，KLDivLos表示 KL散度， ${ \mathbf { \nabla } } p \left( { { x } _ { i } } \right)$ ）表示目标分布， $q \left( \boldsymbol { \mathscr { x } } _ { i } \right)$ ）表示训练得到的分布.

表1　不 同 $\partial$ 在 $\mathbf { F } \mathbf { F } + + \mathbf { C } 2 3$ 数据集上的 $A U C$ 比较  

<html><body><table><tr><td>a</td><td>FF++C23</td></tr><tr><td>0.0</td><td>0.9986</td></tr><tr><td>0.1</td><td>0.9981</td></tr><tr><td>0.2</td><td>0.9997</td></tr><tr><td>0.3</td><td>0.996 0</td></tr></table></body></html>

# 3 实验结果与分析

# 3．1 公共实验数据集

F ＋＋（FaceForensics $+ + )$ ）是一个用于人脸图像伪造检测的数据集，也是当前广泛使用的公开数据集之一．其数据主要由4种类型的数据组成，分 别 是 Face2Face，DepFakes，FaceSwap，NeuralTextures．Face2Face和 FaceSwap 是基于计算机图形学的方法，DepFakes和 NeuralTex－tures是基于学习的方法．其中 NeuralTextures是由GAN生成的，在同一压缩率上，目前的检测方法在该子数据集上的表现一般都差于前3种子数据集．此外，考虑到在网络上传播的视频和图像一般都经过压缩操作，这会导致数据有一定程度的失真，因此，一般会对 $\mathrm { F F } + +$ 伪造的视频裁剪而来的图像进行压缩．根据压缩率的不同，从而有当前的低压缩率数据集 $\mathrm { ( F F + + C 2 3 ) }$ ）、高压缩率数据集 $( \mathrm { F F ^ { + } \mathrm { + } C 4 0 } )$ ）．大量研究表明在2种不同压缩率的数据集上网络模型的表现也有差异，一般模型对低压缩率的图像表现较好，高压缩率的图像对当前的多数模型仍然具有很大的挑战．图4展示了 $\mathrm { F F } + +$ 数据集中4种不同伪造方法伪造的图像，第1列表示 $\mathrm { F F ^ { + + } \mathrm { + C 2 3 } }$ 数据集图像，第2列表示 $\mathrm { F F ^ { + + } \mathrm { C 4 0 } }$ 数据集图像

![](images/63a602c7b2acaab2a7eb1682343685f455ccba9337fbbf1a1db7e08a6a2db44a.jpg)  
图4　F ＋＋数据集示例

在此方法的实验中，还使用深度人脸提取数据集（Cele－DF）作为泛化性实验的测试集，该数据集也是公开数据集．Cele－DF的原始视频由YouTube不同性别、年龄和种族的名人公开的视频剪辑而成，伪造的视频是使用改进的DepFake合成方法生成的．因此，与 $\mathrm { F F } + +$ 等数据集相比，Cele－DF合成的视频视觉质量有了很大的提高，较明显的视觉伪影显著减少，Celeb－DF对现有的大多数检测方法都是一个很大的挑战 $\mathrm { F F } + +$ 数据集与

Cele－DF数据集的部分示例如图5所示，在本文方法中， $\mathrm { F F } + +$ 数据集用来作域内实验，即训练集、测试集都是来自于 $\mathrm { F F } + + .$ ．Cele－DF数据集仅用于域外实验，即训练集和测试集来自2种不同的域，使用Cele－DF作测试集

![](images/57a262cb91bd37cdd45eaf8c17b4839e0c59ceebfc4f9fa368511f6b294d3cc6.jpg)  
图5　Cele－DF数据集示例

# 3．2 评价指标

AUC（area　under　curve）是一种用于评估二分类模型性能的指标，指的是 ROC（receiver　operat－ing　characteristic　curve）曲线下的面积．其数值范围在 $0 . 0 { \sim } 1$ 之间， $A U C$ 的计算涉及对 ROC曲线进行积分，ROC曲线的横轴表示的是 $F P R$ （falsepositive　rate）（如式（2）所示），纵轴表示的是 ${ T P R }$ （true　positive　rate）（如式（3）所示）

$$
F P R = \frac { F P } { F P + T N } ,
$$

$$
T P R = \frac { T P } { T P + F N } ,
$$

FPR表示正样本中被分类器预测类别为负样本的比例， $T P R$ 表示正样本中被分类器预测类别为正的比例.其中 $T P$ 表示测试数据集的正样本中正预测的数量， $F P$ 表示测试数据集的负样本中正预测的数量， $T N$ 表示测试数据集的正样本中正预测的数量， $F N$ 表示测试数据集的正样本中负预测的数量.AUC的值是对 ROC曲线的积分，计算如式（4）所示：

$$
A U C = \int _ { 0 } ^ { 1 } y \mathrm { d } x , \quad
$$

其中 $y$ 表示ROC曲线纵轴的 $T P R , x$ 表示 ROC曲线的横轴的 $F P R$ .

# 3．3 对比实验与分析

在本节中将对本文模型进行实验，并与当前领先的先进模型进行比较，以验证本文方法的有效性

$\mathrm { F F } + +$ 数据集的4个子数据集代表了不同的情境和应用场景，在这些不同的子数据集上进行实验可以验证模型性能表现．本文在 $\mathrm { F F } + + \mathrm { C } 2 3$ （ $\mathrm { F F } + +$ 经压缩后的高质量数据集）的4个子数据集上作了一系列的实验，实验结果如表2所示可以看出在 $\mathrm { F F } + + \mathrm { C } 2 3$ 数据集的2个子集DepFakes和Face2Face上，本文模型显著优于现有的 方 法，包 括 Steg．Features［11］、Cozolino 等人［23］、Rahmouni等人［24］、Bayar等人［25］、Nirkin等人［26］、MHA（EficientNetV2S－ViT）［17］．结果表明，本文模型在这2个具有挑战性的数据集中，对于伪造图像的检测具有更高的准确率．然而，在 $\mathrm { F F ^ { + + } + C 2 3 }$ 的另外2个子集——FaceSwap和NeuralTextures上，本文模型的表现并未超越MHA（EficientNetV2S－ViT）［17］．这可能是由于这2个子集包含了不同类型的图像伪造技术，导致模型在这方面的泛化能力受到限制．尽管如此，本文模型在这4个子集上的整体表现仍然是竞争性的，特别是在处理 DepFakes和 Face2Face这样的复杂伪造技术时．这一发现突显了本文方法在特定条件下对伪造图像检测的有效性，并为未来的研究提供了有价值的参考

在子数据集上实验后，本文又将 $\mathrm { F F } { + } +$ 的4个子数据集等比例混合，这可以进一步评估本文模型的学习能力．表3所示为本文方法在域内与先进方法对比的实验结果．在此实验中，使用 $\mathrm { F F } + +$ 的2种不同的压缩率的图像作为数据集， $\mathrm { F F ^ { + + } \mathrm { + C 2 3 } }$ 是使用低压缩率压缩后的高质量数据集， $\mathrm { F F ^ { + + } \mathrm { C 4 0 } }$ 是使用高压缩率压缩后的低质量数据集．此外，在评价指标的选取上，本文使用 $A U C$ 和AC 这2个评价指标共同评价本文模型的效果．在对比方法的选取上，本文选取的方法有基于频域与基于空间域等设计的，这种选取方式有利于更全面地评估本文模型．由表3也可以看出，在 $\mathrm { F F ^ { + + } \mathrm { C 2 3 } }$ 上本文方法表现出最高的 $A U C$ 和 $A C C$ ，但在高压缩率的低质量数据 $\mathrm { F F ^ { + + } + C 4 0 }$ 上本文方法没有取得最佳结果，说明本文方法在低质量图像上的指标还有一定的提升空间

表2　在 $\mathbf { F } \mathbf { F } + + \mathbf { C } 2 3$ 的4个子数据集上采用不同方法的AC  

<html><body><table><tr><td>方法</td><td>DeepFakes</td><td>Face2Face</td><td>FaceSwap</td><td>NeuralTextures</td></tr><tr><td>Steg.Features[11]</td><td>0.736 0</td><td>0.737 0</td><td>0.689 0</td><td>0.6303</td></tr><tr><td>Cozzolino等人[23]</td><td>0.8540</td><td>0.6780</td><td>0.7370</td><td>0.7800</td></tr><tr><td>Rahmouni等人[24]</td><td>0.8540</td><td>0.6420</td><td>0.5630</td><td>0.6000</td></tr><tr><td>Bayar等人[25]</td><td>0.8450</td><td>0.7370</td><td>0.8250</td><td>0.7060</td></tr><tr><td>YuvalNirkin等人[26]</td><td>0.9450</td><td>0.8030</td><td>0.845 0</td><td>0.7400</td></tr><tr><td>MHA(EfficientNetV2S-ViT)[17]</td><td>0.9838</td><td>0.9919</td><td>0.9939</td><td>0.9443</td></tr><tr><td>本文</td><td>0.9903</td><td>0.992 4</td><td>0.9928</td><td>0.932 6</td></tr></table></body></html>

表3　在F ＋＋数据集上不同方法的AUC和 $A C C$ 对比  

<html><body><table><tr><td rowspan="2">方法</td><td colspan="2">FF++C23</td><td colspan="2">FF++C40</td></tr><tr><td>AUC</td><td>ACC</td><td>AUC</td><td>ACC</td></tr><tr><td>EfficientNet-NS-B3[27]</td><td>0.9920</td><td>0.9680</td><td>0.8960</td><td>0.8720</td></tr><tr><td>FDFL[28]</td><td>0.993 0</td><td>0.9669</td><td>0.924 0</td><td>0.8900</td></tr><tr><td>PEL[29]</td><td>0.993 2</td><td>0.9763</td><td>0.9428</td><td>0.905 2</td></tr><tr><td>MAT[9]</td><td>0.992 9</td><td>0.9760</td><td>0.904 0</td><td>0.886 9</td></tr><tr><td>F3Net[15]</td><td>0.987 0</td><td>0.9752</td><td>0.933 0</td><td>0.9040</td></tr><tr><td>Two-Stream-Net[10]</td><td>0.9918</td><td>1</td><td>0.8659</td><td>1</td></tr><tr><td>Add-Net[30]</td><td>0.977 4</td><td>0.9678</td><td>0.9101</td><td>0.8750</td></tr><tr><td>RECCE[31]</td><td>0.993 2</td><td>0.9706</td><td>0.950 2</td><td>0.9103</td></tr><tr><td>本文</td><td>0.998 8</td><td>0.990 2</td><td>0.8404</td><td>0.8200</td></tr></table></body></html>

在评估模型的泛化性实验中，本文进行了2组实验，一组是因为 $\mathrm { F F } + +$ 数据集有4个不同的场景和环境子数据集，所以可以仅使用 $\mathrm { F F } + +$ 数据集就能测试模型的泛化性．实验结果如表4所示，从表4可以看出，在以Face2Face和FaceSwap为训练集．其他数据集为测试集时，与其他方法相比本文方法也具有明显的优势．此外，以 $\mathrm { F F ^ { + + } \mathrm { + C 2 3 } }$ 为训练集，Celeb－DF为测试集验证模型的泛化性，实验结果如表5所示，可以看出本文方法在准确率和泛化性指标上都优于对比方法

表4　采用不同方法在 $\mathbf { F } \mathbf { F } { + } + \mathbf { \Gamma }$ 跨数据集上的AUC比较  

<html><body><table><tr><td rowspan="2">方法</td><td rowspan="2">训练集</td><td colspan="4">测试集</td></tr><tr><td>DeepFake</td><td>Face2Face</td><td>FaceSwap</td><td>NeuralTextures</td></tr><tr><td>EfficientNet-B4[32]</td><td rowspan="5">Face2Face</td><td>0.845 2</td><td>0.9920</td><td>0.5814</td><td>0.6371</td></tr><tr><td>MAT[9]</td><td>0.8615</td><td>0.9913</td><td>0.6014</td><td>0.6459</td></tr><tr><td>Two-Stream-Net[10]</td><td>0.892 3</td><td>0.9910</td><td>0.6130</td><td>0.6477</td></tr><tr><td>DCL[33]</td><td>0.9191</td><td>0.9921</td><td>0.5958</td><td>0.6667</td></tr><tr><td>本文</td><td>0.8429</td><td>0.9998</td><td>0.703 2</td><td>0.6824</td></tr><tr><td>EfficientNet-B4[32]</td><td rowspan="5">FaceSwap</td><td>0.692 5</td><td>0.6769</td><td>0.9989</td><td>0.4861</td></tr><tr><td>MAT[9]</td><td>0.6413</td><td>0.6639</td><td>0.9967</td><td>0.5010</td></tr><tr><td>Two-Stream-Net[10]</td><td>0.7021</td><td>0.6872</td><td>0.9985</td><td>0.499 1</td></tr><tr><td>DCL[33]</td><td>0.748 0</td><td>0.6975</td><td>0.999 0</td><td>0.5260</td></tr><tr><td>本文</td><td>0.6014</td><td>0.773 4</td><td>0.999 0</td><td>0.542 2</td></tr></table></body></html>

表5　采用不同方法在跨数据集上的AUC比较  

<html><body><table><tr><td>方法</td><td>FF++C23</td><td>Celeb-DF</td></tr><tr><td>Mesolnception4[3]</td><td>0.8300</td><td>0.5360</td></tr><tr><td>Multi-task[34]</td><td>0.7630</td><td>0.5430</td></tr><tr><td>F3Net[15]</td><td>0.9810</td><td>0.6517</td></tr><tr><td>EfficientNet-B4[32]</td><td>0.9970</td><td>0.6429</td></tr><tr><td>Two Branch[16]</td><td>0.9318</td><td>0.7341</td></tr><tr><td>MAT[9]</td><td>0.9980</td><td>0.674 4</td></tr><tr><td>M2TR[35]</td><td>0.9950</td><td>0.6570</td></tr><tr><td>EfficientNet-NS-B3[27]</td><td>0.9920</td><td>0.7365</td></tr><tr><td>本文</td><td>0.998 8</td><td>0.7614</td></tr></table></body></html>

# 3．4 消融实验与分析

消融实验是科研领域中一种强有力的实验手段，其核心思想在于通过有目的地剔除系统中的某些部分，以揭示这些部分在整个系统中的作用和影响．在机器学习领域，特别是在复杂的深度神经网络中，消融实验被广泛用来分析模型的鲁棒性、解释性和泛化能力．通过有选择性地去除网络的某些层、节点或特征，研究人员能够洞察模型对不同输入和变化的响应．这种分析有助于理解模型内部是如何处理信息的，哪些部分对于模型的性能至关重要，从而为模型的改进和优化提供指导本文通过逐次增加功能模块或者改变基础网络的一些组成部分观察相应改变对分类性能的影响．实验结果如表6所示，实验在 $\mathrm { F F } + +$ 数据集上验证域内有效性，在Celeb－DF数据集上验证域外有效性．从表6可以看出，每次对原有模型的修改，在保持域内AUC指标几乎保持不变甚至有所提升的情况下，域外实验的AUC指标逐步升高，所以每次的改进对网络整体都是有效的

表6　在不同数据集上关于AUC比较的消融实验  

<html><body><table><tr><td>方法</td><td>FF++C23</td><td>Celeb-DF</td></tr><tr><td>ConvNeXt-tiny</td><td>0.8300</td><td>0.5360</td></tr><tr><td>ConvNeXt-tiny+SPA</td><td>0.7630</td><td>0.5430</td></tr><tr><td>ConvNeXt-tiny+SPA+ CK-Loss</td><td>0.9810</td><td>0.6517</td></tr><tr><td>ConvNeXt-tiny+SPA+ CK-Loss+SPA</td><td>0.997 0</td><td>0.642 9</td></tr><tr><td>ConvNeXt-tiny+SPA+ CK-Loss+SPA+RIB</td><td>0.9988</td><td>0.7614</td></tr></table></body></html>

# 4　结　　语

本文探索了当前伪造人脸检测模型的设计准则，分析了当前检测模型存在的局限性，在提升网络的泛化性并保持网络在域内表现不降低的情况下，以ConvNeXt为基础网络，通过增加模块和对训练损失函数的调整提升网络的性能．大量实验表明本文方法达到了预期效果，在泛化性评估中，将基础网络的AUC值从0．710　9提升到0．761　4．因为每次对网络的改进都是为了提高对网络的泛化性，相较于当前流行的一些方法，本文方法在泛化性上具有明显优势．然而，通过分析相关的实验结果，可以明显看出本文设计的网络在高质量数据集 $\mathrm { ( F F ^ { + } + C 2 3 ) }$ ）上的各项指标都高于所有对比方法，但在低质量数据集 $( \mathrm { F F ^ { + } + C 4 0 } )$ ）上的实验却和当前先进的方法有一定的距离．因此，在后续的研究中，还需继续探索如何提高网络模型在低质量数据集上的表现

# 参 考 文 献

［1］ Sun　Xinwei，Wu　Botong，Chen　Wei．Identifying　invarianttexture　violation　for　robust　DepFake　detection［J］．arXivpreprint，arXiv：2012．10580，2020  
［2］ Li　Lingzhi，Bao　Jianmin，Zhang　Ting，et　al．Face　X－ray　formore　general　face　forgery　detection［C］/Proc　of　the　IEEE/CVF　Conf　on　Computer　Vision　and　Patern　RecognitionPiscataway，NJ：IEEE，2020：501－5010  
［3］ Afchar　D，Nozick　V，Yamagishi　J，et　al．Mesonet：Acompact　facial　video　forgery　detection　network［C］/Procof　2018IEEE　Int　Workshop　on　Information　Forensics　andSecurity（WIFS）．Piscataway，NJ：IEEE，2018：1－7  
［4］ 彭舒凡，蔡满春，刘晓文，等．基于图像细粒度特征的深度伪造检测算法［J］．信息网络安全，202 ，2 （1 ）：7 －84  
［5］ 张亚，金鑫，江倩，等．基于自动编码器的深度伪造图像检测方法［J］．计算机应用，2021，41（10）：2985－290  
［6］ Li　Yuezun，Chang　Mingching，Lyu　S．In　ictu　oculi：Exposing　AI　created　fake　videos　by　detecting　eye　blinking［C］/Proc　of　2018IEEE　Int　Workshop　on　InformationForensics　and　Security （WIFS）．Piscataway，NJ：IEEE，2018：1－7  
［7］ Qi　Hua，Guo　Qing，Juefei－Xu　F，et　al．Deprhythm：Exposing　DepFakes　with　atentional　visual　heartbeatrhythms ［C］/Proc　of　the　28th　ACM　Int　Conf　onMultimedia．New　York：ACM，2020：4318－4327  
［8］ Liu　Zhengzhe，Qi　Xiaojuan，Tor　P　H　S．Global　textureenhancement　for　fake　face　detection　in　the　wild［C］/Procof　the　IEEE/CVF　Conf　on　Computer　Vision　and　PaternRecognition．Piscataway，NJ：IEEE，2020：8060－8069  
［9］ Zhao　Hanqing，Zhou　Wenbo，Chen　Dongdong，et　alMulti－atentional　DepFake　detection ［C］/Proc　of　theIEEE/CVF　Conf　on　Computer　Vision　and　Patern　RecognitionPiscataway，NJ：IEEE，2021：2185－2194Patern　Recognition （CVPR）．Piscataway，NJ：IEEE，2021：16312－16321  
［1 ］ Dural　R，Keuper　M，Pfreundt　F　J，et　al．UnmaskingDepFakes　with　simple　features［J］．arXiv　preprint，arXiv：191 ．0686，2019  
［12］ 黄珊珊，金鑫，吴楠，等．结合频域信息与对抗网络的虚假图像检测［J］．信息安全学报，2023，8（6）：37－47  
［13］ Liu　Hongu，Li　Xiaodan，Zhou　Wenbo，et　al．Spatial－phase　shalow　learning：Rethinking　face　forgery　detectionin　frequency　domain［C］/Proc　of　the　IEEE/CVF　Conf　onComputer　Vision　and　Patern　Recognition．Piscataway，NJ：IEEE，2021：72－781  
［14］ Wang　Gaojian，Jiang　Qian，Jin　Xin，et　al．MC－LCR：Multimodal　contrastive　clasification　by　localy　corelatedrepresentations　for　efective　face　forgery　detection ［J］Knowledge－Based　Systems，202 ，250：10914  
［15］ Qian　Yuyang，Yin　Guojun，Sheng　Lu，et　al．Thinking　infrequency：Face　forgery　detection　by　mining　frequency－aware　clues［C］/Proc　of　European　Conf　on　ComputerVision．Berlin：Springer，2020：86－103  
［16］ Masi　I，Kilekar　A，Mascarenhas　R　M，et　al．Two－branchrecurent　network　for　isolating　DepFakes　in　videos［C］ $/ /$ Proc　of　the　16th　European　Conf　on　Computer　VisionBerlin：Springer，2020：67－684  
［17］ Deng　Liwei，Wang　Jiandong，Liu　Zhen．Cascaded　networkbased　on　eficientnet　and　transformer　for　DepFake　videodetection［J］．Neural　Procesing　Leters，2023 ［2025－02－15］．htps：/link．springer．com/article/10．107/s1063－023－1249－6  
［18］ Liu　Zhuang，Mao　Hanzi，Wu　Chaoyun，et　al．A　convnetfor　the　2020s ［C］ $/ /$ Proc　of　the　IEEE/CVF　Conf　onComputer　Vision　and　Patern　Recognition．Piscataway，NJ：IEEE，202 ：1976－1986  
［19］ Vaswani　A，Shazer　N，Parmar　N，et　al．Atention　is　alyou　ned［J］．arXiv　preprint，arXiv：1706．03762，2017  
［20］ Dosovitskiy　A，Beyer　L，Kolesnikov　A，et　al．An　image　isworth $1 6 \times 1 6$ words：Transformers　for　image　recognitionat　scale［J］．arXiv　preprint，arXiv：2010．1929，2020  
［21］ Liu　Ze，Lin　Yutong，Cao　Yue，et　al．Swin　transformer：Hierarchical　vision　transformer　using　shifted　windows［C］/Proc　of　the　IEEE/CVF　Int　Conf　on　Computer　VisionPiscataway，NJ：IEEE，2021：1012－102  
［2 ］ Liu　Huajun，Liu　Fuqiang，Fan　Xinyi，et　al．Polarized　self－atention：Towards　high－quality　pixel－wise　maping ［J］Neurocomputing，202 ，506：158－167  
［23］ Cozolino　D，Pogi　G，Verdoliva　L．Recasting　residual－based　local　descriptors　as　convolutional　neural　networks：An　aplication　to　image　forgery　detection［C］/Proc　of　the5th　ACM　Workshop　on　Information　Hiding　and　MultimediaSecurity．New　York：ACM，2017：159－164  
［24］ Rahmouni　N，Nozick　V，Yamagishi　J，et　al．Distinguishingcomputer　graphics　from　natural　images　using　convolutionneural　networks［C］ $/ /$ Proc　of　2017IEEE　Workshop　onInformation　Forensics　and　Security （WIFS）．Piscataway，NJ：IEEE，2017：1－6  
［25］ Bayer　B，Stamm　M　C．A　dep　learning　aproach　touniversal　image　manipulation　detection　using　a　newconvolutional　layer［C］/Proc　of　the　4th　ACM　Workshopon　Information　Hiding　and　Multimedia　Security．NewYork：ACM，2016：5－10  
［26］ Nirkin　Y，Wolf　L，Keler　Y，et　al．DepFake　detectionbased　on　discrepancies　betwen　faces　and　their　context［J］IEEE　Trans　on　Patern　Analysis　and　Machine　Inteligence，2021，4 （10）：611－6121  
［27］ Xie　Q，Luong　M　T，Hovy　E，et　al．Self－training　with　noisystudent　improves　imagenet　clasification［C］/Proc　of　theIEEE/CVF　Conf　on　Computer　Vision　and　Patern　RecognitionPiscataway，NJ：IEEE，2020：10687－10698  
［28］ Li　Jiaming，Xie　Hongtao，Li　Jiahong，et　al．Frequency－aware　discriminative　feature　learning　supervised　by　single－center　los　for　face　forgery　detection ［C］ $/ /$ Proc　of　theIEEE/CVF　Conf　on　Computer　Vision　and　PaternRecognition．Piscataway，NJ：IEEE，2021：6458－6467  
［29］ Gu　Qiqi，Chen　Shen，Yao　Taiping，et　al．Exploiting　fine－grained　face　forgery　clues　via　progresive　enhancementlearning ［C］/Proc　of　the　AAAI　Conf　on　ArtificialInteligence．Menlo　Park，CA：AAAI，202 ：735－743  
［30］ Zi　Bojia，Chang　Minghao，Chen　Jingjing，et　al．WildDepFake：A　chalenging　real－world　dataset　for　DepFakedetection ［C］/Proc　of　the　28th　ACM　Int　Conf　onMultimedia．New　York：ACM，2020：2382－2390  
［31］ Cao　Junyi，Ma　Chao，Yao　Taiping，et　al．End－to－endreconstruction－clasification　learning　for　face　forgerydetection［C］/Proc　of　the　IEEE/CVF　Conf　on　ComputerVision　and　Patern　Recognition．Piscataway，NJ：IEEE，202 ：413－412  
［32］ Tan　Mingxing，Le　Q．Eficientnet：Rethinking　modelscaling　for　convolutional　neural　networks［C］/Proc　of　IntConf　on　Machine　Learning．New　York：PMLR，2019：6105－614  
［3 ］ Sun　Ke，Yao　Taiping，Chen　Shen，et　al．Dual　contrastivelearning　for　general　face　forgery　detection［C］/Proc　of　theAAAI　Conf　on　Artificial　Inteligence．Menlo　Park，CA：AAAI，202 ：2316－2324  
［34］ Nguyen　H　H，Fang　F，Yamagishi　J，et　al．Multi－tasklearning　for　detecting　and　segmenting　manipulated　facialimages　and　videos［C］/Proc　of　the　10th　2019IEEE　IntConf　on　Biometrics　Theory，Aplications　and　Systems（BTAS）．Piscataway，NJ：IEEE，2019：1－8  
［35］ Wang　Junke，Wu　Zuxuan，Ouyang　W，et　al．M2TR：Multi－modal　 multi－scale　transformers　for　DepFakedetection［C］/Proc　of　the　202 Int　Conf　on　MultimediaRetrieval．New　York：ACM，202 ：615－623

![](images/fb8593aa2f621b8591380f13f4c3d911c8dac7db7754d526b9b56bdefa84dcd9.jpg)

# 何德芬

硕士研究生．主要研究方向为网络安全、计算机视觉、图像伪造检测、图像篡改检测、图像处理  
291087273＠q ．com

![](images/343752d3d39449a6e851f39415edba0607780afedb7aec576a918fca9e2ed1d2.jpg)

# 江　倩

博士，副教授，硕士生导师．主要研究方向为机器学习、图像处理、信息安全、生物信息  
jiangqian＿121＠163．com

![](images/39583db2113b6327ba9d0157d389b68e7af942fc5502337f5b944222d8cfbd7e.jpg)

# 金　鑫

博士，副教授，硕士生导师．主要研究方向为人工神经网络理论与应用、图像处理、遥感信息处理  
xinxin＿jin＠163．com  
冯　明  
硕士研究生．主要研究方向为红外图像彩  
色化、计算机视觉  
1831076737＠163．com

![](images/d052ae6b175736f754b3d7732a340fe2b12cefb7f2afacc278c5c2ae032ef792.jpg)

![](images/16013bcffea88baefef07ac872ec51a94df037387d4a1ae2f38567d5ed713289.jpg)

# 苗圣法

博士，副教授，硕士生导师．主要研究方向为机器学习、智慧物流、智能风控、结构健康监测  
miaosf＠ynu．edu．cn

![](images/8162ca5635cf43b98cadbc06bfb419ee283fc60386a23cc24692f92d41f60562.jpg)

# 易华松

硕士研究生．主要研究方向为计算机视觉、伪造图像检测、图像篡改检测与定位yihuasong＠stu．ynu．edu．cn