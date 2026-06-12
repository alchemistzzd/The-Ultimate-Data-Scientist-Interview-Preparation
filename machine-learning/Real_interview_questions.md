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


## HM
Questions asked:
1. Tradeoffs you made with the Flux Analysis project
2. Strength and weaknesses
3. Global model how does neural prophet work if different accounts join differently in timing
4. Pipelines of flux model from data ingestion
5. How would you use the macroeconomics features
6. How do you know if it's the current value or lagged value of a metrics is contributing to the forecast target

## Coding
We want to build a production model that predicts on every snapshot_date=ds, and 

for every monthly active user (MAU = active at least once in window [ds - 28d, ds]), 

their total future 12-month revenue from the snapshot_date forward. 


(a) How do you define the label?

(b) How do you build a sample for your training data? 
user a, 2025-01-01-2025-01-31, 2025-02-01-2025-12-31




snapshot date = '2026-01-15'
MAU = active at least once in the window ['2026-01-15' - 28d, '2026-01-15']


+++++++++++++++++++++++++++++

Problem set up: We have the following two source tables. 

Task: Generate the following features for 365 snapshot dates between 2023-01-01 and 2023-12-31, across 50M MAUs, for each MAU–snapshot_date pair. 
Keep Scale Optimization in Mind. 
- revenue_last_28d: Revenue in [ds-28, ds-1]
- days_since_last_purchase_28d: Days from last purchase within 28d before ds

ds = snapshot_date
MAU = every monthly active user (MAU = active at least once in window [ds - 28d, ds])

-- Source table 1: Fact table: User activity events (50 BILLION rows) partitioned by event_date
CREATE TABLE fct_user_events (
    user_id BIGINT,
    event_date DATE,  
    event_type VARCHAR(50),  --- 'chat', 'purchase', 'play', etc.
    revenue DECIMAL(10,2),--- NULL for non-purchase events
    session_id VARCHAR(100), 
...
);


-- Source table 2: Partitioned by signupevent_date, ~100M events/day
CREATE TABLE dim_users (
    user_id BIGINT,
    signup_date DATE,
);
with snapshot_period as
(
    select
    event_date,
    event_date - interval '28 days' as start_date
    user_id,
    sum(case when event_type = 'purchase' then revenue else 0 end) as  daily_revenue,
    max(event_date) over(partition by user_id) as last_purchase_date
    from fct_user_events
    where event_date between date(2023-01-01) - interval '28 days' and date(2023-12-31)
    group by event_date, user_id
),
feature_t


user a, 2023-01-01, revnu in last 28d, days_since_last_purchase_28d
user a, 2023-01-02, revnu in last 28d, days_since_last_purchase_28d



+++++++++++Python 
Question: Design a production pipeline of this revenue model. 
Describe:
- A very brief architectural design of the modules
- Data schema and the types of data input validations you would do
- Error handling ?




"""
TODO: This pipeline has several issues. Fix them and add best practices:
a..Add data contracts for features and predictions
b. Validate input. Validate output before writing to production
c. Add proper error handling
d. Add logging
Bonus:
atomic write to staging table
"""

import pandas as pd
import joblib
from datetime import datetime

# ============================================================================
# ISSUE 1: No data contracts defined
# ============================================================================

# TODO: Define these classes: FeatureContract and PredictionContract
# specifying rules around the expected data inputs.


# ============================================================================
# ISSUE 2: No validation function
# ============================================================================

# TODO: Implement validate_data(df, contract) function
# What checks should it perform?


# ============================================================================
# PIPELINE MODULES
# ============================================================================

class FeaturePipeline:
    """Load features"""
    
    def __init__(self, snapshot_date: str):
        self.snapshot_date = snapshot_date
    
    def run(self):
        # ISSUE 3: No error handling
        try:
            df = pd.read_parquet(f"s3://features/{self.snapshot_date}.parquet")
        Except:
            return 'path does not exist'
        
        # ISSUE 4: No validation - what if features are corrupted?
        if df.dropna().shape[0] <df.shape[0]:
            df.fillna()
        try:
            for col in df.columns:
                if df[col].isna():
                    df = df.drop(col)
                    break
        Except:
            return 'feature {} is missing'.format(col)
        
        return df


