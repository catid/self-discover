import openai
import os
import time

from openai import OpenAI

# Edit this part for your setup
#client = OpenAI(api_key="yourkey")
client = OpenAI(api_key="local-generated-key", base_url="http://devnuc.lan:5000/v1")


def query_llm(messages, max_tokens=2048, temperature=0.1):
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
            print("Failure querying the AI. Retrying...")
            time.sleep(1)

def query_openai(prompt):
    messages = [
        { "role": "user", "content": prompt }
    ]
    return query_llm(messages)

# STAGE 1

def select_reasoning_modules(task_description, reasoning_modules):
    """
    Step 1: SELECT relevant reasoning modules for the task.
    """
    prompt = f"주어진 과제: {task_description}, 다음 추론 모듈들 중 관련이 있는 것은 무엇입니까? 이유를 자세히 설명하지 마세요.\n\n" + "\n".join(reasoning_modules)
    selected_modules = query_openai(prompt)
    return selected_modules

def adapt_reasoning_modules(selected_modules, task_example):
    """
    Step 2: ADAPT the selected reasoning modules to be more specific to the task.
    """
    prompt = f"전체 해결 과정을 실행시키지 말고 다음 추론 모듈들을 과제에 맞게 조정하세요:\n{selected_modules}\n\n우리의 과제:\n{task_example}"
    adapted_modules = query_openai(prompt)
    return adapted_modules

def implement_reasoning_structure(adapted_modules, task_description):
    """
    Step 3: IMPLEMENT the adapted reasoning modules into an actionable reasoning structure.
    """
    prompt = f"전체 해결책을 실행시키지 말고 조정된 추론 모듈들을 사용하여 과제에 대한 실행 가능한 추론 구조를 만드세요:\n{adapted_modules}\n\n과제 설명:\n{task_description}"
    reasoning_structure = query_openai(prompt)
    return reasoning_structure

# STAGE 2

def execute_reasoning_structure(reasoning_structure, task_instance):
    """
    Execute the reasoning structure to solve a specific task instance.
    """
    prompt = f"다음 추론 구조를 사용하세요: {reasoning_structure}\n\n과제를 해결하세요, 최종 답변을 제공하세요: {task_instance}"
    solution = query_openai(prompt)
    return solution

