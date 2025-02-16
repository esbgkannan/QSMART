/* Neural SAS Scoring*/
/*%PRODUCER: JMP - Neural */
/*%TARGET: IC50 */
/*%INPUT: PKA_263_EXP_X_Fingerprint_826 */
/*%INPUT: PKA_280_B62_X_Fingerprint_819 */
/*%INPUT: EXP_ERN2_X_EXP_LRGUK */
/*%INPUT: EXP_FGR_X_EXP_APOB */
/*%INPUT: EXP_ITK_X_EXP_CD28 */
/*%INPUT: EXP_PHKG2_X_EXP_C1QTNF1 */
/*%INPUT: EXP_TXK_X_EXP_PHLPP1 */
/*%INPUT: PWY_R_HSA_199418_X_PWY_R_HSA_562 */
/*%OUTPUT: IC50_Predicted */
LABEL IC50_Predicted = 'Predicted: IC50';
/* Transformation Code */

/* Hidden Layer Code */
H1 = tanh(.5*(1.41785776588438*PKA_263_EXP_X_Fingerprint_826 + 0.599729249477683*PKA_280_B62_X_Fingerprint_819 + 1.15744187629857*EXP_ERN2_X_EXP_LRGUK + -1.50763139475877*EXP_FGR_X_EXP_APOB + 1.11321773038267*EXP_ITK_X_EXP_CD28 + 0.322843399929574*EXP_PHKG2_X_EXP_C1QTNF1 + 0.0396481979653442*EXP_TXK_X_EXP_PHLPP1 + 1.30347288500321*PWY_R_HSA_199418_X_PWY_R_HSA_562 + -18.2007412994449));
H2 = tanh(.5*(-1.98597504373714*PKA_263_EXP_X_Fingerprint_826 + 0.00420911436796341*PKA_280_B62_X_Fingerprint_819 + 0.648942603013035*EXP_ERN2_X_EXP_LRGUK + 3.59269662913653*EXP_FGR_X_EXP_APOB + -3.5842782224036*EXP_ITK_X_EXP_CD28 + -0.416736339402413*EXP_PHKG2_X_EXP_C1QTNF1 + -0.134904081010638*EXP_TXK_X_EXP_PHLPP1 + -0.00423314949105127*PWY_R_HSA_199418_X_PWY_R_HSA_562 + 4.42116794457145));
H3 = tanh(.5*(1.0052427310922*PKA_263_EXP_X_Fingerprint_826 + -0.371691608502569*PKA_280_B62_X_Fingerprint_819 + -2.18518580466163*EXP_ERN2_X_EXP_LRGUK + 0.991551757434857*EXP_FGR_X_EXP_APOB + 0.764573066756146*EXP_ITK_X_EXP_CD28 + 0.0546965914829139*EXP_PHKG2_X_EXP_C1QTNF1 + -0.0829692158412911*EXP_TXK_X_EXP_PHLPP1 + -0.762892798234953*PWY_R_HSA_199418_X_PWY_R_HSA_562 + 5.49580828138564));
H4 = tanh(.5*(0.262409964841215*PKA_263_EXP_X_Fingerprint_826 + 0.00474913226828063*PKA_280_B62_X_Fingerprint_819 + 0.765964170584579*EXP_ERN2_X_EXP_LRGUK + 0.63783331751367*EXP_FGR_X_EXP_APOB + -3.48688227388248*EXP_ITK_X_EXP_CD28 + -0.781780623196969*EXP_PHKG2_X_EXP_C1QTNF1 + -0.0224252727270888*EXP_TXK_X_EXP_PHLPP1 + -1.17737991774077*PWY_R_HSA_199418_X_PWY_R_HSA_562 + 32.8109218662436));
H5 = tanh(.5*(0.628647121476658*PKA_263_EXP_X_Fingerprint_826 + -4.81089564560664*PKA_280_B62_X_Fingerprint_819 + -0.826539350541297*EXP_ERN2_X_EXP_LRGUK + 4.8056130362496*EXP_FGR_X_EXP_APOB + -3.6062130825347*EXP_ITK_X_EXP_CD28 + 0.266170343325025*EXP_PHKG2_X_EXP_C1QTNF1 + 0.445441282702011*EXP_TXK_X_EXP_PHLPP1 + -1.16009646125046*PWY_R_HSA_199418_X_PWY_R_HSA_562 + -13.770842849714));
H6 = tanh(.5*(2.37845473030238*PKA_263_EXP_X_Fingerprint_826 + 0.712839539819565*PKA_280_B62_X_Fingerprint_819 + 0.400443682651684*EXP_ERN2_X_EXP_LRGUK + -3.88017906002778*EXP_FGR_X_EXP_APOB + -3.52507217371179*EXP_ITK_X_EXP_CD28 + 0.344882423878855*EXP_PHKG2_X_EXP_C1QTNF1 + 0.174248660382906*EXP_TXK_X_EXP_PHLPP1 + -0.665402387881131*PWY_R_HSA_199418_X_PWY_R_HSA_562 + 50.9299477467092));
H7 = tanh(.5*(2.9182107878328*PKA_263_EXP_X_Fingerprint_826 + 2.32652729304918*PKA_280_B62_X_Fingerprint_819 + -0.599534912611662*EXP_ERN2_X_EXP_LRGUK + 1.86368576330043*EXP_FGR_X_EXP_APOB + -0.170573554645023*EXP_ITK_X_EXP_CD28 + 0.177562872494508*EXP_PHKG2_X_EXP_C1QTNF1 + 0.548948738012087*EXP_TXK_X_EXP_PHLPP1 + -0.119695233436493*PWY_R_HSA_199418_X_PWY_R_HSA_562 + -20.1235008951283));
H8 = tanh(.5*(-2.65016210457576*PKA_263_EXP_X_Fingerprint_826 + 2.89375678286435*PKA_280_B62_X_Fingerprint_819 + 1.14708126016724*EXP_ERN2_X_EXP_LRGUK + 0.319941857651954*EXP_FGR_X_EXP_APOB + -3.05330342371348*EXP_ITK_X_EXP_CD28 + 0.60104002018327*EXP_PHKG2_X_EXP_C1QTNF1 + -0.124194917429144*EXP_TXK_X_EXP_PHLPP1 + -1.07806380381405*PWY_R_HSA_199418_X_PWY_R_HSA_562 + -0.725361075188363));

/* Final Layer Code */
THETA1=1.01029563151902*H1 + -0.480152056211842*H2 + -0.635112790505582*H3 + 0.0386640738399413*H4 + 0.392834700531934*H5 + -0.369233725283624*H6 + -0.373186219440024*H7 + -0.462593924927461*H8 + 2.62009062756816;

/* Response Mapping Code */
IC50_Predicted = THETA1;

