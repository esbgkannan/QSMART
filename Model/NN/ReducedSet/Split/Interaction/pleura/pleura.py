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
	return {"creator": u"Neural", "modelName": u"", "predicted": u"IC50", "table": u"pleura", "version": u"14.1.0", "timestamp": u"2019-08-01T01:09:14Z"}


def getInputMetadata():
    return {
        u"EXP_BTK_X_EXP_CD79A": "float",
        u"EXP_MARK3_X_EXP_IQGAP1": "float",
        u"EXP_MARK3_X_EXP_PPP2CB": "float",
        u"EXP_MET_X_EXP_CBLC": "float",
        u"EXP_MET_X_EXP_FGF12": "float",
        u"EXP_MET_X_EXP_PDGFA": "float",
        u"EXP_MET_X_EXP_RAPGEF1": "float",
        u"EXP_PTK6_X_EXP_CCND1": "float"
	}


def getOutputMetadata():
    return {
        u"Predicted IC50_1": "float"
	}


def score(indata, outdata):
    # H2_1
    # H2_2
    # H2_3
    # H2_4
    # H2_5
    # H2_6
    # H2_7
    # H2_8
    # H2_9
    # H2_10
    # H2_11
    # H1_1
    # H1_2
    # H1_3
    # H1_4

    H2_1 = tanh((2.94986947732531 + -0.275212033738239 * indata[u"EXP_BTK_X_EXP_CD79A"] + 0.0408722952387545 * indata[u"EXP_MARK3_X_EXP_IQGAP1"] + -0.0124860070939659 * indata[u"EXP_MARK3_X_EXP_PPP2CB"] + 0.0931241957881643 * indata[u"EXP_MET_X_EXP_CBLC"] + 0.000223857057316969 * indata[u"EXP_MET_X_EXP_FGF12"] + -0.043434328880105 * indata[u"EXP_MET_X_EXP_PDGFA"] + -0.157441092127577 * indata[u"EXP_MET_X_EXP_RAPGEF1"] + 0.0410326120072673 * indata[u"EXP_PTK6_X_EXP_CCND1"]))

    H2_2 = tanh((-6.17255792856369 + -0.183202947487181 * indata[u"EXP_BTK_X_EXP_CD79A"] + 0.0315355010406602 * indata[u"EXP_MARK3_X_EXP_IQGAP1"] + -0.105705427424816 * indata[u"EXP_MARK3_X_EXP_PPP2CB"] + 0.0863450499208624 * indata[u"EXP_MET_X_EXP_CBLC"] + 0.0449981899667322 * indata[u"EXP_MET_X_EXP_FGF12"] + 0.085960140227646 * indata[u"EXP_MET_X_EXP_PDGFA"] + 0.133117319644994 * indata[u"EXP_MET_X_EXP_RAPGEF1"] + 0.200456587572186 * indata[u"EXP_PTK6_X_EXP_CCND1"]))

    H2_3 = tanh((-4.57446742954722 + -0.388583240642167 * indata[u"EXP_BTK_X_EXP_CD79A"] + -0.0903117988351034 * indata[u"EXP_MARK3_X_EXP_IQGAP1"] + 0.00873252049960955 * indata[u"EXP_MARK3_X_EXP_PPP2CB"] + -0.0340094731373114 * indata[u"EXP_MET_X_EXP_CBLC"] + -0.0356010469830989 * indata[u"EXP_MET_X_EXP_FGF12"] + 0.256721334533313 * indata[u"EXP_MET_X_EXP_PDGFA"] + 0.235233066760971 * indata[u"EXP_MET_X_EXP_RAPGEF1"] + 0.00827743678915714 * indata[u"EXP_PTK6_X_EXP_CCND1"]))

    H2_4 = tanh((8.0014001073484 + -0.767915299743151 * indata[u"EXP_BTK_X_EXP_CD79A"] + -0.0169337485575758 * indata[u"EXP_MARK3_X_EXP_IQGAP1"] + 0.0420561823917405 * indata[u"EXP_MARK3_X_EXP_PPP2CB"] + -0.00713901177001188 * indata[u"EXP_MET_X_EXP_CBLC"] + -0.0287581716099712 * indata[u"EXP_MET_X_EXP_FGF12"] + 0.0032153647013381 * indata[u"EXP_MET_X_EXP_PDGFA"] + 0.0361711471225478 * indata[u"EXP_MET_X_EXP_RAPGEF1"] + -0.199319990902183 * indata[u"EXP_PTK6_X_EXP_CCND1"]))

    H2_5 = tanh((-5.3780065489988 + 0.378695415928331 * indata[u"EXP_BTK_X_EXP_CD79A"] + 0.0651193127835638 * indata[u"EXP_MARK3_X_EXP_IQGAP1"] + 0.0537770396088899 * indata[u"EXP_MARK3_X_EXP_PPP2CB"] + 0.18767733883281 * indata[u"EXP_MET_X_EXP_CBLC"] + -0.174129902171197 * indata[u"EXP_MET_X_EXP_FGF12"] + -0.0531217873827665 * indata[u"EXP_MET_X_EXP_PDGFA"] + -0.00793850949472127 * indata[u"EXP_MET_X_EXP_RAPGEF1"] + -0.162860723376927 * indata[u"EXP_PTK6_X_EXP_CCND1"]))

    H2_6 = tanh((-3.03252804490771 + -0.274009086696379 * indata[u"EXP_BTK_X_EXP_CD79A"] + 0.0772254041782931 * indata[u"EXP_MARK3_X_EXP_IQGAP1"] + 0.0383470121993224 * indata[u"EXP_MARK3_X_EXP_PPP2CB"] + -0.140704190526702 * indata[u"EXP_MET_X_EXP_CBLC"] + 0.148480154999565 * indata[u"EXP_MET_X_EXP_FGF12"] + -0.127183600736561 * indata[u"EXP_MET_X_EXP_PDGFA"] + -0.0537470076976258 * indata[u"EXP_MET_X_EXP_RAPGEF1"] + 0.0662296947941212 * indata[u"EXP_PTK6_X_EXP_CCND1"]))

    H2_7 = tanh((9.13969915906861 + -1.22417134448783 * indata[u"EXP_BTK_X_EXP_CD79A"] + 0.0582970136726637 * indata[u"EXP_MARK3_X_EXP_IQGAP1"] + -0.0471762647546409 * indata[u"EXP_MARK3_X_EXP_PPP2CB"] + -0.000170685745102933 * indata[u"EXP_MET_X_EXP_CBLC"] + -0.151545346930966 * indata[u"EXP_MET_X_EXP_FGF12"] + -0.0722176562489744 * indata[u"EXP_MET_X_EXP_PDGFA"] + 0.0239721705406645 * indata[u"EXP_MET_X_EXP_RAPGEF1"] + 0.176800515393137 * indata[u"EXP_PTK6_X_EXP_CCND1"]))

    H2_8 = tanh((-0.928380127840979 + -0.307785075511393 * indata[u"EXP_BTK_X_EXP_CD79A"] + 0.006230596990698 * indata[u"EXP_MARK3_X_EXP_IQGAP1"] + 0.0420756064812166 * indata[u"EXP_MARK3_X_EXP_PPP2CB"] + -0.0630788304566414 * indata[u"EXP_MET_X_EXP_CBLC"] + -0.160905172493498 * indata[u"EXP_MET_X_EXP_FGF12"] + -0.011524980523088 * indata[u"EXP_MET_X_EXP_PDGFA"] + 0.00785613086856304 * indata[u"EXP_MET_X_EXP_RAPGEF1"] + 0.127926603525593 * indata[u"EXP_PTK6_X_EXP_CCND1"]))

    H2_9 = tanh((16.0176063280731 + -1.47681383213768 * indata[u"EXP_BTK_X_EXP_CD79A"] + 0.0234394983665124 * indata[u"EXP_MARK3_X_EXP_IQGAP1"] + 0.0354078442773609 * indata[u"EXP_MARK3_X_EXP_PPP2CB"] + -0.0136625457823116 * indata[u"EXP_MET_X_EXP_CBLC"] + -0.11651444907628 * indata[u"EXP_MET_X_EXP_FGF12"] + 0.00541000189515028 * indata[u"EXP_MET_X_EXP_PDGFA"] + -0.129271218520741 * indata[u"EXP_MET_X_EXP_RAPGEF1"] + -0.141256659123491 * indata[u"EXP_PTK6_X_EXP_CCND1"]))

    H2_10 = tanh((7.25763357758676 + 0.305821082365029 * indata[u"EXP_BTK_X_EXP_CD79A"] + -0.038726124460649 * indata[u"EXP_MARK3_X_EXP_IQGAP1"] + 0.0690566530955918 * indata[u"EXP_MARK3_X_EXP_PPP2CB"] + -0.192609268763069 * indata[u"EXP_MET_X_EXP_CBLC"] + -0.0311300017303948 * indata[u"EXP_MET_X_EXP_FGF12"] + -0.096686061854918 * indata[u"EXP_MET_X_EXP_PDGFA"] + 0.049624978909888 * indata[u"EXP_MET_X_EXP_RAPGEF1"] + -0.270782472837677 * indata[u"EXP_PTK6_X_EXP_CCND1"]))

    H2_11 = tanh((0.4432269679745 + 0.857248780967148 * indata[u"EXP_BTK_X_EXP_CD79A"] + -0.000242607032888289 * indata[u"EXP_MARK3_X_EXP_IQGAP1"] + -0.0146727627067533 * indata[u"EXP_MARK3_X_EXP_PPP2CB"] + -0.222438225489256 * indata[u"EXP_MET_X_EXP_CBLC"] + 0.0525450992093115 * indata[u"EXP_MET_X_EXP_FGF12"] + -0.0608715797979645 * indata[u"EXP_MET_X_EXP_PDGFA"] + -0.000270887966531935 * indata[u"EXP_MET_X_EXP_RAPGEF1"] + -0.085409278085482 * indata[u"EXP_PTK6_X_EXP_CCND1"]))

    H1_1 = tanh((0.526552162732684 + 0.801136756589959 * H2_1 + 0.272963959665737 * H2_10 + -0.000289873644808166 * H2_11 + -0.00210046740535876 * H2_2 + -1.09512183062262 * H2_3 + 0.092694202816123 * H2_4 + -0.295112368286363 * H2_5 + 0.319447645736559 * H2_6 + 0.237009279235928 * H2_7 + 0.0349995658946298 * H2_8 + 0.258347473502949 * H2_9))

    H1_2 = tanh((0.186605017111595 + -0.242902183893929 * H2_1 + -0.0532502547088416 * H2_10 + 0.06833305894385 * H2_11 + 0.537280293472332 * H2_2 + 0.0307970254455598 * H2_3 + -0.357626372374244 * H2_4 + 0.289823015779063 * H2_5 + 0.135525542013746 * H2_6 + 0.0668464788295256 * H2_7 + -0.0353423901816935 * H2_8 + -0.45358627915043 * H2_9))

    H1_3 = tanh((0.464465429589243 + 0.044977623208802 * H2_1 + -0.585545820586697 * H2_10 + -0.365533037490452 * H2_11 + 0.0565839330165562 * H2_2 + -0.312241830270265 * H2_3 + 0.190098409067704 * H2_4 + 0.376113574892402 * H2_5 + 0.72227405707274 * H2_6 + -0.554916500396813 * H2_7 + 0.0115585234555463 * H2_8 + -0.0680041592671239 * H2_9))

    H1_4 = tanh((0.670117530963963 + -0.0171660948867272 * H2_1 + -0.456652056525229 * H2_10 + -0.0310857908067026 * H2_11 + 0.000178242251362758 * H2_2 + -0.56551538240642 * H2_3 + 0.497334538926532 * H2_4 + -0.434210105925599 * H2_5 + -0.501605967288972 * H2_6 + -0.113779458677642 * H2_7 + -0.777781014673469 * H2_8 + -0.140217820934505 * H2_9))

    outdata[u"Predicted IC50_1"] = 2.98829753225729 + 0.76369269580302 * H1_1 + 1.40753410584217 * H1_2 + -0.982197757766767 * H1_3 + 0.152081457671265 * H1_4

    return outdata[u"Predicted IC50_1"]


