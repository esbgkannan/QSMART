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
	return {"creator": u"Neural", "modelName": u"", "predicted": u"IC50", "table": u"thyroid", "version": u"14.1.0", "timestamp": u"2019-05-13T03:57:48Z"}


def getInputMetadata():
    return {
        u"EXP_CLK4": "float",
        u"EXP_PLK3": "float",
        u"EXP_PRKCG": "float",
        u"EXP_STK10": "float",
        u"EXP_TLK1": "float",
        u"Fingerprint_611": "float",
        u"Fingerprint_617": "float",
        u"Fingerprint_629": "float",
        u"Fingerprint_635": "float",
        u"Fingerprint_646": "float",
        u"Fingerprint_648": "float",
        u"Fingerprint_677": "float",
        u"Fingerprint_686": "float",
        u"Fingerprint_687": "float",
        u"Fingerprint_694": "float",
        u"Fingerprint_697": "float",
        u"Fingerprint_709": "float",
        u"Fingerprint_710": "float",
        u"Fingerprint_776": "float",
        u"Fingerprint_780": "float",
        u"Fingerprint_797": "float",
        u"Fingerprint_799": "float",
        u"Fingerprint_806": "float",
        u"Fingerprint_818": "float",
        u"Fingerprint_819": "float",
        u"Fingerprint_825": "float",
        u"Fingerprint_826": "float",
        u"Fingerprint_828": "float",
        u"Fingerprint_834": "float",
        u"Fingerprint_835": "float",
        u"Fingerprint_860": "float",
        u"From_Sanger": "float",
        u"GO_0034976": "float"
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

    H1_1 = tanh((-3.58134099832395 + -0.371317854927085 * indata[u"EXP_CLK4"] + 0.155183305724111 * indata[u"EXP_PLK3"] + 3.83248917673779 * indata[u"EXP_PRKCG"] + 0.0320470637968189 * indata[u"EXP_STK10"] + -0.406197796045815 * indata[u"EXP_TLK1"] + -1.36889035847421 * indata[u"Fingerprint_611"] + 1.26830097999468 * indata[u"Fingerprint_617"] + 10.2911527984887 * indata[u"Fingerprint_629"] + -1.0619606664628 * indata[u"Fingerprint_635"] + -1.61764317493733 * indata[u"Fingerprint_646"] + 8.39940150473118 * indata[u"Fingerprint_648"] + -4.76251965946963 * indata[u"Fingerprint_677"] + 4.07739949340321 * indata[u"Fingerprint_686"] + -8.11036395900109 * indata[u"Fingerprint_687"] + -3.3870280849573 * indata[u"Fingerprint_694"] + -2.24985048159658 * indata[u"Fingerprint_697"] + 2.28944642979716 * indata[u"Fingerprint_709"] + -4.46344164740429 * indata[u"Fingerprint_710"] + 0.422250823147433 * indata[u"Fingerprint_776"] + 7.13240899406345 * indata[u"Fingerprint_780"] + -1.12385145128026 * indata[u"Fingerprint_797"] + -3.5768164420408 * indata[u"Fingerprint_799"] + 8.8113188848193 * indata[u"Fingerprint_806"] + 2.20884549259276 * indata[u"Fingerprint_818"] + -5.4327927814133 * indata[u"Fingerprint_819"] + 0.455267225657338 * indata[u"Fingerprint_825"] + 4.22450349108342 * indata[u"Fingerprint_826"] + 1.54210895143755 * indata[u"Fingerprint_828"] + 3.03951883371603 * indata[u"Fingerprint_834"] + 7.21828197688573 * indata[u"Fingerprint_835"] + 0.472564173787098 * indata[u"Fingerprint_860"] + 0.479877208631815 * indata[u"From_Sanger"] + -0.4561176852974 * indata[u"GO_0034976"]))

    H1_2 = tanh((-12.1625907941392 + -0.500700704625312 * indata[u"EXP_CLK4"] + -0.122434547311029 * indata[u"EXP_PLK3"] + 6.07005627423083 * indata[u"EXP_PRKCG"] + -0.879065730139144 * indata[u"EXP_STK10"] + 0.158972956980698 * indata[u"EXP_TLK1"] + 0.480223798745194 * indata[u"Fingerprint_611"] + -4.23695278253859 * indata[u"Fingerprint_617"] + -2.3377130221372 * indata[u"Fingerprint_629"] + 1.76204051893721 * indata[u"Fingerprint_635"] + 5.20207557523024 * indata[u"Fingerprint_646"] + 7.17000458426783 * indata[u"Fingerprint_648"] + 7.68220216787182 * indata[u"Fingerprint_677"] + 1.18356708821446 * indata[u"Fingerprint_686"] + -0.836219326049231 * indata[u"Fingerprint_687"] + -11.8696720184061 * indata[u"Fingerprint_694"] + -0.635297108053374 * indata[u"Fingerprint_697"] + -6.49379513893568 * indata[u"Fingerprint_709"] + -5.90932821816067 * indata[u"Fingerprint_710"] + 0.389903034333172 * indata[u"Fingerprint_776"] + -5.71303286170674 * indata[u"Fingerprint_780"] + 2.17460327965614 * indata[u"Fingerprint_797"] + -3.75885878813997 * indata[u"Fingerprint_799"] + -5.86435433863044 * indata[u"Fingerprint_806"] + -5.68547302213935 * indata[u"Fingerprint_818"] + -1.26555537168825 * indata[u"Fingerprint_819"] + 1.82102620883033 * indata[u"Fingerprint_825"] + -4.24501346608766 * indata[u"Fingerprint_826"] + -8.07016706092969 * indata[u"Fingerprint_828"] + 3.85241471975649 * indata[u"Fingerprint_834"] + -1.47094528844679 * indata[u"Fingerprint_835"] + 2.46959923637303 * indata[u"Fingerprint_860"] + 4.39572371268511 * indata[u"From_Sanger"] + 0.228642700219568 * indata[u"GO_0034976"]))

    H1_3 = tanh((-0.915020092025741 + -0.0558866460579258 * indata[u"EXP_CLK4"] + -0.065626973437225 * indata[u"EXP_PLK3"] + -0.2618559050479 * indata[u"EXP_PRKCG"] + 0.00697194020327165 * indata[u"EXP_STK10"] + 0.0569535260164392 * indata[u"EXP_TLK1"] + 0.242871506372374 * indata[u"Fingerprint_611"] + -0.0224856697161831 * indata[u"Fingerprint_617"] + 0.674266345349328 * indata[u"Fingerprint_629"] + 0.520046812980814 * indata[u"Fingerprint_635"] + -0.140493052754972 * indata[u"Fingerprint_646"] + 1.81460045273901 * indata[u"Fingerprint_648"] + -5.18080910698768 * indata[u"Fingerprint_677"] + -1.34454801405778 * indata[u"Fingerprint_686"] + 2.22216758837685 * indata[u"Fingerprint_687"] + -0.0907791361676821 * indata[u"Fingerprint_694"] + 0.982698557873693 * indata[u"Fingerprint_697"] + 6.18573663157683 * indata[u"Fingerprint_709"] + 0.297692608115729 * indata[u"Fingerprint_710"] + 0.71356924933344 * indata[u"Fingerprint_776"] + 4.77408877427969 * indata[u"Fingerprint_780"] + -1.84138647449381 * indata[u"Fingerprint_797"] + 0.276300770135404 * indata[u"Fingerprint_799"] + -2.46616501420808 * indata[u"Fingerprint_806"] + -1.45497643777135 * indata[u"Fingerprint_818"] + 2.78112147468162 * indata[u"Fingerprint_819"] + -2.42991159293327 * indata[u"Fingerprint_825"] + 3.31882931042857 * indata[u"Fingerprint_826"] + 1.85282285627881 * indata[u"Fingerprint_828"] + -0.209825708880253 * indata[u"Fingerprint_834"] + 12.0038981989605 * indata[u"Fingerprint_835"] + -0.373816402122511 * indata[u"Fingerprint_860"] + -0.763193662529669 * indata[u"From_Sanger"] + 0.0346126626080857 * indata[u"GO_0034976"]))

    H1_4 = tanh((-3.11187847636242 + 0.439176629229699 * indata[u"EXP_CLK4"] + 0.198680427391402 * indata[u"EXP_PLK3"] + 0.462190574464228 * indata[u"EXP_PRKCG"] + -0.0262350611820972 * indata[u"EXP_STK10"] + -0.166251293604537 * indata[u"EXP_TLK1"] + 1.77765541034942 * indata[u"Fingerprint_611"] + -1.6124990726176 * indata[u"Fingerprint_617"] + -4.10998493256984 * indata[u"Fingerprint_629"] + -1.87130041203512 * indata[u"Fingerprint_635"] + 0.619296078941304 * indata[u"Fingerprint_646"] + -0.0522370708033435 * indata[u"Fingerprint_648"] + 2.93142807936962 * indata[u"Fingerprint_677"] + -3.68160927770388 * indata[u"Fingerprint_686"] + 5.01602040404607 * indata[u"Fingerprint_687"] + -4.97227437807278 * indata[u"Fingerprint_694"] + 1.75147844867643 * indata[u"Fingerprint_697"] + 1.84687264598954 * indata[u"Fingerprint_709"] + -3.05673451330966 * indata[u"Fingerprint_710"] + -0.141210983854992 * indata[u"Fingerprint_776"] + 1.27754348670485 * indata[u"Fingerprint_780"] + -3.7941761394298 * indata[u"Fingerprint_797"] + -7.18953636519478 * indata[u"Fingerprint_799"] + -0.6089561678445 * indata[u"Fingerprint_806"] + -2.27081672008946 * indata[u"Fingerprint_818"] + 6.90232711711596 * indata[u"Fingerprint_819"] + -1.66166003657572 * indata[u"Fingerprint_825"] + -4.5588092574625 * indata[u"Fingerprint_826"] + 3.42857567343355 * indata[u"Fingerprint_828"] + -2.15428281499633 * indata[u"Fingerprint_834"] + -0.272961361906645 * indata[u"Fingerprint_835"] + -1.20371064183329 * indata[u"Fingerprint_860"] + 0.771509655196275 * indata[u"From_Sanger"] + -0.148465845664518 * indata[u"GO_0034976"]))

    H1_5 = tanh((-0.242266723452985 + -0.457469349853255 * indata[u"EXP_CLK4"] + 0.741291644009023 * indata[u"EXP_PLK3"] + -2.07808601569382 * indata[u"EXP_PRKCG"] + 0.17109316026465 * indata[u"EXP_STK10"] + -0.882968364702227 * indata[u"EXP_TLK1"] + 0.569443770786152 * indata[u"Fingerprint_611"] + 1.75399341301609 * indata[u"Fingerprint_617"] + 9.2366885659759 * indata[u"Fingerprint_629"] + 6.46308058738829 * indata[u"Fingerprint_635"] + 2.01263937259338 * indata[u"Fingerprint_646"] + 4.19230373474097 * indata[u"Fingerprint_648"] + -0.574573449101357 * indata[u"Fingerprint_677"] + 1.71449139460488 * indata[u"Fingerprint_686"] + -5.90569408262076 * indata[u"Fingerprint_687"] + 3.38278661180541 * indata[u"Fingerprint_694"] + 4.63843381027468 * indata[u"Fingerprint_697"] + 6.28412557050347 * indata[u"Fingerprint_709"] + -1.12655946839499 * indata[u"Fingerprint_710"] + 1.64229447066378 * indata[u"Fingerprint_776"] + -3.04099810965395 * indata[u"Fingerprint_780"] + -4.71204044686496 * indata[u"Fingerprint_797"] + -3.29527510139647 * indata[u"Fingerprint_799"] + -4.8366805667282 * indata[u"Fingerprint_806"] + -2.32228033155046 * indata[u"Fingerprint_818"] + 3.71566164297492 * indata[u"Fingerprint_819"] + -1.27166423099826 * indata[u"Fingerprint_825"] + 3.00833664563646 * indata[u"Fingerprint_826"] + -1.12700511788244 * indata[u"Fingerprint_828"] + -4.52688118360411 * indata[u"Fingerprint_834"] + -2.20281721931743 * indata[u"Fingerprint_835"] + -5.23896295917817 * indata[u"Fingerprint_860"] + 2.86126603129685 * indata[u"From_Sanger"] + -0.0401479974376074 * indata[u"GO_0034976"]))

    H1_6 = tanh((-2.86073056937901 + 0.389968198441701 * indata[u"EXP_CLK4"] + -0.0329104983907205 * indata[u"EXP_PLK3"] + -1.40376890097553 * indata[u"EXP_PRKCG"] + 0.475368501223879 * indata[u"EXP_STK10"] + -0.0605363929710342 * indata[u"EXP_TLK1"] + 2.20751112722882 * indata[u"Fingerprint_611"] + 0.344266656756445 * indata[u"Fingerprint_617"] + 1.76270571862392 * indata[u"Fingerprint_629"] + -2.35200513898022 * indata[u"Fingerprint_635"] + 2.72454465746797 * indata[u"Fingerprint_646"] + -6.39275978252504 * indata[u"Fingerprint_648"] + -9.5912678460906 * indata[u"Fingerprint_677"] + -6.32805212901208 * indata[u"Fingerprint_686"] + -2.99376320292218 * indata[u"Fingerprint_687"] + 7.60038023594459 * indata[u"Fingerprint_694"] + 0.868735526457389 * indata[u"Fingerprint_697"] + 4.49458282160835 * indata[u"Fingerprint_709"] + 4.31347481153287 * indata[u"Fingerprint_710"] + 2.63756402977608 * indata[u"Fingerprint_776"] + -1.72216748728393 * indata[u"Fingerprint_780"] + 1.4804297340951 * indata[u"Fingerprint_797"] + 7.03188185610213 * indata[u"Fingerprint_799"] + -5.92248696505518 * indata[u"Fingerprint_806"] + -1.27284552135946 * indata[u"Fingerprint_818"] + 6.36495089811147 * indata[u"Fingerprint_819"] + -6.03885457502141 * indata[u"Fingerprint_825"] + 8.37691914191213 * indata[u"Fingerprint_826"] + 2.91744257087921 * indata[u"Fingerprint_828"] + 3.8668585114297 * indata[u"Fingerprint_834"] + 15.1587290444379 * indata[u"Fingerprint_835"] + -1.51372031847198 * indata[u"Fingerprint_860"] + -0.557058589946164 * indata[u"From_Sanger"] + -0.423297802998447 * indata[u"GO_0034976"]))

    outdata[u"Predicted IC50_1"] = 2.93654189467356 + -1.73578423900138 * H1_1 + 1.29470512106152 * H1_2 + 4.27713905839637 * H1_3 + -2.13675079622225 * H1_4 + -1.31484451958504 * H1_5 + -1.9590690780027 * H1_6

    return outdata[u"Predicted IC50_1"]


