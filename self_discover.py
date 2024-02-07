import openai
import os
import time

# OpenAI
from openai import OpenAI
client = OpenAI(api_key="14d78630027e15de243c8b3b489a91fa", base_url="http://devnuc.lan:5000/v1")

def query_llm(messages, max_tokens=512, temperature=0.1):
    # Retry forever
    while True:
        try:
            response = client.chat.completions.create(
                model="the best model",
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                n=1,
            )

            content = response.choices[0].message.content.strip()

            return content
        except Exception as e:
            time.sleep(1)

def query_openai(prompt):
    messages = [
        { "role": "user", "content": prompt }
    ]
    return query_llm(messages)

def select_reasoning_modules(task_description, reasoning_modules):
    """
    Step 1: SELECT relevant reasoning modules for the task.
    """
    prompt = f"Given the task: {task_description}, which of the following reasoning modules are relevant?\n\n" + "\n".join(reasoning_modules)
    selected_modules = query_openai(prompt)
    return selected_modules

def adapt_reasoning_modules(selected_modules, task_examples):
    """
    Step 2: ADAPT the selected reasoning modules to be more specific to the task.
    """
    prompt = f"Adapt the following reasoning modules to be specific to our task:\n{selected_modules}\n\nTask Examples:\n{task_examples}"
    adapted_modules = query_openai(prompt)
    return adapted_modules

def implement_reasoning_structure(adapted_modules, task_description):
    """
    Step 3: IMPLEMENT the adapted reasoning modules into an actionable reasoning structure.
    """
    prompt = f"Create an actionable reasoning structure for the task using these adapted reasoning modules:\n{adapted_modules}\n\nTask Description:\n{task_description}"
    reasoning_structure = query_openai(prompt)
    return reasoning_structure

# Example usage
if __name__ == "__main__":
    task_description = "Explain how to solve a simple algebra problem."
    reasoning_modules = [
        "1. Break down the problem into smaller parts.",
        "2. Use critical thinking.",
        "3. Apply algebraic principles.",
        "4. Check the solution for accuracy."
    ]
    task_examples = "Solve for x: 2x + 3 = 7"
    
    selected_modules = select_reasoning_modules(task_description, reasoning_modules)
    print("Selected Modules:\n", selected_modules)
    
    adapted_modules = adapt_reasoning_modules(selected_modules, task_examples)
    print("\nAdapted Modules:\n", adapted_modules)
    
    reasoning_structure = implement_reasoning_structure(adapted_modules, task_description)
    print("\nReasoning Structure:\n", reasoning_structure)

