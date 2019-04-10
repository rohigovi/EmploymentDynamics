library(caTools)
library(randomForest)
library(dplyr)
library(caret)
file = read.csv("C:/Ran/Berkeley/IEOR/290/Project/Data/TrainingDatasetV2.csv")


file$Birth.Year <- as.numeric(file$Birth.Year)
file$Skillset1 <- as.factor(file$Skillset1)
file$Skillset2 <- as.factor(file$Skillset2)
file$laid_off <- as.factor(file$laid_off)
spl = sample.split(file$laid_off, SplitRatio = 0.7)

train = file %>% filter(spl == TRUE)
test = file %>% filter(spl == FALSE)

set.seed(101)
rf <- randomForest(laid_off ~ .-ID -City.of.profile -Country.of.profile -Elite.Institution -Start.Date 
                  -StartFlag -End.Date -EndFlag -CurrentEmployFlag -Role -Dept -Company -Company_Norm -Ticker
                  -Exchange -Location -Industry -Layoff.Date -Company.Name -Skillset1.Weight - Skillset2.Weight,
                  data = train, importance = TRUE)



pred = predict(rf, newdata = test)
table(test$laid_off, pred)

acc = (29353+252)/nrow(test)

importance(rf)# Measured by avaraged decrease in impurity(Gini) over all trees
#importance(rf, type=1) #Measured by decrease in accuracy

varImpPlot(rf,type=2)
