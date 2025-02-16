from __future__ import division
import jmp_score as jmp
from math import *
import numpy as np


""" ==================================================================
 Copyright(C) 2018 SAS Institute Inc.All rights reserved.
 
 Notice:
 The following permissions are granted provided that the
 above copyright and this notice appear in the score code and
 any related documentation. Permission to copy, modify
 and distribute the score code generated using
 JMP(R) software is limited to customers of SAS Institute Inc. ("SAS")
 and successive third parties, all without any warranty, express or
 implied, or any other obligation by SAS. SAS and all other SAS
 Institute Inc. product and service names are registered
 trademarks or trademarks of SAS Institute Inc. in the USA
 and other countries. Except as contained in this notice,
 the name of the SAS Institute Inc. and JMP shall not be used in
 the advertising or promotion of products or services without
 prior written authorization from SAS Institute Inc.
 ================================================================== """

""" Python code generated by JMP v14.1.0 """

def getModelMetadata():
	return {"creator": u"Neural", "modelName": u"", "predicted": u"IC50", "table": u"central_nervous_system", "version": u"14.1.0", "timestamp": u"2019-07-23T02:35:19Z"}


def getInputMetadata():
    return {
        u"CLS_Histology_subtype_1_astrocytoma_Grade_III": "float",
        u"EXP_CAMK1": "float",
        u"EXP_CLK4": "float",
        u"EXP_MAP3K20": "float",
        u"EXP_MAPK1": "float",
        u"EXP_STRADB": "float",
        u"EXP_TBK1": "float",
        u"EXP_TRIM33": "float",
        u"EXP_TRPM7": "float",
        u"GO_0007166_CSV": "float",
        u"GO_0008283": "float",
        u"GO_0008283_EXP": "float",
        u"GO_0010506": "float",
        u"GO_0016572": "float",
        u"GO_0030509_EXP": "float",
        u"GO_0032147_CSV": "float",
        u"GO_0050766_CSV": "float",
        u"GO_0071560": "float",
        u"MUT_EIF2AK1": "float",
        u"PWY_R_HSA_1852241_EXP": "float",
        u"PWY_R_HSA_453279": "float",
        u"REC_R_HSA_450346": "float",
        u"SFAM_DYRK1": "float"
	}


def getOutputMetadata():
    return {
        u"Predicted IC50_1": "float"
	}


