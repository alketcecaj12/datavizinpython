import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(0,100,size=(252, 4)), columns=list('ABCD'))
print(df)
print(df.cov())