FinctrdTbl
| where timestamp > ago(10s)
| summarize TotalVolume = sum(quantity) by symbol
