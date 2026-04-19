import streamlit as st
import os
import time
from engine import SystemCore

st.set_page_config(page_title="Core Alpha v1.0.0", page_icon="💎", layout="wide")

if 'core' not in st.session_state:
    st.session_state.core = SystemCore()

st.title("💎 System Core Alpha: Official Release v1.0.0")

# --- Dashboard Layout ---
col_stats, col_action = st.columns([1, 2])

with col_stats:
    st.subheader("System Health")
    if st.session_state.core.status == "OFFLINE":
        st.error("SYSTEM IS OFFLINE")
    else:
        st.success("SYSTEM IS ONLINE")
    
    if st.button("🚀 Initialize System", use_container_width=True):
        st.session_state.core.boot_sequence()
        st.rerun()

with col_action:
    st.subheader("Operations")
    is_ready = st.session_state.core.status == "ONLINE"
    if st.button("⚡ EXECUTE POLYGLOT ENGINE", use_container_width=True, disabled=not is_ready):
        with st.spinner("Syncing C++, Kotlin, and Python..."):
            st.session_state.core.run_logic_task([10, 20, 30])
            st.session_state.core.run_hardware_module()
            st.session_state.core.run_validation_check()
            st.success("Execution Successful!")

st.divider()

# --- Logging & Export ---
st.subheader("📜 System Audit Logs")
if os.path.exists("system.log"):
    with open("system.log", "r") as f:
        log_data = f.read()
        st.code(log_data[-1000:], language="bash") # Show last 1000 chars
        
        # Release Feature: Download Button
        st.download_button(
            label="📥 Download Audit Logs",
            data=log_data,
            file_name=f"system_audit_{int(time.time())}.log",
            mime="text/plain"
        )