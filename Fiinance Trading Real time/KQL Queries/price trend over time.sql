FinctrdTbl
| summarize AvgPrice = avg(price) by bin(timestamp, 10s)
| order by timestamp asc