class ModelPipeline:
    """Load model and generate predictions"""
    
    def __init__(self, model_version: str = "latest"):
        self.model_version = model_version
        self.model = None
    
    def load_model(self):
        # ISSUE 5: No error handling
        model_path = f"s3://models/revenue_predictor/{self.model_version}/model.pkl"
        try: 
            self.model = joblib.load(model_path)
        except:
            print('model path invalid or job failed during loading')
        return True
    
    def predict(self, features_df):
        # ISSUE 6: What if features have nulls? Model will crash
        X = features_df[['revenue_last_28d', 'revenue_last_90d', 
                         'active_days_last_28d', 'days_since_signup']]
        
        
        predictions = self.model.predict(X)
        
        output_df = pd.DataFrame({
            'user_id': features_df['user_id'],
            'snapshot_date': features_df['snapshot_date'],
            'predicted_revenue_12mo': predictions
        })
        
        return output_df


class OutputPipeline:
    """Write predictions"""
    
    def run(self, predictions_df, snapshot_date: str):
        # ISSUE 7: Direct overwrite - what if predictions are bad?
        output_path = f"s3://predictions/revenue_12mo/snapshot_date={snapshot_date}"
        if predictions_df.isna():
            return 'prediction is null'
            
        predictions_df.to_parquet(output_path, mode='overwrite')
        
        print("Predictions written")
        return True


# ============================================================================
# MAIN ORCHESTRATOR
# ============================================================================

class RevenuePredictionPipeline:
    """Main pipeline orchestrator"""
    
    def __init__(self, snapshot_date: str):
        self.snapshot_date = snapshot_date
    
    def run(self) -> bool:
        # ISSUE 9: No error handling - one failure breaks everything
        # ISSUE 10: No logging - can't debug failures
        try:
            # Load features
            print('building feature Pipeline')
            feature_pipeline = FeaturePipeline(self.snapshot_date)
            features_df = feature_pipeline.run()
            
            # Load model
            print('loading models')
            model_pipeline = ModelPipeline(model_version='latest')
            model_pipeline.load_model()
            
            # Generate predictions
            print('making predictions')
            predictions_df = model_pipeline.predict(features_df)
            
            # Write output
            print('writing output')
            output_pipeline = OutputPipeline()
            output_pipeline.run(predictions_df, self.snapshot_date)
        except error as e:
            print('error message', e)
        
        return True


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    import sys
    snapshot_date = sys.argv[1]
    
    pipeline = RevenuePredictionPipeline(snapshot_date)
    pipeline.run()

Answer: adding data contracts 

from dataclasses import dataclass

@dataclass
class FeatureContract:
    """Expected schema and constraints for features"""
    required_columns = [
        'user_id', 'snapshot_date', 'revenue_last_28d', 
        'days_since_last_purchase_28d'
    ]
    
    non_nullable = ['user_id', 'snapshot_date', 'revenue_last_28d', 
                   ]
    
    value_ranges = {
        'revenue_last_28d': (0, 1_000_000),
           }
    
    expected_row_count = (5_000_000, 20_000_000)

@dataclass
class PredictionContract:
    """Expected schema and constraints for predictions"""
    required_columns = ['user_id', 'snapshot_date', 'predicted_revenue_12mo']
    
    non_nullable = ['user_id', 'snapshot_date', 'predicted_revenue_12mo']
    
    value_ranges = {
        'predicted_revenue_12mo': (0, 100_000)  # No negatives
    }



## case study

1. Prophet parameter for trend and growth
2. To predict each user's probability of purchasing in next 7 days, preverence of purchase is 2% in overall population
3. Time series on global DAU for next 90 days, steady upward trend
4. 40% dau surge on an event date, how do you know if it is due to event or model failing



**What I can improve:** 
1. align fast instead of jumping to solution fast
2. answer in the same depth level, only go deeper when probed, be crisp
3. I should not focus on showing off how much do I know
4. I was trying hard to match back to anything I've prepared. But this harmed me but confusing myself with the question.
5. Practice on mostly AI based content with repetitive mock that limited my thinking and turned my focus to memorizing.
6. Interviews reward: polished execution, not just real ability
7. Be decisive in picking a path and dive deep in

What I did well:
I listed a lot of tradeoffs! Did thorough product search and gave a few very Roblox specific product insights.

