# Case study how to answer?

## 1 Measure success
1. Clarifying questions: (What it does? How is it used? Who is it for?)
    - I assume the goal is..., right?
    - How excatly is the metric defined?
    - Scope: time, geo, segments
    - What baseline are we comparing to? Last week? Last year?

Users that use the product (small business owner vs user, creator vs follower, user and advertiser). From 1point 3acres bbs
Use cases of the product (private event vs public, small group vs large, view vs create)

https://www.1point3acres.com/bbs/thread-780970-1-1.html

2. First answer (by modular with mini pause)
    - High level framework： like giving a table of contents, break this into ... and start by defining metrics (does that sound good?)
    - Metrics
        - My primary metrics(success metrics, directly tied to the feature) would be ...(be specific to the user journey level)
        - Supporting metrics that explain or influence the primary metric are ...
        - Guardrail metrics that we do not want to hurt are ...

3. Validate
Design experimentation







## 2 Diagnose a change
1. Clarifying questions: (where and how much did the change happen)
    - How is the metric defined?
    - Time: sudden or progressively?
        - internal (data source, data collection, pipeline bug)
        - external (seasonality, industry trend, competitors, event, natural disaster)
    - Where and when did the change happend? Specific user segment/time/geo/senario?
    - Which stage in user funnel did it happen?
    - Other features/product change/launch? Similar change in related products?
(Optional: decompose the metrics, eg. DAU = existing + new + recurrected - churn)
2. Generate hypothesis (Demand/supply/matching/price)
3. Validate
    - quantify X's impact on Y by looking at Y across different X buckets, compare before vs after to see if the relationship shifts
4. Fix

## 3 Launch or not
1. Clarifying questions: 
    - What is the goal of launching this feature?
2. Metrics
    - My primary metrics(success metrics, directly tied to the feature) would be ...(be specific to the user journey level)
    - Supporting metrics that explain or influence the primary metric are ...
    - Guardrail metrics that we do not want to hurt are ...
3. Evaluate impact
    - primary prove by how much, both statistically and practically significant?
    - link result to business goal (feature lift translate to business impact, also consider cost)
4. Check tradeoffs
    - conflicting result (translate impact to user and business) ?
    - Short-term vs long-term




3. Going deeper
    - Controlled exploration by layer
    - Hypothesis driven
    - Tradeoff awareness
4. You need to have a default hypothesis template for Uber







# Uber product space
## Fare
- Rides: 
    - Demand: riders
    - Supply: drivers
- Eats: 
    - Demand: eaters
    - Supply 1: delivery drivers
    - - Supply 2: restaurants

##  Uber metrics collection
- ratio of buyers to sellers

## ?
- How would I know what funnel stages? For defining metrics
- North Star metric? Success metric has to be oppostie? how about guardrail?
	•	North Star (behavior change):
        → Request conversion rate = requests / price views
	•	Business metric (tradeoff):
        → Revenue per user
	•	Marketplace guardrails:
        → Match rate
        → ETA
        → Cancellation rate






## BPS questions
Case / Experimentation (Rider Referral)
	•	How would you design an experiment for a rider referral feature?
	•	Would you use A/B testing or something else?
	•	What are the interference issues in this setup?
	•	How would you handle interference?
	•	Would you use:
	    •	cluster randomization?
	    •	switchback?
	•	What are the challenges of switchback experiments?
	•	How would you choose the unit of randomization?
	•	What metrics would you use:
	    •	primary metrics
	    •	guardrail metrics
	•	How do you compare two campaigns?
	•	How do you evaluate tradeoffs (e.g., trips vs pricing)?
	•	What are potential unintended consequences of the feature?
	•	How would you measure referral effectiveness / conversion?
Product understanding
	•	Explain the “Wait & Save” feature
	•	What is the goal of this feature?

⸻

Core case questions
	•	What are the impacts of Wait & Save?
	•	What are the benefits / tradeoffs?
	•	How does it affect:
	•	riders
	•	drivers
	•	system / matching

⸻

Deeper probing
	•	Are there other angles beyond pricing and matching?
	•	How does this affect supply-demand imbalance?
	•	Does it fully solve supply issues?
	•	How does it affect driver behavior?
	•	How does it affect matching efficiency / region coverage?

⸻

Metrics
	•	What is the North Star metric?
	•	What are the tracking metrics?
	•	What are the guardrail metrics?
	•	How do you measure:
	•	rider behavior
	•	driver behavior
	•	system health
	•	financial impact

⸻

Experimentation / data questions
	•	How would you evaluate this feature?
	•	Would you run an A/B test?
	•	How would you randomize (unit of randomization)?

⸻

Debugging scenario
	•	If overall cancellation = 10% but Wait & Save is higher, what do you do?
	•	How would you:
	•	segment users?
	•	analyze funnel behavior?
	•	understand when users cancel?
	•	How do you decide if this is actually a problem?
