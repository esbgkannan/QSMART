java -classpath weka.jar weka.filters.unsupervised.attribute.Remove -R 2-3 -i ../../../../TrainingSet/FullSet/breast.csv -o ./breast_085_tmp.arff
java -classpath weka.jar weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -V 0.001 -S 1 -c 1 -x 10 -K 20 -M 1 -depth 0 -t ./breast_085_tmp.arff > ./breast_085.txt
rm ./breast_085_tmp.arff
