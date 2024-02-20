from gpt_utils import get_completion, write_json, json_to_df, tag_reviews
from business_context import business_context
from prompt import PROMPT

class AutoTag():
    def __init__(self,custom_prompt,feedbacks):
        self.custom_prompt = custom_prompt
        self.feedbacks = feedbacks
    def tag_reviews():	
        tagged_responses = []
        if self.feedbacks:
            for i in range(len(self.feedbacks)):
                feedback = self.feedbacks[i]
                prompt_str = self.custom_prompt + feedback 
                try:
                    response = get_completion(prompt_str) 
                    tagged_responses.append(response)
                except Exception as e:
                    print(e)
                    pass
        return tagged_responses
    def write_reviews():
        

def __init__(self, ref_path, text_col, sample_sheet='0', keyword_expansions='keyword_expansions',
                 custom_afterprompt='\n\nEach Review can mention multiple {}.\n\n', titles_col=False):
        self.ref_path = ref_path
        self.text_col = text_col
        self.sample_sheet_name = sample_sheet
        self.kw_expansions_name = keyword_expansions
        self.sample_sheet = pd.read_excel(ref_path, sheet_name=sample_sheet)
        self.keyword_expansions = pd.read_excel(ref_path, sheet_name=keyword_expansions
                                                ).set_index('keyword')['expansions'].str.split(',').apply(
            lambda x: [r.strip() for r in x]).to_dict()
        xls = pd.ExcelFile(ref_path)
        self.task_names = xls.sheet_names[2:]
        print(self.task_names)
        self.descriptions = dict(map(lambda x: (x, pd.read_excel(ref_path, sheet_name=x).columns[1]), self.task_names))
        self.includes = dict(
            map(lambda x: (x, {k: v for k, v in zip(pd.read_excel(ref_path, sheet_name=x, skiprows=[0])[x],
                                                    [[e.strip() for e in cl if e != ''] for cl in
                                                     pd.read_excel(ref_path, sheet_name=x, skiprows=[0])[
                                                         'Include_Keywords']
                                                    .fillna('').str.split(',')])}), self.task_names))
        self.excludes = dict(
            map(lambda x: (x, {k: v for k, v in zip(pd.read_excel(ref_path, sheet_name=x, skiprows=[0])[x],
                                                    [[e.strip() for e in cl if e != ''] for cl in
                                                     pd.read_excel(ref_path, sheet_name=x, skiprows=[0])[
                                                         'Exclude_Keywords']
                                                    .fillna('').str.split(',')])}), self.task_names))
        self.exclude_specifics = dict(
            map(lambda x: (x, {k: v for k, v in zip(pd.read_excel(ref_path, sheet_name=x, skiprows=[0])[x],
                                                    [[e.strip() for e in cl if e != ''] for cl in
                                                     pd.read_excel(ref_path, sheet_name=x, skiprows=[0])[
                                                         'Exclude_keywords_specific_applied_to']
                                                    .fillna('').str.split(',')])}), self.task_names))

        self.tasks = dict(map(lambda x: (x, pd.read_excel(ref_path, sheet_name=x, skiprows=[0])), self.task_names))
        self.prompts = dict(map(lambda x: (x,
                                           f'{self.descriptions[x].strip()} The {x} fall into {len(self.tasks[x])} categories:\n' + '\n'.join(
                                               map(
                                                   lambda y: f'{y[0] + 1}. {y[1][1][0]} - {y[1][1][1]}',
                                                   enumerate(self.tasks[x].iterrows()))) + custom_afterprompt.format(
                                               x)), self.task_names))
    

def get_completion(prompt, model="gpt-3.5-turbo"): # Andrew mentioned that the prompt/ completion paradigm is preferable for this class
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def write_json(response,output_file):
    with open(output_file, "w") as file:
        json.dump(response, file, indent=4)
    print("JSON list has been written to", output_file)



def json_to_df(input_file,output_file):
    with open(input_file, "rb") as file:
        responses = json.loads(file.read())
    
    results = []
    for response in responses:
        results.append(json.loads(response))
    
    pd.json_normalize(results).to_csv(output_file,index=False)

