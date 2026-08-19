import streamlit as st
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Resource Sharing Platform",
    page_icon="🎓",
    layout="wide"
)

# ---------------- FOLDERS ----------------
MATERIAL_FOLDER = "materials"
os.makedirs(MATERIAL_FOLDER, exist_ok=True)

# ---------------- TITLE ----------------
st.title("🎓 Student Resource Sharing Platform")
st.write("Welcome to our college resource platform")

# ================= SIDEBAR =================

st.sidebar.title("📚 Menu")

option = st.sidebar.selectbox(
    "Choose a section",
    [
        "Home",
        "Study Materials",
        "Useful Resources",
        "Announcements"
    ]
)

st.sidebar.divider()

st.sidebar.subheader("👤 Student Profile")

student_name = st.sidebar.text_input(
    "Your Name",
    placeholder="Enter your name"
)

semester = st.sidebar.selectbox(
    "Your Semester",
    [
        "1st Semester",
        "2nd Semester",
        "3rd Semester",
        "4th Semester",
        "5th Semester",
        "6th Semester",
        "7th Semester",
        "8th Semester"
    ]
)

if student_name:
    st.sidebar.success(f"Welcome, {student_name}!")

# ==================================================
# HOME
# ==================================================


# ================= STUDENT PROFILE =================

if option == "Home":
    st.sidebar.subheader("👤 Student Profile")

    student_name = st.sidebar.text_input(
        "Enter your name"
    )

    semester = st.sidebar.selectbox(
        "Select your semester",
        [
            "1st Semester",
            "2nd Semester",
            "3rd Semester",
            "4th Semester",
            "5th Semester",
            "6th Semester",
            "7th Semester",
            "8th Semester"
        ]
    )

    if student_name:
        st.sidebar.success(f"Welcome, {student_name}!")




# ==================================================
# STUDY MATERIALS
# ==================================================

elif option == "Study Materials":

    st.header("📚 Study Materials")

    # Subject selection
    subject = st.selectbox(
        "Select Subject",
        [
            "Python",
            "Data Structures",
            "Mathematics",
            "Computer Science",
            "Other"
        ]
    )

    st.write(f"Selected Subject: **{subject}**")

    # Upload
    st.subheader("📤 Upload Study Material")

    uploaded_file = st.file_uploader(
        "Upload your PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        file_path = os.path.join(
            MATERIAL_FOLDER,
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(
            f"✅ {uploaded_file.name} uploaded successfully!"
        )

    # ------------------------------------------------
    # SEARCH
    # ------------------------------------------------

    st.subheader("🔎 Find Study Material")

    search = st.text_input(
        "Search by file name"
    )

    files = os.listdir(MATERIAL_FOLDER)

    pdf_files = [
        file for file in files
        if file.lower().endswith(".pdf")
    ]

    # Search filtering
    if search:

        pdf_files = [
            file for file in pdf_files
            if search.lower() in file.lower()
        ]

    # ------------------------------------------------
    # DISPLAY FILES
    # ------------------------------------------------

    st.subheader("📂 Available Materials")

    if len(pdf_files) == 0:

        st.info("No matching study materials found.")

    else:

        for file in pdf_files:

            file_path = os.path.join(
                MATERIAL_FOLDER,
                file
            )

            file_size = os.path.getsize(file_path) / 1024

            with st.container():

                st.write(f"📄 **{file}**")
                st.caption(
                    f"Size: {file_size:.1f} KB | Subject: {subject}"
                )

                with open(file_path, "rb") as f:

                    st.download_button(
                        label="⬇️ Download PDF",
                        data=f,
                        file_name=file,
                        mime="application/pdf",
                        key=f"download_{file}"
                    )

                st.divider()


# ==================================================
# USEFUL RESOURCES
# ==================================================

elif option == "Useful Resources":

    st.header("🔗 Useful Resources")

    st.write(
        "Helpful websites and learning platforms for students."
    )

    st.subheader("🐍 Python")

    st.markdown(
        "• Python Documentation"
    )

    st.subheader("💻 Coding Practice")

    st.markdown(
        "• LeetCode\n\n"
        "• HackerRank\n\n"
        "• GeeksforGeeks"
    )

    st.subheader("🎓 Learning")

    st.markdown(
        "• YouTube Learning\n\n"
        "• Free online courses"
    )


# ==================================================
# ANNOUNCEMENTS
# ==================================================

elif option == "Announcements":

    st.header("📢 College Announcements")

    st.info(
        "📌 Hackathon registration is open."
    )

    st.warning(
        "📌 Students should check the college notice board regularly."
    )

    st.success(
        "📌 New study materials can now be uploaded."
    )

    st.write(
        "More official college announcements can be added here."
    )