java -classpath weka.jar weka.filters.unsupervised.attribute.Remove -R 2-3 -i ../../../../TrainingSet/FullSet/ovary.csv -o ./ovary_027_tmp.arff
java -classpath weka.jar weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -V 0.001 -S 1 -c 1 -x 10 -K 5 -M 10 -depth 10 -t ./ovary_027_tmp.arff > ./ovary_027.txt
rm ./ovary_027_tmp.arff
