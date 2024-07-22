import os


def interview_assistant_prompt(context, domain, question):
    response_format = """The output should be a markdown code snippet formatted in the following schema, including the leading and trailing "```json" and "```":
                ``` json
                {
                'response' : [ //list of dictionory
                    {
                        "question": // The question which is alread provided
                        "answer": // The relevant answer which identified from the interview context with respective to question
                        "citation":[ // list of string, provide the citatiom or justification why you provided the answer.
                            
                        ]
                        "answer_score": // integer, the score of the answer with respective to question in 0 to 100 like a percantage
                        "communication_score": // integer, the score of the communication in 0 to 100 like a percentage.
                       
                    }
                ]
                }
                ```
        """
    prompt = f"""
    system role: You are an specialized interviewer with respective to {domain} domain and tasked to validate the answer for the asked question by interviewer
    
    user role:
    Below are the interview context, domain and question
    interview_context: {context}
    domain: {domain}
    question: {question}
    
    Instruction:
    - you should act as generic interviewer without any bias at any situation.
    - Dont provide any junk data.
    - Interviewer refers to the person who is taking interview and asking question and candiate refers to the person who applied for the job.
    
    Please follow below steps,
    Step1: Get the above provided question and collect all the relevant information or answer form the interview_context
    Step2: As a {domain} domain specific interviewer validate the collected answer is valid for the question if ther is no answer provided provide no infoemation found.
    Step3: Collect the citation for the answer if it is valid the citation should be exact same sentence in interview_context.
    Step4: Calculate the score for the answer identified and for the question provided in the range of 0 to 100 like a percantage.
    Step5: As a communication moniter provide the score in percentage, by considering the english profficiency, grammatic parts and how he explains the answer for the question. 
    Step5: Strictly provide the response in below format.
    
    Response_format: {response_format}
    
    """
    return prompt


def interview_assistant_prompt3(context, domain):
    response_format = """The output should be a markdown code snippet formatted in the following schema, including the leading and trailing "```json" and "```":
                ``` json
                {
                'response' : [ //list of dictionory
                    {
                        "question": //string Question identified from the interview_context, which is asked by interviwer
                       
                    }
                ]
                }
                ```
        """
    prompt =f"""
    system role: You are an specialized interviewer with respective to {domain} domain and tasked to anlyse the required information is satisfied from the provided interview context which extracted from interview video.
    User role:
    Below is the interview context which extracted from interview video.
    interview_context: {context}
    
    Instruction:
    - you should act as generic interviewer without any bias at any situation.
    - Need to analyze whether required requirments have been satisfied
    - Dont provide any junk data.
    - Interviewer refers to the person who is taking interview and asking question and candiate refers to the person who applied for the job.
    
    Step1: Collect all the question asked in inteview only with respective to the domain {domain}, only the technical question which is asked.
    Step2: Provide the response in below format.
    
    Response_format:{response_format}
    """
    return prompt
def interview_assistant_prompt2(context, domain):
    response_format = """The output should be a markdown code snippet formatted in the following schema, including the leading and trailing "```json" and "```":
                ``` json
                {
                'question_qnswer' : [ //list of dictionory, question and answers identified from the interview_context. 
                    {
                        "question": //string Question identified from the interview_context, which is asked by interviwer
                        "answer": //string Answer identified from the interview_context, which is answered by candidate.
                    }
                ]
                }
                ```
        """
    prompt = f"""
    system role: You are an specialized interviewer with respective to {domain} domain and taked to anlyse the required information is satisfied from the procided interview context which extracted from interview video.
    
    User role:
    Below is the interview context which extracted from interview video.
    interview_context: {context}
    
    Instruction:
    - you should act as generic interviewer without any bias at any situation.
    - Need to analyze whether required requirments have been satisfied
    - Dont provide any junk data.
    - Interviewer refers to the person who is taking interview and asking question and candiate refers to the person who applied for the job.
    Step1: undersatand the entire interview context with respect to the {domain} domain, since the position is for {domain}.
    Step2: In the interview there may one or more interviwers can be there and asking question with the candidate, you need uderstand what are all the question asked by the interview and what is the respective answer provided by the candidate. while collecting the question answer dont leave any questions and answer pari, analyse and collect all the question and answer pairs.
    Step3: Strictly provide the response in below format.
    
    Response_format: {response_format} 
    
    """
    return prompt