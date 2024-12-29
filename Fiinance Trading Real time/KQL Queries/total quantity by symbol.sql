FinctrdTbl
| where timestamp > ago(5s)
| summarize TotalQuantity = sum(quantity) by symbol
| order by TotalQuantity desc
