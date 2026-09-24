import streamlit as st

from agents.coordinator import create_final_plan
from agents.communication import generate_messages, generate_explanation
from data.disaster_data import resources


st.set_page_config(
    page_title="ResQ-AI",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 ResQ-AI")
st.subheader("Multi-Agent Disaster Response Coordinator")

st.write(
    "AI-assisted coordination of limited disaster-response "
    "resources across multiple affected zones."
)

st.success("🟢 System Status: ACTIVE")
st.info("📡 Connectivity: OFFLINE MODE (Simulated Reports)")

final_plan = create_final_plan()


# Agent Status

st.header("🤖 Agent Status")

col1, col2, col3, col4 = st.columns(4)

col1.success("🏥 Medical Agent")
col2.success("🚚 Logistics Agent")
col3.success("🤖 Coordinator")
col4.success("📢 Communication")


# Available Resources

st.header("📦 Available Resources")

col1, col2, col3, col4 = st.columns(4)

col1.metric("🚑 Ambulances", resources["ambulances"])
col2.metric("🚚 Rescue Vehicles", resources["rescue_vehicles"])
col3.metric("🩹 Medical Kits", resources["medical_kits"])
col4.metric("🏠 Shelter Capacity", resources["shelter_capacity"])


# Zone Response Plan

st.header("🗺️ Zone Response Plan")

for item in final_plan:

    if item["priority"] > 600:
        level = "🔴 CRITICAL"
    elif item["priority"] > 300:
        level = "🟠 HIGH"
    else:
        level = "🟡 MEDIUM"

    with st.expander(
        f"{level} | {item['zone']} | Score {item['priority']}"
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

        st.write("### 🧠 Why this allocation?")

        reasons = generate_explanation(item)

        for reason in reasons:
            st.write(f"• {reason}")


# Communication Messages

st.header("📢 Response Messages")

messages = generate_messages()

for message in messages:
    st.info(message)


# Response Control

st.header("🔄 Response Control")

if st.button("🔄 Re-plan Resources"):

    st.success(
        "Resources have been recalculated using the latest "
        "disaster information."
    )

    st.rerun()


# New Disaster Zone Simulation

if st.button("➕ Simulate New Disaster Zone"):

    st.warning(
        "🚨 New disaster zone detected! "
        "Resource re-planning is required."
    )