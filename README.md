# df_store
This is a quick way to store dataframes as files while preserving the columns dtypes.

Example usage:
```
import store

store.store_df(sample_df, "stored_sample_df.dat")
retrieved_df = store.get_df("stored_sample_df.dat")
```