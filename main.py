from agents.medical import get_medical_priorities
from agents.logistics import allocate_resources
from agents.coordinator import create_final_plan
from agents.communication import generate_messages


print("================================")
print("       RESQ-AI SYSTEM")
print("================================")

print("\n1. MEDICAL PRIORITIES")
print(get_medical_priorities())

print("\n2. LOGISTICS ALLOCATION")
print(allocate_resources())

print("\n3. FINAL RESOURCE PLAN")
print(create_final_plan())

print("\n4. COMMUNICATION MESSAGES")

messages = generate_messages()

for message in messages:
    print("-", message)