# 基于 GradGR 多源特征融合的面部伪造检测方法

韩栋宇1ꎬ郭　 婷2ꎬ杨高明1∗ꎬ朱　 鹏1ꎬ宋一帆1(1.安徽理工大学 计算机科学与工程学院ꎬ安徽 淮南 232001ꎻ2.安徽理工大学 安全科学与工程学院ꎬ安徽 淮南 232001)

摘要:针对当前的面部伪造检测方法在特定伪造操作上表现良好ꎬ但其跨数据集泛化能力存在明显不足的问题ꎬ提出了基于图像梯度引导重建( image gradient－guided reconstructionꎬGradGR) 的面部伪造检测模型ꎮ 该模型在图像重建主干的基础上ꎬ构建了辅助的梯度重建分支ꎮ 通过特征传递机制ꎬ该分支的中间特征被用来引导主干网络聚焦于梯度所揭示的伪造区域ꎮ 此外ꎬGradGR 模型中还包含了多源特征融合(multi－source feature fusionꎬMSFF)模块ꎮ 该模块通过整合编解码器中间特征与双路重建差异ꎬ有效加强了跨层级特征的交互ꎬ并显著提升了特征融合的效率ꎮ 结果表明ꎬGradGR 模型不仅在数据集内均达到了最优水平ꎬ还在跨数据集上较极端初始(extreme inceptionꎬXception)模型的平均准确率提升了 $3 . 2 2 \%$ ꎮ 该模型为面部伪造检测提供了新的研究思路ꎮ

关键词:面部伪造检测ꎻ深度学习ꎻ计算机视觉ꎻ图像重建学习ꎻ图像梯度ꎻ多源特征融合 中图分类号:TP391.4ꎻTP18ꎻTP309 文献标志码:A

引用格式:韩栋宇ꎬ郭婷ꎬ杨高明ꎬ等.基于 GradGR 多源特征融合的面部伪造检测方法[J/ OL].湖北民族大学学报(自然科学版)ꎬ2025ꎬ43(2):1－8.DOI:10.13501 / j.cnki.42－1908 / n.2025.06.018.

# Face Forgery Detection Method Based on Multi－source Features Fusion of GradGR

HAN Dongyu1ꎬGUO Ting2ꎬYANG Gaoming1∗ꎬZHU Peng1ꎬSONG Yifan1 (1.School of Computer Science and EngineeringꎬAnhui University of Science and TechnologyꎬHuainan 232001ꎬChina 2.School of Safety Science and EngineeringꎬAnhui University of Science and TechnologyꎬHuainan 232001ꎬChina)

Abstract: To address the issue that the existing face forgery detection methods performed well on specific forgery operations but had obvious deficiencies in cross－dataset generalization abilityꎬa face forgery detection model based on image gradient－ guided reconstruction (GradGR) was proposed.This model constructed an auxiliary gradient reconstruction branch on top of the original image reconstruction backbone. Through a feature transfer mechanismꎬ the intermediate features of this branch were used to guide the backbone to focus on the forged region revealed by the gradient. In additionꎬa multi－source feature fusion (MSFF) module was included in the GradGR modelꎬwhich effectively enhanced cross－layer feature interactions and markedly improved the efficiency of feature fusion by integrating codec intermediate features with two － way reconstruction differences.The results demonstrated that the GradGR model not only achieved the optimal level within the datasets but also improved the average cross－dataset accuracy by nearly $3 . 2 2 \%$ compared with the extreme inception( Xception) model. This model provided a new research idea for face forgery detection.

Keywords:facial forgery detectionꎻ deep learningꎻ computer visionꎻ image reconstruction learningꎻ image gradientꎻ multi － source feature fusion

随着生成式 对 抗 网 络 ( generative adversarial networkꎬ GAN) 和 变 分 自 编 码 器 ( variational autoencoderꎬVAE)等生成模型的突破性进展ꎬ面部伪造技术已能够生成具有高度视觉逼真度的合成人脸图像ꎮ 攻击者可利用该技术实施假新闻传播、名人形象伪造以及生物特征认证破解等恶意行为ꎬ引发严重的政治、社会及国家安全问题[1]ꎮ 全球社交媒体平台每日新增面部伪造视频超过 20000 条ꎬ其中 $3 7 \%$ 属于恶意伪造内容[2]ꎮ此类技术滥用不仅威胁个人隐私和司法取证可靠性ꎬ更对国家安全构成重大挑战ꎬ这使得面部伪造检测技术

收稿日期:2025－03－27

成为多媒体信息安全领域亟待突破的关键研究方向ꎮ

