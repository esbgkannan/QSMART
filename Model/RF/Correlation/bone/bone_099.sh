java -classpath weka.jar weka.filters.unsupervised.attribute.Remove -R 2-3 -i ../../../../TrainingSet/FullSet/bone.csv -o ./bone_099_tmp.arff
java -classpath weka.jar weka.classifiers.trees.RandomForest -P 100 -I 100 -num-slots 1 -V 0.001 -S 1 -c 1 -x 10 -K 20 -M 10 -depth 10 -t ./bone_099_tmp.arff > ./bone_099.txt
rm ./bone_099_tmp.arff
