from SimplerLLM.language.llm import LLM,LLMProvider
from SimplerLLM.tools.json_helpers import extract_json_from_text
from prompt import react_system_prompt_base
from actions import get_seo_page_report

llm_instance = LLM.create(LLMProvider.GEMINI,model_name="gemini-3.6-flash",temperature=0)

available_actions = {
    "get_seo_page_report": get_seo_page_report
}


user_query = """
what is the response time for this website : 
https://www.buildwithkishan.xyz/
"""

messages = [
    {"role": "system", "content": react_system_prompt_base},
    {"role": "user", "content": user_query}
]

turn_count = 1
max_turns = 5


while turn_count < max_turns:
    print (f"Loop: {turn_count}")
    print("----------------------")
    turn_count += 1

    agent_response = llm_instance.generate_response(messages=messages) # type: ignore

    messages.append({"role": "assistant", "content": agent_response}) # type: ignore

    print(agent_response)

    #extract action JSON From Text Response.
    action_json = extract_json_from_text(agent_response)
    # print("Action json : ",action_json)

    if action_json:
        function_name = action_json[0]['function_name']
        function_parms = (action_json[0].get("function_params")
                           or action_json[0].get("function_parms")
                           )
        if function_parms is None:
            raise ValueError("Function parameters missing")
        if function_name not in available_actions:
            raise Exception(f"Unknown action: {function_name}: {function_parms}")
        print(f" -- running {function_name} {function_parms}")
        action_function = available_actions[function_name]
        #call the function
        result = action_function(**function_parms)
        print("Action_Response:", result)
        function_result_messge = f"Action_Response: {result}"
        messages.append({"role": "user", "content": function_result_messge})
        print("----------------------")
    else:
        break