java -classpath weka.jar weka.filters.unsupervised.attribute.Remove -R 2-3 -i ../../../../TrainingSet/FullSet/central_nervous_system.csv -o ./central_nervous_system_037_tmp.arff
java -classpath weka.jar weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -V 0.001 -S 1 -c 1 -x 10 -K 5 -M 1 -depth 0 -t ./central_nervous_system_037_tmp.arff > ./central_nervous_system_037.txt
rm ./central_nervous_system_037_tmp.arff