面部伪造检测任务通常被形式化为 2 分类范式[3－4]ꎮ 早期研究方法主要采用预训练卷积神经网络(convolutional neural networkꎬCNN) 作为主干网络进行人脸真伪判别[5－8] ꎮ 以多注意力 ( multi － attentionꎬMAT)模型[9]为例ꎬ该模型通过分析图像纹理细节特征构建伪造检测框架ꎬ但存在对训练数据中特定伪造痕迹的过拟合现象ꎬ这种现象限制了模型的泛化能力ꎮ 人脸伪造的频率网络(frequency in face forgery networkꎬ${ \mathrm { F } } ^ { 3 } { \mathrm { - } } { \mathrm { N e t } } { \dot { } }$ )模型[10]将特征分析拓展至频域空间ꎬ揭示了真伪样本在频谱能量分布上的统计差异ꎬ然而未能充分挖掘跨频域关联特征ꎮ 现有方法在应对伪造痕迹低信噪比的复杂样本时表现出明显局限性ꎬ特别是在异常特征或边缘差异呈现微幅波动却具有判别性的复杂场景中ꎬ过度依赖单一模态特征(如空域纹理、频域分量或噪声分布等)而缺乏多模态特征协同机制ꎬ往往导致模型难以找到最优决策边界ꎮ

近年来ꎬ一些研究开始尝试超越传统2 分类范式ꎬ通过构建多任务学习框架来捕获更本质的伪造特征表征[11－13] ꎮ 例如ꎬ重建分类学习(reconstruction－classification learningꎬRECCE)模型[11] 引入图像重建任务ꎬ通过分析重构误差中的异常模式定位伪造痕迹ꎻ差异引导重建学习( discrepancy－guided reconstruction learningꎬDisGRL)模型[12]结合空域卷积推理与图结构推理ꎬ进一步丰富了伪造特征提取能力ꎻ融合梯度和内容特征的重构学习(reconstruction learning fusing gradient and content featuresꎬRLGC)模型[13] 则利用图像梯度信息增强重建特征以改进检测效果ꎮ

然而ꎬ现有方法仍存在明显不足:RECCE 模型仅对真实样本施加重建约束ꎬ限制了其对伪造样本内在特征的挖掘ꎻDisGRL 模型的整体重建效果欠佳ꎬ尤其是图推理分支的表现较弱ꎻRLGC 模型虽引入梯度信息ꎬ但未充分作用于编码器ꎬ导致特征表达能力受限ꎮ 针对这些不足ꎬ提出了基于图像梯度引导重建( imagegradient－guided reconstructionꎬGradGR)的面部伪造检测模型ꎮ 该模型突破了现有模型在特征空间上的局限性ꎬ实现了梯度域特征与空间域特征的协同感知ꎬ充分利用梯度信息引导图像重建全流程ꎬ从而增强模型对细微伪造痕迹的建模能力ꎮ 该模型由图像重建主干和梯度重建分支构成ꎬ并引入多源特征融合(multi－source feature fusionꎬMSFF)模块对多尺度特征进行融合ꎬ通过跨尺度特征级联与注意力机制实现高效的多源信息融合ꎮ

# 1 GradGR 模型

# 1.1 图像梯度引导重建

对于面部伪造图像来说ꎬ伪造痕迹常出现在面部轮廓边缘区域ꎮ 而 Prewitt 算子的核心思想便是通过计算图像中每个像素点的梯度幅值和方向来检测边缘ꎮ 因此ꎬGradGR 模型首先使用 Prewitt 算子进行图像梯度的获取ꎬ得到的梯度信息将在梯度重建分支进行重建ꎮ 然后ꎬ该模型将梯度重建分支的中间特征信息向图像重建主干进行传递ꎮ 在梯度重建分支进行传递时ꎬ梯度编码器 $\varrho _ { \mathrm { e n c o d e r } }$ 和梯度解码器 $g _ { \mathrm { d e c o d e r } }$ 分别会产生 3 组中间特征图序列ꎬ可表示为

