from collections import Counter
import pandas as pd

def extract_ips(filepath):
    """Extract IP addresses from a log file (assumes IP is first element per line)."""
    ips = []
    with open(filepath, "r") as f:
        for line in f:
            parts = line.split()
            if parts:
                ips.append(parts[0])
    return ips

def count_requests(ips):
    """Count number of requests per IP."""
    return Counter(ips)

def create_dataframe(counter):
    """Convert Counter object to DataFrame for analysis."""
    return pd.DataFrame(counter.items(), columns=["IP", "RequestCount"])

def get_statistics(df):
    """Compute basic traffic statistics."""
    return {
        "total_unique_ips": len(df),
        "total_requests": df["RequestCount"].sum(),
        "mean": df["RequestCount"].mean(),
        "median": df["RequestCount"].median(),
        "std": df["RequestCount"].std(),
        "top_hits": df.sort_values(by="RequestCount", ascending=False)
    }