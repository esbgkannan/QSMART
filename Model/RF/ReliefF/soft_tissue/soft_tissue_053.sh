java -classpath weka.jar weka.filters.unsupervised.attribute.Remove -R 2-3 -i ../../../../TrainingSet/FullSet/soft_tissue.csv -o ./soft_tissue_053_tmp.arff
java -classpath weka.jar weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -V 0.001 -S 1 -c 1 -x 10 -K 10 -M 1 -depth 0 -t ./soft_tissue_053_tmp.arff > ./soft_tissue_053.txt
rm ./soft_tissue_053_tmp.arff
