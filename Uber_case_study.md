# Case study how to answer?

1. Clarifying questions: (What it does? How is it used? Who is it for?)
    - I assume the goal is..., right?
    - How excatly is the metric defined?
    - Scope: time, geo, segments
    - What baseline are we comparing to? Last week? Last year?

Users that use the product (small business owner vs user, creator vs follower, user and advertiser). From 1point 3acres bbs
Use cases of the product (private event vs public, small group vs large, view vs create)

https://www.1point3acres.com/bbs/thread-780970-1-1.html

2. High level framework
    - like giving a table of contents, does that direction make sense?

3. Going deeper
    - Controlled exploration by layer
    - Hypothesis driven
    - Tradeoff awareness


4. You need to have a default hypothesis template for Uber

5. Fare
- Rides: 
    - Demand: riders
    - Supply: drivers
- Eats: 
    - Demand: eaters
    - Supply 1: delivery drivers
    - - Supply 2: restaurants

6. Uber metrics collection
- ratio of buyers to sellers

7.?
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






7. BPS questions
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
