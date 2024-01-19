import streamlit as st
from transformers import pipeline
import pdfplumber
import bs4 as bs
import urllib.request
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

st.sidebar.header("By Kuldeep Joshi")
st.sidebar.header("Transformer Model used: deepset/tinyroberta-squad2 ")
st.sidebar.markdown("""Either enter a wikipedia link or you can enter your own context text and get ANSWERS to your questions based on the refrence text!""")
st.sidebar.markdown("""When running the app the first time, it may take some time to initialise due to the requirements needing to be downloaded.""")
tool = st.sidebar.selectbox("Tool", ["Wikipedia Q&A", "Textbox Q&A"])


model_name = "deepset/tinyroberta-squad2"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': 'Why is model conversion important?',
    'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
}
res = nlp(QA_input)



def generateAnswer(question, context):
    answer = nlp(question=question, context=context)
    return answer['answer']


 





## ------------------------------ Wikipedia Q&A ------------------------------ ##
def wikipedia_qna():
    heading = """
    # Wikipedia Q&A  
    """
    heading
    user_input = st.text_input("Wikipedia Link:", value="")
    question = st.text_input("Question:")

    if st.button("Answer"):
        scraped_data = urllib.request.urlopen(user_input)
        article = scraped_data.read()

        parsed_article = bs.BeautifulSoup(article,'lxml')

        paragraphs = parsed_article.find_all('p')

        article_text = ""
        for p in paragraphs:
            article_text += p.text

        answer = generateAnswer(question, article_text)
        st.header("Answer")
        st.write(answer)



## ------------------------------ Textbox Q&A ------------------------------ ##
def textbox_qna():
    heading = """
    # Textbox Q&A  
    
    """
    heading
    dummy_text = '''
    
    
    '''
    user_input = st.text_area("Text:", value=dummy_text)
    question = st.text_input("Question:")

    if st.button("Answer"):
        answer = generateAnswer(question, user_input)
        st.header("Answer")
        st.write(answer)





if tool == "Wikipedia Q&A":
    wikipedia_qna()

if tool == "Textbox Q&A":
    textbox_qna()