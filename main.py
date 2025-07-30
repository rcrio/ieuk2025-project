import analyser as a

# Extract IP addresses from the log file
ips = a.extract_ips("logs.log")

# Count requests per IP
ip_counter = a.count_requests(ips)

# Convert to DataFrame for easier analysis
df = a.create_dataframe(ip_counter)

# Compute traffic statistics
stats = a.get_statistics(df)

# Output summary statistics
print("==============================")
print("Total unique IPs:", stats["total_unique_ips"])
print("Total requests:", stats["total_requests"])
print("Mean requests per IP:", stats["mean"])
print("Median requests per IP:", stats["median"])
print("Standard deviation:", stats["std"])
print("==============================")

# Output top 20 IPs by request count
print("\n==============================")
print(stats["top_hits"].head(20))
print("==============================")
