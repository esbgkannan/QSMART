java -classpath weka.jar weka.filters.unsupervised.attribute.Remove -R 2-3 -i ../../../../TrainingSet/FullSet/lung_other.csv -o ./lung_other_025_tmp.arff
java -classpath weka.jar weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -V 0.001 -S 1 -c 1 -x 10 -K 5 -M 1 -depth 0 -t ./lung_other_025_tmp.arff > ./lung_other_025.txt
rm ./lung_other_025_tmp.arff
