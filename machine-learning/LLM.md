# LLM architecture and training (transformers, RLHF, instruction-tuning)

https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi

---

## Attention

- **Attention head:**
- **Query:** the questions that an word asks other words to achieve a goal. Visually it maps the embedding vectors to a smaller dimensional space
- **Key:** the answer to that query. It also maps the embedding vestors to the same smaller dimensional space as the query matrix. Key and query are matched when they are close to each other.
- Initial embedding for each word only tells you what word is it and what is its position. Using the initial embedding multiplies query matrix and key matrix separately and positioned in X and Y axis, we can compute the dot product of queries and keys. The big product indicates that the initial word corresponding to the key "attend to" the initial word corresponding the the query
- Compute Softmax over all vectors over word's Query axis (Y) to normalize and so it's between 0-1 like a probability
- You get a grid, called Attention Pattern
- **Masking:** set pre parameters to be negative infinity, so after softmax they are all zero and would not be leaking info
- **Value:** value multiples word vector to be the projected word
- **Muiltihead attention:** it gives the model the capacity to learn many distinct ways that context changes meaning

## Transformer

- Tokens
- Embedding a word: put a token in a geometric space
- RNN (Recurrent Neural Network)
- Positional encoding
- Attention

## Reinforcement Learning

Traditional RL is built on the Markov Decision Process (MDP). It's a loop with four key components: **Agent:** The "brain" (your model). **State (\(s\)):** The current situation or "snapshot" of the world. **Action (\(a\)):** What the agent chooses to do. **Reward (\(r\)):** The immediate feedback (positive or negative).

## Supervised fine-tuning

Supervised Fine-Tuning uses a dataset with pairs of human created prompts and human created responses. So it turns a pre-trained model to an expert in a certain domain. More powerful than RAG since the expertise is baked into the model itself, weights are updated.

But it is costly and time consuming + easily overfitting (since the datset is way smaller)

In other words, if was super cheap to have people create a huge dataset for Supervised Fine-Tuning, then we would probably do that instead.

- High computational costs due to updating billions of parameters
- Significant memory needs requiring advanced hardware.
- Time-intensive and demands expertise for large-scale models.
- lssues like catastrophic forgetting, storage, hyperparameter tuning

**Fine-tuning vs RAG**

1. RAG is faster if data/info updates fast, since it is always using the latest
2. RAG is great to provide sources
3. Fine-tuning is great to make the model industry specific and using past data in the org
4. Best senario to use them

## RLHF (Reinforcement learning from human feedback)

- LLM generates a better answer and a worse answer, human select the better one
- Loss Function: -log(Sigmoid(Reward_better - Reward_worse)) We want the diff to be big between the two rewards

## Instruction-tuning

- The goal is to obtain a model which is capable of following instructions
- Instruction tuning is a technique for fine-tuning large language models (LLMs) on a labeled dataset of instructional prompts and corresponding outputs.
- It provides pairs of (Instruction, Correct Response). By seeing thousands of these examples, the model learns the pattern of helpfulness. It realizes that when a prompt ends in a question mark or a command, the "statistically likely" next words should be the answer, not more questions. Isolate the "task" (e.g., "Summarize this") from the "data"

## Parameter-efficient Fine-tuning (PEFT)

---

# Prompt engineering (reducing hallucinations, structured outputs, maintaining stability)

- Prompt engineering (no training involved)

---

# Retrieval systems (RAG pipelines, embeddings, chunking)

https://www.youtube.com/watch?v=00Q0G84kq3M

## Chunking

https://medium.com/the-ai-forum/semantic-chunking-for-rag-f4733025d5f5

- Fixed size chunking
- Recursive Chunking
- Document Specific Chunking
- **Semantic Chunking**  
  Semantic chunking involves taking the embeddings of every sentence in the document, comparing the similarity of all sentences with each other, and then grouping sentences with the most similar embeddings together.

  - **Step 1: Sentence Splitting:** Break the document into individual sentences.
  - **Step 2: Vectorization:** Turn each sentence into an embedding (a vector) using a model like text-embedding-3-small.
  - **Step 3: Calculate Similarity:** Look at the cosine similarity between sentence \(A\) and sentence \(B\).
  - **Step 4: Set a Threshold:** If the similarity drops below a certain point (e.g., the model suddenly starts talking about "Tax Law" instead of "Revenue Growth"), you create a breakpoint and start a new chunk.

  Sliding Window (e.g., comparing a group of 3 sentences to the next 3) to smooth out the noise and ensure the "thematic shift" is real and not just a one-sentence outlier

