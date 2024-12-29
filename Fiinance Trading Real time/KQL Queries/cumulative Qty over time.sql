FinctrdTbl
| where timestamp > ago(1m)
| summarize CumulativeQuantity = sum(quantity) by bin(timestamp, 1m)
| order by timestamp asc
