library(glmnet)
mydata = read.table("../../../../TrainingSet/FullSet/Lasso/lung_other.csv",head=T,sep=",")
x = as.matrix(mydata[,4:ncol(mydata)])
y = as.matrix(mydata[,1])
set.seed(123)
glm = cv.glmnet(x,y,nfolds=10,type.measure="mae",alpha=0.3,family="gaussian",standardize=FALSE)
sink('./lung_other_044.txt',append=TRUE)
print(glm$glmnet.fit)
sink()
