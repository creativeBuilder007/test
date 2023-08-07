from openagent import compiler

import re

# we use GPT-4 here, but you could use gpt-3.5-turbo as well
llm = compiler.llms.OpenAI(model="gpt-3.5-turbo",api_key="sk")


with open("experts.🖊️", "r") as f:
       file_content = f.read()
experts = compiler(template='''{{file_content}} hey how are things''', llm=llm, stream = False,log=True)


# execute the program for a specific goal
out = experts(query='How can I be more productive?', file_content=file_content)

print(out())
