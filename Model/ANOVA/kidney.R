mydata = read.table('../../TrainingSet/FullSet/AvgRank/kidney.csv',head=T,sep=",")
model = lm(IC50 ~ factor(Cancer) + factor(Drug), data=mydata)
sse <- c(crossprod(model$residuals))
sink('./kidney.txt',append=TRUE)
print(summary(model))
print(sse)
sink()
