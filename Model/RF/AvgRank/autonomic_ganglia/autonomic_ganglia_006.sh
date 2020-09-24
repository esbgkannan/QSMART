java -classpath weka.jar weka.filters.unsupervised.attribute.Remove -R 2-3 -i ../../../../TrainingSet/FullSet/autonomic_ganglia.csv -o ./autonomic_ganglia_006_tmp.arff
java -classpath weka.jar weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -V 0.001 -S 1 -c 1 -x 10 -K 0 -M 5 -depth 5 -t ./autonomic_ganglia_006_tmp.arff > ./autonomic_ganglia_006.txt
rm ./autonomic_ganglia_006_tmp.arff
