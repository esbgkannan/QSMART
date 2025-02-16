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
	return {"creator": u"Neural", "modelName": u"", "predicted": u"IC50", "table": u"liver", "version": u"14.1.0", "timestamp": u"2019-08-09T13:52:37Z"}


def getInputMetadata():
    return {
        u"EXP_COQ8A_X_EXP_PDSS1": "float",
        u"EXP_PRKAA2_X_EXP_TP53": "float",
        u"EXP_SRC_X_EXP_ARRB2": "float",
        u"EXP_SRC_X_EXP_CASP8": "float",
        u"EXP_SRC_X_EXP_FN1": "float",
        u"EXP_STK11_X_EXP_ATIC": "float",
        u"GO_0032212_X_GO_0043066": "float",
        u"PKA_172_ASA_X_Fingerprint_644": "float",
        u"PKA_280_CSV_X_Fingerprint_644": "float"
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

    H1_1 = tanh((7.41115701813887 + -0.117127720166281 * indata[u"EXP_COQ8A_X_EXP_PDSS1"] + 0.183924222854701 * indata[u"EXP_PRKAA2_X_EXP_TP53"] + -0.0207847390748602 * indata[u"EXP_SRC_X_EXP_ARRB2"] + -0.0645929281450732 * indata[u"EXP_SRC_X_EXP_CASP8"] + -0.0190273809549092 * indata[u"EXP_SRC_X_EXP_FN1"] + -0.0545579846502565 * indata[u"EXP_STK11_X_EXP_ATIC"] + -1.02635140997866 * indata[u"GO_0032212_X_GO_0043066"] + -0.163212928374975 * indata[u"PKA_172_ASA_X_Fingerprint_644"] + -2.30529544338217 * indata[u"PKA_280_CSV_X_Fingerprint_644"]))

    H1_2 = tanh((-3.14837596738296 + 0.051124094064213 * indata[u"EXP_COQ8A_X_EXP_PDSS1"] + -0.088711535555831 * indata[u"EXP_PRKAA2_X_EXP_TP53"] + 0.0308120039655324 * indata[u"EXP_SRC_X_EXP_ARRB2"] + -0.0403625809549604 * indata[u"EXP_SRC_X_EXP_CASP8"] + -0.0217835284392899 * indata[u"EXP_SRC_X_EXP_FN1"] + 0.087250076446912 * indata[u"EXP_STK11_X_EXP_ATIC"] + 0.22511204422771 * indata[u"GO_0032212_X_GO_0043066"] + 0.385209023514696 * indata[u"PKA_172_ASA_X_Fingerprint_644"] + 1.35112884061192 * indata[u"PKA_280_CSV_X_Fingerprint_644"]))

    H1_3 = tanh((1.4540775297793 + -0.0296703758740285 * indata[u"EXP_COQ8A_X_EXP_PDSS1"] + -0.000742191377677224 * indata[u"EXP_PRKAA2_X_EXP_TP53"] + 0.155349365600984 * indata[u"EXP_SRC_X_EXP_ARRB2"] + -0.160431386751762 * indata[u"EXP_SRC_X_EXP_CASP8"] + 0.0457529467093823 * indata[u"EXP_SRC_X_EXP_FN1"] + -0.0685400924254472 * indata[u"EXP_STK11_X_EXP_ATIC"] + -0.541391805958146 * indata[u"GO_0032212_X_GO_0043066"] + 0.116741040688865 * indata[u"PKA_172_ASA_X_Fingerprint_644"] + -2.01725299642547 * indata[u"PKA_280_CSV_X_Fingerprint_644"]))

    H1_4 = tanh((12.1792274836372 + 0.0539476555763522 * indata[u"EXP_COQ8A_X_EXP_PDSS1"] + -0.229408316114662 * indata[u"EXP_PRKAA2_X_EXP_TP53"] + 0.00361514067671286 * indata[u"EXP_SRC_X_EXP_ARRB2"] + -0.0307941046624023 * indata[u"EXP_SRC_X_EXP_CASP8"] + -0.0820723002201537 * indata[u"EXP_SRC_X_EXP_FN1"] + -0.127737579262891 * indata[u"EXP_STK11_X_EXP_ATIC"] + 1.42958857537251 * indata[u"GO_0032212_X_GO_0043066"] + -0.324343298094115 * indata[u"PKA_172_ASA_X_Fingerprint_644"] + -0.790738500719218 * indata[u"PKA_280_CSV_X_Fingerprint_644"]))

    H1_5 = tanh((-6.80016277603647 + -0.0538419887353638 * indata[u"EXP_COQ8A_X_EXP_PDSS1"] + -0.0525456054172201 * indata[u"EXP_PRKAA2_X_EXP_TP53"] + 0.00116855305549689 * indata[u"EXP_SRC_X_EXP_ARRB2"] + 0.0979998111329785 * indata[u"EXP_SRC_X_EXP_CASP8"] + -0.0201493340923899 * indata[u"EXP_SRC_X_EXP_FN1"] + 0.169433320457982 * indata[u"EXP_STK11_X_EXP_ATIC"] + 0.997970432793228 * indata[u"GO_0032212_X_GO_0043066"] + -0.0915440802714708 * indata[u"PKA_172_ASA_X_Fingerprint_644"] + 0.28487625728123 * indata[u"PKA_280_CSV_X_Fingerprint_644"]))

    H1_6 = tanh((-7.86248380426113 + 0.0735295655965755 * indata[u"EXP_COQ8A_X_EXP_PDSS1"] + 0.182236905931248 * indata[u"EXP_PRKAA2_X_EXP_TP53"] + -0.0226639456009134 * indata[u"EXP_SRC_X_EXP_ARRB2"] + 0.0269843924473506 * indata[u"EXP_SRC_X_EXP_CASP8"] + 0.0320977378128645 * indata[u"EXP_SRC_X_EXP_FN1"] + 0.0111761333539574 * indata[u"EXP_STK11_X_EXP_ATIC"] + 0.080480817319552 * indata[u"GO_0032212_X_GO_0043066"] + 0.0969888438424346 * indata[u"PKA_172_ASA_X_Fingerprint_644"] + 1.43215167115096 * indata[u"PKA_280_CSV_X_Fingerprint_644"]))

    H1_7 = tanh((3.20007647583973 + 0.0158376068077332 * indata[u"EXP_COQ8A_X_EXP_PDSS1"] + 0.199646511552678 * indata[u"EXP_PRKAA2_X_EXP_TP53"] + -0.0551430959307875 * indata[u"EXP_SRC_X_EXP_ARRB2"] + -0.150022486037467 * indata[u"EXP_SRC_X_EXP_CASP8"] + 0.0169643387108228 * indata[u"EXP_SRC_X_EXP_FN1"] + -0.0818411408496944 * indata[u"EXP_STK11_X_EXP_ATIC"] + 0.569622066605296 * indata[u"GO_0032212_X_GO_0043066"] + 0.121665707103562 * indata[u"PKA_172_ASA_X_Fingerprint_644"] + 0.897229930669932 * indata[u"PKA_280_CSV_X_Fingerprint_644"]))

    outdata[u"Predicted IC50_1"] = 2.93102604550438 + 0.0498094247633634 * H1_1 + -0.253923094909801 * H1_2 + -0.105404422546204 * H1_3 + 0.636287268870104 * H1_4 + 0.392001750829278 * H1_5 + 1.27724132981367 * H1_6 + -0.0642736273009996 * H1_7

    return outdata[u"Predicted IC50_1"]


