# IsTeslaAnAutomobileCompany-
Using machine learning predictions to look at trends between well established automobile and tech companies alongside Tesla. Hoping to use model accuracies to determine which division Tesla finds the most accuracy under and thus where it can be categorized.

## Findings
When training the two sets, I used Tesla as my independent variable used to test against. 

In the automobile training, I pulled one year of closing prices (250 days considering weekends and hollidays the market is closed) from 5 prominent automobile companies. These companies were Ford, Fiat Chrystler, General Motors, Honda, and Toyota. I then trained a model which would make a prediction based on the rise or fall of a stock price based on how these companies acted within a day. 
Once these predictions were made using a logistic regression method, I compared them to the testing section of the Tesla stock and found an accuracy of 54%. 

When training the tech companies model, I again pulled one year of closing price data, this time from 5 prominent tech companies. These companies being Apple, Google, Netflix, Amazon and Facebook. I trained this model in the same fassion using a logistic regression algorithm.
When looking at this portfolios relation to Tesla, I found the accuracy to be 70%.

In this training it can be seen that based on the data of the past year, a model can be found with higher accuracy when comparing Tesla to tech companies than to automobile companies. 
Thus my response to this quesiton of should Tesla be considered a tech or car company is that, even though Tesla is technically making cars, it should be considered a tech company. 





### AutoCompanyDataSources
* Tesla: https://finance.yahoo.com/quote/TSLA/history?p=TSLA  
* Ford: https://finance.yahoo.com/quote/F/history?period1=1517115600&period2=1548651600&interval=1d&filter=history&frequency=1d  
* Fiat Chrystler: https://finance.yahoo.com/quote/FCAU/history?period1=1517115600&period2=1548651600&interval=1d&filter=history&frequency=1d  
* General Motors: https://finance.yahoo.com/quote/GM/history?p=GM&.tsrc=fin-srch
* Honda: https://finance.yahoo.com/quote/HMC/history?period1=1517115600&period2=1548651600&interval=1d&filter=history&frequency=1d  
* Toyota: https://finance.yahoo.com/quote/TM/history?period1=1517115600&period2=1548651600&interval=1d&filter=history&frequency=1d  

### TechCompanyDataSources
* Tesla: https://finance.yahoo.com/quote/TSLA/history?p=TSLA    
* Facebook: https://finance.yahoo.com/quote/FB/history?period1=1517248885&period2=1548784885&interval=1d&filter=history&frequency=1d  
* Google: https://finance.yahoo.com/quote/GOOG/history?p=GOOG&.tsrc=fin-srch  
* Amazon: https://finance.yahoo.com/quote/AMZN/history?period1=1517248885&period2=1548784885&interval=1d&filter=history&frequency=1d  
* Netflix: https://finance.yahoo.com/quote/NFLX/history?p=NFLX&.tsrc=fin-srch  
* Apple: https://finance.yahoo.com/quote/AAPL/history?p=AAPL&.tsrc=fin-srch  
