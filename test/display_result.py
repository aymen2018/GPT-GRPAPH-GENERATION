def display_result(users_questions, sql_chain):
    for user_question in users_questions:
        print("********************************************************************")
        print("User question:", user_question)
        print("********************************************************************")
        response = sql_chain.invoke({"question": user_question})
        print("********************************************************************")
        print("response:", response)
        print("********************************************************************")
