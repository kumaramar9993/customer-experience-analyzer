import json
import openai
import pandas as pd

# get a response from OpenAi Api 
def get_completion(prompt, model="gpt-3.5-turbo"): 
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

# write response into JSON
def write_json(response,output_file):
    with open(output_file, "w") as file:
        json.dump(response, file, indent=4)
    print("JSON list has been written to", output_file)

# read response into JSON
def read_json(input_file):
    with open(input_file, "rb") as file:
        responses = json.loads(file.read())
    return responses
    
# list of dict to output
def json_to_df(responses):
    results = []
    for response in responses:
        results.append(json.loads(response))
    return pd.json_normalize(results)
    
def write_to_csv(df,output_file):
    df.to_csv(output_file,index=False)
    
   
def tag_reviews(custom_prompt,feebacks):	
    results = []
    for i in range(len(feebacks)):
        feeback = feebacks[i]
        print(i,feeback)
        prompt_str = custom_prompt + feeback 
        res = get_completion(prompt_str) 
        results.append(res)
    return results

