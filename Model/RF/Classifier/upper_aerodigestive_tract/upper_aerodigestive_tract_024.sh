java -classpath weka.jar weka.filters.unsupervised.attribute.Remove -R 2-3 -i ../../../../TrainingSet/FullSet/upper_aerodigestive_tract.csv -o ./upper_aerodigestive_tract_024_tmp.arff
java -classpath weka.jar weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -V 0.001 -S 1 -c 1 -x 10 -K 5 -M 15 -depth 15 -t ./upper_aerodigestive_tract_024_tmp.arff > ./upper_aerodigestive_tract_024.txt
rm ./upper_aerodigestive_tract_024_tmp.arff