$$
\left\{ \begin{array} { l } { { \displaystyle g _ { \mathrm { e n c o d e r } } ( \mathbf G ) = E _ { \scriptscriptstyle G 1 } , E _ { \scriptscriptstyle G 3 } , E _ { \scriptscriptstyle G 5 } , } } \\ { { \displaystyle g _ { \mathrm { d e c o d e r } } ( \mathbf G ) = { \cal D } _ { \scriptscriptstyle G 1 } , { \cal D } _ { \scriptscriptstyle G 3 } , { \cal D } _ { \scriptscriptstyle G 5 } \circ } } \end{array} \right.
$$

式中: $\pmb { { \cal E } } _ { G 1 } \ 、 \pmb { { \cal E } } _ { G 3 }$ 和 $\pmb { { \cal E } } _ { G 5 }$ 为第1、3、5 层梯度编码器的中间特征图ꎬ $\smash { D _ { G 1 } \mathopen { } \mathclose \bgroup \left. D _ { G 3 } \aftergroup \egroup \right. }$ 和 $\pmb { D } _ { G 5 }$ 为第1、3、5 层梯度解码器的中间特征图ꎮ 紧接着ꎬ经由单通道 $1 \times 1$ 卷积 $( f _ { \mathrm { s c } } )$ 与 S 型生长曲线 $( \delta _ { \mathrm { s i g m o i d } } )$ 激活函数依次进行处理ꎬ分别获取对应的注意力图ꎬ其计算公式如下所示:

$$
M _ { E i / D i } = \delta _ { \mathrm { s i g m o i d } } ( f _ { \mathrm { s c } } ( E _ { G i } / D _ { G i } ) ) , \quad i \in \{ 1 , 3 , 5 \} \mathrm { ~ , }
$$

式中: $M$ 为对应的梯度注意力图 ${ E _ { G } } / { D _ { G i } }$ 代表输入的特征信息为 $\pmb { { \cal E } } _ { G i }$ 或者 $\pmb { D } _ { G i }$ ꎬ图像编码器 $f _ { \mathrm { e n c o d e r } }$ 和图像解码器 $f _ { \mathrm { d e c o d e r } }$ 利用这些注意力图对其中间特征 $\pmb { E } _ { X i }$ 或 $\pmb { D } _ { X i }$ 进行逐元素加权 $( \otimes )$ 处理ꎬ计算公式如下所示:

$$
{ \cal F } _ { E i / D i } = ( { \cal E } _ { { \scriptscriptstyle X i } } / { \cal D } _ { { \scriptscriptstyle X i } } ) \bigotimes M _ { E i / D i } \circ
$$

最终ꎬ模型将加权后的增强特征 $\pmb { F } _ { E i / D i }$ 作为多源特征融合模块的输入ꎮ

# 1.2 MSFF 模块

利用重建学习产生更多潜在特征对于揭示伪造信息至关重要ꎮ GradGR 模型中引入了 MSFF 模块来富集各种特征ꎬ该模块结构如图1 所示ꎮ 由图 1 可知ꎬ来自编码器、解码器与重建差异的特征信息均在 MSFF模块中被融合ꎮ 该模块首先是对于编码器和解码器的中间特征图进行卷积下采样融合ꎮ 由于编码器和解码

器均为漏斗状结构ꎬ编码器在编码过程中不断下采样图像ꎬ而解码器在解码过程中不断上采样图像ꎮ 因此ꎬ其中间特征图存在大小不一的现象ꎮ MSFF 模块使用特定的卷积 $( f _ { \mathrm { c } } )$ 不断缩小大尺寸特征ꎬ以匹配其临近特征的大小ꎬ其过程如下所示:

$$
\begin{array} { r } { \pmb { F } _ { E i + 2 / D i + 2 } ^ { \prime } = f _ { \mathrm { c } } ( \pmb { F } _ { E i / D i } ) \oplus \pmb { F } _ { E i + 2 / D i + 2 } , \quad i \in \{ 1 , 3 \} \mathrm { ~ , ~ } } \end{array}
$$

式中: $\oplus$ 代表逐元素相加ꎮ 接下来ꎬ将融合后的编码器特征与解码器特征进行拼接( $\varphi _ { \mathrm { c o n c a t } } \mathrm { . }$ )后ꎬ再使用注意力化后的重建差异对其进行逐元素加权ꎬ以突出潜在伪造痕迹区域的特征数值ꎬ这一过程可表示为:

$$
M _ { \mathit { G } \mathit { X } } = \delta _ { \mathrm { s i g m o i d } } ( f _ { \mathrm { c s } } ( ( G - G ^ { \prime } ) / ( X - X ^ { \prime } ) ) ) .
$$

$$
F _ { \mathrm { E D } } ^ { \prime } = \varphi _ { \mathrm { c o n c a t } } ( M _ { G } \circledast F _ { \mathrm { E D } } , M _ { X } \circledast F _ { \mathrm { E D } } ) ,
$$

式中: $G ^ { \prime }$ 和 $X ^ { \prime }$ 分别表示重建过后的梯度与图像ꎬ $\boldsymbol { F } _ { \mathrm { E D } }$ 为融合后的编码器与解码器特征ꎮ 最终ꎬ注意力化的 $F _ { \mathrm { E D } } ^ { \prime }$ 经拼接与卷积调整后进入分类器判别真假类别ꎮ

![](images/d50fbaf5e88815e01f87dbd63a46f7621494b484bd70fec53dcbc005804e35c5.jpg)  
图 1　 多源特征融合模块结构  
Fig.1　 Module structure of multi－source feature fusion

# 1.3 损失函数

GradGR 模型训练过程中涉及2 种损失函数ꎬ分别是重建损失和分类损失ꎮ 其中ꎬ重建损失的本质为 $L _ { 1 }$ 损失函数ꎮ 以图像重建主干为例ꎬ其重建损失( $\cdot { \mathcal { L } } _ { \mathrm { r e c } } ^ { X }$ )计算公式如下所示:

$$
\mathcal { L } _ { \mathrm { r e c } } ^ { X } = \frac { 1 } { H \times \mathit { W } } \sum _ { k = 1 } ^ { H \times \mathit { W } } \left\| X _ { k } - X ^ { \prime } { } _ { k } \right\| _ { 1 } \circ
$$

式中: $H$ 与 $W$ 分别为重建图像的高度与宽度ꎬ $k$ 为像素序号ꎬ $\| \cdot \| _ { 1 }$ 为 $\mathrm { L } _ { 1 }$ 范数ꎮ 同理ꎬ对于梯度重建分支其重建损失表示为 $\mathcal { L } _ { \mathrm { r e c } } ^ { G }$ ꎮ 分类任务常用的损失函数为交叉熵损失ꎬ而面部伪造检测任务是简单的二分类问题ꎮ因此ꎬ交叉熵损失 $\cdot \mathcal { L } _ { \mathrm { r e c } } \backslash$ )可以简化为

