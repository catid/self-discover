# SELF-DISCOVER

This implements Google's algorithm from https://arxiv.org/pdf/2402.03620.pdf

## Setup

Install Conda: https://docs.conda.io/projects/miniconda/en/latest/

```bash
conda create -n sd python=3.10 -y && conda activate sd

git clone https://github.com/catid/self-discover.git
cd self-discover

pip install -r requirements.txt
```

## Demo

Edit `self_discover.py` to add your OpenAI API key.

```bash
python self_discover.py
```

## Output

I ran this using a self-hosted Miqu 70B model ( https://huggingface.co/LoneStriker/miqu-1-70b-sf-4.0bpw-h6-exl2 ) on two 4090 GPUs.

This is querying for the default task:

```
Lisa has 10 apples. She gives 3 apples to her friend and then buys 5 more apples from the store. How many apples does Lisa have now?

(The answer is 12.)
```

```bash
(sd) ➜  self-discover git:(main) ✗ python self_discover.py

Stage 1 SELECT: Selected Modules:
 9. How can I break down this problem into smaller, more manageable parts?

The problem can be broken down into two parts: first, calculating how many apples Lisa has after giving some away, and second, calculating how many apples she has after buying more. This approach simplifies the problem and makes it easier to solve.

Additionally, 10. Critical Thinking: This style involves analyzing the problem from different perspectives, questioning assumptions, and evaluating the evidence or information available. It focuses on logical reasoning, evidence-based decision-making, and identifying potential biases or flaws in thinking.

Critical thinking is always relevant in problem-solving as it helps to ensure that the solution is based on sound reasoning and evidence. In this case, it can help to confirm that the problem is being interpreted correctly and that the solution is logical and accurate.

Therefore, both 9 and 10 are relevant reasoning modules for this problem.

Stage 1 ADAPT: Adapted Modules:
 1. Breaking down the problem:
The problem can be broken down into two smaller tasks:

a) Calculate how many apples Lisa has after giving 3 to her friend.
b) Calculate how many apples Lisa has after buying 5 more apples from the store.

By breaking down the problem into these smaller tasks, it becomes easier to solve.

2. Critical thinking:
Apply critical thinking to ensure that the problem is being interpreted correctly and that the solution is logical and accurate. This involves:

a) Confirming that the problem is understood correctly (Lisa starts with 10 apples, gives away 3, and buys 5 more).
b) Ensuring that the order of operations is followed correctly (subtracting the apples given away before adding the apples bought).
c) Double-checking the calculations to ensure accuracy.

By applying critical thinking, you can be confident that the solution is based on sound reasoning and evidence.

Stage 1 IMPLEMENT: Reasoning Structure:
 1. Breaking down the problem:

a) Calculate how many apples Lisa has after giving 3 to her friend:
- Lisa starts with 10 apples
- She gives away 3 apples
- Subtract the number of apples given away from the initial number of apples

b) Calculate how many apples Lisa has after buying 5 more apples from the store:
- After giving away 3 apples, Lisa has a certain number of apples left (from task a)
- She then buys 5 more apples
- Add the number of apples bought to the remaining number of apples

2. Critical thinking:

a) Confirm that the problem is understood correctly:
- Lisa starts with 10 apples
- She gives 3 apples away
- She buys 5 more apples

b) Ensure that the order of operations is followed correctly:
- First, subtract the apples given away
- Then, add the apples bought

c) Double-check the calculations:
- Verify that the correct number of apples was subtracted
- Verify that the correct number of apples was added

By following this reasoning structure, you can solve the problem by breaking it down into smaller tasks, applying critical thinking, and double-checking your calculations. The final answer should be accurate and based on sound reasoning.

Stage 2: Final Result:
 1. Breaking down the problem:

a) Calculate how many apples Lisa has after giving 3 to her friend:
- Lisa starts with 10 apples
- She gives away 3 apples
- Subtract the number of apples given away from the initial number of apples: 10 - 3 = 7 apples

b) Calculate how many apples Lisa has after buying 5 more apples from the store:
- After giving away 3 apples, Lisa has 7 apples left (from task a)
- She then buys 5 more apples
- Add the number of apples bought to the remaining number of apples: 7 + 5 = 12 apples

2. Critical thinking:

a) Confirm that the problem is understood correctly:
- Lisa starts with 10 apples
- She gives 3 apples away
- She buys 5 more apples

b) Ensure that the order of operations is followed correctly:
- First, subtract the apples given away (10 - 3)
- Then, add the apples bought (7 + 5)

c) Double-check the calculations:
- Verify that the correct number of apples was subtracted (10 - 3 = 7)
- Verify that the correct number of apples was added (7 + 5 = 12)

Final answer: Lisa has 12 apples now.
```
