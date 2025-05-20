'''
First ask the LLM to pick a business area that might be worth exploring for an Agentic AI opportunity.
Then ask the LLM to present a pain-point in that industry - something challenging that might be ripe for an Agentic solution.
Finally have third LLM call propose the Agentic AI solution.
'''

from openai import OpenAI
from dotenv import load_dotenv

import os

# Load environment variables
load_dotenv(override=True)

# Initialize OpenAI client
openai = OpenAI()

# First step: Ask for a business area
messages = [{"role": "user", "content": "Please suggest a specific business area or industry that would benefit from an Agentic AI solution. Focus on areas with high potential for automation and efficiency gains."}]

response = openai.chat.completions.create(
    model="gpt-4.1-nano",
    messages=messages
)

business_area = response.choices[0].message.content
print("Business Area:", business_area)

# Second step: Ask for pain points in that industry
messages = [{"role": "user", "content": f"Given the business area of {business_area}, what are the key pain points or challenges that could be addressed with an Agentic AI solution? Focus on specific, actionable problems."}]

response = openai.chat.completions.create(
    model="gpt-4.1-nano",
    messages=messages
)

pain_points = response.choices[0].message.content
print("\nPain Points:", pain_points)

# Third step: Propose an Agentic AI solution
messages = [{"role": "user", "content": f"Based on the business area of {business_area} and the identified pain points, propose a specific Agentic AI solution. Include how it would work, what it would automate, and what benefits it would provide."}]

response = openai.chat.completions.create(
    model="gpt-4.1-nano",
    messages=messages
)

solution = response.choices[0].message.content
print("\nProposed Solution:", solution) 