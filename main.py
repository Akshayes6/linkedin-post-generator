import streamlit as st
from few_shot import FewShotPosts
from postgen import generate_post

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]


def main():
    st.title('Linked In Post Generator')
    col1, col2, col3 = st.columns(3) 
    fs = FewShotPosts()

    with col1:
        selected_tag = st.selectbox('Topic', options=fs.get_tags())  
    
    with  col2:
        selected_len = st.selectbox('Length', options=length_options)
    
    with col3:
        selected_lang = st.selectbox('Language',options=language_options)
        
    if st.button('generate'):
        post = generate_post(selected_len, selected_lang, selected_tag)
        st.write(post)

if __name__ == '__main__':
    main()