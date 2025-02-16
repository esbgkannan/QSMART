library(glmnet)
mydata = read.table("../../../../TrainingSet/FullSet/Classifier/soft_tissue.csv",head=T,sep=",")
x = as.matrix(mydata[,4:ncol(mydata)])
y = as.matrix(mydata[,1])
set.seed(123)
glm = cv.glmnet(x,y,nfolds=10,type.measure="mae",alpha=0.01,family="gaussian",standardize=TRUE)
sink('./soft_tissue_007.txt',append=TRUE)
print(glm$glmnet.fit)
sink()
