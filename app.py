import streamlit as st
from langchain import OpenAI, LLMChain, PromptTemplate
import os
# from dotenv import load_dotenv
# load_dotenv()

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Initialize the app
st.title("Auto To-Do tada! 🤖")
st.subheader("🕹️ to-do list that does itself.")

gform_url = "https://docs.google.com/forms/d/e/1FAIpQLSfPnRek7CtzKSLrcpicpAaDegNvVfwDcr1KxB0rmML4605s_g/viewform"
st.markdown(f"Join the [waitlist]({gform_url}) for the full-version of the app.")

# add task_list session state variable
if "task_list" not in st.session_state:
    st.session_state.task_list = []

# add new_task session state variable
if "new_task" not in st.session_state:
    st.session_state.new_task = ""

# add checkbox status as the session state variable
if "checkbox_states" not in st.session_state:
    st.session_state.checkbox_states = {}

# function for adding new tasks
def add_task(new_task):
    if new_task and add_button:
        st.session_state.task_list.append(new_task)
        st.session_state.new_task = ""

# creating a form for adding tasks
with st.form("add_task_form"):
    st.session_state.new_task = st.text_input("Enter a new task", value = st.session_state.new_task, placeholder="start using! enter a task", label_visibility= "collapsed")
    add_button = st.form_submit_button("Add Task")

# adding a new task using add_task function
add_task(st.session_state.new_task)

# displaying the checkboxes and storing the checkbox states
if len(st.session_state.task_list) > 0:
    # st.divider()
    st.subheader("Tasks")
    for task in st.session_state.task_list:
        if task not in st.session_state.checkbox_states:
            st.session_state.checkbox_states[task] = False
        st.session_state.checkbox_states[task] = st.checkbox(task, value = st.session_state.checkbox_states[task])

#list of checked tasks
checked_tasks = [task for task in st.session_state.checkbox_states if st.session_state.checkbox_states[task]]



# process checked tasks
# def process_checked_tasks():
#     global checked_tasks
#     checked_tasks = [task for task in st.session_state.checkbox_states if st.session_state.checkbox_states[task]]
#     st.write("Checked tasks:", checked_tasks)

llm = OpenAI(temperature = 0)

template = """ 
            You are an assitant which helps in accomplishing the to-do list items. 
            The main motive for you is to get me started with the following task that I am doing.
            {task}
            """
prompt = PromptTemplate(input_variables = ['task'], template = template)
llm_chain = LLMChain(llm = llm, prompt = prompt)


# Function to process checked tasks using LangChain
def process_checked_tasks():
    task_results = {}
    for task in checked_tasks:
        task_results[task] = llm_chain.run(task)

    # st.markdown("### Task Results")
    # st.table(pd.DataFrame(task_results.items(), columns=["Task", "Result"]))
    # st.markdown("### Task Results")
    # for task, result in task_results.items():
    #     st.markdown(f"**{task}:** {result}")
    st.markdown("### Task Results")
    for task, result in task_results.items():
        st.markdown(f"""**Task: {task}**""")
        st.write(f"""_Response: {result}_""")
        st.divider()



# button to process checked tasks
# checking in the task_list is non-empty and display submit button
if len(st.session_state.task_list) > 0:
    submit_button = st.button("do these tasks for me")

    if submit_button:
        if len(checked_tasks) > 0:
            if len(checked_tasks) > 3:
                st.write("you can select a maximum of 3 tasks!")
            else:    
                process_checked_tasks()
        else:
            st.write("select at least one task")




st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

linkedin_url = "https://www.linkedin.com/in/satvik-paramkusham-76a33610a/"
st.markdown(f"Reach out to me on [LinkedIn]({linkedin_url})")