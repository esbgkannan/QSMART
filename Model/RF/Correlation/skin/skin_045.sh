java -classpath weka.jar weka.filters.unsupervised.attribute.Remove -R 2-3 -i ../../../../TrainingSet/FullSet/skin.csv -o ./skin_045_tmp.arff
java -classpath weka.jar weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -V 0.001 -S 1 -c 1 -x 10 -K 10 -M 1 -depth 0 -t ./skin_045_tmp.arff > ./skin_045.txt
rm ./skin_045_tmp.arff
