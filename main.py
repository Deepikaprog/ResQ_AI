from agents.medical import get_ai_medical_assessments
from agents.logistics import get_ai_logistics_assessments
from agents.coordinator import create_final_plan
from agents.communication import generate_messages


print("================================")
print("        RESQ-AI SYSTEM")
print("================================")


print("\n1. 🏥 MEDICAL AI AGENT")

medical_results = get_ai_medical_assessments()

for item in medical_results:
    print("\nZone:", item["zone"])
    print(item["assessment"])


print("\n2. 🚚 LOGISTICS AI AGENT")

logistics_results = get_ai_logistics_assessments()

for item in logistics_results:
    print("\nZone:", item["zone"])
    print(item["logistics_assessment"])


print("\n3. 🤖 COORDINATOR AGENT")

final_plan = create_final_plan()

for item in final_plan:

    print("\nZone:", item["zone"])
    print("Priority:", item["priority"])
    print("Ambulances:", item["ambulances"])
    print("Rescue Vehicles:", item["rescue_vehicles"])
    print("Medical Kits:", item["medical_kits"])
    print("Shelter Slots:", item["shelter_slots"])


print("\n4. 📢 COMMUNICATION AI AGENT")

messages = generate_messages()

for item in messages:

    print("\nZone:", item["zone"])
    print(item["message"])


print("\n================================")
print("       RESQ-AI COMPLETE")
print("================================")