java -classpath weka.jar weka.filters.unsupervised.attribute.Remove -R 2-3 -i ../../../../TrainingSet/FullSet/upper_aerodigestive_tract.csv -o ./upper_aerodigestive_tract_060_tmp.arff
java -classpath weka.jar weka.classifiers.functions.SMOreg -C 1 -I "weka.classifiers.functions.supportVector.RegSMOImproved -T 0.001 -V -P 1.0E-12 -L 0.0001 -W 1" -K "weka.classifiers.functions.supportVector.RBFKernel -G 0.1" -c 1 -x 10 -t ./upper_aerodigestive_tract_060_tmp.arff > ./upper_aerodigestive_tract_060.txt
rm ./upper_aerodigestive_tract_060_tmp.arff
