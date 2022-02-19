import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Fowad Ijaz, MBA
##### *Resume* 
''')

image = Image.open('dp.png')
st.image(image, width=200)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced business leader, decision-maker and administrator with 4 years of experience in data-oriented environment and a passion for delivering insights based on predictive modeling. 
- Strong verbal and written communication skills as demonstrated by extensive participation in societies and associations.
- Strong track record in business analysis and developing recommendations.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/fowad-ijaz/" target="_blank">Fowad Ijaz</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Master Of Business Administration** (Business Analytics), *DeGroote School of Business, McMaster University*, Hamilton',
'2018-2020')
st.markdown('''
- GPA: `3.89`
- Dean's List.
- President, MBA Operations Management Association.
''')

txt('**Bachelors of Science** (Biological Science), *University of Toronto*, Toronto',
'2013-2017')
st.markdown('''
- GPA: `3.65`
- Dean's List with First Class Honors.
- Orientation leader, 2017.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Senior Business Analyst**, Health Benefits Management, TELUS Health, Toronto',
'2021-Present')
st.markdown('''
- Reporting to VP, Health Benefits Management, manage the business unit scorecard which secures compensation for 119 team members.
- Developed internal communications for vice president to communicate new mandate of four key priorities.
- Organized 2 training sessions to communicate the benefits of Google Suite to team members; 67 attendees.  
''')

txt('**Operations Analyst, Co-op**, Health Benefits Management, TELUS Health, Toronto',
'2020')
st.markdown('''
-	Applied `analytical` and `problem-solving` skills to large datasets of healthcare provider data; used pivot tables, cost-benefit, and time-series analysis to create a business model that identified over `$100,000` in cost savings through the implementation of Robotic Process Automation.
-	Reporting to the Senior Strategy Manager, undertook the implementation of TELUS Health’s first Robotic Process automation project, including drafting `business requirements` for the development team, creating a `risk management plan`, and `internal communications` to keep stakeholders appraised about project status. 
-	Submitted monthly financial reports and quarterly scorecards to Vice President of Health Benefits Management team; automated the reporting process using VBA and pivot tables to reduce manual effort when pulling data from multiple sources.
-	Completed ad hoc projects, including defining KPIs in collaboration with external consultants, responding to an RFP on short notice by gathering and distilling key capabilities of TELUS Health products and services, and creating a virtual care matrix to keep senior leadership appraised of the competitive landscape. 
''')

txt('**Risk Analyst - Co-op**, Royal Bank of Canada, Toronto',
'2019')
st.markdown('''
- Used analytical skills to conduct qualitative and quantitative analysis to arrive at an internal risk rating for RBC clients, determining lending rates for non-banking financial institutions with assets ranging from $100M to $10B.
- Authored `17` analyst reports and 250 counterparty risk reviews which summarized the analysis conducted and serve as justification behind RBC credit risk ratings, which were used to establish borrowing terms for RBC clients. Exceeded target of less than `10 percent` reviews outstanding.
''')

txt('**Policy Advisor - Co-op**, Government of Ontario, Toronto',
'2019')
st.markdown('''
-	Created project plan for delivery of Ontario Automotive Modernization Plan, including creating process flow for old vs new program delivery, engaging external stakeholders to get input on possible improvements, creating Gantt chart to establish team member roles & responsibilities, and risk mitigation plan.
-	Analyzed SME proposals for grant funding based on financial feasibility, delivery team expertise, change management plan, and overall strength of proposal.
''')



#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`tableau`, `PowerBI`, `matplotlib`, `seaborn`, `plotly`, `ggplot2`')
txt3('Web development', '`Django`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `Heroku`, `AWS`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/fowad-ijaz/')
txt2('GitHub', 'https://github.com/FowadIjaz')
