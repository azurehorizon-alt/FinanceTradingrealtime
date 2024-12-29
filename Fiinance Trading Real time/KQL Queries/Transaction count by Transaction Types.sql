FinctrdTbl
| where timestamp > ago(5s)
| summarize Count = count() by transaction_type
