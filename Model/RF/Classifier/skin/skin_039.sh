java -classpath weka.jar weka.filters.unsupervised.attribute.Remove -R 2-3 -i ../../../../TrainingSet/FullSet/skin.csv -o ./skin_039_tmp.arff
java -classpath weka.jar weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -V 0.001 -S 1 -c 1 -x 10 -K 5 -M 10 -depth 10 -t ./skin_039_tmp.arff > ./skin_039.txt
rm ./skin_039_tmp.arff
