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
	return {"creator": u"Neural", "modelName": u"", "predicted": u"IC50", "table": u"liver", "version": u"14.1.0", "timestamp": u"2019-07-22T18:34:30Z"}


def getInputMetadata():
    return {
        u"FAM_TKL_CSV": "float",
        u"GO_0000278": "float",
        u"GO_0016477": "float",
        u"SFAM_RIPK": "float"
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

    H1_1 = tanh((-0.165479057940854 + -1.03618839463765 * indata[u"FAM_TKL_CSV"] + -0.00585148279432828 * indata[u"GO_0000278"] + 0.84272148024754 * indata[u"GO_0016477"] + 0.510391484646512 * indata[u"SFAM_RIPK"]))

    H1_2 = tanh((-0.200167998414639 + -0.00662226501195151 * indata[u"FAM_TKL_CSV"] + 0.606038697660092 * indata[u"GO_0000278"] + -0.00854077591053155 * indata[u"GO_0016477"] + -0.0177517869118916 * indata[u"SFAM_RIPK"]))

    H1_3 = tanh((-0.375878939211996 + 0.0104028539507389 * indata[u"FAM_TKL_CSV"] + -0.784177776978309 * indata[u"GO_0000278"] + -0.00217634493354354 * indata[u"GO_0016477"] + 1.26423073358608 * indata[u"SFAM_RIPK"]))

    H1_4 = tanh((-1.53138878574192 + 1.41168212180189 * indata[u"FAM_TKL_CSV"] + -0.479194173549354 * indata[u"GO_0000278"] + 0.00725549635819957 * indata[u"GO_0016477"] + -0.0373704009092209 * indata[u"SFAM_RIPK"]))

    H1_5 = tanh((0.0432574850977565 + 0.243630118325831 * indata[u"FAM_TKL_CSV"] + 0.863236682908404 * indata[u"GO_0000278"] + -0.464770211685112 * indata[u"GO_0016477"] + 0.790238215503838 * indata[u"SFAM_RIPK"]))

    H1_6 = tanh((0.11511691755976 + -0.554761577937971 * indata[u"FAM_TKL_CSV"] + 1.80356961289494 * indata[u"GO_0000278"] + -0.715355963976457 * indata[u"GO_0016477"] + -0.003326928795603 * indata[u"SFAM_RIPK"]))

    H1_7 = tanh((-0.106208555674064 + 0.04347757212928 * indata[u"FAM_TKL_CSV"] + 0.707207977452579 * indata[u"GO_0000278"] + -0.00281308416236546 * indata[u"GO_0016477"] + -0.624290462736768 * indata[u"SFAM_RIPK"]))

    outdata[u"Predicted IC50_1"] = 3.81327246360184 + 0.268987578648459 * H1_1 + -2.16161513905602 * H1_2 + 2.36447038116472 * H1_3 + 0.705593459100041 * H1_4 + -0.463476615677313 * H1_5 + 0.510956258882414 * H1_6 + 2.93171618361747 * H1_7

    return outdata[u"Predicted IC50_1"]


