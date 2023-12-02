import pandas as pd
import cali_val2
#use pandas cuz why not

txt_df = pd.read_csv("Day1/input.txt", names=["val"])
txt_df = txt_df.map(cali_val2.get_cali_value)
sum = txt_df["val"].sum()
print(sum)