$$
\mathcal { L } _ { \mathrm { c l s } } = - \frac { 1 } { N } \sum _ { i = 1 } ^ { N } \left[ \gamma _ { i } \mathrm { l g } ( p _ { i } ) + ( 1 - \gamma _ { i } ) \mathrm { l g } ( 1 - p _ { i } ) \right] ,
$$

式中: $y _ { i }$ 为真实类别 $p _ { i }$ 为预测类别 $N$ 为单批次下的样本数量ꎮ 最终ꎬ总损失( $\mathcal { L } _ { \mathrm { a l l } }$ )可表示为

$$
\mathcal { L } _ { \mathrm { a l l } } = \mathcal { L } _ { \mathrm { c l s } } + \mathcal { L } _ { \mathrm { r e c } } ^ { X } + \mathcal { L } _ { \mathrm { r e c } } ^ { G } 
$$

# 1.4 模型总体结构

GradGR 模型可分为3 部分结构ꎬ包括图像信息重建主干、梯度信息重建分支和多尺度特征融合模块ꎮGradGR 模型框架如图2 所示ꎮ 由图2 可知ꎬ该模型首先需要输入1 幅可疑图像 $\pmb { X } \in \mathbf { R } ^ { 3 \times H \times W }$ ꎬ经梯度算子进行提取后获得该图像的原始梯度 $\pmb { G } \in \mathbf { R } ^ { 1 \times H \times W }$ ꎮ 随后ꎬ图像 $X$ 交由重建主干进行重建ꎬ而梯度 $\textbf { \textit { G } }$ 则交由重建分支进行重建ꎮ 在主干与分支同步进行重建过程中ꎬ由梯度编解码器产生的中间特征图被分别传递至图像编解码器ꎮ 此外ꎬ为了充分利用在重建过程中产生的丰富中间特征ꎬGradGR 模型还使用了多源特征融合机制ꎮ该机制统筹编解码器的中间特征图与重建的差异图来进行伪造痕迹的富集ꎬ实现对多种来源信息的提炼ꎮ最后ꎬ这些增强特征交由分类器来辨别图像真伪ꎬ从而对可疑图像进行判别ꎮ

# 2　 实验环境与评价指标

![](images/d0a5454cc278b8b6d9ebd528db8c61902373483d36a01179a881bb7664095989.jpg)  
图 2　 基于图像梯度引导重建的面部伪造检测模型框架Fig.2　 Model framework of facial forgery detection via image gradient－guided reconstruction

# 2.1 数据集

为了评估模型的性能与验证组件的效用ꎬ实验选取了 4 个公开的面部伪造数据集ꎬ即面部取证(faceforensics $^ { + + }$ ꎬ $\mathrm { F F } { + } { + } \dot { { ^ { } } }$ ) [14] 、名人深度伪造第 1 版(celebrity deepfake forensics version 1ꎬCDFv1) [15] 、名人深度伪造第 2 版(celebrity deepfake forensics version 2ꎬCDFv2) [15] 和混合假脸(hybrid fake faceꎬHFF)数据集[16] ꎮ 具体而言: $\textcircled{1}$ ${ \mathrm { F F } } { + } +$ 数据集常作为面部伪造检测的基准ꎬ包含 4 种篡改方法ꎬ分别为面对面(face to faceꎬF2F)、面部交换(face swapꎬFS)、深度伪造(deep fakesꎬDF)、神经纹理(neural texturesꎬNT)方法ꎮ $\textcircled{2}$ CDFv1、CDFv2 数据集是使用同源真实视频构建的 2 个不同数据集ꎮ 由于 CDFv2 数据集中的伪造视频拥有较好的视觉质量(伪造痕迹不明显)ꎬ这使其伪造检测更富有挑战性ꎮ $\textcircled{3}$ HFF 数据集包含3 种不同分辨率的真实图像和5 种不同篡改方法的伪造图像ꎬ其不仅从现有人脸数据集中提取不同分辨率的真实图像ꎬ还使用生成模型和计算机图形学方法生成伪造图像ꎮ

实验中严格遵循各数据集的官方标准划分训练集、验证集和测试集ꎮ 针对真实视频与伪造视频比例满足 $1 : 1$ 的情况ꎬ采用不同采样速率分别进行提取ꎮ

# 2.2 评价指标

面部伪造检测被定性为2 分类任务ꎮ 在衡量模型的性能方面ꎬ准确率(accuracyꎬACC)和接收者操作特征曲线下面积(area under the receiver operating characteristic curveꎬAUC) 指标被用于不同的评估场景ꎮ ACC是最直观的性能指标之一ꎬ即模型正确预测的样本数量占总样本数量的比例ꎬ提供了全局性的视角ꎬ帮助快速了解模型的整体表现ꎻAUC 被用于衡量模型的综合分类能力ꎬ是接收者操作特征( receiver operatingcharacteristicꎬROC)曲线下的面积ꎮ

