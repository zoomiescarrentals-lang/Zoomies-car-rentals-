import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Zoomies Car Rentals", page_icon="🚗", layout="wide")

# --- Constants & Data ---
OFFICE_ADDRESS = "Near Raghavendra's Panchajanya, Miyapur, Hyderabad, Telangana - 500049"
CONTACT_1 = "+91 9160045730"
CONTACT_2 = "+91 9866197146"

# Average rental data for Hyderabad (2026 Estimates)
VEHICLE_STATS = {
    "Hatchback (Swift, Tiago)": {"avg_rent": 1200, "commission": 0.30},
    "Sedan (City, Dzire)": {"avg_rent": 1800, "commission": 0.35},
    "SUV (XUV700, Creta)": {"avg_rent": 2800, "commission": 0.40},
    "Luxury (BMW, Audi)": {"avg_rent": 6500, "commission": 0.45}
}

# --- Sidebar Navigation ---
st.sidebar.title("Zoomies Menu")
page = st.sidebar.radio("Go to", ["Home", "Rent a Car", "Attach Your Car (Owners)", "Contact Us"])

# --- Home Page ---
if page == "Home":
    st.title("🚗 Welcome to Zoomies Car Rentals")
    st.subheader("Zero Deposit | Unlimited Kilometres | Your Journey, Your Way")
    st.image("https://images.unsplash.com")
    st.write(f"Zoomies is Hyderabad's premier self-drive platform. Visit our Miyapur office today!")

# --- Owner Attachment & Calculator Page ---
elif page == "Attach Your Car (Owners)":
    st.title("🤝 Partner with Zoomies")
    
    # --- Earnings Calculator Section ---
    st.header("💰 Monthly Earnings Calculator")
    st.info("Estimate how much your car can earn per month based on 2026 market rates in Hyderabad.")
    
    col_calc1, col_calc2 = st.columns(2)
    with col_calc1:
        v_type = st.selectbox("Select Vehicle Type", list(VEHICLE_STATS.keys()))
        days_listed = st.slider("Days listed per month", 1, 30, 15)
        
    # Calculation Logic
    daily_rate = VEHICLE_STATS[v_type]["avg_rent"]
    comm_rate = VEHICLE_STATS[v_type]["commission"]
    total_revenue = daily_rate * days_listed
    owner_earnings = total_revenue * (1 - comm_rate)
    
    with col_calc2:
        st.metric("Estimated Monthly Earnings", f"₹{owner_earnings:,.0f}", delta="Passive Income")
        st.caption(f"Based on avg. rate of ₹{daily_rate}/day minus Zoomies service fee.")

    st.markdown("---")

    # --- Attachment Form ---
    st.header("📝 Vehicle Attachment Form")
    with st.form("owner_form"):
        col1, col2 = st.columns(2)
        with col1:
            owner_name = st.text_input("Full Name")
            owner_phone = st.text_input("Mobile Number")
        with col2:
            vehicle_model = st.text_input("Car Make & Model")
            vehicle_number = st.text_input("Registration Number")
        
        st.subheader("Upload Documents")
        rc_copy = st.file_uploader("Upload RC Copy", type=['pdf', 'jpg', 'png'])
        car_photos = st.file_uploader("Upload Car Photos", type=['jpg', 'png'], accept_multiple_files=True)
        
        if st.form_submit_button("Submit Application"):
            if owner_name and owner_phone and rc_copy:
                st.success(f"Success! Our team will contact you at {owner_phone} regarding your {vehicle_model}.")
            else:
                st.error("Please provide your name, phone, and RC copy.")

# --- Contact Us Page ---
elif page == "Contact Us":
    st.title("📞 Contact Zoomies")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### Reach Us At")
        st.write(f"📱 **Primary:** {CONTACT_1}")
        st.write(f"📱 **Secondary:** {CONTACT_2}")
    with c2:
        st.markdown("### Office Address")
        st.write(f"📍 {OFFICE_ADDRESS}")

# --- Rent a Car Page ---
elif page == "Rent a Car":
    st.title("Available Fleet")
    st.write("Browse our top-rated cars available for immediate booking.")
    for car, data in VEHICLE_STATS.items():
        with st.expander(f"{car} - Starting @ ₹{data['avg_rent']}/day"):
            st.write("✅ Sanitized Vehicle")
            st.write("✅ 24/7 Roadside Assistance")
            st.button(f"Book {car.split('(')[0]}", key=car)
