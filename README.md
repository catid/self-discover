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
A farmer wants to buy some chickens and goats. He goes to the market with $100, knowing that a chicken costs $5 and a goat costs $20. If he wants to buy at least one of each animal and must spend all his money, how many chickens and goats can he buy?
```

```bash
(sd) ➜  self-discover git:(main) ✗ python self_discover.py

Stage 1 SELECT: Selected Modules:
 To solve a simple algebra problem, the following reasoning modules are relevant:

4. How can I simplify the problem so that it is easier to solve?
9. How can I break down this problem into smaller, more manageable parts?
16. What is the core issue or problem that needs to be addressed?
36. What is the best way to modify this current best solution, given what you know about these kinds of problem specification?
39. Let’s make a step by step plan and implement it with good notation and explanation.

Explanation:

1. Simplify the problem: In algebra, it is often helpful to simplify the problem by combining like terms, eliminating unnecessary variables, or rearranging the equation to isolate the variable you are trying to solve for.
2. Break down the problem: Algebra problems can often be broken down into smaller, more manageable parts. For example, if you are solving for x in an equation with multiple variables, you might first solve for one variable in terms of the others and then substitute that expression back into the original equation to solve for x.
3. Identify the core issue: In order to solve an algebra problem, it is important to understand what the problem is asking for. This might involve identifying the variable you are trying to solve for, understanding the relationships between different variables, and recognizing any constraints or conditions that apply to the problem.
4. Modify the current best solution: If you have a solution to the problem, but it is not quite right, it can be helpful to think about how you might modify that solution to better fit the problem. This might involve adjusting constants, rearranging terms, or making other small changes to the equation.
5. Make a step-by-step plan: To solve an algebra problem, it is often helpful to make a step-by-step plan. This might involve listing out the steps you need to take to solve the problem, using good notation and explanation to make sure each step is clear and easy to follow. This can help you stay organized and focused as you work through the problem, and can also make it easier to identify any errors or mistakes you might have made along the way.

Stage 1 ADAPT: Adapted Modules:
 1. Simplify the problem: In this problem, we can simplify the problem by recognizing that the farmer wants to buy at least one of each animal, so we know that he will buy at least 1 chicken and 1 goat. This means that he will spend at least $25 on the first chicken and goat. We can then subtract this amount from the total amount of money he has to find out how much money he has left to spend on additional chickens and goats.
2. Break down the problem: We can break down this problem into two smaller parts: first, finding out how many additional chickens the farmer can buy with the money he has left after buying the first chicken and goat, and second, finding out how many goats he can buy with the remaining money.
3. Identify the core issue: The core issue in this problem is to determine how many chickens and goats the farmer can buy with the money he has, while still spending all of his money and buying at least one of each animal.
4. Modify the current best solution: If we have a solution to this problem, but it is not quite right, we might need to adjust the number of chickens or goats we think the farmer can buy. For example, if we initially think he can buy 10 chickens and 2 goats, but then realize that this would only cost $90, we would need to adjust our solution to account for the remaining $10.
5. Make a step-by-step plan: To solve this problem, we can make a step-by-step plan as follows:

a. Subtract the cost of the first chicken and goat from the total amount of money the farmer has.
b. Divide the remaining money by the cost of a chicken to find out how many additional chickens the farmer can buy.
c. Multiply the number of additional chickens by the cost of a chicken to find out how much money the farmer will spend on chickens.
d. Subtract the cost of the chickens from the remaining money to find out how much money is left for goats.
e. Divide the remaining money by the cost of a goat to find out how many goats the farmer can buy.
f. Add the number of goats to the initial goat the farmer bought to find out the total number of goats he can buy.
g. Add the number of chickens and goats together to find out the total number of animals the farmer can buy.

Stage 1 IMPLEMENT: Reasoning Structure:
 To solve the problem of a farmer who wants to buy chickens and goats with a budget of $120, where each chicken costs $10 and each goat costs $20, and he wants to buy at least one of each animal, we can use the following reasoning structure:

1. Simplify the problem:
The farmer wants to buy at least one of each animal, so we know that he will spend at least $25 on the first chicken and goat. We can subtract this amount from the total amount of money he has to find out how much money he has left to spend on additional chickens and goats.
2. Break down the problem:
We can break down this problem into two smaller parts: first, finding out how many additional chickens the farmer can buy with the money he has left after buying the first chicken and goat, and second, finding out how many goats he can buy with the remaining money.
3. Identify the core issue:
The core issue in this problem is to determine how many chickens and goats the farmer can buy with the money he has, while still spending all of his money and buying at least one of each animal.
4. Modify the current best solution:
If we have a solution to this problem, but it is not quite right, we might need to adjust the number of chickens or goats we think the farmer can buy. For example, if we initially think he can buy 10 chickens and 2 goats, but then realize that this would only cost $90, we would need to adjust our solution to account for the remaining $10.
5. Make a step-by-step plan:
To solve this problem, we can make a step-by-step plan as follows:

a. Subtract the cost of the first chicken and goat from the total amount of money the farmer has.
b. Divide the remaining money by the cost of a chicken to find out how many additional chickens the farmer can buy.
c. Multiply the number of additional chickens by the cost of a chicken to find out how much money the farmer will spend on chickens.
d. Subtract the cost of the chickens from the remaining money to find out how much money is left for goats.
e. Divide the remaining money by the cost of a goat to find out how many goats the farmer can buy.
f. Add the number of goats to the initial goat the farmer bought to find out the total number of goats he can buy.
g. Add the number of chickens and goats together to find out the total number of animals the farmer can buy.

By following this reasoning structure, we can solve the problem and determine how many chickens and goats the farmer can buy with his budget of $120.

Stage 2: Final Result:
 To solve a simple algebra problem, we can use the following reasoning structure:

1. Simplify the problem:
Look for any terms that can be simplified or combined to make the equation easier to work with. For example, if the equation is 3x + 2 - x = 8, we can simplify it to 2x + 2 = 8.
2. Break down the problem:
Identify the different parts of the equation and what each part represents. For example, in the equation 2x + 2 = 8, the 2x represents the variable term, the +2 represents the constant term, and the = 8 represents the solution or goal.
3. Identify the core issue:
The core issue in a simple algebra problem is to find the value of the variable that makes the equation true. In the equation 2x + 2 = 8, the core issue is to find the value of x that makes the equation true.
4. Modify the current best solution:
If we have a solution to the problem, but it is not quite right, we might need to adjust our solution to make the equation true. For example, if we initially think that x = 3, but then realize that this would make the equation 2(3) + 2 = 8 or 8 = 8, we would need to adjust our solution to find the correct value of x.
5. Make a step-by-step plan:
To solve a simple algebra problem, we can make a step-by-step plan as follows:

a. Isolate the variable term:
Move all the terms that do not contain the variable to one side of the equation. In the equation 2x + 2 = 8, we can subtract 2 from both sides to get 2x = 6.

b. Solve for the variable:
Divide both sides of the equation by the coefficient of the variable to find the value of the variable. In the equation 2x = 6, we can divide both sides by 2 to get x = 3.

By following this reasoning structure, we can solve the simple algebra problem and find the value of the variable that makes the equation true. In this case, the final answer is x = 3.
```
