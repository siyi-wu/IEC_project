# 《计算机工程与应用》网络首发论文

题目：  
作者：  
网络首发日期：  
引用格式：  
基于 ConvNeXt-Mamba 的双编码器图像伪造检测  
潘苗绒，王燚  
2025-03-26  
潘苗绒，王燚．基于 ConvNeXt-Mamba 的双编码器图像伪造检测[J/OL]．计算  
机工程与应用. https://link.cnki.net/urlid/11.2127.TP.20250326.1328.011

![](images/81429f57f7258fcb43e4a4628413bd91cdc8d8a27d0e2dd8ab3a7ec68ecf79b1.jpg)

网络首发：在编辑部工作流程中，稿件从录用到出版要经历录用定稿、排版定稿、整期汇编定稿等阶段。录用定稿指内容已经确定，且通过同行评议、主编终审同意刊用的稿件。排版定稿指录用定稿按照期刊特定版式（包括网络呈现版式）排版后的稿件，可暂不确定出版年、卷、期和页码。整期汇编定稿指出版年、卷、期、页码均已确定的印刷或数字出版的整期汇编稿件。录用定稿网络首发稿件内容必须符合《出版管理条例》和《期刊出版管理规定》的有关规定；学术研究成果具有创新性、科学性和先进性，符合编辑部对刊文的录用要求，不存在学术不端行为及其他侵权行为；稿件内容应基本符合国家有关书刊编辑、出版的技术标准，正确使用和统一规范语言文字、符号、数字、外文字母、法定计量单位及地图标注等。为确保录用定稿网络首发的严肃性，录用定稿一经发布，不得修改论文题目、作者、机构名称和学术内容，只可基于编辑规范进行少量文字的修改。

出版确认：纸质期刊编辑部通过与《中国学术期刊（光盘版）》电子杂志社有限公司签约，在《中国学术期刊（网络版）》出版传播平台上创办与纸质期刊内容一致的网络版，以单篇或整期出版形式，在印刷出版之前刊发论文的录用定稿、排版定稿、整期汇编定稿。因为《中国学术期刊（网络版）》是国家新闻出版广电总局批准的网络连续型出版物（ISSN 2096-4188，CN 11-6037/Z），所以签约期刊的网络版上网络首发论文视为正式出版。

# 基于 ConvNeXt-Mamba 的双编码器图像伪造检测

潘苗绒 1，王燚 1,2,3

1.成都信息工程大学网络空间安全学院（芯谷产业学院），成都 610225  
2.先进密码技术与系统安全四川省重点实验室（芯谷产业学院），成都 610225  
3.先进微处理器技术国家工程研究中心（工业控制与安全分中心），成都 610225

摘要：图像伪造检测在网络安全领域中是一项基础且关键的任务。卷积神经网络（CNN）是当前图像伪造检测领域的主流方法，但 CNN 通常只能提取局部特征，难以捕获全局特征。为此，本研究提出了融合 Mamba和 ConvNeXt 的双编码器结构，其中 Mamba 负责捕获全局上下文特征，ConvNeXt 则聚焦于局部细节特征，通过两者的协同实现特征的综合提取。为了进一步强化关键特征表达，引入通道注意力模块（SE Block），通过自适应调整特征通道的权重提升特征表达能力。针对伪造区域边界复杂带来的漏检问题，增加了边缘损失以提高模型对伪造轮廓的识别准确性。在 CASIAv1 等 4 个基准数据集上的实验表明，本方法在曲线下面积 (AUC)分数和 F1 分数上分别平均提升 $1 . 5 2 \%$ 和 $5 . 4 5 \%$ ，显著优于现有方法，尤其在复杂伪影和模糊边界场景下展现出更强鲁棒性。

关键词：图像伪造检测；网络安全；卷积神经网络；Mamba；全局特征；局部特征文献标志码:A 中图分类号:TP391 doi：10.3778/j.issn.1002-8331.2501-0136

# Double encoder image forgery detection based on ConvNeXt and Mamba

PAN Miaorong1,  WANG Yi1,2,3

1.School of Cyberspace Security, Chengdu University of Information Technology (Xingu Industrial College), Chengdu 610225, China   
2.Sichuan Provincial Key Laboratory of Advanced Cryptography and System Security (Xingu Industrial College), Chengdu 610225, China   
3.National Engineering Research Center for Advanced Microprocessor Technology (Industrial Control and Security   
Branch), Chengdu 610225, China