**feedbacks**
1. pros: good coding, interesting project, took feedbacks well
2. cons: python handling exception part, forecasting model part, some communications might go into the weeds
    - went too deep into details too early or unnecessarily
    - need to focus more on business big picture first
    - You used more words than needed to make your point
    - Hard to extract the key idea



# Uber
## BPS2
Questions asked:
1. Walk me through a project
2. New feature wait and save,
    1) why are we launching it?
        1. Why does it help with matching?
        2. Why does it help with driver supply?
        3. incremental 

    2) we did experiment but no difference in number of completed trips, what could be the reason?
        1. low adoption/exposure due to: rider choice, feature not compelling
        2. positive and negative offset
        3. only mix of ride types changed, but did not increase new trips
        4. supply side bottleneck still dorminates
        5. matching gain was too small
        6. metrics issue

**What I can improve:**
1. Had structure but did not have a brief reason/mechanism for each point
2. Need an anchor for each answer - decisive


A feature is launched, metric A dropped - framework
1. Validate the metric and data
First, I confirm whether the drop is real—checking metric definitions, logging changes, and pipeline issues to rule out measurement errors.

2. Localize the issue
I break the metric down by key segments—such as user cohorts, geography, device type, or new vs. existing users—to identify where the drop is concentrated.

3. Diagnose the root cause
Then I analyze the user journey or funnel to pinpoint where behavior changed, and investigate whether the feature introduced friction, confusion, or unintended side effects.

4. Assess broader impact
Finally, I look at related metrics—like engagement, revenue, and system performance—to understand trade-offs and whether the issue is isolated or systemic.

Based on this, I can form hypotheses and decide whether to roll back, iterate, or run further experiments.”


## BPS1

def reverse(input):
    
    res = []
    n = len(input)
    if n == 0:
        return []
    for i in range(n-1, -1, -1): #O(n)
        res.append(input[i])
    return res

def reverse2(input):
    n = len(input)
    if n == 0:
        return []

    for i in range(round(n/2)):
        temp = input[n-i-1]
        input[n-i-1] = input[i]
        input[i] = temp
        
    return input
    




print(reverse2([1,-2,3,5,0]))


program rider referral

rider referral: existing user refer new user, both get bonus for signup also first 5 trips

goal: more new users

compaign 10% discount

10/user, 7/user
10-7




# Tonal

## HM
1. Walk me through a project. 
2. We are releasing a feature to everyone, how do we measure the if the feature impacts engagement?
3. The product team wants us to pick a metric for engagment, like duration of workouts, number of workouts, active user number, how would you pick?
4. How did you support a KPI project? Why do you train your model monthly?
5. When it comes to data viz, what are you principles when presenting to non technical audiances?

## Tech 1
1. PCA does it need normalization
2. he give me a plot with x axis monthly runing volumne, y axis marathon time, and said they fitted a piece wise two linear regression up to median of x, and conclude that people should only run up to that median point, not running any more than that. How do I feel about their way of forming that recommendataion

## Tech 2
import numpy as np
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

df = pd.read_csv('/home/coderpad/data/tonal_chatbot_experiment_small.csv')

print(df.head())

# 2,000 users
# 21 days
# 50% assigned to treatment (chatbot access)
# 50% assigned to control (no access)
# Not all treatment users actually used the chatbot (imperfect compliance)
# Each row is a user-day



# Does chatbot access increase the likelihood that a user works out on a given day?
def p_value_daily(date):
    df_date = df[df['date'] == date]
    treatment_mean = np.mean(df_date[df_date['treatment_group'] == 1]['did_workout'])
    control_mean = np.mean(df_date[df_date['treatment_group'] == 0]['did_workout'])

    treatment_ste = np.sqrt(np.var(df_date[df_date['treatment_group'] == 1]['did_workout']))
    control_ste = np.sqrt(np.var(df_date[df_date['treatment_group'] == 0]['did_workout']))

    z = (treatment_mean - control_mean)/np.sqrt(treatment_ste/1000+control_ste/1000)
    # p_value = np.getpvalue(z)
    return z

p_values = [p_value_daily(day) for day in df['date'].unique()]
print(p_values)

# Now imagine we discover a bug:
# Premium members were more likely to be assigned to treatment.
# Assignment is no longer random.
# How would this bug change your previous answer?
initial treatment, initial control
output: prob
new treatment, new control
d1 diff = mean(did_workout) for treatment - mean(did_workout) for control
d2 diff

