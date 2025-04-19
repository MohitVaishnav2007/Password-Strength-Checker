import streamlit as st
import logging
from typing import Dict, Any

from controllers.password_controller import PasswordController
from utils.logging_config import setup_logging

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

def main():
    """
    Main function for the Streamlit password strength and breach checker application.
    """
    try:
        # Set page configuration
        st.set_page_config(
            page_title="Password Strength & Breach Checker",
            page_icon="🔒",
            layout="centered"
        )
        
        # Initialize controller
        password_controller = PasswordController()
        
        # App header
        st.title("Password Strength & Breach Checker")
        st.markdown("""
        This tool helps you check:
        - The strength of your password using advanced pattern and entropy analysis
        - Whether your password has been exposed in data breaches
        
        *Your password is processed securely and never stored or transmitted in plaintext.*
        """)
        
        # Password input with password masking
        password = st.text_input("Enter a password to check:", type="password")
        
        if st.button("Check Password"):
            if not password:
                st.error("Please enter a password.")
            else:
                with st.spinner("Analyzing password..."):
                    # Process the password through controller
                    results = password_controller.process_password(password)
                    display_results(results)
        
        # Add footer with information
        st.markdown("---")
        st.markdown("""
        ### How it works:
        1. Password strength is analyzed using the [zxcvbn](https://github.com/dropbox/zxcvbn) algorithm
        2. Breach checking uses the [HaveIBeenPwned API](https://haveibeenpwned.com/API/v3) with k-anonymity
        3. Your password is never sent over the network in plaintext
        """)
                
    except Exception as e:
        logger.error(f"Unexpected error in the application: {str(e)}", exc_info=True)
        st.error(f"An unexpected error occurred: {str(e)}")

def display_results(results: Dict[str, Any]):
    """
    Display the password analysis results in a user-friendly way.
    
    Args:
        results: Dictionary containing strength score, feedback, and breach status
    """
    # Split the display into two columns
    col1, col2 = st.columns(2)
    
    # Password Strength Section
    with col1:
        st.subheader("Password Strength")
        
        # Display score with appropriate color
        score = results["strength"]["score"]
        score_text = {
            0: "Very Weak",
            1: "Weak",
            2: "Fair",
            3: "Good",
            4: "Strong"
        }.get(score, "Unknown")
        
        score_color = {
            0: "red",
            1: "orange",
            2: "yellow",
            3: "lightgreen",
            4: "green"
        }.get(score, "gray")
        
        st.markdown(f"<h3 style='color: {score_color};'>Score: {score}/4 ({score_text})</h3>", unsafe_allow_html=True)
        
        # Display strength meter
        st.progress(score/4)
        
        # Display crack time estimation if available
        if "crack_times_display" in results["strength"]:
            st.markdown("#### Estimated time to crack:")
            crack_times = results["strength"]["crack_times_display"]
            st.markdown(f"- Online attack: **{crack_times['online_throttling_100_per_hour']}**")
            st.markdown(f"- Offline attack: **{crack_times['offline_slow_hashing_1e4_per_second']}**")
    
    # Breach Status Section
    with col2:
        st.subheader("Breach Status")
        
        if results["breach"]["found"]:
            st.markdown(f"<h3 style='color: red;'>⚠️ Found in {results['breach']['count']} breaches!</h3>", unsafe_allow_html=True)
            st.markdown("This password has been exposed in data breaches and should not be used.")
        else:
            st.markdown("<h3 style='color: green;'>✅ No breaches found</h3>", unsafe_allow_html=True)
            st.markdown("This password hasn't been found in known data breaches.")
    
    # Improvement Suggestions Section
    st.subheader("Improvement Suggestions")
    
    if results["strength"]["feedback"]["warning"]:
        st.warning(results["strength"]["feedback"]["warning"])
    
    if results["strength"]["feedback"]["suggestions"]:
        st.markdown("#### Suggestions to improve password strength:")
        for suggestion in results["strength"]["feedback"]["suggestions"]:
            st.markdown(f"- {suggestion}")
    elif score >= 3 and not results["breach"]["found"]:
        st.success("Great password! It's strong and hasn't been found in known breaches.")

if __name__ == "__main__":
    main()
