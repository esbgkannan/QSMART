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
	return {"creator": u"Neural", "modelName": u"", "predicted": u"IC50", "table": u"liver", "version": u"14.1.0", "timestamp": u"2020-09-16T19:17:12Z"}


def getInputMetadata():
    return {
        u"EXP_COQ8A_X_EXP_PDSS1": "float",
        u"EXP_PRKAA2_X_EXP_TP53": "float",
        u"EXP_SRC_X_EXP_ARRB2": "float",
        u"EXP_SRC_X_EXP_CASP8": "float",
        u"FAM_TKL_CSV": "float",
        u"Fingerprint_611": "float",
        u"Fingerprint_617": "float",
        u"Fingerprint_635": "float",
        u"Fingerprint_644": "float",
        u"Fingerprint_646": "float",
        u"Fingerprint_658": "float",
        u"Fingerprint_672": "float",
        u"Fingerprint_673": "float",
        u"Fingerprint_677": "float",
        u"Fingerprint_685": "float",
        u"Fingerprint_686": "float",
        u"Fingerprint_697": "float",
        u"Fingerprint_698": "float",
        u"Fingerprint_710": "float",
        u"Fingerprint_714": "float",
        u"Fingerprint_797": "float",
        u"Fingerprint_818": "float",
        u"Fingerprint_819": "float",
        u"Fingerprint_821": "float",
        u"Fingerprint_822": "float",
        u"Fingerprint_824": "float",
        u"Fingerprint_834": "float",
        u"From_Sanger": "float",
        u"GO_0000278": "float",
        u"GO_0016477": "float",
        u"GO_0032212_X_GO_0043066": "float",
        u"PKA_172_ASA_X_Fingerprint_644": "float"
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

    H1_1 = tanh((14.5103486116407 + 0.144705161788599 * indata[u"EXP_COQ8A_X_EXP_PDSS1"] + -0.380267597083477 * indata[u"EXP_PRKAA2_X_EXP_TP53"] + -0.180782497138254 * indata[u"EXP_SRC_X_EXP_ARRB2"] + -0.449886739340003 * indata[u"EXP_SRC_X_EXP_CASP8"] + -6.51869782766554 * indata[u"FAM_TKL_CSV"] + 7.32015423459944 * indata[u"Fingerprint_611"] + -7.08570200550808 * indata[u"Fingerprint_617"] + -7.71647956342327 * indata[u"Fingerprint_635"] + 0.115403871081478 * indata[u"Fingerprint_644"] + -0.421938644389399 * indata[u"Fingerprint_646"] + 10.0583099508251 * indata[u"Fingerprint_658"] + -1.86549971674752 * indata[u"Fingerprint_672"] + -1.21887734001927 * indata[u"Fingerprint_673"] + 10.479864551117 * indata[u"Fingerprint_677"] + 0.71239505347205 * indata[u"Fingerprint_685"] + -19.4580952885735 * indata[u"Fingerprint_686"] + -3.46906556212329 * indata[u"Fingerprint_697"] + -8.16774260624658 * indata[u"Fingerprint_698"] + 0.218782576647928 * indata[u"Fingerprint_710"] + 13.7014401687705 * indata[u"Fingerprint_714"] + 3.6212177205147 * indata[u"Fingerprint_797"] + -19.6264613485576 * indata[u"Fingerprint_818"] + -11.260703341707 * indata[u"Fingerprint_819"] + -5.75591451492227 * indata[u"Fingerprint_821"] + -11.5381369418815 * indata[u"Fingerprint_822"] + -0.177584869146833 * indata[u"Fingerprint_824"] + 3.53487466542178 * indata[u"Fingerprint_834"] + -6.23747076858892 * indata[u"From_Sanger"] + 0.192699553621557 * indata[u"GO_0000278"] + -0.734217377367171 * indata[u"GO_0016477"] + -2.79789646512742 * indata[u"GO_0032212_X_GO_0043066"] + 1.13250374085037 * indata[u"PKA_172_ASA_X_Fingerprint_644"]))

    H1_2 = tanh((-5.64622959642539 + 0.0712979187666404 * indata[u"EXP_COQ8A_X_EXP_PDSS1"] + 0.51095094589215 * indata[u"EXP_PRKAA2_X_EXP_TP53"] + 0.126403326695118 * indata[u"EXP_SRC_X_EXP_ARRB2"] + -0.101327048881646 * indata[u"EXP_SRC_X_EXP_CASP8"] + 0.337232295016532 * indata[u"FAM_TKL_CSV"] + 7.5857131847856 * indata[u"Fingerprint_611"] + -9.33546257631888 * indata[u"Fingerprint_617"] + 21.2274532533173 * indata[u"Fingerprint_635"] + 7.51257783183134 * indata[u"Fingerprint_644"] + -4.14308326029643 * indata[u"Fingerprint_646"] + 31.5126958090711 * indata[u"Fingerprint_658"] + -4.12226553100326 * indata[u"Fingerprint_672"] + 6.68796721937287 * indata[u"Fingerprint_673"] + -8.44786093574619 * indata[u"Fingerprint_677"] + 12.3637858057292 * indata[u"Fingerprint_685"] + -9.57868634784344 * indata[u"Fingerprint_686"] + -7.57872848120901 * indata[u"Fingerprint_697"] + -1.55121080865341 * indata[u"Fingerprint_698"] + 1.10201960616644 * indata[u"Fingerprint_710"] + 8.609870271245 * indata[u"Fingerprint_714"] + -11.1391667115927 * indata[u"Fingerprint_797"] + 2.98772757762589 * indata[u"Fingerprint_818"] + -11.1168492391277 * indata[u"Fingerprint_819"] + 5.82203850922295 * indata[u"Fingerprint_821"] + -8.96801382978885 * indata[u"Fingerprint_822"] + 9.54249571201238 * indata[u"Fingerprint_824"] + -0.53412404855063 * indata[u"Fingerprint_834"] + -1.88977981134521 * indata[u"From_Sanger"] + -1.3945194395907 * indata[u"GO_0000278"] + 1.29604112388886 * indata[u"GO_0016477"] + -3.06823253990792 * indata[u"GO_0032212_X_GO_0043066"] + 0.319249142053188 * indata[u"PKA_172_ASA_X_Fingerprint_644"]))

    H1_3 = tanh((6.3130667159926 + 0.312710696999256 * indata[u"EXP_COQ8A_X_EXP_PDSS1"] + -0.128525957818727 * indata[u"EXP_PRKAA2_X_EXP_TP53"] + -0.0770165239414084 * indata[u"EXP_SRC_X_EXP_ARRB2"] + -0.195450830826484 * indata[u"EXP_SRC_X_EXP_CASP8"] + 1.52059398656268 * indata[u"FAM_TKL_CSV"] + 1.56201893406006 * indata[u"Fingerprint_611"] + -7.27122268063951 * indata[u"Fingerprint_617"] + -1.27132788178481 * indata[u"Fingerprint_635"] + -1.57558485265196 * indata[u"Fingerprint_644"] + -12.6246827246467 * indata[u"Fingerprint_646"] + -7.98661994315149 * indata[u"Fingerprint_658"] + 4.96067869332046 * indata[u"Fingerprint_672"] + 6.60657597634761 * indata[u"Fingerprint_673"] + -7.73089068767532 * indata[u"Fingerprint_677"] + -6.50848532204436 * indata[u"Fingerprint_685"] + 8.39162990716543 * indata[u"Fingerprint_686"] + 11.066790387232 * indata[u"Fingerprint_697"] + 8.58722395734164 * indata[u"Fingerprint_698"] + -3.10945048866538 * indata[u"Fingerprint_710"] + -13.3825972040226 * indata[u"Fingerprint_714"] + 5.79612981698098 * indata[u"Fingerprint_797"] + -11.6455241559126 * indata[u"Fingerprint_818"] + 3.45539345316862 * indata[u"Fingerprint_819"] + -3.9709282611473 * indata[u"Fingerprint_821"] + 14.0901224140975 * indata[u"Fingerprint_822"] + 3.29709628669064 * indata[u"Fingerprint_824"] + -5.77806072152367 * indata[u"Fingerprint_834"] + -9.88206210394817 * indata[u"From_Sanger"] + -0.827254819929598 * indata[u"GO_0000278"] + 0.095207920650385 * indata[u"GO_0016477"] + -2.1636491929488 * indata[u"GO_0032212_X_GO_0043066"] + 0.801340476882619 * indata[u"PKA_172_ASA_X_Fingerprint_644"]))

    H1_4 = tanh((-10.386258895196 + -0.0494625223979245 * indata[u"EXP_COQ8A_X_EXP_PDSS1"] + 0.400765192475592 * indata[u"EXP_PRKAA2_X_EXP_TP53"] + 0.037589071730324 * indata[u"EXP_SRC_X_EXP_ARRB2"] + -0.0464998751538229 * indata[u"EXP_SRC_X_EXP_CASP8"] + 1.80793570171638 * indata[u"FAM_TKL_CSV"] + -3.5710820371522 * indata[u"Fingerprint_611"] + 0.0960099890445785 * indata[u"Fingerprint_617"] + 18.9625334180717 * indata[u"Fingerprint_635"] + 8.98829522341031 * indata[u"Fingerprint_644"] + 8.0163127102706 * indata[u"Fingerprint_646"] + -22.990439271482 * indata[u"Fingerprint_658"] + -13.1508576496467 * indata[u"Fingerprint_672"] + 19.0987335216204 * indata[u"Fingerprint_673"] + -7.69145403127059 * indata[u"Fingerprint_677"] + -2.34218058647488 * indata[u"Fingerprint_685"] + -2.0331584681164 * indata[u"Fingerprint_686"] + -0.38389843614146 * indata[u"Fingerprint_697"] + 6.70883524792136 * indata[u"Fingerprint_698"] + 15.1536423562916 * indata[u"Fingerprint_710"] + -9.53978903044629 * indata[u"Fingerprint_714"] + -6.7035805351459 * indata[u"Fingerprint_797"] + -2.01500706071684 * indata[u"Fingerprint_818"] + 14.5805141264562 * indata[u"Fingerprint_819"] + 3.74892755081152 * indata[u"Fingerprint_821"] + -16.8205833840531 * indata[u"Fingerprint_822"] + 1.11622928273224 * indata[u"Fingerprint_824"] + -1.7753464971559 * indata[u"Fingerprint_834"] + 1.9599659289494 * indata[u"From_Sanger"] + -0.747046541326595 * indata[u"GO_0000278"] + 0.114750376674867 * indata[u"GO_0016477"] + -1.03357327549465 * indata[u"GO_0032212_X_GO_0043066"] + 0.691460438194802 * indata[u"PKA_172_ASA_X_Fingerprint_644"]))

    H1_5 = tanh((6.15227799290442 + 0.0917126345656515 * indata[u"EXP_COQ8A_X_EXP_PDSS1"] + -0.332157334619545 * indata[u"EXP_PRKAA2_X_EXP_TP53"] + 0.130574047790542 * indata[u"EXP_SRC_X_EXP_ARRB2"] + -0.216646021148578 * indata[u"EXP_SRC_X_EXP_CASP8"] + 2.66123158487469 * indata[u"FAM_TKL_CSV"] + 0.34781014662077 * indata[u"Fingerprint_611"] + -2.44001121212883 * indata[u"Fingerprint_617"] + -1.42711700210749 * indata[u"Fingerprint_635"] + -6.02985468479574 * indata[u"Fingerprint_644"] + -11.4922747384795 * indata[u"Fingerprint_646"] + -1.50260662818736 * indata[u"Fingerprint_658"] + 16.7739883851274 * indata[u"Fingerprint_672"] + -8.75221094001771 * indata[u"Fingerprint_673"] + -10.7723987365055 * indata[u"Fingerprint_677"] + 10.4840057594427 * indata[u"Fingerprint_685"] + -7.64505327991457 * indata[u"Fingerprint_686"] + -7.05800604713643 * indata[u"Fingerprint_697"] + 6.43232577823574 * indata[u"Fingerprint_698"] + 12.1654237609279 * indata[u"Fingerprint_710"] + -2.35483959630498 * indata[u"Fingerprint_714"] + 2.86367663426206 * indata[u"Fingerprint_797"] + -8.10722977787981 * indata[u"Fingerprint_818"] + 16.136203156839 * indata[u"Fingerprint_819"] + 3.40833978981868 * indata[u"Fingerprint_821"] + -2.53908021025156 * indata[u"Fingerprint_822"] + -2.86947887835896 * indata[u"Fingerprint_824"] + 16.3399620193411 * indata[u"Fingerprint_834"] + -16.9267836460903 * indata[u"From_Sanger"] + -0.624682996945842 * indata[u"GO_0000278"] + -2.8578467275305 * indata[u"GO_0016477"] + -5.85772707144314 * indata[u"GO_0032212_X_GO_0043066"] + -0.0612818357303353 * indata[u"PKA_172_ASA_X_Fingerprint_644"]))

    H1_6 = tanh((-3.83180103576968 + 0.0926977119811065 * indata[u"EXP_COQ8A_X_EXP_PDSS1"] + 0.114804179174651 * indata[u"EXP_PRKAA2_X_EXP_TP53"] + -0.1622535391126 * indata[u"EXP_SRC_X_EXP_ARRB2"] + 0.0703135805972745 * indata[u"EXP_SRC_X_EXP_CASP8"] + 0.0473839628156826 * indata[u"FAM_TKL_CSV"] + 4.51090030923197 * indata[u"Fingerprint_611"] + -8.76099933502182 * indata[u"Fingerprint_617"] + 21.0544618990929 * indata[u"Fingerprint_635"] + 0.453565472189854 * indata[u"Fingerprint_644"] + -10.0325208596339 * indata[u"Fingerprint_646"] + 15.8139282038927 * indata[u"Fingerprint_658"] + 0.428939916575518 * indata[u"Fingerprint_672"] + 12.9119607535199 * indata[u"Fingerprint_673"] + -2.81365502482224 * indata[u"Fingerprint_677"] + -3.87034108479969 * indata[u"Fingerprint_685"] + -6.28666510403144 * indata[u"Fingerprint_686"] + 10.014314421217 * indata[u"Fingerprint_697"] + 1.79885450813737 * indata[u"Fingerprint_698"] + -11.7862682136844 * indata[u"Fingerprint_710"] + 2.43778844663667 * indata[u"Fingerprint_714"] + 8.90042646635205 * indata[u"Fingerprint_797"] + 8.7183652658341 * indata[u"Fingerprint_818"] + -3.28727987457058 * indata[u"Fingerprint_819"] + 4.87858553939029 * indata[u"Fingerprint_821"] + 13.2057088082254 * indata[u"Fingerprint_822"] + 7.17177776480161 * indata[u"Fingerprint_824"] + -10.2732278485654 * indata[u"Fingerprint_834"] + 8.37165022108555 * indata[u"From_Sanger"] + -0.0200481254544649 * indata[u"GO_0000278"] + -0.262920572189548 * indata[u"GO_0016477"] + -0.154906604815266 * indata[u"GO_0032212_X_GO_0043066"] + 0.650337207079563 * indata[u"PKA_172_ASA_X_Fingerprint_644"]))

    H1_7 = tanh((21.1765602666049 + -0.446694354761151 * indata[u"EXP_COQ8A_X_EXP_PDSS1"] + -0.561931798423144 * indata[u"EXP_PRKAA2_X_EXP_TP53"] + 0.213476234830058 * indata[u"EXP_SRC_X_EXP_ARRB2"] + 0.260008173738725 * indata[u"EXP_SRC_X_EXP_CASP8"] + -0.0887785444221713 * indata[u"FAM_TKL_CSV"] + 13.0827349171799 * indata[u"Fingerprint_611"] + 4.87808230223416 * indata[u"Fingerprint_617"] + -29.3140741368578 * indata[u"Fingerprint_635"] + 8.37372651867726 * indata[u"Fingerprint_644"] + 5.01250189197489 * indata[u"Fingerprint_646"] + 2.92832864841005 * indata[u"Fingerprint_658"] + -11.9258833451511 * indata[u"Fingerprint_672"] + -3.66307590572502 * indata[u"Fingerprint_673"] + 5.01523609950998 * indata[u"Fingerprint_677"] + -7.34891158838627 * indata[u"Fingerprint_685"] + -9.69182806027143 * indata[u"Fingerprint_686"] + -20.6594810590309 * indata[u"Fingerprint_697"] + -4.69883340766199 * indata[u"Fingerprint_698"] + -4.05555558172901 * indata[u"Fingerprint_710"] + -5.09210479306099 * indata[u"Fingerprint_714"] + 5.64722146641488 * indata[u"Fingerprint_797"] + 8.76318368375387 * indata[u"Fingerprint_818"] + -2.55088197753751 * indata[u"Fingerprint_819"] + 1.64234684434541 * indata[u"Fingerprint_821"] + -27.2756276743237 * indata[u"Fingerprint_822"] + -4.03423305028357 * indata[u"Fingerprint_824"] + -2.16385955240197 * indata[u"Fingerprint_834"] + 2.43939125007722 * indata[u"From_Sanger"] + 3.21181212692343 * indata[u"GO_0000278"] + 0.439424586302319 * indata[u"GO_0016477"] + 2.57145726217565 * indata[u"GO_0032212_X_GO_0043066"] + 0.136638990483162 * indata[u"PKA_172_ASA_X_Fingerprint_644"]))

    outdata[u"Predicted IC50_1"] = 2.77734044230884 + -0.63574670289528 * H1_1 + 1.28206628126003 * H1_2 + 1.00376700271059 * H1_3 + -0.72104815388902 * H1_4 + -0.947306116111545 * H1_5 + -1.59747753442889 * H1_6 + -1.07734416583968 * H1_7

    return outdata[u"Predicted IC50_1"]