I lost you on Zoom :/

**Solutions**
1. Propensity score matching - step by step
- First, propensity score cannot be used if there was no treatment happened before. Since it needs to learn from real exposure.


# TCP
Profound - 150ppl
30-40 eng; 3-4 ds, machine learning


# Servicenow
## HR

1. How much of your time is systems ownership vs modeling / reasoning / evaluation?
2. In practice, does no handoff mean owning internal tools and pipelines, or also owning service reliability and on-call?
3. What differentiates a strong performer in this role — is it more about system reliability or insights/model quality?
4. What are the most common ways projects in this space fail — is it around data quality, adoption, or system reliability?

# Windfall
## HM
- customer facing, user adoption, directly drives decisions
1. For a typical propensity or lead scoring model here, what parts of the lifecycle would I own end-to-end?
    data issue, feature less for commercial, down market, need feature space,
    identify features, feature engineering, 
2. What is the biggest challenge? improving model performance or scaling the systems behind them?

The team needs:
1) better feature engineering for the scoring models
2) customer enabaled modeling automation


# Superhuman

## ML

logisitic regression:
how to you explain it?
what is the bias term?
what is the bias term used for?
how do you pass the linear combination of features to sigmoid?
decision boundaries for logistic regression?
Why would you use L2 over L1 regularization?
Do you need to normazlie for logistic regression, if not what is the conceuqeunces?
   - Different feature scales distort the optimization landscape, making gradient descent inefficient.
   - Without normalization, regularization penalizes features unevenly, which can distort feature importance.

Class imbalance:
what is the risk?
if we use precision, recall and f1 does class imbalance not matter?