# 2.3 实验环境

实验中所有模型均在相同环境下进行ꎬ并且其主干网络均加载了在图像网络(ImageNet)数据集上进行预训练得到的权重ꎮ 在数据预处理阶段ꎬDlib 库被用于对包含面部的视频帧进行了提取、对齐和裁剪ꎬ所有图像的大小均被调整为256 像素 $\times 2 5 6$ 像素ꎬ并使用 Albumentations 库对数据进行增强ꎬ包括水平翻转、随机裁剪和色彩变换等ꎮ 在模型训练阶段ꎬ模型结合默认配置的带权重衰减的自适应矩估计(adaptive momentestimation with weight decayꎬAdamW)优化器与步长学习率调度器进行训练ꎮ 其中ꎬ优化器的初始学习率被设置为0.0002ꎬ权重衰减被设置为 0.0001ꎬ调度器的步长被设置为 1ꎮ 除此之外ꎬ模型训练中批次大小被设置为 32ꎮ 实验的代码平台为 DeepfakeBench 代码库ꎬ实验的服务器平台包含英伟达 GeForce RTX 4090 显卡ꎮ实验中模型计训练10 轮ꎬ完成约36000 次迭代ꎮ

# 3　 实验结果与分析

# 3.1 对比实验

实验中选用7 种常见的面部伪造检测模型与 GradGR 模型进行对比ꎬ包括极端初始(extreme inceptionꎬXception)模型[17] 、 基于注意力的深度伪造检测网络 ( attention － based deepfake detection networksꎬ ADD －

Net) [18] 、 $\mathrm { { F ^ { 3 } } - N e t ^ { [ 1 0 ] } }$ 、代表性伪证挖掘( representative forgery miningꎬRFM) [19] 、 $\mathrm { M A T } ^ { [ 9 ] }$ 、RECCE[11] 、DisGRL 模型[12]ꎮ 并且分别在 $\mathrm { F F } { + } { + } , \mathrm { C D F v 1 } , \mathrm { C D F v 2 }$ 和 HFF 这4 个数据集上展开了数据集内的性能对比ꎬ以验证模型的整体建模能力ꎮ 模型还在 $\mathrm { F F } { + } { + }$ 数据集上进行训练ꎬ在 CDFv1、CDFv2 和 HFF 3 个数据集上进行跨数据集的性能对比ꎬ以验证模型对于未见伪造类型的泛化能力ꎮ 实验中所有模型均采用 ACC 和 AUC 双指标进行评估ꎮ

对于面部伪造检测任务的建模能力是模型可以有效检测图像真伪的基础ꎮ 评估方法采用“在当前数据集训练ꎬ在当前数据集测试”的模式ꎬ可以准确地反映模型是否有效完成伪造检测ꎮ 数据集内的模型性能评估结果如表1 所示ꎮ 由表 1 可知ꎬ各模型对数据特性呈现敏感差异ꎬ即在 $\mathrm { F F } + +$ 数据集中ꎬGradGR 模型的ACC 和 AUC 领先ꎬ体现其强大的系统性建模能力ꎮ 而在 CDFv1 数据集中ꎬGradGR 模型与 DisGRL 模型的ACC 占据前 2 位ꎮ GradGR 模型的 ACC 较 Xception 模型提升了 $9 . 5 9 \%$ ꎬ表明双路径重建学习框架能有效捕捉细致伪影ꎮ 此外ꎬGradGR 模型还在 CDFv2、HFF 数据集上取得了最优的结果ꎬ这得益于利用梯度信息来丰富空间信息ꎬ实现更高质量的建模ꎬ使得真伪判别边界更为清晰ꎮ

Tab.1　 Model performance evaluation within the dataset   

<html><body><table><tr><td rowspan="2">模型</td><td colspan="2">FF++</td><td colspan="2">CDFv1</td><td colspan="2">CDFv2</td><td colspan="2">HFF</td></tr><tr><td>ACC/%</td><td>AUC/%</td><td>ACC/%</td><td>AUC/%</td><td>ACC/%</td><td>AUC/%</td><td>ACC/%</td><td>AUC/%</td></tr><tr><td>Xception</td><td>95.73</td><td>96.30</td><td>77.25</td><td>86.76</td><td>97.90</td><td>99.73</td><td>79.35</td><td>89.50</td></tr><tr><td>ADD-Net</td><td>96.78</td><td>97.74</td><td>76.25</td><td>86.17</td><td>96.93</td><td>99.55</td><td>78.71</td><td>89.85</td></tr><tr><td>F³-Net</td><td>97.52</td><td>98.10</td><td>80.66</td><td>87.53</td><td>95.95</td><td>98.93</td><td>76.17</td><td>88.39</td></tr><tr><td>RFM</td><td>95.69</td><td>98.79</td><td>77.38</td><td>83.92</td><td>97.96</td><td>99.94</td><td>80.83</td><td>89.75</td></tr><tr><td>MAT</td><td>97.60</td><td>99.29</td><td>82.86</td><td>90.71</td><td>97.92</td><td>99.90</td><td>76.81</td><td>90.32</td></tr><tr><td>RECCE</td><td>97.06</td><td>99.32</td><td>83.25</td><td>92.02</td><td>98.59</td><td>99.94</td><td>81.20</td><td>91.33</td></tr><tr><td>DisGRL</td><td>97.69</td><td>99.48</td><td>84.53</td><td>93.27</td><td>98.71</td><td>99.91</td><td>82.35</td><td>92.50</td></tr><tr><td>GradGR</td><td>97.71</td><td>99.50</td><td>84.66</td><td>93.32</td><td>98.83</td><td>99.95</td><td>83.11</td><td>92.68</td></tr></table></body></html>

