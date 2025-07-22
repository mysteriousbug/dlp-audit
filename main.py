import streamlit as st 

st.title("📁 Upload and Download Multiple Files")

# Allow multiple file uploads
uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded.")

    for file in uploaded_files:
        st.write(f"📄 **{file.name}**")
        
        # Read content
        content = file.read()
        
        # Try to display content if it's a text file
        try:
            text = content.decode("utf-8")
            #st.text_area(f"Content of {file.name}:", text, height=150)
        except Exception:
            #st.info(f"{file.name} may be a binary or non-text file.")
            st.info("")
        
        # Download button
        st.download_button(
            label=f"⬇️ Download {file.name}",
            data=content,
            file_name=file.name,
            mime="application/octet-stream"
        )

        st.markdown("---")
else:
    st.info("Upload some files to view and download.")