# Example usage
if __name__ == "__main__":
    reasoning_modules = [
        "1. 그 문제를 해결하는 데 도움이 되는 실험을 어떻게 고안할 수 있나요?",
        "2. 이 문제를 해결하기 위한 아이디어 목록을 작성하고 이를 문제에 하나씩 적용하여 어떠한 진전이 있는지 확인하세요.",
        #"3. 이 문제의 진행 상황을 어떻게 측정할 수 있나요?",
        "4. 문제를 더 쉽게 해결하기 위해 어떻게 단순화할 수 있습니까?",
        "5. 이 문제의 기저에 깔려 있는 주요 가정들은 무엇입니까?",
        "6. 각 해결책의 잠재적 위험과 단점들은 무엇입니까?",
        "7. 이 문제에 대한 대안적인 관점이나 시점은 무엇입니까?",
        "8. 이 문제와 그 해결책의 장기적인 영향은 무엇입니까?",
        "9. 이 문제를 어떻게 더 작고 관리하기 쉬운 부분으로 나눌 수 있습니까?",
        "10. 비판적 사고: 이 스타일에는 다양한 관점에서 문제를 분석하고, 가정에 의문을 제기하고, 이용 가능한 증거나 정보를 평가하는 것이 포함됩니다. 논리적 추론, 증거에 기반한 의사 결정, 사고의 잠재적 편견이나 결함 식별에 중점을 둡니다.",
        "11. 창의적 사고를 시도하고 혁신적이고 기발한 아이디어를 창출하여 문제를 해결하세요. 기존의 경계를 뛰어넘어 사고하고 상상력과 독창성을 장려하는 색다른 솔루션을 탐색해 보세요.",
        #"12. 문제를 해결하기 위해 다른 사람의 입력과 협력을 구하세요. 효과적인 솔루션을 찾기 위해 팀워크, 열린 의사소통, 그룹의 다양한 관점과 전문 지식을 활용하는 것을 강조합니다.",
        "13. 시스템적 사고 사용: 문제를 더 큰 시스템의 일부로 고려하고 다양한 요소의 상호 연결성을 이해합니다. 문제에 영향을 미치는 근본적인 원인, 피드백 루프 및 상호 의존성을 식별하고 시스템 전체를 다루는 전체적인 해결책을 개발하는 데 중점을 둡니다.",
        "14. 위험 분석 사용: 문제에 대한 다양한 해결책이나 접근 방식과 관련된 잠재적 위험, 불확실성 및 장단점을 평가합니다. 잠재적인 결과와 성공 또는 실패 가능성을 평가하고, 위험과 이점에 대한 균형잡힌 분석을 바탕으로 정보에 입각한 결정을 내리는 것을 강조합니다.",
        #"15. 성찰적 사고 사용: 문제에서 물러나서 성찰과 자기 반성의 시간을 가지십시오. 문제 해결에 영향을 미칠 수 있는 개인적인 편견, 가정 및 정신적 모델을 조사하고 미래의 접근 방식을 개선하기 위해 과거 경험을 통해 배우는 데 열려 있도록 하십시오.",
        "16. 해결해야 할 핵심 사안 또는 문제는 무엇입니까?",
        "17. 문제를 일으키는 근본적인 원인이나 요인은 무엇입니까?",
        "18. 이전에 시도된 잠재적인 해결책이나 전략이 있습니까? 그렇다면, 그 결과와 교훈은 무엇이었습니까?",
        "19. 이 문제를 해결하는 데 발생할 수 있는 잠재적인 장애물이나 과제는 무엇입니까?",
        "20. 문제에 대한 통찰력을 제공할 수 있는 관련 데이터나 정보가 있습니까? 그렇다면 어떤 데이터 소스를 사용할 수 있으며 어떻게 분석할 수 있습니까?",
        "21. 문제로 인해 직접적인 영향을 받는 이해관계자나 개인이 있습니까? 그들의 관점과 요구는 무엇입니까?",
        "22. 문제를 효과적으로 해결하려면 어떤 자원(재정, 인적, 기술 등)이 필요합니까?",
        "23. 문제 해결의 진전이나 성공을 어떻게 측정하거나 평가할 수 있습니까?",
        "24. 어떤 지표나 측정법을 사용할 수 있나요?",
        "25. 문제가 특정 전문 지식이나 기술을 요구하는 기술적이거나 실용적인 문제입니까? 아니면 개념적이거나 이론적인 문제에 더 가깝습니까?",
        "26. 문제에 제한된 리소스, 인프라 또는 공간과 같은 물리적 제약이 관련되어 있습니까?",
        "27. 문제가 사회적, 문화적, 심리적 문제 등 인간 행동과 관련된 것입니까?",
        "28. 문제가 불확실성이나 상충되는 목표 하에서 선택을 해야 하는 의사결정 또는 계획과 관련되어 있습니까?",
        "29. 문제가 데이터 분석, 모델링 또는 최적화 기술이 필요한 분석적인 문제입니까?",
        "30. 문제가 창의적인 솔루션과 혁신이 필요한 디자인 과제입니까?",
        "31. 문제가 개별 사례가 아닌 체계적 또는 구조적 문제를 해결해야 합니까?",
        "32. 문제가 시간에 민감하거나 즉각적인 주의와 조치가 필요한 긴급한 것입니까?",
        "33. 이러한 종류의 문제 사양에 대해 일반적으로 어떤 종류의 해결책이 생성됩니까?",
        "34. 문제 사양과 현재 최상의 해결책이 주어졌을 때, 다른 가능한 해결책을 추측해 보세요."
        "35. 현재 최고의 해결책이 완전히 틀렸다고 가정해 보겠습니다. 문제 사양에 대해 생각할 수 있는 다른 방법은 무엇입니까?"
        "36. 이러한 종류의 문제 사양에 대해 알고 있는 내용을 고려할 때 현재 최고의 해결책을 수정하는 가장 좋은 방법은 무엇입니까?"
        "37. 현재 최고의 해결책을 무시하고 문제에 대한 완전히 새로운 해결책을 만드세요."
        #"38. 단계별로 생각해 보세요."
        "39. 단계별 계획을 세우고, 좋은 표기와 설명와 함께 실행해 보세요."
    ]


    task_example = "리사는 사과 10개를 가지고 있습니다. 그녀는 친구에게 사과 3개를 주고, 가게에서 사과 5개를 더 삽니다. 리사는 지금 사과를 몇 개나 갖고 있나요?"



    selected_modules = select_reasoning_modules(task_example, reasoning_modules)
    print("Stage 1 SELECT: Selected Modules:\n", selected_modules)
    
    adapted_modules = adapt_reasoning_modules(selected_modules, task_example)
    print("\nStage 1 ADAPT: Adapted Modules:\n", adapted_modules)
    
    reasoning_structure = implement_reasoning_structure(adapted_modules, task_example)
    print("\nStage 1 IMPLEMENT: Reasoning Structure:\n", reasoning_structure)

    result = execute_reasoning_structure(reasoning_structure, task_example)
    print("\nStage 2: Final Result:\n", result)
