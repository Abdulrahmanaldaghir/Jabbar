from openai import OpenAI
import time

client = OpenAI(api_key="yor api")

assistant = client.beta.assistants.create(
    name="FRIEND",
    instructions="You are a friend you should talk be funny and helpful ",
    model="gpt-4-1106-preview",
)
MATH_ASSISTANT_ID = assistant.id
thread  = client.beta.threads.create()
LAST_MSG_ID = ""

def submit_message(assistant_id, thread, user_message):
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=user_message
    )
    return client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )

def get_response(thread):
    global LAST_MSG_ID
    response = client.beta.threads.messages.list(thread_id=thread.id, after=LAST_MSG_ID, order="asc")
    for message in response:
        LAST_MSG_ID = message.id
        print(f"{message.role}: {message.content[0].text.value}")
    return response


def pretty_print(messages):
    print("# Messages")
    for m in messages:
        print(f"{m.role}: {m.content[0].text.value}")
        LAST_MSG_ID = m
    print()

def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run

def ai(query):
    run = submit_message(MATH_ASSISTANT_ID, thread, query)
    run = wait_on_run(run, thread)
    pretty_print(get_response(thread))
    ans =get_response(thread)
    return ans 