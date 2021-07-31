# df_store
This is a quick way to store and retrieve dataframes as files while preserving the column dtypes.

Example usage:
```
import store

store.store_df(sample_df, "stored_sample_df.dat")
retrieved_df = store.get_df("stored_sample_df.dat")
```
