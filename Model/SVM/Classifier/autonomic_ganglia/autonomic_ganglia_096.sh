java -classpath weka.jar weka.filters.unsupervised.attribute.Remove -R 2-3 -i ../../../../TrainingSet/FullSet/autonomic_ganglia.csv -o ./autonomic_ganglia_096_tmp.arff
java -classpath weka.jar weka.classifiers.functions.SMOreg -C 10 -I "weka.classifiers.functions.supportVector.RegSMOImproved -T 0.001 -V -P 1.0E-12 -L 0.1 -W 1" -K "weka.classifiers.functions.supportVector.PolyKernel" -c 1 -x 10 -t ./autonomic_ganglia_096_tmp.arff > ./autonomic_ganglia_096.txt
rm ./autonomic_ganglia_096_tmp.arff
