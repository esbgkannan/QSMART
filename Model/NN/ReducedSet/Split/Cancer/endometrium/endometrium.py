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
	return {"creator": u"Neural", "modelName": u"", "predicted": u"IC50", "table": u"endometrium", "version": u"14.1.0", "timestamp": u"2019-07-23T03:10:58Z"}


def getInputMetadata():
    return {
        u"CLS_average_ploidy": "float",
        u"GO_0030878_EXP": "float",
        u"REC_R_HSA_141409": "float",
        u"REC_R_HSA_141409_EXP": "float"
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

    H2_1 = tanh((0.451282250581599 + -0.240164893504788 * indata[u"CLS_average_ploidy"] + -0.0033564830159675 * indata[u"GO_0030878_EXP"] + 0.169304807825324 * indata[u"REC_R_HSA_141409"] + -0.200799450483793 * indata[u"REC_R_HSA_141409_EXP"]))

    H2_2 = tanh((-1.17439112628372 + 0.945385404667746 * indata[u"CLS_average_ploidy"] + 0.0844762934050072 * indata[u"GO_0030878_EXP"] + -1.07095983538835 * indata[u"REC_R_HSA_141409"] + -0.105202121898748 * indata[u"REC_R_HSA_141409_EXP"]))

    H2_3 = tanh((-1.39270958066871 + 0.256260870918879 * indata[u"CLS_average_ploidy"] + 0.0511913486424986 * indata[u"GO_0030878_EXP"] + -0.0108022278341889 * indata[u"REC_R_HSA_141409"] + 0.145360131037518 * indata[u"REC_R_HSA_141409_EXP"]))

    H2_4 = tanh((1.04200714486196 + -0.762837977817704 * indata[u"CLS_average_ploidy"] + 0.0272964507076644 * indata[u"GO_0030878_EXP"] + 0.35422321735829 * indata[u"REC_R_HSA_141409"] + 0.0419016309393887 * indata[u"REC_R_HSA_141409_EXP"]))

    H2_5 = tanh((-0.765241247425775 + 0.677914885693375 * indata[u"CLS_average_ploidy"] + -0.00643899445667975 * indata[u"GO_0030878_EXP"] + -0.86058078771506 * indata[u"REC_R_HSA_141409"] + 0.002097122167405 * indata[u"REC_R_HSA_141409_EXP"]))

    H2_6 = tanh((3.70040162535574 + -1.27422643937267 * indata[u"CLS_average_ploidy"] + -0.080847302687585 * indata[u"GO_0030878_EXP"] + 0.103861327956922 * indata[u"REC_R_HSA_141409"] + 0.0398055880668685 * indata[u"REC_R_HSA_141409_EXP"]))

    H2_7 = tanh((-1.2976811336558 + 0.794990943395692 * indata[u"CLS_average_ploidy"] + 0.0669420753242888 * indata[u"GO_0030878_EXP"] + -0.645887608036206 * indata[u"REC_R_HSA_141409"] + 0.0801863013834822 * indata[u"REC_R_HSA_141409_EXP"]))

    H2_8 = tanh((3.06610210911989 + -1.18740778596185 * indata[u"CLS_average_ploidy"] + 0.0249825937097586 * indata[u"GO_0030878_EXP"] + -0.136036037585055 * indata[u"REC_R_HSA_141409"] + -0.0576488892268949 * indata[u"REC_R_HSA_141409_EXP"]))

    H2_9 = tanh((1.94763427015532 + -0.519213811642655 * indata[u"CLS_average_ploidy"] + 0.124474350277796 * indata[u"GO_0030878_EXP"] + -1.44882645842561 * indata[u"REC_R_HSA_141409"] + 0.00551290973434688 * indata[u"REC_R_HSA_141409_EXP"]))

    H2_10 = tanh((-0.380852375131084 + 0.00812734338453029 * indata[u"CLS_average_ploidy"] + -0.000243580148991114 * indata[u"GO_0030878_EXP"] + -0.645643138142771 * indata[u"REC_R_HSA_141409"] + 0.0727794188161566 * indata[u"REC_R_HSA_141409_EXP"]))

    H2_11 = tanh((1.55094991598989 + -0.476583782953048 * indata[u"CLS_average_ploidy"] + -0.0578617247527633 * indata[u"GO_0030878_EXP"] + -0.878949141872742 * indata[u"REC_R_HSA_141409"] + 0.114303801295708 * indata[u"REC_R_HSA_141409_EXP"]))

    H1_1 = tanh((-0.969697468443976 + 0.604381660498821 * H2_1 + -0.189075793590694 * H2_10 + 0.122944474588483 * H2_11 + -0.580152944464766 * H2_2 + -0.55559636555362 * H2_3 + -0.126024918685252 * H2_4 + -0.239221986734818 * H2_5 + -0.206226694106925 * H2_6 + 0.00699145287128565 * H2_7 + 0.293804649697973 * H2_8 + 0.376403219844388 * H2_9))

    H1_2 = tanh((0.130484034538847 + -0.130501356105987 * H2_1 + -0.945263462321485 * H2_10 + 0.821891096460285 * H2_11 + -0.232929623122266 * H2_2 + -0.174154754355413 * H2_3 + 0.0148750799654537 * H2_4 + -0.0550285749253858 * H2_5 + -0.642067972966178 * H2_6 + -0.545063124783985 * H2_7 + 0.352842356878759 * H2_8 + -0.546847027652541 * H2_9))

    H1_3 = tanh((-0.219574797388758 + 0.32622440458321 * H2_1 + 0.910763513571989 * H2_10 + 0.4339439791983 * H2_11 + -0.494343032053498 * H2_2 + -0.510821194817829 * H2_3 + 0.0351236745759537 * H2_4 + -0.047114666209561 * H2_5 + 0.148695877243805 * H2_6 + -1.06951539856497 * H2_7 + 0.776122339656957 * H2_8 + -0.235240434305001 * H2_9))

    H1_4 = tanh((0.11499003462601 + -0.477378438872082 * H2_1 + 0.518727396389981 * H2_10 + -0.200289564091671 * H2_11 + 0.224289153843541 * H2_2 + 0.662502339224329 * H2_3 + -0.573989518705799 * H2_4 + 0.537400082334493 * H2_5 + -0.0427256993341683 * H2_6 + -0.0904954904257757 * H2_7 + 0.506763125806948 * H2_8 + -0.334963255182443 * H2_9))

    outdata[u"Predicted IC50_1"] = 6.21944758520235 + 7.65217733981785 * H1_1 + 3.21322156917679 * H1_2 + -2.88736582770881 * H1_3 + 0.4308437733992 * H1_4

    return outdata[u"Predicted IC50_1"]


