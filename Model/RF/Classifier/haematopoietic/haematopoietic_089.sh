java -classpath weka.jar weka.filters.unsupervised.attribute.Remove -R 2-3 -i ../../../../TrainingSet/FullSet/haematopoietic.csv -o ./haematopoietic_089_tmp.arff
java -classpath weka.jar weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -V 0.001 -S 1 -c 1 -x 10 -K 20 -M 1 -depth 0 -t ./haematopoietic_089_tmp.arff > ./haematopoietic_089.txt
rm ./haematopoietic_089_tmp.arff