Abstract：Image forgery detection is a fundamental and critical task in the field of cybersecurity. Convolutional Neural Networks (CNNs) are the mainstream approach in image forgery detection; however, CNNs typically extract only local features, making it difficult to capture global characteristics. To address this limitation, this study proposes a dual-encoder architecture integrating Mamba and ConvNeXt, where Mamba is responsible for capturing global contextual features, while ConvNeXt focuses on local detail features. The synergy between these two components enables comprehensive feature extraction. To further enhance the representation of key features, a channel attention module (SE Block) is introduced, which adaptively adjusts the weights of feature channels to improve feature expressiveness. To mitigate the issue of missed detections caused by complex forged region boundaries, an edge loss term is incorporated to enhance the model’s accuracy in identifying forgery contours. Experiments conducted on four benchmark datasets, including CASIAv1, demonstrate that the proposed method achieves an average improvement of $1 . 5 2 \%$ in 基金项目：四川省科技计划项目(2023YFG0292，2021ZYD0011），国家社会科学基金（23BSH061），体系与人工智能实验室 开创基金资助。

作者简介：潘苗绒(1999—)，女，硕士，CCF 会员，主要研究为网络安全、图像处理；王燚(1968—)，通信作者，男，博士，教授，主要研究为图像识别、自然语言处理、基于人工只能的芯片安全检测，E-mail: wangyi1177@cuit.edu.cn。

Area Under the Curve (AUC) and $5 . 4 5 \%$ in F1-score, significantly outperforming existing approaches. Notably, it exhibits superior robustness in handling complex artifacts and blurry boundary scenarios.

Key words：Image Forgery Detection; Cybersecurity; Convolutional Neural Networks; Mamba; Global features； Local features

随着图像处理技术的飞速发展，越来越多针对非专业用户的图像编辑软件的出现使得任何人都可以轻而易举的对原始图像进行篡改[1]，常见操作包括删除不需要的元素、面部交换以及修改图像属性等。这些编辑技术在本质上是中立的，但可能被恶意用于制造虚假内容，例如伪造新闻、保险诈骗和制作假签名等。这些行为严重影响了视觉信息的可靠性并对社会造成了一定的误导性。因此，开发出能够准确的检测出图像是否被篡改，并能像素级别精确定位篡改区域的网络变得愈发重要。

目前，研究者们在图像篡改检测领域已经提出了很多方法[2]，主要分为传统方法和深度学习方法两大类。传统方法通常依赖于特定图像属性的不一致性，如色彩滤镜阵列（CFA）模式不匹配、传感器图案噪声（SPN），以及 JPEG 压缩痕迹等。尽管这些方法在单一场景中能够获得良好的表现，但它们在面对来自相同设备的拼接图像或非 JPEG 格式图像时常常效果不佳，这些限制表明，需要更为全面和灵活的方法来应对日益复杂的图像篡改技术。

近年来，深度学习技术极大地推动了计算机视觉领域，现有的基于深度学习的检测方法大多数都依赖于 CNN 作为特征提取器，但 CNN 在捕捉全局依赖关系及非语义伪影方面具有局限性。例如，Guo[3],Bi[4]对传统的 U-Net 架构进行了改进，通过增加环形残差块增强了梯度传递和信息流动，有效改善了梯度消失问题。然而，该模型无法捕获全局特征信息，使得图像元素之间的空间关系无法判别，从而对于复杂篡改手段并不敏感。 Kwon[5]的 CAT-Net 通过结合 RGB 和DCT 数据流，增强了对压缩伪影的关注。但该网络主要集中于压缩相关的局部伪影特征，其对于全局上下文的理解和利用不足，导致模型在理解整幅图像内容时出现偏差，从而容易产生出现误检和漏检。 $\mathrm { W u } ^ { [ 6 ] }$ 提出了一种全卷积网络和自我监督学习的检测方法，将篡改区域定位视为局部异常检测问题，使用长短期记忆（LSTM）对局部异常进行检测，但经过内容感知处理的图像难以识别。Wei[7],Zhu[8]等人的方法其局部特征提取强大，但在全局上下文建模和计算开销方面仍有提升空间。Dong[9]等人提出的 MVSS-Net 使用多尺度监督策略，通过像素级、边缘级和图像级的多尺度监督来优化模型的特征提取。尽管这种设计提升了检测的灵活性，但计算复杂度较高，且模型在全局特征提取方面稍显不足。Liu[10]等人设计了两路编码器来分别提取全局和局部特征，但全局特征捕获能力有限，更适合在局部特征主导的任务中使用。Guo[11]采用了层次化结构检测方式, 在复杂和细微的伪造检测上表现突出,但提高了计算成本。由于 Transformer[12]在 NLP领域的成功，其架构随后被广泛应用于图像处理领域。ObjectFormer[13]和 TransForensics[14]这两种方法都使用Transformer 进行编码，其自注意力机制可以弥补 CNN的局限性，但在编码阶段图像的细节信息会被忽略，同时序列长度庞大增加了计算复杂度，限制了处理大规模高分辨率的图像，影响最终的检测效果。为了进一步提高检测准确性和计算效率， $\mathrm { M a } ^ { [ 1 5 ] }$ 等人提出的IML-ViT 以 Vision Transformer 为骨干，利用自注意力机制捕捉图像的全局和局部特征，专为大尺度伪造区域的检测而设计。然而，由于 Vision Transformer 将图像划分为固定大小的块处理，IML-ViT 在精细局部特征捕捉上存在局限，容易丢失小尺度和边缘区域的空间信息。此外，其计算复杂度依然较高，限制了在资源受限环境中的应用。基于 VIT 的缺陷，Liu[16]等人提出了 Swin Transformer 通过平移窗口的自注意力机制，能够同时提取局部和全局特征。Lin[17]等人利用其滑动窗口机制来提取全局和局部噪声特征来捕捉不同篡改操作留下的痕迹，从而进一步提升了模型的性能。然而，这些方法尽管在检测精度方面取得了较好表现，但仍然依赖于较大的计算资源和内存开销，难以在资源受限的环境上高效运行，限制了其实用性。因此，伪造检测任务亟需轻量化的解决方案，以降低计算负担并提升检测效率。

轻量化伪造检测指的是在计算资源有限的环境下（如智能手机、便携式取证设备、实时监控系统），依然能够高效、准确地完成图像伪造检测任务。相比于高计算量的方法，轻量化方法需要在减少计算复杂度和存储开销的前提下，尽可能保持检测精度，以适应低功耗、高实时性的应用场景。

最近，状态空间模型（SSM）逐渐引起了广泛关注，主要是因为它在捕获长期依赖关系方面表现出色，并能通过并行训练显著减少模型参数的数量。研究者们通过引入时变参数到 SSM 中，开发了名为Mamba[18][19]的新算法模型（结构如图 2 所示）。与先前的方法相比，该模型在使用更少的参数的同时，能够达到更优的性能[20]。然而，单一使用 Mamba 作为编码器时，它在捕获细微局部特征方面存在限制，可能导致伪造区域无法被精确识别。为了解决这一问题，本文提出了一种双分支并行编码器的网络结构，这种结构不仅解决了训练过程中对计算资源的高需求，还能同时捕捉到全局和局部特征，从而为解码过程提供了更为丰富的特征信息。此外，为了充分融合全局和局部特征，本文引入了 SE Block[21]。最后，通过计算边缘损失和分割损失组成的联合损失，进一步提升了模型检测的精确度。

# 1 相关工作

在图像篡改检测领域，近年来的研究主要集中在如何有效结合局部和全局特征以提高检测精度和鲁棒性。为了更清晰地展现本文方法的优势，本文重点对比了 MVSS-Net 和 IML-ViT 两种典型模型，并对比其优缺点，以阐明本文方法的创新性与改进优势。为确保实验的公正性和可比性，我们在所有对比方法中采用了相同的数据集和统一的评估指标。表 1 给出了两个方法的关键超参数设置。

表 1  SOTA 模型的关键参数设置  
Table 1  Key parameter settings for SOTA model   

<html><body><table><tr><td>模型</td><td>优化器</td><td>学习率</td><td>学习率调度</td><td>批大小</td><td>训练轮数</td></tr><tr><td>MVSS-Net</td><td>Adam</td><td>1e-4</td><td>周期性衰减</td><td>32</td><td>16-30</td></tr><tr><td>IML-ViT</td><td>Adam</td><td>1e-5</td><td>余弦衰减</td><td>1</td><td>200</td></tr></table></body></html>

# 1.1 MVSS-Net

MVSS-Net 主要通过多视图和多尺度监督结构来提升对细节特征的检测能力。其架构包含边缘监督分支和噪声敏感分支，前者利用 Sobel 算子捕捉图像边缘的微小特征，后者则通过 BayarConv 层提取噪声特征，以便在真实区域和伪造区域之间实现更精确的分离。这种设计使 MVSS-Net 能够在细节丰富的小尺度伪造区域中表现出色，尤其是在需要检测边缘和细微噪声特征的场景中，该方法表现出较强的适应性。

然而，MVSS-Net 偏重局部特征的提取，对全局特征的捕捉较为薄弱。因此，在检测需要长距离依赖或包含大尺度篡改区域的图像时，可能会出现信息遗漏。此外，由于多视图和多尺度设计，MVSS-Net 的计算复杂度较高，不适合用于计算资源受限的环境。

# 1.2 IML-ViT

IML-ViT 则以 Vision Transformer 的自注意力机制为核心，强调全局特征的提取能力。IML-ViT 通过自注意力机制建立图像的长距离依赖关系，使其在大尺度篡改区域的检测中具有较高的准确性。此外，IML-ViT 设计了多尺度特征金字塔和边缘监督机制，以提高对不同尺度和复杂度的伪造区域的检测效果。这种结构使得 ML-ViT 特别适合包含大范围伪造区域的场景，其全局特征提取能力帮助模型有效定位和检测篡改区域。

虽然 IML-ViT 为提升计算效率引入了窗口化自注意力机制，但自注意力机制本身的高计算需求依然存在。尤其是在处理高分辨率图像时，固定大小的块划分方式限制了其对小尺度和复杂细节的捕捉能力。因此，IML-ViT 在需要精细化局部特征提取的场景中表现一般，且高计算复杂度限制了其在实时应用中的适用性。

# 2  本文方法

为了克服现有方法在特征提取精度和计算需求上的不足，本文提出了一种全新的轻量化双分支并行编码器图像伪造检测模型，该模型的整体架构如图 1 所示，与上述方法相比，本文方法能够在保留高精度的同时，优化计算效率，以适应资源受限的环境，具有更广泛的应用潜力。

图像伪造检测任务需要模型在定位局部伪造区域的同时捕捉全局上下文信息。MVSS-Net 虽然通过多视角、多尺度特征提取来同时捕捉全局和局部信息，但计算开销较大，且往往在处理局部细节时存在一定的局限性。而 IML-ViT 则侧重于细粒度的局部特征提取，但其基于 Transformer 的设计导致计算需求高，不适合资源受限的环境。针对这些不足，本文方法设计了两个并行的编码器分支：Mamba 分支和 Con-vNeXt[22] 分支。其中，Mamba 分支专注于全局特征提取，以帮助模型理解图像的整体结构和背景；而 Con-vNeXt 分支则聚焦于局部特征的细致捕捉，尤其在伪造区域边界的识别上效果显著。通过这种双分支设计，模型在编码阶段提取深度与广度兼备的特征，兼顾全局和局部特征的平衡，使其既适用于细节复杂的伪造区域，也适合大尺度篡改检测任务。

此外，本文引入了通道注意力模块 SE Block（结构如图 3 所示）以进一步提升特征融合的效率，并优化模型的计算性能。与现有方法中常见的基于卷积操作或自注意力机制的特征融合方式不同，SE Block 通过自适应地调整特征通道的权重 来实现高效的特征融合。它利用全局平均池化 压缩通道特征后，通过两层全连接网络优化每个通道的权重，从而使得模型能够自动识别并强化关键特征，抑制冗余信息。通过这种轻量化的通道注意力机制，使得我们的方法在计算效率和特征提取精度上相较于 MVSS-Net 和 IML-ViT 有均有所提升。

编码完成后，模型通过跳跃连接将编码器特征与解码器特征相结合，使解码阶段能够保留局部细节与全局信息的完整性，最终实现对伪造区域的精确定位。

![](images/3890b92a6227c607ee9e17ee4b6bf436f32aeb702cd964b13437376ff951b862.jpg)  
图 1  模型结构图  
Fig.1 network structure diagram

# 2.1 双分支并行编码器

图像伪造检测任务需要对复杂的局部伪造区域进行精准识别，同时也要求对整个图像的全局上下文进行准确建模。然而，传统的单一编码器模型在处理这类任务时，往往在全局与局部特征的提取上存在不足。CNN 在提取局部细节特征方面表现优异，尤其擅长通过逐层卷积操作识别图像中的细小区域和边缘变化。这种特性使得 CNN 非常适合处理涉及细节伪造的任务，如边界伪造和纹理修改等。然而，由于卷积操作的局限，CNN 在提取全局信息方面表现不足，难以捕捉到图像中长距离的依赖关系[23][24][25]。

为解决这一问题，本文提出了一种基于 Mamba 编码器和 ConvNeXt 编码器的并行式双编码器结构。Mamba 编码器通过其状态空间模型（SSM）捕捉图像的全局特征，特别擅长处理长距离的上下文依赖性。与此相对，ConvNeXt 编码器则通过深度卷积操作，专注于图像的局部细节提取，精准捕捉伪造区域的边缘与纹理变化。通过这两种编码器的并行组合，模型能够在同一框架内实现全局和局部特征的全面提取，从而提升伪造区域检测的准确度。

# 2.1.1 Mamba 分支

CNN 依赖局部感受野提取特征，这种局部性设计使每个卷积核只关注输入的一小部分像素。随着卷积层的堆叠，感受野会逐渐扩大，但扩大的速度受到卷积核大小、步幅（stride）、池化层设计等因素的限制。这使得 CNN 在处理大规模、复杂的图像时，无法很好地捕捉到全局结构信息或长程依赖关系。而 Mamba 通过多尺度特征学习，能够在不同的尺度上提取图像特征。通过设计不同尺寸的卷积核或者通过融合不同分辨率的特征图，能够同时从局部细节（小尺度）和全局语境（大尺度）进行学习。此外，Mamba 通过引入互注意力机制（Mutual Attention Mechanism），显著增强了对全局依赖关系的建模能力。互注意力机制通过对特征图中的每一个像素或区域进行加权，使得模型能够关注到图像中远距离区域的相互关系。Mamba 通过结合多尺度特征提取和互注意力机制弥补了传统

CNN 在这方面的不足。

Mamba 分支的设计如图 2 所示，输入图像经过补丁划分（patch partition）处理，分解为多个重叠的子块。通过补丁嵌入（patch embedding）操作将各子块展平成向量，并送入 Mamba 模块以进行特征提取。Mamba 模块结构如图 2 所示，其内部将特征矩阵划分为两个并行分支。

![](images/029a82d54f49bb718d866ea121f8d1706e1807fb9622dd137188c62421036089.jpg)  
图 2  Mamba 块结构图  
Fig.2  Mamba block structure diagram

在第一个分支中，特征通道经过线性投影扩展至$\lambda \times$ Channel（其中 $\lambda \times$ Channel 为预定义的通道扩展因子），再应用卷积操作、SiLU 激活函数以及 SSM以实现特征转换。第二个分支同样通过线性投影将特征通道扩展至 $\lambda \times$ Channel，并施加 SiLU 激活函数。最终，两个分支的特征通过 Hadamard 乘积聚合，并经线性投影将通道数还原为初始通道数Channel，生成与输入形状一致的输出 $L _ { o u t }$ 。其过程可表示为：

$$
\left\{ \begin{array} { l l } { L _ { 1 } = S S M \left( S i L U \left( C o n v \big ( L i n e a r ( W _ { i n } ) \big ) \right) \right) } \\ { L _ { 2 } = S i L U ( L i n e a r ( W _ { i n } ) ) } \\ { L _ { o u t } = L i n e a r ( L _ { 1 } \odot L _ { 2 } ) } \end{array} \right.
$$

Mamba 是一种基于 SSM 的新型算法。传统模型的 SSM 通常是有限且固定的，状态变量是手工设计的，适用于特定类型的任务或环境。这些模型常常依赖于精确的物理建模，难以处理复杂或高度动态的环境。而 Mamba 则是一种更为灵活的建模框架，采用的是一种基于多重模态和可学习的模型，它不仅可以处理位置和速度等传统变量，还能够通过学习算法来推断更多隐含的、动态变化的特征或状态。Mamba 是一种将一维函数或序列 $x ( t )$ 映射至 $y ( t ) \in \mathbb { R }$ 的系统，通常表示为以下线性常微分方程：

$$
\left\{ \begin{array} { l } { { h ^ { ' } ( t ) = A h ( t ) + B x ( t ) } } \\ { { y ( t ) = C h ( t ) } } \end{array} \right.
$$

其中， $h ^ { \prime } ( t )$ 表示下一时间步的预测状态， $x ( t ) \ \in$ $\mathbb { R } ^ { N }$ 表示隐式潜在状态， $A \in \mathbb { R } ^ { N \times N }$ 表示状态转移矩阵，$B \in \mathbb { R } ^ { N \times 1 }$ 和 $\boldsymbol { C } \in \mathbb { R } ^ { 1 \times N }$ 分别表示输入到状态和状态到输出的映射矩阵。

由于传统 SSM 只能处理连续数据，而深度学习任务中不仅包含连续输入，还包含离散输入，因此为了适应深度学习的应用需求，通过零阶保持技术（Zero-Order Hold, ZOH）将连续 SSM 转化为离散 SSM。这样，输入与输出之间的映射从函数间的关系 $x ( t ) \longrightarrow$ $y ( t )$ 转变为序列间的映射 $x _ { t } {  } y _ { t }$ 。具体而言，引入时间尺度参数，通过固定的离散化规则将矩阵𝐴和 $B$ 转换为离散参数，公式如下：

其中， $\begin{array} { r } { \hat { \boldsymbol { A } } = \exp ( \Delta \boldsymbol { A } ) } \end{array}$ ， $B = ( \Delta A ) ^ { - 1 } ( \exp ( \Delta A ) - I ) \cdot$ $\Delta B$ 。在离散化后，基于 SSM 的模型可以通过全局卷积进行计算：

$$
y = x * { \bar { K } } , { \bar { K } } = ( C B , C A B , \ldots , C A ^ { L - 1 } B )
$$

该设计不仅实现了对全局特征的高效提取，同时显著降低了计算复杂度，使得模型在大规模数据处理任务中更为轻量化。此外，Mamba 设计了一种数据驱动的参数选择机制，根据输入数据对 SSM 参数 $\Delta , A , B , C$ 进行动态调整，从而实现对信息的选择性处理。此自适应机制显著提升了模型的计算效率与准确性。此外，Mamba 还引入硬件感知算法，通过循环计算与参数优化减少冗余计算，从而显著加速了模型的运算速度。

在后续实验中，将分辨率为 $3 8 4 \times 3 8 4$ 的 2D 图像样本划分为大小为 4 的补丁并进行序列化处理，生成了约 92000 个令牌。而在相同令牌数量下，Transformer 的计算复杂度为 $O ( N ^ { 2 } )$ ，即随着令牌数量 $N$ 的增加，其复杂度迅速增长到约为 8464000000。相比之下，Mamba模块的线性计算复杂度 $O ( N )$ 显著降低了计算开销，且依然能够保持对长序列的有效关联能力。因此，在图像伪造检测任务中，Mamba 模块成为了 Transformer 的有力替代方案，既提升了检测性能，又减少了计算成本。

# 2.1.2 ConvNeXt 分支

在图像篡改检测任务中，数据集通常规模较小，实验表明，若直接使用未经过预训练的 CNN 模型，容易导致模型难以收敛，从而严重降低训练效率。为了解决这一问题，本文选择了基于在 ImageNet-1k 数据集上预训练的 ConvNeXt-S 模型，用于提取图像的局部特征。ConvNeXt 是对经典 ResNet 模型的改进版本。相比于 ResNet，ConvNeXt 通过引入层级均一化和深度可分离卷积，显著减少了模型的参数量，同时提升了训练的稳定性和效率。此外，ConvNeXt 采用了细粒度的阶段划分，逐层调整卷积核的大小和网络宽度，使模型能够灵活适应不同尺度的特征提取需求，这对于定位和识别图像中的细微篡改痕迹至关重要。

ConvNeXt 的特征提取过程被划分为四个阶段，每个阶段负责提取不同层级的特征。具体而言：首先对输入图像 $\boldsymbol { X } \in \mathbb { R } ^ { H \times W \times C }$ 使用 $4 { \times } 4$ 卷积操作进行初步特征提取。在后续的第二、第三和第四阶段，每个阶段都对上一阶段的特征进行 $7 { \times } 7$ 卷积操作，逐步提取更高级的特征。输出特征图的尺寸依次为：第一阶段 $\mathrm { U } _ { 1 } \in \mathbb { R } ^ { 2 5 6 \times 2 5 6 \times 9 6 }$ 、第二阶段 $\mathrm { U } _ { 2 } \in \mathbb { R } ^ { 1 2 8 \times 1 2 8 \times 1 9 2 }$ 和第三阶段 $\mathrm { U } _ { 3 } \in \mathbb { R } ^ { 6 4 \times 6 4 \times 3 8 4 }$ 。这些多层次特征通过跳跃连接与 Mamba 分支的特征相结合，并传递到SE Block 进行后续的特征强化和融合处理。特征提取的过程可以用以下公式表示：

$$
\begin{array} { r l } & { \left( F _ { s t e m } ^ { 0 } = \mathrm { U } _ { 0 } \big ( x _ { c n n \_ i n } \big ) \in \mathbb { R } ^ { \frac { H } { 4 } \times \frac { W } { 4 } \times C } \right. } \\ & { \left. \right. F _ { s t a g e 1 } ^ { 1 } = \mathrm { U } _ { 1 } ( F _ { s t e m } ^ { 0 } ) \in \mathbb { R } ^ { \frac { H } { 4 } \times \frac { W } { 4 } \times C } } \\ & { \left. \right. F _ { s t a g e 2 } ^ { 2 } = \mathrm { U } _ { 2 } \big ( F _ { s t a g e 1 } ^ { 1 } \big ) \in \mathbb { R } ^ { \frac { H } { 8 } \times \frac { W } { 8 } \times 2 C } } \\ & { \left. \right. \left. F _ { s t a g e 3 } ^ { 3 } = \mathrm { U } _ { 3 } \big ( F _ { s t a g e 2 } ^ { 2 } \big ) \in \mathbb { R } ^ { \frac { H } { 1 6 } \times \frac { W } { 1 6 } \times 4 C } \right. } \end{array}
$$

# 2.2 SE Block

在传统的 U-Net[26]结构中，跳跃连接通常将编码器特征和解码器特征直接拼接，但这种方式可能会引入冗余信息，增加不必要的计算开销，削弱模型对伪造区域的敏感度，影响检测精度。本文针对这一问题，引入了 Squeeze-and-Excitation（SE）通道注意力模块，旨在通过自适应调整特征通道的权重，优化特征融合过程，从而减少冗余信息的干扰，提高模型对关键特征的关注度，提升伪造检测的性能。SE 模块通过三个主要步骤（压缩、激励、缩放）来优化特征图：

首先，尺寸相同的 Mamba 和 ConvNeXt 分支的特征图在经过跳跃连接传递之前，通过 SE Block 中的全局平均池化操作，对每个通道进行压缩。经过压缩后，每个通道变成一个标量值，生成尺寸为 $1 \times 1 \times \mathrm { C }$ 的全局特征向量𝑧。这一全局特征向量反映了每个通道在整个特征图中的平均响应，压缩的过程如公式（6）：

$$
\begin{array} { r } { z _ { c } = F _ { s q } ( \mathbf { u } _ { c } ) = \frac { 1 } { H \times W } { \sum _ { i = 1 } ^ { H } } \sum _ { j = 1 } ^ { W } u _ { c } \left( i , j \right) } \end{array}
$$

接下来， $z$ 通过两个全连接层，首先通过权重矩阵${ \pmb w } _ { 1 }$ 进行维度缩减，然后再通过权重矩阵 ${ \pmb W } _ { 2 }$ 恢复为原始通道维度，生成了权重向量 $\mathbf { \sigma } _ { s }$ 。这一过程决定了哪些特征通道在接下来的步骤中将被放大或抑制，表达式为：$s = F _ { e x } ( z , W ) = \sigma ( g ( z , W ) ) = \sigma ( W _ { 2 } \delta ( W _ { 1 } z ) )$ (7)

其中， $\delta$ 表示 ReLU 激活函数， $\sigma$ 表示 siqmoid 激活函数。权重向量𝑠能够自适应地增强关键特征通道。

最后， $s$ 与原始的特征图逐通道相乘得到新的特征图 $\widetilde { \mathbf { u } } _ { c }$ ，其增加了关键特征通道的权重值。随后，这个特征图通过跳跃连接传递给解码器，进行进一步的伪造检测。其表达式为：

$$
\widetilde { \pmb { u } } _ { c } = F _ { s c a l e } ( \pmb { u } _ { c } , s _ { c } ) = s _ { c } \pmb { u } _ { c }
$$

增强后的特征图通过跳跃连接传递给解码器，以进一步提升模型的伪造检测效果。

这种机制使得 SE 模块能够增强对伪造区域特征的敏感度，并提高伪造检测的准确性，尤其是在图像细节和背景信息复杂的情况下。此外，SE 模块通过减少冗余信息的干扰，提高了计算效率，有助于提升模型的整体性能。

![](images/36f029f34052290ae5d92bdb2cb2f590a5927afd638e7863bc68373b25931114.jpg)  
图 3  SE Block 结构图Fig.3 SE Block structure diagram

# 2.3 模型损失

在图像篡改检测中，损失函数的设计直接影响模型对伪造区域的定位精度。本文的损失函数由伪造区域的分割损失和边缘损失两部分组成，分割损失用于度量模型预测的伪造区域与真实标注区域之间的差异，而边缘损失则对伪造区域的边界进行约束，以增强模型对细节边界的检测精度。

首先，分割损失采用了二元交叉熵损失（BCE），该损失函数衡量模型预测的伪造区域概率图 $P$ 与真实标注掩码 $M$ 之间的像素级误差。BCE 损失在伪造区域的整体检测中表现稳定，具体公式如下：

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { L _ { i } = M _ { i } \mathrm { l o g } ( P _ { i } ) + ( 1 - M _ { i } ) \mathrm { l o g } ( 1 - P _ { i } ) } \\ { \mathrm { B C E } ( P , M ) = - \frac { 1 } { N } \sum _ { i = 1 } ^ { N } L _ { i } } \end{array} \right. } \end{array}
$$

其中， $N$ 为图像中的总像素数。

为了进一步提升对伪造区域边界的检测精度，本文引入了边缘损失。边缘损失通过对伪造区域边缘的提取与约束，使模型更关注伪造区域的边界特征，从而提升边界定位的准确性。具体而言，边缘损失通过数学形态学操作提取伪造区域的边缘掩码，计算模型预测边缘与真实边缘之间的差异，公式如下：

$$
\begin{array} { r } { \mathrm { E L } = \frac { 1 } { \mathrm { N } } \sum _ { \mathrm { i = 1 } } ^ { \mathrm { N } } \left| \mathrm { P } _ { \mathrm { i } } ^ { ' } \ - \mathrm { M } _ { \mathrm { i } } ^ { ' } \ \right| } \end{array}
$$

其中， $\boldsymbol { \mathrm { ~ P ~ } ^ { \prime } }$ ′和M′分别表示模型预测的边缘掩码和真实边缘掩码。

最终，本文的损失函数通过将分割损失和边缘损失结合，形成一个联合损失函数，以提升整体检测的精度和鲁棒性，具体公式如下：

$L$ $= \operatorname { B C E } ( P , M ) + \lambda$ $\cdot \ \mathrm { E d g e } \ \mathrm { L o s s } \left( P ^ { ' } , M ^ { ' } \right)$

其中， $\lambda$ 为超参数，用于平衡分割损失和边缘损失之间的权重。通过该联合损失函数，模型不仅能够准确检测伪造区域，还能够精确定位伪造区域的边界，进一步提升检测效果。

# 3  实验结果与分析

为了全面验证所提出方法的有效性，本研究设计了对比实验、消融实验及鲁棒性评估。对比实验用于将本方法与现有主流方法进行比较，以验证其性能提升情况；消融实验旨在分析各个组件对整体性能的贡献；鲁棒性评估则探讨模型在常见后处理操作下的稳定性，以测试其在实际应用场景中的可靠性。

# 3.1 实验设置

在本研究中，模型的训练和测试都在 NVIDIAGeForce RTX 3090 GPU 进行。使用 AdamW 优化器，学习率为 0.0001，学习率按照“余弦衰减(Cosine De-cay)”的策略进行调整，在训练过程中，每个 GPU 的批量大小设置为 1，并应用了累积批量策略，总批量大小为 32，共训练 200 个周期，训练时采用了早停技术。为了在预处理中保留图像的关键细节，本文通过零填充将图像调整为尺寸 1024x1024 的统一大小。

# 3.2 数据集

本研究选择CASIAv2[27] 数据集进行模型训练，主要因为其包含多种伪造方式（如拼接、复制-粘贴等）、较高的图像质量和准确的标签标注，能够帮助模型学习到丰富的伪造特征。CASIAv2 数据集包含 12554张图像，其中 7491 张为真实图像，5063 张为篡改图像，数据规模较大，尽管真实与伪造图像数量不完全均衡，但其多样性为模型提供了充足的训练样本，有助于提升特征学习能力和检测性能。

然而，CASIAv2 数据集也可能存在一定的偏差，主要体现在其伪造方式的局限性。该数据集的伪造方式主要集中于拼接和复制-粘贴等简单伪造方法，而对如深度伪造等复杂伪造方式的覆盖较少，这可能会影响模型在其他伪造方式上的表现。为全面评估模型的泛化能力和鲁棒性，我们在 CASIAv1[27]、COVERAGE[28]、

Columbia[29]和 NIST16[30]等四个数据集上进行了测试。这些数据集的伪造方式和图像质量均有所不同，能够有效评估模型在多样化伪造方式下的表现。

所有数据集在使用前均进行了标准化处理，包括图像尺寸调整和像素值归一化，以确保统一的输入格式。通过跨数据集的测试，我们验证了模型的鲁棒性，减少了数据集偏差的影响。

# 3.3 评价指标

图像篡改区域定位本质上是一个像素级的二元分类问题，本研究采用了两种常用的像素级分类指标来评估模型的性能：AUC（Area Under the ROC Curve）和 F1。AUC 表示接收者操作特性曲线（ROC 曲线）下的面积。高的 AUC 值通常表示模型具有良好的区分假元素和真实元素的能力。F1 分数是精确率（Precision）和召回率（Recall）的调和平均数。它的取值范围为 0-1 与 AUC 一致，值越大表示模型的性能越好。由于图像篡改检测任务中通常存在类别不平衡问题，F1 分数能够有效反映模型在实际应用中的性能F1 的计算公式如下：

$$
\begin{array} { r } { F 1 = 2 \times \frac { P r e c i s i o n \times R e c a l l } { P r e c i s i o n + R e c a l l } } \end{array}
$$

由于对篡改概率图进行二值化操作时，选择不同的概率阈值会直接影响分类结果，从而影响精确率、召回率和最终的 F1 分数。先前的工作通过验证集进行实验并绘制精确率-召回率曲线或 ROC 曲线的性能图，根据分析曲线图找到最佳的阈值。由于哪个阈值是最佳的在实际应用中是未知的，而总是对多个真实数据进行多次试验来找到最佳阈值，在实际应用中并不实用。为了更接近真实场景，在本研究中参考前人[31]的方法选择使用固定的阈值 0.5 来计算 F1 分数。

# 3.4 对比实验

泛化性是深度学习任务目前所面临的一个重要挑战，具有优秀泛化能力的图像伪造检测模型需要具备在输入未知的数据的时候依然能够获得准确的检测结果。为了测试文中所提出方法的泛化性，本文所提出的方法与 MVSS-Net 和 IML-ViT 两个目前性能最优的方法在四个不同的数据集上的性能对比如表 2 表 3 所示，其中最佳值以粗体标记。

表 2  与 SOTA 模型在四个数据集上 F1 的比较Table 2  Comparison of F1 scores with SOTA models acrossfour datasets  

<html><body><table><tr><td>模型</td><td>CASIAv1</td><td>Coverage</td><td>Columbia</td><td>NIST16</td></tr><tr><td>MVSS-Net</td><td>0.418</td><td>0.411</td><td>0.601</td><td>0.268</td></tr><tr><td>IML-ViT</td><td>0.686</td><td>0.379</td><td>0.690</td><td>0.299</td></tr></table></body></html>

<html><body><table><tr><td>Ours</td><td>0.781</td><td>0.431</td><td>0.752</td><td>0.308</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr></table></body></html>

表 3  与 SOTA 模型在四个数据集上 AUC 的比较Table 3  Comparison of AUC scores with SOTA modelsacross four datasets  

<html><body><table><tr><td>模型</td><td>CASIAv1</td><td>Coverage</td><td>Columbia</td><td>NIST16</td></tr><tr><td>MVSS-Net</td><td>0.882</td><td>0.851</td><td>0.814</td><td>0.587</td></tr><tr><td>IML-ViT</td><td>0.953</td><td>0.825</td><td>0.908</td><td>0.770</td></tr><tr><td>Ours</td><td>0.976</td><td>0.853</td><td>0.915</td><td>0.775</td></tr></table></body></html>

从表 2 可以看出，我们提出的方法相比较于先前的方法在 CASIAv1、Coverage、Columbia 以及 NIST16数据集上均得到了最佳的结果，与次优模型 IML-ViT的 F1 相比，文中的方法在 Coverage、Columbia、NIST16数据集上分别提升了约 $5 . 2 \%$ 、 $6 . 2 \%$ 和 $0 . 9 \%$ ，而在CASIAv1 数据集中表现最为优越，F1 指标提升了约$9 . 5 \%$ 。此外，从表 3 可以看出文中的方法在所有测试数据集上 AUC 指标均达到了最优秀的结果，相比较于IML-ViT 分别提高了大约 $2 . 3 \% { , 2 . 8 \% , 0 . 7 \% , 0 . 5 \% }$ 。实验发现，模型在 CASIAv1 和 Coverage 数据集上的性能优势更为显著，而在 Columbia 和 NIST16 数据集上的提升幅度相对有限。经溯源分析，这种差异源于数据集间的域偏移问题：Columbia 和 NIST16 的伪造图像在生成风格与篡改多样性方面与训练集CASIAv2存在显著差异（如纹理合成算法、后处理手段等），导致所有对比模型的泛化性能均受到制约。尽管如此，本模型仍通过多尺度特征融合机制在核心指标上保持稳定优势，证明其具有更强的域适应能力最后，伪造检测任务本身具有较高的复杂性，尤其是在处理高质量伪造图像时，伪造痕迹可能非常细微，因此即使是微弱的提升也可能意味着模型在捕捉这些细微特征方面具有优势。但这些微弱的提升在实际应用中仍具有重要意义。例如，在司法鉴定中，即使是 $0 . 9 \%$ 的 F1 提升也可能显著减少误判的可能性。这一结果得益于双分支结构的多尺度特征融合能力。相比之下，MVSS-Net 由于缺乏全局特征捕捉能力,导致其在处理大尺度伪造区域时表现欠佳；IML-ViT 虽然在全局特征上有所提升，但在细节捕捉方面略显不足。这验证了我们模型在全局一致性和局部细节兼顾上的优势。

从表 4 可以看到，IML-ViT 相较于 MVSS-Net，在参数量上减少了约 $3 7 . 5 \%$ ，计算复杂度降低了 $1 5 . 3 \%$ 。然而，由于 Transformer 结构的自注意力机制需要处理大量的特征块，即使进行了优化，IML-ViT 的计算资源消耗仍然较高，限制了其在资源受限环境中的应用。例如，在便携式数字取证设备中，执法人员往往需要在现场快速分析伪造图像，但受限于设备计算能力，IML-ViT 仍然难以满足实时性要求。此外，在社交媒体平台的内容审核任务中，需要高效筛查海量用户上传的图像，而高计算量的模型可能会增加服务器负担，影响检测效率。相比之下，本文提出的方法在保持精度的前提下，显著降低了参数量和计算复杂度。具体来说，与 IML-ViT 相比，本文提出的方法参数量减少了约 $50 \%$ ，每秒浮点运算数降低了 $9 . 3 4 \%$ 。这使得本研究的方法更适用于这些资源受限的应用场景。

表 4  模型参数量以及计算量分析比较Table 4  Analysis and comparison of model parameters andcomputational complexity  

<html><body><table><tr><td>模型</td><td>参数量</td><td>每秒浮点运算</td></tr><tr><td rowspan="3">MVSS-Net IML-ViT</td><td>146.88M</td><td>681.15G</td></tr><tr><td>91.78M</td><td>576.73G</td></tr><tr><td>41.69M</td><td>522.82G</td></tr></table></body></html>

为了更直观地展示实验结果，在表 2 和表 3 的基础上，本文对不同模型在四个数据集上的检测结果进行了可视化分析（如图 4 所示）。可以看出，相较于目前最先进的方法，本研究提出的模型在定位伪造区域方面表现出更高的精确性。可见文中的方法能够充分的利用图像的全局特征和局部特征，同时文中的方法对图像修改区域的边界识别效果也更好，这主要得益于在模型中引入的边缘损失，改善了边界识别效果使得边缘的分割更加精细化。

具体而言，在 CASIAv1 数据集（图 4(a)）上，本文方法通过全局和局部特征的融合，实现了更准确的伪造区域检测，而 MVSS-Net 和 IML-ViT 分别在边缘清晰度和细节捕捉上有所欠缺。图 4（b）的预测结果可以得出文中的方法对比其他两种方法在区域边缘识别的效更好检测的区域也更加准确。图 4(c) 的伪造区域较为复杂，其他两种方法均出现了明显的误检和边界不连续现象。MVSS-Net 对全局特征提取不足，导致伪造区域检测不完整；而 IML-ViT 虽然能捕捉部分全局特征，但对复杂边界的处理能力有限，但是本文提出的方法仍然可以得到较为准确的伪造区域。图4(d)中的篡改区域比较小，检测难度更大，IML-ViT 在该场景中对小区域的捕捉能力不足，而 MVSS-Net 在边缘区域出现模糊。相比之下，本文方法在小尺度区域的检测中依然保持了良好的表现，准确定位了小伪造区域的位置和边界。

# 3.5 消融实验

为了验证各个子模块对于网络性能的影响，本文对各个模块在 CASIAv1 公开数据集上进行了消融实验。并使用 F1 分数和 AUC 作为评估指标。实验结果如表 5 所示。“-”表示在对应的实验中移除了该模块。

可以看出，去掉各个子模块后网络的 F1 和 AUC指标均有所下降。其中，移除 Mamba 后， F1 分数和AUC 值分别为 0.694，0.874。相比于完整的网络下降了大约 $8 . 7 \%$ ， $5 \%$ 。这表明 Mamba 在捕捉全局特征方面起到了关键作用，没有 Mamba，模型难以有效识别全局图像伪造痕迹。此外，由于图像伪造检测任务的公开数据集具有尺寸大、信息丰富和特征复杂的特点，且数据集规模较小，无法满足原生 ConvNeXt 对于数据量的需求，从表 5 中的实验结果可以看出，使用未预训练过的 ConvNext 模型会导致完全不收敛。然而，在使用经ImageNet-1k 数据集上预训练过的ConvNeXt后， F1 指标从 0.214 大幅提升至 0.781，AUC 分数从0.296 提升至 0.976。移除 ConvNeXt 后，模型缺乏对细节的敏感度，导致性能大幅度下降。F1 和 AUC 指标相比于完整的网络下降了大约 $52 \%$ ， $62 \%$ 。这说明单一的全局特征在图像伪造检测任务中是不够的。移除 SE Block 后，F1 和 AUC 指标相比于完整的网络降低了大约 $4 \%$ ， $3 . 9 \%$ 。这表明 SE Block 在特征融合方面发挥了重要作用，缺少 SE Block 会导致模型无法有效地整合局部和全局信息，从而影响检测精度。移除Edge Loss 后，F1 和 AUC 的指标也都受到了影响，相比较于完整的网络下降了大约 $6 . 9 \%$ ， $5 . 2 \%$ 。其证明了边缘监督策略的有效性，它增强了模型对边缘伪造痕迹的检测能力，使得模型能够更好地捕捉伪造区域的边界特征。

Table 5  Quantitative evaluation results of ablation studies   

<html><body><table><tr><td></td><td>预训练模型</td><td>Mamba</td><td>ConvNext</td><td></td><td>edge supervision</td><td>SE</td><td>F1</td><td>AUC</td></tr><tr><td>w/o Mamba</td><td>ConvNext ImageNet-1k</td><td></td><td></td><td>+</td><td>+</td><td>+</td><td>0.694</td><td>0.874</td></tr><tr><td>w/o ConvNext pretrain</td><td></td><td>十</td><td></td><td>+</td><td>+</td><td>+</td><td>0.214</td><td>0.296</td></tr><tr><td>w/o ConvNext</td><td></td><td></td><td></td><td></td><td>+</td><td>+</td><td>0.253</td><td>0.356</td></tr><tr><td>w/o edge supervision</td><td>ConvNext ImageNet-1k</td><td></td><td></td><td>+</td><td></td><td>+</td><td>0.712</td><td>0.924</td></tr><tr><td>W/o SE</td><td>ConvNext ImageNet-1k</td><td>+</td><td></td><td>+</td><td>+</td><td></td><td>0.741</td><td>0.937</td></tr><tr><td>Full set</td><td>ConvNext ImageNet-1k</td><td>X</td><td></td><td>+</td><td>+</td><td>+</td><td>0.781</td><td>0.976</td></tr></table></body></html>

![](images/953fe39b9884632514e5671bca1c08dab8471a4df3d388a8860f611308fbada6.jpg)

# 图 4  针对四个数据集的对比试验可视化

Fig.4  Visualization of comparative experiments across four datasets

# 3.6 模型鲁棒性分析

为了评估文中方法的鲁棒性，通过在 CASIAv1 数据集上进行实验，应用了高斯模糊和 JPEG 压缩这两种常见的后处理操作，并使用 F1 分数和 AUC 作为评估指标。在高斯模糊鲁棒性测试实验中，使用了（5、11、17）3 种不同的卷积核大小来模拟不同程度的模糊效果。对于 JPEG 压缩攻击，在实验中设置了（100、75、50）三种不同压缩质量。结果如表 6，表 7 所示，无论是在高斯模糊还是 JPEG 压缩攻击下，本文方法的双分支结构和 SE 模块在不同尺度特征的融合上更具自适应性，使得模型在模糊或压缩的攻击下依然能够保持稳定的检测性能。

Table 6  Robustness analysis of Gaussian blur   
表 7  JPEG 压缩鲁棒性分析  

<html><body><table><tr><td>方法</td><td>Kernel</td><td>F1</td><td>AUC</td></tr><tr><td rowspan="3">MVSS-Net</td><td>5</td><td>0.406</td><td>0.879</td></tr><tr><td>11</td><td>0.258</td><td>0.867</td></tr><tr><td>17</td><td>0.197</td><td>0.841</td></tr><tr><td rowspan="3">IML-ViT</td><td>5</td><td>0.681</td><td>0.948</td></tr><tr><td>11</td><td>0.592</td><td>0.931</td></tr><tr><td>17</td><td>0.326</td><td>0.917</td></tr><tr><td rowspan="3">Ours</td><td>5</td><td>0.776</td><td>0.973</td></tr><tr><td>11</td><td>0.627</td><td>0.956</td></tr><tr><td>17</td><td>0.412</td><td>0.934</td></tr></table></body></html>

表 6  高斯模糊鲁棒性分析  
Table 7  Robustness analysis of JPEG compression   

<html><body><table><tr><td>方法</td><td>Quality</td><td>F1</td><td>AUC</td></tr><tr><td rowspan="3">MVSS-Net</td><td>100</td><td>0.418</td><td>0.882</td></tr><tr><td>75</td><td>0.403</td><td>0.875</td></tr><tr><td>50</td><td>0.394</td><td>0.861</td></tr><tr><td rowspan="3">IML-ViT</td><td>100</td><td>0.686</td><td>0.953</td></tr><tr><td>75</td><td>0.659</td><td>0.947</td></tr><tr><td>50</td><td>0.543</td><td>0.939</td></tr><tr><td rowspan="3">Ours</td><td>100</td><td>0.781</td><td>0.976</td></tr><tr><td>75</td><td>0.762</td><td>0.971</td></tr><tr><td>50</td><td>0.673</td><td>0.962</td></tr></table></body></html>

# 4  结束语

本研究提出的双分支编码器模型成功结合了Mamba 的全局特征捕获能力和 ConvNeXt 的局部特征提取能力，优化了特征捕获的全面性，降低了计算复杂度。通过在编码器之间引入 SE Block，模型能够更准确地聚焦关键伪造特征，提升了特征选择的精确度。此外，联合损失策略增强了模型对伪造区域的定位能力和边缘检测的准确度。通过在多个公开数据集上的测试结果表明，该模型在伪造检测方面优于现有的主流方法。

虽然本文在现有公开数据集上取得了不错的表现，但本文仍主要针对二维图像伪造篡改检测，在应用于视频、多模态数据、三维/多光谱图像等复杂场景时，可能存在性能瓶颈。其在复杂数据形式下的有效性和鲁棒性仍需深入研究。同时现有实验依赖的数据集可能与真实应用场景（如工业界、社交媒体）存在偏差。训练数据篡改类型可能单一，图像质量偏高，而真实场景图像降质复杂。 这种数据集偏差可能影响方法在真实复杂场景下的性能。针对以上，本文将进一步探索和提升模型的泛化性，以增强模型在多模态、多源数据集上伪造检测的能力。

# 参考文献:

[1] ZHAI Y, LUAN T, DOERMANN D, et al. Towards generic image manipulation detection with weakly-supervised self- consistency learning[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision, 2023: 22390- 22400. [2] ZANARDELLI M, GUERRINI F, LEONARDI R, et al. Image forgery detection: a survey of recent deep-learning approaches[J]. Multimedia Tools and Applications, 2023, 82(12): 17521-17566.   
[3] GUO Y, JIANG S. A neural network model with the ringed residual block and attention mechanism for image forgery localization[C]//International Conference on Image and Graphics, 2023: 99-110.   
[4] BI X, WEI Y, XIAO B, et al. RRU-Net: The ringed residual U-Net for image splicing forgery detection[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops, 2019: 1-6.   
[5] KWON M J, YU I J, NAM S H, et al. CAT-Net: Compression artifact tracing network for detection and localization of image splicing[C]//Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision, 2021: 375-384.   
[6] WU Y, ABDALMAGEED W, NATARAJAN P. Mantra-Net: Manipulation tracing network for detection and localization of image forgeries with anomalous features[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2019: 9543-9552.   
[7] WEI Y, MA J, WANG Z, et al. Image splicing forgery detection by combining synthetic adversarial networks and hybrid dense U‐Net based on multiple spaces[J]. International Journal of Intelligent Systems, 2022, 37(11): 8291-8308.   
[8] ZHU H, CAO G, ZHAO M, et al. Effective image tampering localization with multi-scale ConvNext feature fusion[J]. Journal of Visual Communication and Image Representation, 2024, 98: 103981.   
[9] DONG C, CHEN X, HU R, et al. MVSS-Net: Multi-view multi-scale supervised networks for image manipulation detection[J]. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2022, 45(3): 3539-3553.   
[10] YANG Z, LIU B, BI X, et al. D-Net: A dual-encoder network for image splicing forgery detection and localization[J]. Pattern Recognition, 2024, 155: 110727.   
[11] GUO X, LIU X, REN Z, et al. Hierarchical fine-grained image forgery detection and localization[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2023: 3155-3165.   
[12] VASWANI A, SHAZEER N, PARMAR N, et al. Attention is all you need[J]. Advances in Neural Information Processing Systems, 2017, 30.   
[13] WANG J, WU Z, CHEN J, et al. ObjectFormer for image manipulation detection and localization[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2022: 2364-2373.   
[14] HAO J, ZHANG Z, YANG S, et al. Transforensics: Image forgery localization with dense self-attention[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision, 2021: 15055-15064.   
[15] MA X, DU B, LIU X, et al. IML-ViT: Image manipulation localization by vision transformer[J]. arXiv preprint arXiv: 2307.14863, 2023.   
[16] LIU Z, NING J, CAO Y, et al. Video Swin Trans- former[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2022: 3202-3211.   
[17] LIN X, WANG S, DENG J, et al. Image manipulation detection by multiple tampering traces and edge artifact enhancement[J]. Pattern Recognition, 2023, 133: 109026.   
[18] MA J, LI F, WANG B. U-mamba: Enhancing long-range dependency for biomedical image segmentation[J]. arXiv preprint arXiv:2401.04722, 2024.   
[19] GU A, DAO T. Mamba: Linear-time sequence modeling with selective state spaces[J]. arXiv preprint arXiv:2312.00752, 2023.   
[20] ZHANG M, YU Y, JIN S, et al. VM-UNET-V2: Rethinking Vision Mamba UNet for Medical Image Segmentation[C]//International Symposium on Bioinformatics Research and Applications, 2024: 335-346.   
[21] HU J, SHEN L, SUN G. Squeeze-and-excitation networks[C]//Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2018: 7132-7141.   
[22] LIU Z, MAO H, WU C Y, et al. A ConvNet for the 2020s[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2022: 11976-11986. [23] YUAN F, ZHANG Z, FANG Z. An effective CNN and Transformer complementary network for medical image segmentation[J]. Pattern Recognition, 2023, 136: 109228.   
[24] ARKIN E, YADIKAR N, XU X, et al. A survey: Object detection methods from CNN to transformer[J]. Multimedia Tools and Applications, 2023, 82(14): 21353-21383.   
[25] WU R, LIANG P, HUANG X, et al. Automatic skin lesion segmentation based on higher-order spatial interaction model[C]//2023 IEEE International Conference on Medical Artificial Intelligence (MedAI), 2023: 447-452.   
[26] RONNEBERGER O, FISCHER P, BROX T. U-Net: Convolutional networks for biomedical image segmentation[C]// Medical Image Computing and Computer-Assisted Intervention – MICCAI 2015: 18th International Conference, Munich, Germany, October 5-9, 2015, Proceedings, Part III 18, 2015: 234- 241.   
[27] DONG J, WANG W, TAN T. CASIA image tampering detection evaluation database[C]//2013 IEEE China Summit and International Conference on Signal and Information Processing, 2013: 422-426.   
[28] WEN B, ZHU Y, SUBRAMANIAN R, et al. COVERAGE—A novel database for copy-move forgery detection[C]//2016 IEEE International Conference on Image Processing (ICIP), 2016: 161-165.   
[29] HSU Y F, CHANG S F. Detecting image splicing using geometry invariants and camera characteristics consistency[C]// 2006 IEEE International Conference on Multimedia and Expo, 2006: 549-552.   
[30] GUAN H, KOZAK M, ROBERTSON E, et al. MFC datasets: Large-scale benchmark datasets for media forensic challenge evaluation[C]//2019 IEEE Winter Applications of Computer Vision Workshops (WACVW), 2019: 63-72.   
[31] GUILLARO F, COZZOLINO D, SUD A, et al. Trufor: Leveraging all-round clues for trustworthy image forgery detection and localization[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2023: 20606- 20615.