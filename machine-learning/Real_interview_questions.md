# Rillet

## Round 1 - ML/AI Breadth

1. What are the fine tuning techniques
2. What is instruction tuning
3. What is the difference between smaller and bigger sematic chuncks, benefits?
4. Explain how to train a Transformer
5. How to make sure the model give deterministic answers? Consistency?
6. Difference between a base model and fine-tuned model
7. How does an agent work? Explain the gist.
8. How to evaluate a model before shipping(offline), and after shipping(online)
9. Temperature: Lower temperature gives more consistency
10. Compare benefits and downsides of chunking sentences bigger or smaller

**What I can improve:**

- Self intro can be more impressive
- How to conclude an answer
- Follow up questions on the basic tech, especially real production related

**Their answers to my questions**

Fast, iterative environment, 40-50h/week. Every week meeting with CEO to define what to do this week. Everyone has a little feature to work on but also collaborate together on a big project (chatbot right now)

## Round 2 - ML System design

1. Walk through a project, he asked detail questions
   - what is your role, how did you collaborate with other parties
   - how did you use llm, since it does not do well at being fed a lot of data
   - what are the challenges you had tech wise and in general

2. ML design: A data matching and reconciliation problem: bank statement vs internal invoice.

   - how would you use XGboost
   - what features would you use
   - if we do not have labeled data, only historical data, how would you use the historical data
   - if you take top ranked result, applied threshold, what are the risks of this method
   - how do you do your candidate generation
   - how would you handle imbalanced data

**What I can improve:**

- can specify my role on a project early on, I led end to end
- be more organized when explaning the tech details
- always think of the pros and cons when proposing something

Chatgpt did pretty well in predicting what problem will be asked. That means everyone can do this and be prepared like me. So it's more important to tell your story well and to have fluent communication.

## Round 3 - ML coding
Rillet ML Coding Interview
Instructions
Context
In accounting, cash reconciliation is the process of comparing a company's internal cash balance (from general ledger, invoices, and expenses) with external records such as bank statements to ensure they match.

A transaction from a bank statement will contain the following fields:

amount
date
merchant
description and we use all of them for the matching.
In this exercise you will focus on the merchant field and you will implement a preprocessing step to ensure that the data is in good state for matching.

Part 1
You are given a dataset of bank transactions: "bank_transactions.csv"
A merchant might appear with different names in different transactions in the dataset. For example "AMAZON MKTPLACE PMTS", "AMZN MKTPLCE 12345", "Amazon.com" and "Amazon" might refer to the exact same merchant.
Your task is to normalize the merchant names so that every merchant within the dataset will appear with exactly one name. E.g. the merchant for transactions with "AMAZON MKTPLACE PMTS", "AMZN MKTPLCE 12345", "Amazon.com" and "Amazon" will become "Amazon" (or any of the other 3 names).
Part 2
You are also given the names of the merchants as defined within Rillet in the dataset "merchants_rillet.csv."
Produce a new dataset "bank_transactions_preprocessed.csv" where all merchant names from the original dataset are mapped to the respective one in Rillet.
Part 3
Evaluation: you are also given a dataset "labeled_data.csv" that contains the correct mapping between the merchant as it appears in a bank transaction and as it shows within Rillet. Use it to evaluate the quality of your pipeline.


Chatgpt feedback:
Your biggest improvement areas for next time:
	•	Lead with the simplest viable baseline
	•	Speak in a numbered plan
	•	Only introduce embeddings/modeling after showing why string rules are insufficient
	•	When stuck, narrate clearly: “I’m spending too long on this library detail; I’ll switch to a simpler implementation”
	•	Tie every modeling choice to business error cost

**What I can improve:**

1. Completely caught off guard since interview guide was about implementing a preditive model. But was given a natural language processing task from scratch.
2. A lot of technical issues. Guide did not say where and said I'm free to use my own platform so I assumed vscode. But interviewer asked me to do a google colab. Then he asked me to share my screen which required me to restart my chrome and left the meeting room. 




---

# Parafin

## Round 1 - Past experience

1. Why are you interested in Parafin
2. Walk me end to end of a project you did

**What I can improve:**

- Self intro prepare more early and tailored
- A end to end proud project

---

# Walmart

## Director round

**Questions she asked:**

1. What kind of role the role is in your mind?
2. **Case1:** if you are working on a project and a new policy comes in, you need to delivery in a shorter time, what is your thought process of dealing with these  
   She said need someone to do the tradeoff and cut the unnecessary features if needed
3. **Case2:** if someone have unrealistic expectations on AI projects, how would you explain it to them?

## Laura

1. What are you looking for in this role
2. Tell me about how you drive an end-to-end project cross functionally
3. Tell me about a time when you have to explain something techinal to non technical stakeholders
4. Tell me about a time you had a disagreement with the stakeholder, how did you solve it

---

# Waymo

## Coding round

**Problem:** A variant of Number of islands. But there are lakes in between the islands, you need to input a land coordinate (x,y) and return the number of island adjacent to the land.

**What I can improve:**

