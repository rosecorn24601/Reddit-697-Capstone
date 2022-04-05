import streamlit as st
from torch import hann_window
#import pandas as pd
#import joblib
#from sklearn.linear_model import LogisticRegression


# Title
st.title("Project Augury: Predicting which Investing posts on Reddit are likely to become popular")
st.caption(" **augury** _noun_; a sign of what will happen in the future     -- Cambridge Dictionary")
st.markdown(">Course: SIADS 697/698  \n>> Git Repository: link  \n>> Blog Post: link  \n>Authors:  \n>> Antoine Wermenlinger (awerm@umich.edu)  \n>> Chris Lynch (cdlynch@umich.edu)  \n>> Erik Lang (eriklang@umich.edu)")

st.header("Summary")
st.write('''
    Placeholder text
    ''')

st.header("Background")
st.subheader("Motivation")
st.write('''
    Reddit is a popular social media networking site. From an investing perspective there are a few subreddits that have discussions related to investing.  A subreddit is a forum on Reddit that is dedicated to a specific topic, in our case we have chosen four subreddits to investigate:

    Investing
    Wall Street Bets, aka WSB
    Stock Market
    Stocks

    WSB achieved some notoriety during the “GameStop” incident where Keith Gill, a formerly little known trader achieved gains of $40M plus in a short period of time referred to as the ‘Reddit Rally’. Reuters claimed his ‘punchy move’ sparked thousands of comments on the WSB subreddit, causing his post(s) to go viral and his stock position to dramatically rise in value.  

    Project Augury is focussed on exploring what makes a post on these subreddits to be popular. We are looking at a group of four subreddits as each subreddit itself has relatively low volumes of posts each day, when compared to the biggest subreddit’s like AskReddit, and our background research confirmed that predictive tasks on social media work better in thematic subreddits and do not necessarily generalize from one theme or subreddit to another.
    ''')
st.subheader("Related Work")
st.write('''
    placeholder
    ''')
st.subheader("Ethical Considerations")
st.write('''
    There are clearly ethical implications relating from broadcasting messages on social media and the related investments to which these messages refer, as highlighted by the ‘Reddit Rally’. In project Augury we are only looking at the popularity of posts, and we have not correlated this to market activity, which could be an extension of this work.  To some extent this research has already been investigated in XXX   . Therefore we have made no further mitigations in our project related to market ethics.

Another consideration is the free and open nature of online social media, and Reddit in particular. This can, and does, lead to environments which can become toxic in a number of ways. The subreddits which are looking at Investment are typically more professional in nature so the main way in which toxicity occurs in these fora is through the use of profane language. In our pipeline we have removed this language from our analysis using the python module profanity-filter 1.3.3 which replaces profane words with the character “#”.  

    ''')


st.header("Our Approach")
st.subheader("Project Pipeline")
st.markdown("_image placeholder_")
st.write('''
    The data scrape we finally put into use called upon the PRAW library to make efficient requests to Reddit’s API.  Our approach to scraping was informed by the following article’s XXXX and the code which we eventually used can be found on the project repo, linked at the head of this page. We knew that we wanted to capture the evolution of a posts popularity over time in order to see how and when popular posts developed, so we designed a pipeline that:
    ''')
st.markdown('''
    - Captured a sample of ‘new posts’ each hour.
        - These were initially five posts per hour, but the consequences of the remainder of our cleaning function meant that this process would ‘timeout’ on AWS Lambda.  So we decided at the end of February 2022 to strip our ‘new posts’ back to one per hour.
    - Tracked these posts over a 24 hour period.
        - Each subsequent scrape would recapture the data related to our target posts, such as the number of comments, the text of those comments, the karma (for which you might assume ‘popularity’) of the comment and post authors.
    - Cleaned the data
        -  Before we stored the data onto our AWS RDS (a postgresql instance) our code did a lot of the early cleaning work for us.  Initially our requests backed libraries wrote large JSON files to our database, when we went into production we had developed code that extracted and formatted the data we wanted from the subreddit’s, making downstream processing of the data much slicker.  For example XXXX 
    - Load the data
        - Our database design/schema of tables is shown below.  This design was to optimize the functioning of the RDS and minimize storage, by reducing duplication to a minimum.


    ''')


















st.header("Testing Interactivity")
st.markdown("> Just for fun, enter a number and choose a team member to see what happens...")








#  This is equivalent to <input type = "number"> in HTML.
# Input bar 1
a = st.number_input("Enter a Number")

# # Input bar 2
# b = st.number_input("Input another Number")

# This is equivalent to the <select> tag for the dropdown and the <option> tag for the options in HTML.
# Dropdown input
names = st.selectbox("Select Team Member", ("Erik", "Chris","Antoine"))

# put it in an if statement because it simply returns True if pressed. This is equivalent to the <button> tag in HTML.
# If button is pressed
if st.button("Submit"):
    
    # # Unpickle classifier
    # clf = joblib.load("clf.pkl")
    
    # # Store inputs into dataframe
    # X = pd.DataFrame([[height, weight, eyes]], 
    #                  columns = ["Height", "Weight", "Eyes"])
    # X = X.replace(["Brown", "Blue"], [1, 0])
    
    # # Get prediction
    # prediction = clf.predict(X)[0]
    
    # Output prediction
    st.text(f"{names} just won {a} dollars!!!")
    # Note that print() will not appear on a Streamlit app.
    st.markdown(f"{names} just won {a} dollars!!!")


#st.markdown renders any string written using Github-flavored Markdown. It also supports HTML but Streamlit advises against allowing it due to potential user security concerns.

st.header("Project Start")
st.subheader("In Introduction to our Project")
st.markdown("But seriously, we're here to talke about our blog.  This might be how text will appear in our blog.")





st.subheader("A Code Block")
# st.code renders single-line as well as multi-line code blocks. There is also an option to specify the programming language.
st.code("""
def Team_Augury_feature_functions(df):
    df = df.copy
    df['column'] = df['old_column'].apply(lambda x: 1 if True else 0, axis1)
    return None
""", language="python")