注:加粗数字是该列最优值ꎬ加下划线数字为该列次优值ꎮ

在面部伪造检测领域ꎬ拥有良好泛化性能的检测模型在真实场景下更具实用价值ꎮ 因此ꎬ跨数据集实验便是模仿这一现实场景ꎬ该实验采用“在当前数据集训练ꎬ在其他数据集测试”的模式ꎬ可以更全面地评估模型对于未见数据的泛化性ꎮ 跨数据集的模型性能评估结果如表2 所示ꎮ 由表2 可知ꎬGradGR 模型在所有数据集的平均 ACC 和平均 AUC 性能上均居首位ꎬ其平均 ACC 较 Xception 模型提高了 $3 . 2 2 \%$ ꎮ 值得注意的是ꎬGradGR 模型相比同样采用重建学习方法的 RECCE、DisGRL 模型有着明显的性能优势ꎬ这不仅得益于梯度信息的引导重建ꎬ还得益于多源特征信息的融合设计ꎮ

表 1　 数据集内的模型性能评估  
表 2　 跨数据集的模型性能评估  
Tab.2　 Model performance evaluation across datasets   

<html><body><table><tr><td rowspan="2">模型</td><td colspan="2">CDFv1</td><td colspan="2">CDFv2</td><td colspan="2">CDFv2</td><td colspan="2">平均值</td></tr><tr><td>ACC/%</td><td>AUC/%</td><td>ACC/%</td><td>AUC/%</td><td>ACC/%</td><td>AUC/%</td><td>ACC/%</td><td>AUC/%</td></tr><tr><td>Xception</td><td>76.55</td><td>77.94</td><td>72.69</td><td>73.65</td><td>69.42</td><td>70.77</td><td>72.89</td><td>74.12</td></tr><tr><td>ADD-Net</td><td>77.99</td><td>78.97</td><td>66.72</td><td>66.80</td><td>61.12</td><td>61.32</td><td>68.61</td><td>69.03</td></tr><tr><td>F³-Net</td><td>76.00</td><td>77.69</td><td>73.19</td><td>73.52</td><td>69.79</td><td>70.21</td><td>72.99</td><td>73.81</td></tr><tr><td>RFM</td><td>77.56</td><td>77.93</td><td>75.27</td><td>75.52</td><td>69.78</td><td>69.95</td><td>74.20</td><td>74.46</td></tr><tr><td>MAT</td><td>77.71</td><td>77.98</td><td>73.84</td><td>74.28</td><td>70.96</td><td>71.54</td><td>74.17</td><td>74.60</td></tr><tr><td>RECCE</td><td>69.60</td><td>70.66</td><td>73.03</td><td>73.32</td><td>70.93</td><td>71.28</td><td>71.19</td><td>71.75</td></tr><tr><td>DisGRL</td><td>73.98</td><td>74.26</td><td>75.11</td><td>75.78</td><td>70.63</td><td>70.75</td><td>73.24</td><td>73.60</td></tr><tr><td>GradGR</td><td>79.06</td><td>79.22</td><td>75.60</td><td>75.81</td><td>71.06</td><td>71.57</td><td>75.24</td><td>75.53</td></tr></table></body></html>

注:加粗数字是该列最优值ꎬ加下划线数字为该列次优值ꎮ

# 3.2 消融实验

为了验证 GradGR 模型和其配备的 MSFF 模块的有效性ꎬ进行了消融实验ꎮ 4 种不同情况下的检测性能有着明显的变化ꎬ各模块的有效性验证结果如表 3 所示ꎮ 由表 3 可知ꎬ在采用了图像梯度引导重建模块和MSFF 模块的情况下ꎬ取得了最优的性能ꎬ证明了这种训练方法与融合模块的有效性ꎮ 当保留图像梯度引导

重建模块ꎬ而不使用 MSFF 模块时ꎬ模型依旧维持着相对优异的性能ꎮ 这也表明图像梯度引导重建模块是提高模型建模能力的有效方法ꎬ可以提高模型对于潜在伪造细节的获取能力ꎮ

表 3　 模型各模块的有效性验证  
Tab.3 Validation of each module of the model   