- Agentic Chunking

## Hallucinations: How to stop them?

- Use System Prompts ("Answer only using the provided context")
- Chain-of-Thought ("Think step-by-step")
- Self-Correction agents

---

# Agents and tool use (design patterns, failure modes, production challenges)

## ReAct Agents (Reasoning and understanding)

1. **Think:** The model reflects ("I need to check X").
2. **Act:** It makes API/tool calls ("search Wikipedia for X").
3. **Observe:** It reads the result.
4. **Think again:** It reevaluates based on new data.
5. Repeat or conclude.

## Failure modes

- **Infinite Loops:** An agent keeps calling the same failing tool.  
  **The Fix:** Set a Max Iteration Limit (e.g., if it doesn't solve it in 5 steps, it must stop and ask the user for help).

- **Tool Hallucination:** The LLM tries to use a tool that doesn't exist (e.g., calculate_tax()) because it "feels" like it should.  
  **The Fix:** Use Strict Schema Validation (Pydantic). If the model generates a tool call that doesn't match your exact list of available Python functions, the system catches the error before it even runs.

- **State Management:** Agents "forget" what they were doing mid-task.  
  **The Fix:** Use a State Machine (like LangGraph) to strictly define which "node" the agent is in so it doesn't get lost.

---

# Evaluation and operations (offline vs online evals, production metrics)

Offline Evals tell you if the model is smart, but Online Metrics tell you if the model is useful.

## Offline

- **Golden Datasets:** You curate a "ground truth" set of 50–100 high-quality Q&A pairs that represent your most important use cases.
- **LLM-as-a-Judge:** You use a stronger model (like GPT-4o) to grade your current model's responses against that "Golden Set" based on a rubric (e.g., "On a scale of 1-5, how helpful is this?").
- **Regression Testing:** Every time you change a prompt or a chunking strategy, you re-run the offline eval to make sure your new version didn't get worse at things the old version was good at.

## Online

- **Implicit Feedback:** You track user behavior. If a user "copy-pastes" an answer or doesn't ask a follow-up question, it's a signal of success. If they immediately re-generate the response, it's a failure.
- **Explicit Feedback:** The classic "Thumbs Up/Down" buttons. While data is sparse, it is the highest quality signal you have.
- **Guardrails:** Using small, fast models (like NeMo Guardrails) to scan outputs in real-time for hallucinations or toxic content before the user sees them.

## Production Metrics

These are the "Vitals" that keep the system running.

- **P95 Latency:** This means 95% of your users get a response in under \(X\) seconds. It's better than "Average Latency" because it accounts for those annoying "slow" spikes that ruin user experience.
- **Token Usage/Cost:** Tracking how many tokens are consumed per session to ensure your "Finance Automation" tool doesn't cost more to run than the money it saves.
- **Throughput (TPS):** Tokens Per Second. This tells you if your infrastructure (the "AI Hub" you mentioned) can handle multiple users at once.
- **Faithfulness/Groundedness:** Specifically for RAG—does the answer actually come from the retrieved documents, or did the model make it up?

---

# Classical ML concepts (regularization, neural networks) and LLM-specific topics (fine-tuning, inference optimization)

## Neural Networks

- **Feed forward layer**  
  Neurons, weights, activation (Sigmoid function, so it will be between 0 and 1), next layer

- **Cost function**  
  Sum of squared error (actual - predicted) for all output neurons

- **Gradient descent**  
  Take derivtaive of each weight to the cost function to know how to adjust the weight to produce a smaller cost

- **Back propagation**  
  The recursive application of the chain rule (derivatives)

  1. Forward propagation
  2. Calculate activations and evaluate output derive activation
  3. Compute weight derivatives
  4. Gradient descent
     - **Batch gradient descent:** Calculate the gradient for each sample and average them; Update all the parameters based on that average gradient; Repeat 1 and 2 until convergence
     - **Stochastic gradient descent:** Randomly sort the list of training observations; Calculate the gradient from one training sample; Update all the parameters based on that error; Repeat 2 and 3 until all training samples have been used, then repeat 1-3 until convergence
     - **Minibatch gradient descent**
       - Shuffle the dataset to ensure each mini-batch is representative of the entire data distribution.
       - Divide the dataset into mini-batches of a specified size.
       - Compute the gradient for each mini-batch by calculating the loss and its derivative.
       - Update model parameters based on the computed gradient.
       - Repeat the process until convergence is achieved or a stopping criterion is met.

- **Dropout**
