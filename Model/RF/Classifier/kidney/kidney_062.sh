java -classpath weka.jar weka.filters.unsupervised.attribute.Remove -R 2-3 -i ../../../../TrainingSet/FullSet/kidney.csv -o ./kidney_062_tmp.arff
java -classpath weka.jar weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -V 0.001 -S 1 -c 1 -x 10 -K 15 -M 5 -depth 5 -t ./kidney_062_tmp.arff > ./kidney_062.txt
rm ./kidney_062_tmp.arff