<html><body><table><tr><td>序号</td><td>基模型</td><td>图像度</td><td>MSFF</td><td>ACC/%</td><td>AUC/%</td><td>序号</td><td>基模型</td><td>图像度</td><td>MSFF</td><td>ACC/%</td><td>AUC/%</td></tr><tr><td>1</td><td>√</td><td>×</td><td>×</td><td>95.73</td><td>96.30</td><td>3</td><td>√</td><td>×</td><td>√</td><td>97.03</td><td>98.95</td></tr><tr><td>2</td><td>√</td><td>√</td><td>×</td><td>97.24</td><td>99.02</td><td>4</td><td>√</td><td>√</td><td>√</td><td>97.71</td><td>99.50</td></tr></table></body></html>

注: $\surd$ 表示使用了该功能模块ꎬ而 $\mathrm { \bar { \times } }$ 表示未使用ꎬ加粗数字是该列最优值ꎮ

# 3.3 可视化实验

基于深度学习的端到端模型通常面临着可解释性差的困境ꎮ 当前ꎬ可视化方法是间接解释模型运作机理的手段ꎮ 在实验中ꎬ利用3 种不同的可视化方法来揭示模型能够有效检测面部伪造的原因ꎮ

首先ꎬ对模型分类前的潜在特征空间进行了可视化ꎮ 其主要是利用 t 分布－随机邻近嵌入(t－distributedstochastic neighbor embeddingꎬt－SNE) [20] 降维技术对一系列高维数据进行低维映射ꎬ目的是凸显模型的分类决策边界ꎬ更加直观地展示模型的分类能力ꎮ 基于 t－SNE 方法的特征空间可视化结果如图 3 所示ꎮ 由图 3可知ꎬGradGR 模型拥有着更加明显且简单的决策边界ꎬ这表明其区分真伪数据的能力出众ꎮ 此外ꎬGradGR模型与其他模型相比ꎬ同一类别分布更加集中ꎬ更容易得到通用的分类界限ꎮ

![](images/93d90fb4663fb573b1166140e32b9729f7392a79ca1410d0c1fa846c1cb073d7.jpg)

然后ꎬ由于 GradGR 模型立足于重建学习方法ꎬ其双路重建图像的效果也直接影响着模型的检测性能ꎮGradGR 模型的双路径重建效果可视化结果如图4 所示ꎮ 由图4 可知ꎬ实验中分别对真假图像都进行了重建可视化ꎬ可以观察到 GradGR 模型基本重建了输入图像的全局信息ꎬ对于一些无关信息在重建过程中适当地丢弃ꎮ 对于梯度信息的重建ꎬ可以发现其对于一些纹理信息的保留不明显ꎬ反而重点重建了图像的边缘信息ꎬ这对于挖掘潜在伪影至关重要ꎮ

![](images/35a271d6516fef3afd322ec916e275cb11b886319f0f0c3f52ba2633286f760f.jpg)  
图 3　 基于 t－SNE 方法的特征空间可视化Fig.3　 Feature space visualization based on t－SNE method  
图 4　 模型的双路重建效果可视化  
Fig.4　 Visualization of dual－path reconstruction effect of the model

最后ꎬ利用梯度加权类激活映射(gradient－weighted class activation mappingꎬGradCAM) [21] 技术对模型进行分类决策时的图像关注区域进行可视化ꎮ 该技术通过捕获模型反向传播时的梯度变化来反映模型的注意力ꎮ 基于该方法的模型决策区域可视化结果如图5 所示ꎮ 由图 5 可知ꎬ激活区域图是捕获的最原始的梯度变化图ꎬGradCAM 将其与原始输入图像进行叠加ꎬ得到了区域热图ꎬ更加直观地反映了模型在进行分类前的决策区域ꎮ 显而易见ꎬGradGR 模型注意力均集中在面部区域ꎬ尤其是对于出现伪影频率高的区域ꎮ 这证明GradGR 模型能够有效地根据伪造图像不自然的信息进行判断ꎬ从而正确关注到可疑区域ꎮ

![](images/08b117a88b2a9cd245aa192b5058edd0b73d66bd7bc8fd98a7d2d0dab7ea11df.jpg)  
图 5　 基于 GradCAM 方法的模型决策区域可视化 Fig.5 Visualization of model decision regions based on Grad－CAM method

# 4　 结论

针对当前面部伪造检测领域泛化性不足的问题ꎬ提出了 GradGR 模型ꎮ 该模型在图像重建过程中探索挖掘了更具泛化性的分类依据ꎮ 为了更加关注于图像中高梯度值区域ꎬGradGR 模型在原有重建路径上引入了全新的梯度重建分支ꎮ 利用梯度重建分支产生的丰富信息引导图像重建主干ꎬ迫使主干学习到更细致的特征ꎮ 此外ꎬGradGR 模型还引入了 MSFF 模块来统筹编解码器产生的中间特征信息ꎬ并增强了伪影特征区域ꎬ最终在输入至分类器前充分利用多源特征信息进行融合ꎮ 大量的实验证明了 GradGR 模型的综合建模能力和泛化性为最优ꎬ还验证了 GradGR 模型及其改进模块的有效性ꎮ 未来ꎬ考虑将重建功能更加细致化以捕获更准确的伪造区域ꎮ

# 参考文献:

[1]　 丁峰ꎬ匡仁盛ꎬ周越ꎬ等.深度伪造及其取证技术综述[J].中国图象图形学报ꎬ2024ꎬ29(2):295－317.   
[2]　 赵娅ꎬ郜明超ꎬ姚文达ꎬ等.基于深度学习的伪造人脸检测技术综述[J].计算机系统应用ꎬ2025ꎬ34(4):1－17.   
[3]　 范智贤ꎬ程晴晴ꎬ杨高明.基于注意力机制和一致性损失的深度伪造人脸检测方法[ J].湖北民族大学学报(自然科学版)ꎬ2023ꎬ41(3): 338－343.   
[4]　 冯才博ꎬ刘春晓ꎬ王昱烨ꎬ等.结合图像块比较与残差图估计的人脸伪造检测[J].中国图象图形学报ꎬ2024ꎬ29(2):457－467.   
[5]　 董佳乐ꎬ邓正杰ꎬ李喜艳ꎬ等.基于频域和空域多特征融合的深度伪造检测方法[J].图学学报ꎬ2025ꎬ46(1):104－113.   
[6]　 李兆威ꎬ高欣健ꎬ笪子凯ꎬ等.结合深度伪造特征对比的人脸伪造检测[J].模式识别与人工智能ꎬ2024ꎬ37(9):786－797.   
[7]　 张溢文ꎬ蔡满春ꎬ陈咏豪ꎬ等.融合空间特征的多尺度深度伪造检测方法[J].计算机工程ꎬ2024ꎬ50(7):240－250.   
[8] 　 XIAO SꎬLAN Gꎬ YANG Jꎬ et al. MCS － GAN: a different understanding for generalization of deep forgery detection [ J] . IEEE Transactions on Multimediaꎬ2024ꎬ26:1333－1345.   
[9] 　 ZHAO HꎬZHOU WꎬCHEN Dꎬet al.Multi－attentional deepfake detection[ C] / / Proceedings of the IEEE / CVF Conference on Computer Vision and Pattern Recognition.Online:IEEEꎬ2021:2185－2194.   
[10] 　 QIAN Yꎬ YIN Gꎬ SHENG Lꎬ et al. Thinking in frequency: face forgery detection by mining frequency － aware clues [ C] / / Proceedings of the European Conference on Computer Vision.Glasgow:Springerꎬ2020:86－103.   
[11] 　 CAO JꎬMA CꎬYAO Tꎬet al. End －to－end reconstruction －classification learning for face forgery detection[ C] / / Proceedings of the IEEE / CVF Conference on Computer Vision and Pattern Recognition.New Orleans:IEEEꎬ2022:4113－4122.   
[12] 　 SHI ZꎬCHEN HꎬCHEN Lꎬet al. Discrepancy－guided reconstruction learning for image forgery detection[ C] / / Proceedings of the International Joint Conference on Artificial Intelligence.Macao:IJCAIꎬ2023:1387－1395.   
[13] XU Kꎬ HU Xꎬ ZHOU Xꎬ et al. RLGC: reconstruction learning fusing gradient and content features for efficient deepfake detection [ J] . IEEE Transactions on Consumer Electronicsꎬ2024ꎬ70(3):6084－6094.   
[14] ROSSLER AꎬCOZZOLINO DꎬVERDOLIVA Lꎬet al. FaceForensics $^ { + + }$ :learning to detect manipulated facial images[ C] / / Proceedings of the IEEE / CVF International Conference on Computer Vision.Seoul:IEEEꎬ2019:1－11.   
[15] LI YꎬYANG XꎬSUN Pꎬet al.Celeb－DF:a large－scale challenging dataset for deepfake forensics[ C] / / Proceedings of the IEEE / CVF Conference on Computer Vision and Pattern Recognition.Seattle:IEEEꎬ2020:3207－3216.   
[16] 　 GUO Zꎬ YANG Gꎬ CHEN Jꎬ et al. Fake face detection via adaptive manipulation traces extraction network [ J] . Computer Vision and Image Understandingꎬ2021ꎬ204:1－10.   
[17] CHOLLET F.Xception:deep learning with depthwise separable convolutions[ C] / / Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition.Honolulu:IEEEꎬ2017:1800－1807.   
[18] ZI Bꎬ CHANG Mꎬ CHEN Jꎬ et al. WildDeepfake: a challenging real － world dataset for deepfake detection [ C ] / / Proceedings of the ACM International Conference on Multimedia.Online:ACMꎬ2020:2382－2390.   
[19] WANG CꎬDENG W.Representative forgery mining for fake face detection[ C] / / Proceedings of the IEEE / CVF Conference on Computer Vision and Pattern Recognition.Online:IEEEꎬ2021:14918－14927.   
[20] VAN M LꎬHINTON G.Visualizing data using t－SNE[J].Journal of Machine Learning Researchꎬ2008ꎬ86:2579－2605.   
[21] SELVARAJU R RꎬCOGSWELL MꎬDAS Aꎬet al. Grad － CAM:visual explanations from deep networks via gradient － based localization [ C] / / Proceedings of the IEEE International Conference on Computer Vision.Venice:IEEEꎬ2017:618－626.

责任编辑:郑玥雷