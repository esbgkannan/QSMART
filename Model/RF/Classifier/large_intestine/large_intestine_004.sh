java -classpath weka.jar weka.filters.unsupervised.attribute.Remove -R 2-3 -i ../../../../TrainingSet/FullSet/large_intestine.csv -o ./large_intestine_004_tmp.arff
java -classpath weka.jar weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -V 0.001 -S 1 -c 1 -x 10 -K 0 -M 15 -depth 15 -t ./large_intestine_004_tmp.arff > ./large_intestine_004.txt
rm ./large_intestine_004_tmp.arff