Word Segmentation
Description
Word Segmentation
Given a string without whitespaces, and avocabulary, write a function that splits thestring into words.
For example, given the string
helloworld!
and the vocabulary
['he'，'hell'，'hello'，'low',
world'，'!']，
your function should return the list
['hello'，'world'，'!'].
Edge cases
 If there are multiple ways to split a
string, your function should return thelist with the least number of words.
 The string is not guaranteed to besplittable. In cases it is not, your functionshould return an empty list.
 If the string is empty, your function
should return an empty list.


**What I can improve:**
1. OMG it is the same LC problem I see people posting online, but I did not see all the questions...

Feedbacks:
1. Medium on both ML and coding
2. Logistic - input feature norm does not matter, and it can model non linear using log; incorrect statement
3. Coding - not multiple ways to break work, storing not initiated, implementation




# Apple

## Coding screen

How do you evaluate A vs B:
	Image_id	ground_truth	prediction_A	confidence_score_A	prediction_B	confidence_score_B	lighting	distance
1	1	1	1	0.472	0	0.012	Extremely_low	1
2	2	1	1	0.412	0	0.018	Extremely_low	1
3	3	1	1	0.638	0	0.012	Extremely_low	1
4	4	1	1	0.499	0	0.018	Extremely_low	1
5	5	1	1	0.485	1	0.591	Extremely_low	1
6	6	1	1	0.564	0	0.145	Extremely_low	5
7	7	1	1	0.495	0	0.183	Extremely_low	5
8	8	1	1	0.312	1	0.508	Extremely_low	5
9	9	1	1	0.489	0	0.203	Extremely_low	5
10	10	1	1	0.434	1	0.501	Extremely_low	5
11	11	1	1	0.523	0	0.182	Extremely_low	10
12	12	1	1	0.221	0	0.084	Extremely_low	10
13	13	1	0	0.435	0	0.284	Extremely_low	10
14	14	1	0	0.698	1	0.522	Extremely_low	10
15	15	1	1	0.7	1	0.564	Extremely_low	10
16	16	1	0	0.793	1	0.589	Extremely_low	20
17	17	1	0	0.682	1	0.501	Extremely_low	20
18	18	1	1	0.632	1	0.592	Extremely_low	20
19	19	1	0	0.446	1	0.523	Extremely_low	20
20	20	1	0	0.511	1	0.632	Extremely_low	20


## HM
Questions:
1. Tell me about yourself
2. Where is your interest?
3. Why did you leave?
4. Are you more tradition ML or LLM? 
5. What is your career expectation? 
6. How comfortable you are with Python?
Her team:
Infrastructure eng + ds 
LLM-as-a-judge + agentic system eval + simulator + evaluator + golden dataset
Run evaluation on their pipeline, labeling, define core values and inform labelers.
Iterations, scaling 
Scenario based simulations
Ater critical steps stops human labeling

**improvements**
1. Structure every answer
2. Be more decisive
3. Make your project concrete

# Drata

## HM
Questions asked:
1. What are your biggest strength and weaknesses?
2. How did you create the golden dataset?
3. If there is no human review, how would you evaluate the flux model?
4. What feedback did you get changed the way you work?
5. What feedbacks you get you disagreed with?
6. How did you design the MVP?
7. Why are you looking to leave Autodesk?

## Architecture design
Imagine McDonald’s does not have any sort of Kiosk ordering system and wanted to implement brand new, AI-First, self-service order kiosks in all their locations. The goal is to enhance customer experience and increase operational efficiency. The new system should allow customers to place orders through these kiosks, it must integrate seamlessly with the current operations of the restaurant, and it must utilize AI in ways that make sense to accomplish the previously stated goals.

To simplify the problem a bit, you can assume the restaurant already has some way to accept payments, send orders to the kitchen, etc, and that all of these systems have very nice REST APIs for you to interact with.

Your task is to both come up with at least 3 ways AI could improve the basic ordering Kiosk, and then design an end-to-end architecture for this new AI enhanced Kiosk system. Keep in mind that your design should be scalable, reliable, and secure, and it should efficiently manage data across various systems and components.

We're looking for a high-level design, and we want to understand your thought process, decision-making, and the trade-offs you might make in designing such a system. Feel free to make any other assumptions as necessary, but be sure to state them.

Take a few moments to think about the problem, and please ask us questions before you start designing the system, we're here to help.

**improvement**
rushing into rag based llm without exploring ml yet. trying to pull solution towards what I prepared for.
i need to do a few ml system design practice with both classification and prediction



**improvement**
You tended to:
	•	ramble
	•	repeat ideas
	•	lose crispness

Example:
	•	Watchdog explanation
	•	Flux explanation

👉 You had strong content, but:

signal got diluted
---
You said:
	•	“chunking, retrieving, storage”
	•	“learned a lot”

But you did NOT clearly say:
	•	how you chose chunk size
	•	what embedding model
	•	how you improved retrieval
	•	trade-offs

👉 For this role:

this is a major gap

---
🔴 3. Evaluation answers were fuzzy

Your evaluation answer:
	•	“compare to analyst”
	•	“human review”
	•	“golden dataset”

👉 But missing:
	•	concrete metrics
	•	how accuracy measured
	•	failure cases

👉 Felt:

hand-wavy instead of rigorous

⸻

🔴 4. Not enough “decision clarity”

You described WHAT you did, but not always:
	•	why this approach vs alternatives
	•	what trade-offs you considered

⸻

🔴 5. Weak concise storytelling

Your MVP story was good, but:

👉 Took too long to land key point

Strong version should be:
	•	problem
	•	solution
	•	impact (numbers)


1. Problem
2. Approach
3. Trade-offs
4. Impact


# Apple

## R2
1. What data would you use for the Apple vision pro hand gesture feature?
2. If there is a very edge case, how would you know that that data point is out of distribution?
3. How would you decide the sample size is sufficient enough for evaluation? What is the equation you would use?
4. What did you make sure your model is doing well? How do you know your model is improving?


# Laurel AI
Laurel is an AI-powered timekeeping product for professional services firms (law + accounting). When a timekeeper uses Laurel, they can create time entries in multiple ways:

Using Laurel’s AI suggestions (called "work groups") to create entries
Using Laurel's captured Activities to create entries
Timers / Manual: fall back to more traditional time entry patterns
We call (1) and (2) Laurel's "Core Workflow" in that both methods involve the user using Laurel captured activities to create entries. However, ideally, Laurel's AI can automatically construct a "perfect" entry and the user accepts as-is.

The goal of this exercise is an example user retention / churn analysis.

You have access to the following tables

users: This is the core table unique at the user_id level. Data has already been pulled so that for each user you observe, which customer they're associated with, vertical, and Laurel Usage statistics (i.e. Creating and Releasing Entries). The fields are:
user_id – Unique identifier for a user
customer_id – Unique identifier for the firm/customer the user belongs to
vertical – Industry vertical the customer operates in (e.g., legal, accounting)
customer_segment – Business segmentation for the customer
customer_mandated_usage_flag – Indicates whether the firm required users to use the product
user_role – Role of the user (e.g., Timekeeper vs Admin)
first_activation_date – Date the user first activated their account
first_entry_created_date – Date the user first created a time entry
first_core_workflow_work_date – First date the user engaged with the product’s “core workflow”
total_entries_created_d3 – Count of all entries the user created within their first 3 days
total_core_workflow_entries_created_d3 – Count of core-workflow entries created in the first 3 days
total_entries_created_timers_d3 – Count of timer-based entries created in the first 3 days
total_entries_created_manual_d3 – Count of manually created entries in the first 3 days
total_entries_released_d3 – Total entries released (finalized) within the first 3 days
total_core_workflow_entries_released_d3 – Core workflow entries released within 3 days
total_entries_released_timers_d3 – Timer-based entries released within 3 days
total_entries_released_manual_d3 – Manually created entries released within 3 days
user_attempted_core_workflow_flag – Boolean flag indicating whether the user ever tried the core workflow
user_churned_core_workflow_flag – Boolean flag indicating whether the user churned from the core workflow
user_churned_flag – Boolean flag indicating whether the user churned from the product overall. In this case, churn is simplistically defined to be 1 if the user did not release any entries after their 31th day after activation, else 0.
metrics_automation_score: Indicates whether the user accepted a GenAI Narrative perfectly on their entry on that day
user_id – Unique identifier for a user
work_date – Date of Work
genai_narrative_accepted_flag – equal to 1 if the user accepted a perfect GenAI Narrative on that day. Note, this table only includes the "1s". If the user did not accept a perfect GenAI Narrative (even if the generated narrative was partially accepted), those days will not show up for that user in this table.

You can assume that this data was pulled on January 5th, 2026.



In the users table:

Count how many rows have first_activation_date is null.
Filter out rows where first_activation_date is null.
The customer with customer_id == '63f8bbd6e1e1ec7267b08ee1' not only mandates Laurel usage but also has special tailored trainings during onboarding.
Create a new column customer_mandated_usage_detail_flag with values:
"Not Mandated Usage" if there is no customer mandated usage
"Mandated Usage -- Special Trainings" if customer_id = '63f8bbd6e1e1ec7267b08ee1' and the customer is mandated
"Mandated Usage -- No Special Trainings" for all other mandated customers
Create a new column attempted_core_workflow_d3_flag which is:
1 if the user created at least 1 core workflow entry in the first 3 days
0 otherwise
What percentage of users who attempted core workflow in their first 3 days churned vs users who did not attempt the core workflow in their first 3 days?
Now, specifically for customer_id = '63f8bbd6e1e1ec7267b08ee1', we want to understand whether there is a correlation between the user accepting at least one GenAI Narrative and whether they have churned. Join with metrics_automation_score to determine whether each user for customer_id = '63f8bbd6e1e1ec7267b08ee1' accepted at least one GenAI narrative in the first 3 days after activation. What is the churn rate of users who accepted at least one GenAI Narrative in the first 3 days after activation compared to those who did not?


Moveworks:
1. case study
You're a Data Scientist at Spotify. As a reminder, the main feature of the app is to play music or podcasts, but users can also create/modify playlists and subscribe to playlists created by other users. There is a free version of the app where users have to listen to ads in between songs and cannot decide the order of songs, and a paid version without such limitations. The Head of Product wants to better understand how users are engaging with the platform and has asked you to define the key metrics. Over the course of this interview, we'll walk through how you'd go from defining those metrics all the way to building the data infrastructure to support them.

- How would you measure the success of Spotify's product? What key metrics would you define and track?
- Now pick 2-3 of these metrics and design the data tables you'd need to compute them. Please share your screen and sketch this out — table names, columns, primary keys, and foreign keys.
- Now that you've designed these tables, let's talk about where the data comes from. What events would need to be logged to populate these tables, and where in the system would you emit them?
- Let's zoom out. Can you sketch a high-level data flow — how do these events go from being emitted in the app to being queryable in the tables you designed?