def score(indata, outdata):
    # H1_1
    # H1_2
    # H1_3
    # H1_4
    # H1_5
    # H1_6
    # H1_7
    # H1_8
    # H1_9
    # H1_10
    # H1_11

    H1_1 = tanh((14.1778963166263 + -0.282291591989242 * indata[u"CLS_Histology_subtype_1_astrocytoma_Grade_III"] + -0.911596895208734 * indata[u"EXP_CAMK1"] + -2.05734660487356 * indata[u"EXP_CLK4"] + 0.764582356782303 * indata[u"EXP_MAP3K20"] + 1.06200101481899 * indata[u"EXP_MAPK1"] + 1.41193846202783 * indata[u"EXP_STRADB"] + -1.6826297471183 * indata[u"EXP_TBK1"] + 0.00807762712388549 * indata[u"EXP_TRIM33"] + -0.773619578465309 * indata[u"EXP_TRPM7"] + -3.34702738894409 * indata[u"GO_0007166_CSV"] + 0.604962679498524 * indata[u"GO_0008283"] + -0.0478904349341261 * indata[u"GO_0008283_EXP"] + 0.265527048604023 * indata[u"GO_0010506"] + 0.461051847567623 * indata[u"GO_0016572"] + -0.100658195624545 * indata[u"GO_0030509_EXP"] + -1.1591655714303 * indata[u"GO_0032147_CSV"] + -2.13917058334244 * indata[u"GO_0050766_CSV"] + -0.902535403340049 * indata[u"GO_0071560"] + 4.41023038667502 * indata[u"MUT_EIF2AK1"] + 0.0753152656148571 * indata[u"PWY_R_HSA_1852241_EXP"] + 0.440571209746764 * indata[u"PWY_R_HSA_453279"] + 1.10111057556482 * indata[u"REC_R_HSA_450346"] + -2.83588179949856 * indata[u"SFAM_DYRK1"]))

    H1_2 = tanh((13.5283847607775 + 0.218494355686838 * indata[u"CLS_Histology_subtype_1_astrocytoma_Grade_III"] + 0.432462710787702 * indata[u"EXP_CAMK1"] + -2.66189474939279 * indata[u"EXP_CLK4"] + -0.095530365121785 * indata[u"EXP_MAP3K20"] + 1.29188296052281 * indata[u"EXP_MAPK1"] + -0.107852074853231 * indata[u"EXP_STRADB"] + -0.260600748052643 * indata[u"EXP_TBK1"] + -1.32040400652771 * indata[u"EXP_TRIM33"] + 0.304257360827284 * indata[u"EXP_TRPM7"] + 0.796219914104088 * indata[u"GO_0007166_CSV"] + 0.532473493152597 * indata[u"GO_0008283"] + -0.0386085367839599 * indata[u"GO_0008283_EXP"] + 0.0737571867080197 * indata[u"GO_0010506"] + 0.124619960905731 * indata[u"GO_0016572"] + 0.160546497591486 * indata[u"GO_0030509_EXP"] + -2.01438532694111 * indata[u"GO_0032147_CSV"] + -0.0932379784574031 * indata[u"GO_0050766_CSV"] + -0.48910679639141 * indata[u"GO_0071560"] + -1.48792513831216 * indata[u"MUT_EIF2AK1"] + -0.0932594873364563 * indata[u"PWY_R_HSA_1852241_EXP"] + -0.711044665885468 * indata[u"PWY_R_HSA_453279"] + -0.196587881967597 * indata[u"REC_R_HSA_450346"] + -0.789054991918558 * indata[u"SFAM_DYRK1"]))

    H1_3 = tanh((-21.0931510926625 + 1.30865952323532 * indata[u"CLS_Histology_subtype_1_astrocytoma_Grade_III"] + 2.02253205310697 * indata[u"EXP_CAMK1"] + 1.31977093942096 * indata[u"EXP_CLK4"] + -0.145975524618035 * indata[u"EXP_MAP3K20"] + 0.858957935862051 * indata[u"EXP_MAPK1"] + -1.41702271537888 * indata[u"EXP_STRADB"] + 0.472450334072479 * indata[u"EXP_TBK1"] + -1.05820272545145 * indata[u"EXP_TRIM33"] + 2.10864482615527 * indata[u"EXP_TRPM7"] + 0.123000527803702 * indata[u"GO_0007166_CSV"] + -0.286658257141046 * indata[u"GO_0008283"] + -0.0906192667994929 * indata[u"GO_0008283_EXP"] + 0.422768568621692 * indata[u"GO_0010506"] + -1.43140096439733 * indata[u"GO_0016572"] + 0.296398522882422 * indata[u"GO_0030509_EXP"] + -0.7843364436081 * indata[u"GO_0032147_CSV"] + 3.80323919063546 * indata[u"GO_0050766_CSV"] + 3.39514867859941 * indata[u"GO_0071560"] + -1.40365217594451 * indata[u"MUT_EIF2AK1"] + 0.094338448047224 * indata[u"PWY_R_HSA_1852241_EXP"] + 1.97177997214452 * indata[u"PWY_R_HSA_453279"] + 1.32389762993615 * indata[u"REC_R_HSA_450346"] + 1.8510676376839 * indata[u"SFAM_DYRK1"]))

    H1_4 = tanh((-15.9902448445545 + 1.13518179390607 * indata[u"CLS_Histology_subtype_1_astrocytoma_Grade_III"] + 0.16926027184091 * indata[u"EXP_CAMK1"] + 0.917518688809652 * indata[u"EXP_CLK4"] + 0.0100030036974579 * indata[u"EXP_MAP3K20"] + 0.536279710470438 * indata[u"EXP_MAPK1"] + -0.747625933305035 * indata[u"EXP_STRADB"] + 1.37083907176638 * indata[u"EXP_TBK1"] + -0.723904808763569 * indata[u"EXP_TRIM33"] + 0.81953501595637 * indata[u"EXP_TRPM7"] + 3.77735234318402 * indata[u"GO_0007166_CSV"] + -0.293090276361385 * indata[u"GO_0008283"] + 0.0817238996221107 * indata[u"GO_0008283_EXP"] + -0.429699730244629 * indata[u"GO_0010506"] + 0.389366568422012 * indata[u"GO_0016572"] + -0.251809706653474 * indata[u"GO_0030509_EXP"] + 0.745634809795392 * indata[u"GO_0032147_CSV"] + 7.10760565469313 * indata[u"GO_0050766_CSV"] + 1.21966172563347 * indata[u"GO_0071560"] + -4.17549639281823 * indata[u"MUT_EIF2AK1"] + 0.292454391718426 * indata[u"PWY_R_HSA_1852241_EXP"] + 0.557389097553724 * indata[u"PWY_R_HSA_453279"] + -0.980725734165447 * indata[u"REC_R_HSA_450346"] + 0.103456109107502 * indata[u"SFAM_DYRK1"]))

    H1_5 = tanh((-19.0340801892818 + 0.389279411995239 * indata[u"CLS_Histology_subtype_1_astrocytoma_Grade_III"] + 0.0473342636399644 * indata[u"EXP_CAMK1"] + 2.55979007404832 * indata[u"EXP_CLK4"] + -0.0421067699836034 * indata[u"EXP_MAP3K20"] + 2.66933686493161 * indata[u"EXP_MAPK1"] + 1.05998643298516 * indata[u"EXP_STRADB"] + 0.154569242783735 * indata[u"EXP_TBK1"] + -0.881368283285227 * indata[u"EXP_TRIM33"] + -1.35646842038918 * indata[u"EXP_TRPM7"] + 2.93293560322935 * indata[u"GO_0007166_CSV"] + -0.300605205083992 * indata[u"GO_0008283"] + -0.0630130713339925 * indata[u"GO_0008283_EXP"] + 0.885870358309246 * indata[u"GO_0010506"] + 1.72006148533664 * indata[u"GO_0016572"] + -0.0250066278340535 * indata[u"GO_0030509_EXP"] + 1.26203696915945 * indata[u"GO_0032147_CSV"] + -4.55776650623271 * indata[u"GO_0050766_CSV"] + 3.93300902729069 * indata[u"GO_0071560"] + -5.26667985777576 * indata[u"MUT_EIF2AK1"] + -0.324719960662561 * indata[u"PWY_R_HSA_1852241_EXP"] + -0.258660556514019 * indata[u"PWY_R_HSA_453279"] + -1.14440519369905 * indata[u"REC_R_HSA_450346"] + 0.4355829186229 * indata[u"SFAM_DYRK1"]))

    H1_6 = tanh((16.5686835373515 + 0.501546420217323 * indata[u"CLS_Histology_subtype_1_astrocytoma_Grade_III"] + -2.154002886198 * indata[u"EXP_CAMK1"] + -1.26157420968642 * indata[u"EXP_CLK4"] + 0.0235120015848207 * indata[u"EXP_MAP3K20"] + -0.571854856140316 * indata[u"EXP_MAPK1"] + 0.424478367182194 * indata[u"EXP_STRADB"] + 0.391969310297082 * indata[u"EXP_TBK1"] + -1.05901739896014 * indata[u"EXP_TRIM33"] + 0.836034052627929 * indata[u"EXP_TRPM7"] + -0.34997986463588 * indata[u"GO_0007166_CSV"] + -0.238975824375939 * indata[u"GO_0008283"] + 0.0529328211502564 * indata[u"GO_0008283_EXP"] + -0.971934189094029 * indata[u"GO_0010506"] + 0.731953173692591 * indata[u"GO_0016572"] + 0.208265333784553 * indata[u"GO_0030509_EXP"] + -0.988732848685623 * indata[u"GO_0032147_CSV"] + -0.0817423572700191 * indata[u"GO_0050766_CSV"] + 0.791268381313758 * indata[u"GO_0071560"] + -3.41531819046251 * indata[u"MUT_EIF2AK1"] + -0.0734708053411733 * indata[u"PWY_R_HSA_1852241_EXP"] + -0.125410368248953 * indata[u"PWY_R_HSA_453279"] + 0.579539014570849 * indata[u"REC_R_HSA_450346"] + 1.97456557320354 * indata[u"SFAM_DYRK1"]))

    H1_7 = tanh((6.96868691998581 + -0.83796811257191 * indata[u"CLS_Histology_subtype_1_astrocytoma_Grade_III"] + 0.344105135593478 * indata[u"EXP_CAMK1"] + 0.985486542953318 * indata[u"EXP_CLK4"] + 0.435486770128844 * indata[u"EXP_MAP3K20"] + -0.195118301577238 * indata[u"EXP_MAPK1"] + -0.474964383300563 * indata[u"EXP_STRADB"] + -0.884965916151468 * indata[u"EXP_TBK1"] + -0.802370648825282 * indata[u"EXP_TRIM33"] + 0.14608808363908 * indata[u"EXP_TRPM7"] + 4.88182061311647 * indata[u"GO_0007166_CSV"] + -0.136537577563646 * indata[u"GO_0008283"] + -0.133426991186072 * indata[u"GO_0008283_EXP"] + -0.83353801066343 * indata[u"GO_0010506"] + -0.177593337395915 * indata[u"GO_0016572"] + 0.235891008404977 * indata[u"GO_0030509_EXP"] + 0.862078491955089 * indata[u"GO_0032147_CSV"] + -3.29748887750984 * indata[u"GO_0050766_CSV"] + 1.44164013005409 * indata[u"GO_0071560"] + 1.65482263064389 * indata[u"MUT_EIF2AK1"] + 0.350315371640111 * indata[u"PWY_R_HSA_1852241_EXP"] + 0.450221036894157 * indata[u"PWY_R_HSA_453279"] + -0.213322574444775 * indata[u"REC_R_HSA_450346"] + -0.856952596127132 * indata[u"SFAM_DYRK1"]))

    H1_8 = tanh((-12.2511594114302 + 1.43429116411363 * indata[u"CLS_Histology_subtype_1_astrocytoma_Grade_III"] + -0.708681222853225 * indata[u"EXP_CAMK1"] + -0.54035322943228 * indata[u"EXP_CLK4"] + -0.277608554302636 * indata[u"EXP_MAP3K20"] + 1.04874004037819 * indata[u"EXP_MAPK1"] + 0.429388082836591 * indata[u"EXP_STRADB"] + 0.86488596714173 * indata[u"EXP_TBK1"] + 0.305005685551817 * indata[u"EXP_TRIM33"] + 0.738630803234683 * indata[u"EXP_TRPM7"] + -1.62542154255496 * indata[u"GO_0007166_CSV"] + -0.727096130741723 * indata[u"GO_0008283"] + -0.219237927678717 * indata[u"GO_0008283_EXP"] + 0.232253512473538 * indata[u"GO_0010506"] + -1.20857970897087 * indata[u"GO_0016572"] + 0.0583930862527102 * indata[u"GO_0030509_EXP"] + 0.629037484146025 * indata[u"GO_0032147_CSV"] + 1.12357726397962 * indata[u"GO_0050766_CSV"] + 1.04115379223009 * indata[u"GO_0071560"] + 3.56154340025471 * indata[u"MUT_EIF2AK1"] + -0.0710759424319583 * indata[u"PWY_R_HSA_1852241_EXP"] + -2.48515436672204 * indata[u"PWY_R_HSA_453279"] + -1.17701208495673 * indata[u"REC_R_HSA_450346"] + 1.00102875859409 * indata[u"SFAM_DYRK1"]))

    H1_9 = tanh((-24.9006145564265 + -1.44226187970094 * indata[u"CLS_Histology_subtype_1_astrocytoma_Grade_III"] + 1.20539184478123 * indata[u"EXP_CAMK1"] + 1.5810613806637 * indata[u"EXP_CLK4"] + -0.692981972777361 * indata[u"EXP_MAP3K20"] + 1.24062074634705 * indata[u"EXP_MAPK1"] + -0.414698277170617 * indata[u"EXP_STRADB"] + 0.790399288047616 * indata[u"EXP_TBK1"] + -0.461691930404514 * indata[u"EXP_TRIM33"] + 1.60387474078687 * indata[u"EXP_TRPM7"] + 0.447671416326333 * indata[u"GO_0007166_CSV"] + 1.01865524750874 * indata[u"GO_0008283"] + -0.019736299540883 * indata[u"GO_0008283_EXP"] + 1.34044757349261 * indata[u"GO_0010506"] + 0.624981171068766 * indata[u"GO_0016572"] + 0.00391129865404898 * indata[u"GO_0030509_EXP"] + 1.66468736851463 * indata[u"GO_0032147_CSV"] + -4.31163133693744 * indata[u"GO_0050766_CSV"] + -0.682195323079137 * indata[u"GO_0071560"] + 0.804016671672205 * indata[u"MUT_EIF2AK1"] + 0.244597520619562 * indata[u"PWY_R_HSA_1852241_EXP"] + -2.46367304391972 * indata[u"PWY_R_HSA_453279"] + 0.462466774794669 * indata[u"REC_R_HSA_450346"] + -0.336541264912858 * indata[u"SFAM_DYRK1"]))

    H1_10 = tanh((4.18656043983723 + -2.25388951804639 * indata[u"CLS_Histology_subtype_1_astrocytoma_Grade_III"] + -0.453970146322263 * indata[u"EXP_CAMK1"] + 2.14849671819667 * indata[u"EXP_CLK4"] + 0.284069604831268 * indata[u"EXP_MAP3K20"] + -1.92544221291912 * indata[u"EXP_MAPK1"] + 1.67857564261128 * indata[u"EXP_STRADB"] + -0.170106611365412 * indata[u"EXP_TBK1"] + -1.0041989257467 * indata[u"EXP_TRIM33"] + -0.112715984469647 * indata[u"EXP_TRPM7"] + 0.876109544522634 * indata[u"GO_0007166_CSV"] + -0.284490566940751 * indata[u"GO_0008283"] + 0.211287787380383 * indata[u"GO_0008283_EXP"] + 0.25955580212469 * indata[u"GO_0010506"] + 0.227529212828147 * indata[u"GO_0016572"] + 0.116723050446481 * indata[u"GO_0030509_EXP"] + -3.34197380974438 * indata[u"GO_0032147_CSV"] + 1.02998497367131 * indata[u"GO_0050766_CSV"] + 3.30996393954676 * indata[u"GO_0071560"] + -0.277684971919304 * indata[u"MUT_EIF2AK1"] + 0.157319722271069 * indata[u"PWY_R_HSA_1852241_EXP"] + -1.89511345770154 * indata[u"PWY_R_HSA_453279"] + 0.688995646507061 * indata[u"REC_R_HSA_450346"] + 0.505679345048816 * indata[u"SFAM_DYRK1"]))

    H1_11 = tanh((-2.06209800103817 + 1.47798112435637 * indata[u"CLS_Histology_subtype_1_astrocytoma_Grade_III"] + -0.139741335691127 * indata[u"EXP_CAMK1"] + -1.13263040047432 * indata[u"EXP_CLK4"] + 0.0327817021602791 * indata[u"EXP_MAP3K20"] + 0.732830782763397 * indata[u"EXP_MAPK1"] + 0.381658699525269 * indata[u"EXP_STRADB"] + -0.440388233683358 * indata[u"EXP_TBK1"] + 0.589762793697912 * indata[u"EXP_TRIM33"] + 0.0114885549833983 * indata[u"EXP_TRPM7"] + 0.913120998031107 * indata[u"GO_0007166_CSV"] + -1.82437075536392 * indata[u"GO_0008283"] + 0.0238697703465748 * indata[u"GO_0008283_EXP"] + -0.0987893782534956 * indata[u"GO_0010506"] + -0.169820689144116 * indata[u"GO_0016572"] + 0.215685924773987 * indata[u"GO_0030509_EXP"] + 0.806353063170976 * indata[u"GO_0032147_CSV"] + -2.32573190502039 * indata[u"GO_0050766_CSV"] + 1.80213468991435 * indata[u"GO_0071560"] + 2.84803409039224 * indata[u"MUT_EIF2AK1"] + 0.371835915720166 * indata[u"PWY_R_HSA_1852241_EXP"] + 0.234467691007936 * indata[u"PWY_R_HSA_453279"] + 2.55920824276158 * indata[u"REC_R_HSA_450346"] + 1.54641946225418 * indata[u"SFAM_DYRK1"]))

    outdata[u"Predicted IC50_1"] = 2.4623269428103 + 0.234386649752501 * H1_1 + 0.0411677190902432 * H1_10 + 0.109323424170206 * H1_11 + 0.348882960001004 * H1_2 + -0.179501054835301 * H1_3 + 0.224043919723557 * H1_4 + -0.0328471511941779 * H1_5 + -0.293666619840641 * H1_6 + 0.245190329969612 * H1_7 + 0.286013708227499 * H1_8 + 0.0310831749957822 * H1_9

    return outdata[u"Predicted IC50_1"]


