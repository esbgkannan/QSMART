library(glmnet)
mydata = read.table("../../../../TrainingSet/FullSet/Correlation/ovary.csv",head=T,sep=",")
x = as.matrix(mydata[,4:ncol(mydata)])
y = as.matrix(mydata[,1])
set.seed(123)
glm = cv.glmnet(x,y,nfolds=10,type.measure="mse",alpha=0.6,family="gaussian",standardize=TRUE)
sink('./ovary_065.txt',append=TRUE)
print(glm$glmnet.fit)
sink()
