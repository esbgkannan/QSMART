java -classpath weka.jar weka.filters.unsupervised.attribute.Remove -R 2-3 -i ../../../../TrainingSet/FullSet/lung_other.csv -o ./lung_other_054_tmp.arff
java -classpath weka.jar weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -V 0.001 -S 1 -c 1 -x 10 -K 10 -M 5 -depth 5 -t ./lung_other_054_tmp.arff > ./lung_other_054.txt
rm ./lung_other_054_tmp.arff
