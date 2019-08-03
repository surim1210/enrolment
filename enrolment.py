import pandas as pd

enroll_df = pd.read_csv('data/enrolment_1.csv')

# 코드를 작성하세요.

enroll_df['status'] = 'allowed'
enroll_df.loc[(enroll_df['year'] == 1) & (enroll_df['course name'] == 'information technology'),'status'] = 'not allowed'
enroll_df.loc[(enroll_df['year'] == 4) & (enroll_df['course name'] == 'commerce'), 'status'] == 'not allowed'


c_counts = (enroll_df['course name'].value_counts() < 5)
c_counts = c_counts[c_counts]
c_list=list(c_counts.index)
for i in enroll_df.index:
    if enroll_df.loc[i, 'course name'] in c_list:
        enroll_df.loc[i,'status'] = 'not allowed'


#pass_both = (df['LC'] >= 250) & ( df['RC'] >= 250)