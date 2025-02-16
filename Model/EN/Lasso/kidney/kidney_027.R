library(glmnet)
mydata = read.table("../../../../TrainingSet/FullSet/Lasso/kidney.csv",head=T,sep=",")
x = as.matrix(mydata[,4:ncol(mydata)])
y = as.matrix(mydata[,1])
set.seed(123)
glm = cv.glmnet(x,y,nfolds=10,type.measure="mae",alpha=0.1,family="gaussian",standardize=TRUE)
sink('./kidney_027.txt',append=TRUE)
print(glm$glmnet.fit)
sink()
