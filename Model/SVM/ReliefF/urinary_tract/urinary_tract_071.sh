java -classpath weka.jar weka.filters.unsupervised.attribute.Remove -R 2-3 -i ../../../../TrainingSet/FullSet/urinary_tract.csv -o ./urinary_tract_071_tmp.arff
java -classpath weka.jar weka.classifiers.functions.SMOreg -C 1 -I "weka.classifiers.functions.supportVector.RegSMOImproved -T 0.001 -V -P 1.0E-12 -L 0.1 -W 1" -K "weka.classifiers.functions.supportVector.PolyKernel" -c 1 -x 10 -t ./urinary_tract_071_tmp.arff > ./urinary_tract_071.txt
rm ./urinary_tract_071_tmp.arff
