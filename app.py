import streamlit as st

from agents.medical import get_ai_medical_assessments
from agents.logistics import get_ai_logistics_assessments
from agents.coordinator import create_final_plan
from agents.communication import generate_messages


st.set_page_config(
    page_title="ResQ-AI",
    page_icon="🚨",
    layout="wide"
)


st.title("🚨 ResQ-AI")
st.subheader("Multi-Agent Disaster Response Coordinator")

st.write(
    "AI-powered coordination of disaster-response resources "
    "using specialized local AI agents."
)

st.success("🟢 System Status: ACTIVE")
st.info("🤖 AI Engine: Llama 3.2 via Ollama | Local Mode")


# --------------------------------------------------
# RUN AI PIPELINE
# --------------------------------------------------

with st.spinner("🤖 AI agents are analyzing the disaster situation..."):

    medical_results = get_ai_medical_assessments()

    logistics_results = get_ai_logistics_assessments()

    final_plan = create_final_plan()

    messages = generate_messages()


# --------------------------------------------------
# AGENT STATUS
# --------------------------------------------------

st.header("🤖 AI Agent Status")

col1, col2, col3, col4 = st.columns(4)

col1.success("🏥 Medical Agent\n\nACTIVE")
col2.success("🚚 Logistics Agent\n\nACTIVE")
col3.success("🤖 Coordinator Agent\n\nACTIVE")
col4.success("📢 Communication Agent\n\nACTIVE")


# --------------------------------------------------
# MEDICAL AGENT
# --------------------------------------------------

st.header("🏥 Medical AI Agent")

st.write(
    "Analyzes medical urgency and identifies the response focus "
    "for each disaster zone."
)

for item in medical_results:

    with st.expander(f"🏥 {item['zone']} — Medical Assessment"):

        st.write(item["assessment"])


# --------------------------------------------------
# LOGISTICS AGENT
# --------------------------------------------------

st.header("🚚 Logistics AI Agent")

st.write(
    "Analyzes transportation and logistical priorities using "
    "the disaster information and Medical Agent assessment."
)

for item in logistics_results:

    with st.expander(f"🚚 {item['zone']} — Logistics Assessment"):

        st.write(item["logistics_assessment"])


# --------------------------------------------------
# FINAL RESOURCE PLAN
# --------------------------------------------------

st.header("📦 Final Resource Allocation")

for item in final_plan:

    if item["priority"] >= 600:
        level = "🔴 CRITICAL"

    elif item["priority"] >= 300:
        level = "🟠 HIGH"

    else:
        level = "🟡 MEDIUM"

    with st.expander(
        f"{level} | {item['zone']} | Priority Score: {item['priority']}"
    ):

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "🚑 Ambulances",
            item["ambulances"]
        )

        col2.metric(
            "🚚 Rescue Vehicles",
            item["rescue_vehicles"]
        )

        col3.metric(
            "🩹 Medical Kits",
            item["medical_kits"]
        )

        col4.metric(
            "🏠 Shelter Slots",
            item["shelter_slots"]
        )

        st.write(
            f"**Medical cases:** {item['medical_cases']}"
        )

        st.write(
            f"**Stranded people:** {item['stranded_people']}"
        )

        st.write(
            f"**Road status:** {item['road_status']}"
        )


# --------------------------------------------------
# COORDINATOR DECISION
# --------------------------------------------------

st.header("🤖 Coordinator Decision")

if final_plan:

    coordinator_decision = final_plan[0]["coordinator_decision"]

    st.info(coordinator_decision)


# --------------------------------------------------
# COMMUNICATION AGENT
# --------------------------------------------------

st.header("📢 AI-Generated Response Messages")

for item in messages:

    st.info(
        f"**{item['zone']}**\n\n"
        f"{item['message']}"
    )


# --------------------------------------------------
# RESOURCE SUMMARY
# --------------------------------------------------

st.header("📊 Resource Utilization")

total_ambulances = sum(
    item["ambulances"]
    for item in final_plan
)

total_rescue = sum(
    item["rescue_vehicles"]
    for item in final_plan
)

total_kits = sum(
    item["medical_kits"]
    for item in final_plan
)

total_shelter = sum(
    item["shelter_slots"]
    for item in final_plan
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "🚑 Ambulances Used",
    total_ambulances
)

col2.metric(
    "🚚 Rescue Vehicles Used",
    total_rescue
)

col3.metric(
    "🩹 Medical Kits Used",
    total_kits
)

col4.metric(
    "🏠 Shelter Slots Used",
    total_shelter
)


# --------------------------------------------------
# RE-PLAN
# --------------------------------------------------

st.header("🔄 Response Control")

if st.button("🔄 Re-plan Resources"):

    st.cache_data.clear()

    st.success(
        "🚨 Disaster information re-evaluated. "
        "AI agents are generating a new response plan."
    )

    st.rerun()