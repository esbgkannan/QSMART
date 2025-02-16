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
	return {"creator": u"Neural", "modelName": u"", "predicted": u"IC50", "table": u"cervix", "version": u"14.1.0", "timestamp": u"2019-05-12T04:29:44Z"}


def getInputMetadata():
    return {
        u"EXP_BRD4": "float",
        u"EXP_CLK4": "float",
        u"EXP_DYRK2": "float",
        u"EXP_IRAK3": "float",
        u"Fingerprint_588": "float",
        u"Fingerprint_611": "float",
        u"Fingerprint_617": "float",
        u"Fingerprint_629": "float",
        u"Fingerprint_646": "float",
        u"Fingerprint_648": "float",
        u"Fingerprint_677": "float",
        u"Fingerprint_686": "float",
        u"Fingerprint_687": "float",
        u"Fingerprint_697": "float",
        u"Fingerprint_710": "float",
        u"Fingerprint_714": "float",
        u"Fingerprint_776": "float",
        u"Fingerprint_780": "float",
        u"Fingerprint_782": "float",
        u"Fingerprint_791": "float",
        u"Fingerprint_797": "float",
        u"Fingerprint_799": "float",
        u"Fingerprint_801": "float",
        u"Fingerprint_806": "float",
        u"Fingerprint_813": "float",
        u"Fingerprint_818": "float",
        u"Fingerprint_819": "float",
        u"Fingerprint_820": "float",
        u"Fingerprint_821": "float",
        u"Fingerprint_822": "float",
        u"Fingerprint_828": "float",
        u"Fingerprint_860": "float",
        u"From_Sanger": "float",
        u"GO_0001756": "float",
        u"GO_0030336_EXP": "float",
        u"GO_0038083_CSV": "float",
        u"GO_0048812_EXP": "float"
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

    H1_1 = tanh((10.6488984361335 + -0.496360173520522 * indata[u"EXP_BRD4"] + 0.378904976094906 * indata[u"EXP_CLK4"] + 0.228922048350676 * indata[u"EXP_DYRK2"] + 0.283418589645403 * indata[u"EXP_IRAK3"] + 5.03305996583682 * indata[u"Fingerprint_588"] + -4.28733718546815 * indata[u"Fingerprint_611"] + -6.00086807589465 * indata[u"Fingerprint_617"] + -2.15951531368963 * indata[u"Fingerprint_629"] + -1.62460470778585 * indata[u"Fingerprint_646"] + -11.9063154581493 * indata[u"Fingerprint_648"] + -8.81091125269477 * indata[u"Fingerprint_677"] + -2.39933601741396 * indata[u"Fingerprint_686"] + 8.8643168247926 * indata[u"Fingerprint_687"] + 2.95020296397781 * indata[u"Fingerprint_697"] + -1.19838901706716 * indata[u"Fingerprint_710"] + 3.38304231877347 * indata[u"Fingerprint_714"] + 1.58281159855416 * indata[u"Fingerprint_776"] + 2.23948980325228 * indata[u"Fingerprint_780"] + -9.61371409006594 * indata[u"Fingerprint_782"] + -7.04100647197722 * indata[u"Fingerprint_791"] + -1.58687922236858 * indata[u"Fingerprint_797"] + -4.93414538679413 * indata[u"Fingerprint_799"] + 0.658498964620107 * indata[u"Fingerprint_801"] + -7.08670712242513 * indata[u"Fingerprint_806"] + -8.21033030647313 * indata[u"Fingerprint_813"] + -4.83323047093077 * indata[u"Fingerprint_818"] + 4.12890706740975 * indata[u"Fingerprint_819"] + -5.35560707142622 * indata[u"Fingerprint_820"] + -1.81620436739741 * indata[u"Fingerprint_821"] + 12.9113918797427 * indata[u"Fingerprint_822"] + -2.94435366526536 * indata[u"Fingerprint_828"] + -2.87485264090621 * indata[u"Fingerprint_860"] + 1.62614150108003 * indata[u"From_Sanger"] + 0.0124706879555889 * indata[u"GO_0001756"] + -0.013663526979267 * indata[u"GO_0030336_EXP"] + -0.39129626603139 * indata[u"GO_0038083_CSV"] + -0.019634509832209 * indata[u"GO_0048812_EXP"]))

    H1_2 = tanh((5.28761947035578 + -1.28484336052448 * indata[u"EXP_BRD4"] + 0.430622683303846 * indata[u"EXP_CLK4"] + 0.620171122626693 * indata[u"EXP_DYRK2"] + 0.982438198506117 * indata[u"EXP_IRAK3"] + 0.569995330579524 * indata[u"Fingerprint_588"] + 1.60649564011571 * indata[u"Fingerprint_611"] + 3.53613860120777 * indata[u"Fingerprint_617"] + 3.56775755679082 * indata[u"Fingerprint_629"] + -0.00840399817965426 * indata[u"Fingerprint_646"] + 11.435197369306 * indata[u"Fingerprint_648"] + -9.56409422966756 * indata[u"Fingerprint_677"] + -2.10855177732276 * indata[u"Fingerprint_686"] + -3.40929276515527 * indata[u"Fingerprint_687"] + -1.69156535110771 * indata[u"Fingerprint_697"] + 0.448118385100557 * indata[u"Fingerprint_710"] + -0.448013688164794 * indata[u"Fingerprint_714"] + -3.2357221620202 * indata[u"Fingerprint_776"] + 1.82668145822988 * indata[u"Fingerprint_780"] + 6.06467935393906 * indata[u"Fingerprint_782"] + -0.20774635485045 * indata[u"Fingerprint_791"] + 1.78774991298873 * indata[u"Fingerprint_797"] + -0.247989052768247 * indata[u"Fingerprint_799"] + -7.05457043016545 * indata[u"Fingerprint_801"] + 2.7013902953404 * indata[u"Fingerprint_806"] + 7.57285313324026 * indata[u"Fingerprint_813"] + 1.01134382946108 * indata[u"Fingerprint_818"] + -4.91979094770178 * indata[u"Fingerprint_819"] + -3.42255846087399 * indata[u"Fingerprint_820"] + 0.47204120432648 * indata[u"Fingerprint_821"] + -1.36906603981698 * indata[u"Fingerprint_822"] + 9.94359264799333 * indata[u"Fingerprint_828"] + 18.4969010361521 * indata[u"Fingerprint_860"] + -5.48365841261906 * indata[u"From_Sanger"] + -0.663552393746495 * indata[u"GO_0001756"] + -0.116046455012673 * indata[u"GO_0030336_EXP"] + 0.257969704704322 * indata[u"GO_0038083_CSV"] + 0.15340551711187 * indata[u"GO_0048812_EXP"]))

    H1_3 = tanh((15.8348138793602 + -2.01790595523506 * indata[u"EXP_BRD4"] + -0.498311165013597 * indata[u"EXP_CLK4"] + -0.429137770710091 * indata[u"EXP_DYRK2"] + 0.064519776019711 * indata[u"EXP_IRAK3"] + -6.97656497537891 * indata[u"Fingerprint_588"] + -1.72251360156903 * indata[u"Fingerprint_611"] + 9.46117716428258 * indata[u"Fingerprint_617"] + -1.35528754991236 * indata[u"Fingerprint_629"] + 5.38201466256811 * indata[u"Fingerprint_646"] + -2.7519398302522 * indata[u"Fingerprint_648"] + -4.53568755769832 * indata[u"Fingerprint_677"] + 1.59947024862029 * indata[u"Fingerprint_686"] + -4.66571037084591 * indata[u"Fingerprint_687"] + 1.84702613843698 * indata[u"Fingerprint_697"] + 4.69373540692174 * indata[u"Fingerprint_710"] + 1.22761863384326 * indata[u"Fingerprint_714"] + -3.26588055586625 * indata[u"Fingerprint_776"] + 6.24382504704783 * indata[u"Fingerprint_780"] + -2.0597996687217 * indata[u"Fingerprint_782"] + 1.20615320450061 * indata[u"Fingerprint_791"] + -0.499873383787208 * indata[u"Fingerprint_797"] + -10.2064164126015 * indata[u"Fingerprint_799"] + 0.290661277854805 * indata[u"Fingerprint_801"] + 10.2798694928465 * indata[u"Fingerprint_806"] + -6.83371932480796 * indata[u"Fingerprint_813"] + -1.11286351048771 * indata[u"Fingerprint_818"] + -4.90113267164786 * indata[u"Fingerprint_819"] + -0.0541473984306631 * indata[u"Fingerprint_820"] + -1.20078305543635 * indata[u"Fingerprint_821"] + -0.975515632292665 * indata[u"Fingerprint_822"] + -1.64954359520573 * indata[u"Fingerprint_828"] + -4.36953183466484 * indata[u"Fingerprint_860"] + -2.53746448981877 * indata[u"From_Sanger"] + -1.41537933639856 * indata[u"GO_0001756"] + -0.0268080272004219 * indata[u"GO_0030336_EXP"] + 1.24954701907214 * indata[u"GO_0038083_CSV"] + 0.309910237213547 * indata[u"GO_0048812_EXP"]))

    H1_4 = tanh((25.3013610886664 + -2.93527659628334 * indata[u"EXP_BRD4"] + -1.00669852563171 * indata[u"EXP_CLK4"] + 0.137466251563857 * indata[u"EXP_DYRK2"] + -0.169173130484977 * indata[u"EXP_IRAK3"] + 8.73699002381141 * indata[u"Fingerprint_588"] + -0.941892181346109 * indata[u"Fingerprint_611"] + -2.73215643348053 * indata[u"Fingerprint_617"] + 1.90888399122097 * indata[u"Fingerprint_629"] + 7.39474352411385 * indata[u"Fingerprint_646"] + 6.5747718240219 * indata[u"Fingerprint_648"] + -9.96651103091236 * indata[u"Fingerprint_677"] + 5.36551659092238 * indata[u"Fingerprint_686"] + 3.75194688464454 * indata[u"Fingerprint_687"] + -0.248941861885502 * indata[u"Fingerprint_697"] + 0.139604670915498 * indata[u"Fingerprint_710"] + 2.41237692648093 * indata[u"Fingerprint_714"] + -0.246272914804115 * indata[u"Fingerprint_776"] + -1.6680724114652 * indata[u"Fingerprint_780"] + 8.07127900334691 * indata[u"Fingerprint_782"] + 1.01843395593947 * indata[u"Fingerprint_791"] + -2.02864891965865 * indata[u"Fingerprint_797"] + 17.636881414583 * indata[u"Fingerprint_799"] + 12.1954883117199 * indata[u"Fingerprint_801"] + -8.78144226933218 * indata[u"Fingerprint_806"] + 5.23706329322214 * indata[u"Fingerprint_813"] + -0.445960944541236 * indata[u"Fingerprint_818"] + 1.27201287553279 * indata[u"Fingerprint_819"] + 2.37157245228462 * indata[u"Fingerprint_820"] + 7.39877384734069 * indata[u"Fingerprint_821"] + -6.28096992259286 * indata[u"Fingerprint_822"] + 6.73410460752746 * indata[u"Fingerprint_828"] + 0.145456757885583 * indata[u"Fingerprint_860"] + -3.6157917396315 * indata[u"From_Sanger"] + 0.209433014262324 * indata[u"GO_0001756"] + -0.237346982364406 * indata[u"GO_0030336_EXP"] + -0.179688454261299 * indata[u"GO_0038083_CSV"] + 0.0231545226594579 * indata[u"GO_0048812_EXP"]))

    H1_5 = tanh((-4.43851807207219 + 0.842944324658197 * indata[u"EXP_BRD4"] + 0.505375254777875 * indata[u"EXP_CLK4"] + 1.0613961028534 * indata[u"EXP_DYRK2"] + -0.364282542543496 * indata[u"EXP_IRAK3"] + -0.624740179621713 * indata[u"Fingerprint_588"] + -2.17293392079938 * indata[u"Fingerprint_611"] + -1.74456118192895 * indata[u"Fingerprint_617"] + 5.67152124665733 * indata[u"Fingerprint_629"] + -0.798321298907531 * indata[u"Fingerprint_646"] + -4.02735121521055 * indata[u"Fingerprint_648"] + -1.18091647044904 * indata[u"Fingerprint_677"] + 0.858431363464199 * indata[u"Fingerprint_686"] + 15.1108417825605 * indata[u"Fingerprint_687"] + -2.41390147223794 * indata[u"Fingerprint_697"] + -3.99422460958303 * indata[u"Fingerprint_710"] + -1.69648536023723 * indata[u"Fingerprint_714"] + 0.482085526452969 * indata[u"Fingerprint_776"] + -0.578073020597702 * indata[u"Fingerprint_780"] + -4.0513071693198 * indata[u"Fingerprint_782"] + -0.208886311409096 * indata[u"Fingerprint_791"] + 0.493776706873646 * indata[u"Fingerprint_797"] + -3.00971362148671 * indata[u"Fingerprint_799"] + 5.76821420264385 * indata[u"Fingerprint_801"] + -7.36892303651473 * indata[u"Fingerprint_806"] + 1.95301695513229 * indata[u"Fingerprint_813"] + -3.54989159677033 * indata[u"Fingerprint_818"] + 0.0232479981214004 * indata[u"Fingerprint_819"] + -12.3282767807339 * indata[u"Fingerprint_820"] + 0.267680086603741 * indata[u"Fingerprint_821"] + 0.860224677146204 * indata[u"Fingerprint_822"] + 1.0544496589431 * indata[u"Fingerprint_828"] + -7.07491925806337 * indata[u"Fingerprint_860"] + -4.74779811687285 * indata[u"From_Sanger"] + 0.0924084996108079 * indata[u"GO_0001756"] + -0.102834362174925 * indata[u"GO_0030336_EXP"] + -0.563369487414768 * indata[u"GO_0038083_CSV"] + 0.130500202420596 * indata[u"GO_0048812_EXP"]))

    H1_6 = tanh((9.32124474719207 + -1.09321996433777 * indata[u"EXP_BRD4"] + -0.792118983240436 * indata[u"EXP_CLK4"] + 0.317018715791216 * indata[u"EXP_DYRK2"] + -0.473592957376367 * indata[u"EXP_IRAK3"] + 6.5284910451263 * indata[u"Fingerprint_588"] + 6.32296317366689 * indata[u"Fingerprint_611"] + 3.39876870717963 * indata[u"Fingerprint_617"] + -3.0035955815289 * indata[u"Fingerprint_629"] + 1.60027019405556 * indata[u"Fingerprint_646"] + -2.72218437250126 * indata[u"Fingerprint_648"] + -10.4355655609415 * indata[u"Fingerprint_677"] + 3.13626081617823 * indata[u"Fingerprint_686"] + -1.98017750924098 * indata[u"Fingerprint_687"] + -3.09585992508598 * indata[u"Fingerprint_697"] + -1.05856060369835 * indata[u"Fingerprint_710"] + 10.6938377794839 * indata[u"Fingerprint_714"] + 0.812903392439365 * indata[u"Fingerprint_776"] + 9.32331379866093 * indata[u"Fingerprint_780"] + 10.4029147424563 * indata[u"Fingerprint_782"] + -0.830848360828511 * indata[u"Fingerprint_791"] + 7.79147602363864 * indata[u"Fingerprint_797"] + -5.76064839587989 * indata[u"Fingerprint_799"] + -2.91859566413562 * indata[u"Fingerprint_801"] + -6.94648118639847 * indata[u"Fingerprint_806"] + 4.29452410625133 * indata[u"Fingerprint_813"] + -0.00434838245309358 * indata[u"Fingerprint_818"] + 0.77991246987194 * indata[u"Fingerprint_819"] + 3.04728199856843 * indata[u"Fingerprint_820"] + 2.23504404565029 * indata[u"Fingerprint_821"] + 4.09762843032544 * indata[u"Fingerprint_822"] + 7.36488939192777 * indata[u"Fingerprint_828"] + 5.52550971893251 * indata[u"Fingerprint_860"] + -2.14472432117404 * indata[u"From_Sanger"] + 0.481900577656132 * indata[u"GO_0001756"] + -0.0290287320474627 * indata[u"GO_0030336_EXP"] + 0.126168577179101 * indata[u"GO_0038083_CSV"] + -0.00912665833111081 * indata[u"GO_0048812_EXP"]))

    H1_7 = tanh((2.78432041832687 + -0.347262226389508 * indata[u"EXP_BRD4"] + 0.121759104376399 * indata[u"EXP_CLK4"] + -0.100549988845665 * indata[u"EXP_DYRK2"] + 0.40668235441862 * indata[u"EXP_IRAK3"] + -5.56466254786705 * indata[u"Fingerprint_588"] + 5.2473895387846 * indata[u"Fingerprint_611"] + 6.68150339864023 * indata[u"Fingerprint_617"] + -6.7862361287405 * indata[u"Fingerprint_629"] + -8.93893938149205 * indata[u"Fingerprint_646"] + -19.7902740044417 * indata[u"Fingerprint_648"] + 4.10517366360991 * indata[u"Fingerprint_677"] + 5.09603710141885 * indata[u"Fingerprint_686"] + 1.88778621523289 * indata[u"Fingerprint_687"] + 1.10424780544775 * indata[u"Fingerprint_697"] + -4.59525921784953 * indata[u"Fingerprint_710"] + 2.19710724834217 * indata[u"Fingerprint_714"] + 5.438525467197 * indata[u"Fingerprint_776"] + 12.0344850890184 * indata[u"Fingerprint_780"] + 7.15141320833344 * indata[u"Fingerprint_782"] + 6.43535057356579 * indata[u"Fingerprint_791"] + -0.640556780724049 * indata[u"Fingerprint_797"] + -0.720847482303916 * indata[u"Fingerprint_799"] + 7.46353797264378 * indata[u"Fingerprint_801"] + -3.60452144083942 * indata[u"Fingerprint_806"] + -4.31718038805074 * indata[u"Fingerprint_813"] + 3.84664251891129 * indata[u"Fingerprint_818"] + -7.45751227718139 * indata[u"Fingerprint_819"] + -0.43007937019833 * indata[u"Fingerprint_820"] + -8.13740130051577 * indata[u"Fingerprint_821"] + 6.43788266714003 * indata[u"Fingerprint_822"] + 4.76794440617501 * indata[u"Fingerprint_828"] + 2.60892075112718 * indata[u"Fingerprint_860"] + -3.34761611401116 * indata[u"From_Sanger"] + -0.125354283389786 * indata[u"GO_0001756"] + 0.0235011069823261 * indata[u"GO_0030336_EXP"] + 0.175675135412923 * indata[u"GO_0038083_CSV"] + 0.0020005875938052 * indata[u"GO_0048812_EXP"]))

    outdata[u"Predicted IC50_1"] = 2.81330462468271 + 1.87423341199858 * H1_1 + 1.75354063081367 * H1_2 + -0.672970051056592 * H1_3 + 1.89684559326826 * H1_4 + -1.52772995265426 * H1_5 + -1.90239723212402 * H1_6 + 2.04503552524916 * H1_7

    return outdata[u"Predicted IC50_1"]


