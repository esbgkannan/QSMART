library(glmnet)
mydata = read.table("../../../../TrainingSet/FullSet/Correlation/endometrium.csv",head=T,sep=",")
x = as.matrix(mydata[,4:ncol(mydata)])
y = as.matrix(mydata[,1])
set.seed(123)
glm = cv.glmnet(x,y,nfolds=10,type.measure="mae",alpha=0.7,family="gaussian",standardize=FALSE)
sink('./endometrium_076.txt',append=TRUE)
print(glm$glmnet.fit)
sink()
