from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Imputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
import jieba
import numpy as np
#
# 特征抽取
#
# 导入包
from sklearn.feature_extraction.text import CountVectorizer

# 实例化CountVectorizer

vector = CountVectorizer()

# 调用fit_transform输入并转换数据

res = vector.fit_transform(['''E7820.(a) Monodisperse peak of the complex by gel filtration. The red bar indicates the fraction used for the Coomassie-stained SDS-PAGE gel, shown to the right of the trace. Gel filtration of the complex was repeated at least three times with similar results. (b) Reference-free 2D class averages. The class average highlighted with a green box has signal for the three p-propellers of DDBI and DCAF15, however only B-propellers A and C of DDBl(outlined with a white hatched line)are aligned well, due to the inherent flexibility of DDBl B-propeller B and DCAF15 (c)Representative cryo-EM micrograph at-2.3 um defocus Scale bar indicates 20 nm.
Data collection was performed one time on this sample. (d)Recor highlighting the density for DDBl B-propeller A, DDBl B-propeller C, and DCAF15 at an average resolution of 10 A. (e)The DDBlAB-DCAF15-DDA1-RBM39RRM2 complex bound to E7820 complex displays a monodisperse gel filtration peak after BS3 cross-linking. The higher molecular weight cross-linked complex(180 kDa)is indicated on the SDS-PAGe gel to the right. Cross-linking and gel filtration of this complex was performed at least three times with similar results. (f) Representative micrograph of the DDAl-containing complex imaged with a Volta phase plate(VPP)at-1.I um defocus Scale bar represents 20 nm. Data collection was erformed on this complex from two independent grids over the course of four imaging sessions
(g)Reference-free 2D class averages. (h)Data processing scheme for the crosslinked DDBIAB-
DCAF15-DDAl-E7820-RBM39RRM2 complex Initial 2D and 3D classification resulted
923, 678 particles for Ctf Refinement and Bayesian polishing. Three subsequ ds of 3D lassification and refinement improved map resolution to a final average resolution of 4.4 A Percentages refer to the particles in each class. Red density maps indicate the classes that were used for the next round of processing, while blue density maps are from 3D refinements''','''side chain density for multiple residues. Each density in mesh is shown at a threshold of 0.021
(from Chimera).(e)The crystal structure of DDBlAB-DCAFI5splir-DDAl-RBM39RRMz bound to E7820 was docked and real space-refined into the unsharpened cryo-EM map of DDBIAB-
DCAF15-DDAl-RBM39RRM2 bound to E7820 using phenix dock in map and phenix realspace refine. Shown is the crystal structure(in cartoon)fit into the unsharpened cryo EM density(gray surface). The majority of the cryo-EM density is accounted for by the crystal structure, both indicating that the cryo-EM map is also missing the flexible region between the DCAFIS NTD and CTD and that DCAFI5split recapitulates the fold of full-length DCAF15 The cryo-EM density is shown at a threshold of 0.0145 (from Chimera).(f) Density for E7820 in the sharpened
4.4 A cryo-EM reconstruction Shown is the same docked model as in e, and the compound was placed by superimposing the E7820 bound crystal structure demonstrating density for E7820
(yellow)sandwiched between the DCAF15 NTD(blue), DCAFI5 CTD (green), and RBM39RRM(magenta). The sharpened cryo-EM density(B-factor of -129 from relion postprocessing) is shown in grey at a threshold of 0.0247(from Chimera'''])

# 打印结果
print(vector.get_feature_names())

print(res.toarray())