I did pretty well in writing the whole breath first search part. Maybe better to have a plan stated clearly before started coding(but I started coding because I cannot figure out a whole plan and didn't want to be stuck forever). He gave a few hints along the way and I took them(good). But I didn't have time to finish the last part consolidating input and output. I think I did well in explaining time and space complexity proactively. And in the end I asked him if there is anything else I can clarify further.

I did a good job researching the company and potential interview problems. But I think finding sample problems is not enough, I need to be proactive in thinking how a problem can be extended, and what followup questions interviewers will ask.



# Glean

## HM round

1. What is a project you did recently? What would you do differently if you start again

2. You know E(X), E(Y), how do you calculate E(X + Y)?

3. You know Var(X), Var(Y), how do you calculate Var(X + Y)?


# Roblox

1.Implement an abstract base class Model that represents a supervised predictive model with methods to train on data and predict on new inputs. 
2.Implement a concrete subclass LinearModel that uses a simple linear regression from any Python ML library you prefer. It should train a model and predict using the trained model.

Your implementation should behave sensibly when used incorrectly (e.g., predicting before training, wrong input shapes).

from ABS import abs,abstractmethod
import numpy as numpy
from sklearn import LinearRegression

class LinearRegression(ABC):
    @abstractmethod
    def __init__(self, X, y):
        pass
    
    @abstractmethod
    def train(self):
        pass
    
    @abstractmethod
    def predict(self):
        pass
        
    @abstractmethod:
    def evaluation(self):
        pass
        
        
class LinearRegressionImplement(LinearRegression):
    def __init__(self, X, y, X_test, y_test):
        X = np.array(X) #[[],[],[]]
        y = np.array(y)
        X_test = np.array(X_test) #[[],[],[]]
        y_test = np.array(y_test) 
        y_test = np.flatten(y_test) [[],[],[]] -> [,,,]
        
        
        if len(X[0]) != len(y):
            raise ValueError('X and y must have the same dimensions')
        
        if len(X) == 0 or len(y_test) == 0:
            raise ValueError('X and y must not be empty')
            
        if len(X_test[0]) != len(y_test):
            raise ValueError('X_test and y must have the same dimensions')
        
        if len(X_test) == 0 or len(y_test) == 0:
            raise ValueError('X_test and y must not be empty')
        self.X = X
        self.y = y
        self.X_test = X_test
        self.y_test = y_test
        
    def train(self):
        self.model = LinearRegression.fit(self.X, self.y)
        return self.model
    
    def predict(self):
        if hasattr(self, model) is null:
            raise ValueError('Need to train the model first')
        self.output = self.train().predict(self.X_test)
        return self.output
        
    def evaluation(self):
        if hasattr(self, model) is null:
            raise ValueError('Need to train the model first')
        predicted = predict()
        return np.sum(abs(predicted - y_test)) # mae
    
    
    
 SQL   
    You have two tables that are available: in_app_purchases and match_history. These are massive production tables.  Write SQL queries for the following info:

1.Produce a list of player_id for all players who have spent more than $500 in total.
2.Produce a list of player_id for all players who meet the spending criteria from Part 1 and have also completed more than 200 matches in the "Ranked" game mode within the last 30 days.
3.If you had to produce this list on a daily basis, how would you design the data pipeline for optimal performance and stability?  
# Table: in_app_purchases

| player_id | purchase_timestamp  | usd_amount |

| p101      | 2025-09-01 10:30:15 | 4.99       |

| p102      | 2025-09-01 11:15:45 | 99.99      |

| p101      | 2025-09-03 14:20:00 | 19.99      |

# Table: match_history

| player_id | match_end_timestamp | game_mode |

| p101      | 2025-10-15 18:20:00 | Ranked    |

| p101      | 2025-10-15 18:45:00 | Ranked    |

| p102      | 2025-10-15 19:00:00 | Casual    |


1.
select
    player_id,
    sum(usd_amount) as total_spend
from in_app_purchases
group by player_id
having sum(usd_amount)>500

2. 
with base as 
(
    select
        player_id
    from match_history
    where game_mode = 'Ranked' and date(match_end_timestamp) >= date.today() - 29
    group by player_id
    having count(*)>200
)

select 
    b.player_id
from base b
join (select
    player_id,
    sum(usd_amount) as total_spend
from in_app_purchases
group by player_id
having sum(usd_amount)>500) spend s
on b.player_id = s.player_id




 We ran an ab test to see whether a new recommendation algorithm will increase user play time. In addition to the play time observed during the experiment, we also have pre-experiment user covariates (say past playtime, and device type). 
 Instead of just comparing the average playtime between treatment and control groups, can you use a linear regression adjustment to get the average treatment effect of the new algo on the study population?
 
 
 effect = beta0 + treatment * beta1 + covariates * beta2 ...
 
 treatment -> covariates -> effect


 ## Transcript evaluation

 Weaknesses
	•	Python fluency not strong enough
	•	Lack of crispness in statistical explanations
	•	Not proactively adding depth when prompted

**What I can improve:**
1. SQL forget the syntax for getting today: CURRENT_DATE()
2. Need deeper understanding of statistics, like deriving a p value from a regression model
3. Not very familiar with model training python
4. Answers sometimes scattered



# Tonal

## HM
1. Walk me through a project. 
2. We are releasing a feature to everyone, how do we measure the if the feature impacts engagement?
3. The product team wants us to pick a metric for engagment, like duration of workouts, number of workouts, active user number, how would you pick?