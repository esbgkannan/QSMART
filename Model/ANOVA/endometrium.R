mydata = read.table('../../TrainingSet/FullSet/AvgRank/endometrium.csv',head=T,sep=",")
model = lm(IC50 ~ factor(Cancer) + factor(Drug), data=mydata)
sse <- c(crossprod(model$residuals))
sink('./endometrium.txt',append=TRUE)
print(summary(model))
print(sse)
sink()
