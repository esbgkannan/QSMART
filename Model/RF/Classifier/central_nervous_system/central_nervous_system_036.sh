java -classpath weka.jar weka.filters.unsupervised.attribute.Remove -R 2-3 -i ../../../../TrainingSet/FullSet/central_nervous_system.csv -o ./central_nervous_system_036_tmp.arff
java -classpath weka.jar weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -V 0.001 -S 1 -c 1 -x 10 -K 5 -M 15 -depth 15 -t ./central_nervous_system_036_tmp.arff > ./central_nervous_system_036.txt
rm ./central_nervous_system_036_tmp.arff
