## **Project Overview**

This project demonstrates the development of an end-to-end real-time data streaming and analytics pipeline using Azure Event Hub, Python, and Power BI. The system processes simulated high-frequency financial trading data, enabling real-time insights and actionable intelligence.



## **Project Goals**

1. **Real-time Data Ingestion:** Implement a streaming system to handle high-frequency transactions.
2. **Data Processing:** Streamline real-time data to Azure Fabric for storage and analysis.
3. **Insights & Dashboards:** Visualize the processed data in real-time using Power BI dashboards.



## **System Architecture**

### **Key Components**

1. **Azure Event Hub:** Acts as the message broker for streaming financial transactions.
2. **Python Data Generator:** Simulates financial trading transactions with extreme market variability.
3. **Azure Fabric:** Stores and processes real-time data streams using KQL (Kusto Query Language).
4. **Power BI Dashboards:** Visualizes the streaming data for insights.



## High-Level Process

The high-level process in the diagram represents a real-time data ingestion, processing, and visualisation pipeline using Azure services and Fabric, with Python-generated data as the source. Here's a step-by-step breakdown:

1. **Real-Time Data Generation**:
   - Python scripts generate real-time data that is sent to an **Azure Event Hub**.
2. **Event Hub Creation and Data Ingestion**:
   - The Event Hub acts as the primary data ingress point, capturing and queuing the real-time data streams.
   - A handshake or integration process connects the Azure Event Hub to **Microsoft Fabric**, enabling seamless data transfer.
3. **Event Stream Processing**:
   - The data from the Event Hub flows into the **Event Stream** module within Fabric.
   - Here, data is ingested into an **Event House**, which can be queried using **KQL (Kusto Query Language)** for real-time insights.
4. **Real-Time Intelligence and Querying**:
   - Queries written in KQL process the incoming data and populate a **Table** or dataset for further use.
5. **Visualisation and Dashboard Creation**:
   - The processed data creates **real-time visuals** and dashboards using tools like Power BI or Fabric's visualisation capabilities.
   - Dashboards provide dynamic insights, reflecting the real-time data as it streams in.
6. **Integration with Applications**:
   - Dashboards are integrated into custom-built **applications** (via low-code or no-code platforms like Power Apps).
   - These apps allow end-users to access the real-time dashboards and interact with the data.
7. **Link Sharing and Distribution**:
   - With embedded dashboards, the applications generate shareable links to distribute access to relevant stakeholders.

This pipeline emphasises real-time data processing, visualisation, and distribution using a combination of Azure, Fabric, and supporting tools. It showcases a scalable and interactive approach for real-time intelligence and decision-making.



![High-level](C:\Users\pinakibasu\Documents\Procedd Dig\High-level.png)





### **Create Pre requisite in Azure** 

#### Create the resource group 

![pre-req2
](D:\FABRIC project\Fiinance Trading Real time\images\pre-req2.png)

Create Event Hub

![image-20241229221639010](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229221639010.png)



If the event hub is added to the Favourites, we can choose it from our Favourites, as shown above

![image-20241229222022762](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229222022762.png)

A Throughput Unit (TU) in Azure Event Hubs represents a performance and capacity unit used to measure the ingress (incoming events) and egress (outgoing events) data throughput of an Event Hub namespace. It determines the maximum amount of data that your Event Hub can handle.

Navigate all the way to Review + Create and the Create
For this exercise 1 should be sufficient

![image-20241229222220747](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229222220747.png)





#### Create Event Hub

![image-20241229222259847](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229222259847.png)

Click on the + Event Hub to start the
wizard

![image-20241229222426230](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229222426230.png)

If I am not capturing events in Azure Event Hubs (i.e., I haven't enabled Event Hubs Capture), the events are stored temporarily within the Event Hub itself, in its internal storage. However, this storage is governed by the cleanup policy and retention time I configure.

Click on the Capture wizard.

![image-20241229222610159](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229222610159.png)

Since we are not storing the incoming data in a storage, we use the option as default

![image-20241229222726114](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229222726114.png)

This marks the completion of Event Hub creation.

#### Create a shared access policy

![image-20241229222802593](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229222802593.png)

Shared Access Policy and Event hub name will be required in the Python script.

![image-20241229222918010](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229222918010.png)

1 - Click on the Shared Access policies
2- Click on the ADD
3- Name the policy and Manage\





## Python Script 

### Install Azure-Event hub module

![image-20241229223037260](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229223037260.png)



![image-20241229223044000](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229223044000.png)

### Configure the Python Script



 	![image-20241229223118037](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229223118037.png)



### Test the script 

Run the script - 

![image-20241229223224771](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229223224771.png)





# Configure the Microsoft Fabric 



### Log in to the Fabric 

![image-20241229223306628](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229223306628.png)



**Activities**

![image-20241229223610490](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229223610490.png)

### Go to the Real Time Intelligence Workload

![image-20241229223639973](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229223639973.png)



### Create a workspace

![image-20241229223659991](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229223659991.png)

 

### A complete workspace looks  like following  - 

![image-20241229223741127](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229223741127.png)



At present there are no artefacts created hence the lower panel is blank.



## Create Event House



![image-20241229223905410](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229223905410.png)



#### Adding the source![image-20241229223933491](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229223933491.png)

#### Select the Azure Event Hub

![image-20241229223952792](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229223952792.png)



#### Connection Settings

![image-20241229224108258](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229224108258.png)



###### The settings and its original reference

![image-20241229224228306](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229224228306.png)

Configured Connection details

![image-20241229224253117](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229224253117.png)



![image-20241229224305454](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229224305454.png)

![image-20241229224313115](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229224313115.png)



#### The workflow showing the data generated

![image-20241229224343867](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229224343867.png)

At this point the script should start generating data. PUBLISH the workflow



## Create Event house 

![image-20241229224540521](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229224540521.png)



### Event house showing the activity

![image-20241229224559085](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229224559085.png)

Click on the +Database to start the KQL db creation -

![image-20241229224620135](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229224620135.png)

Add the name and click on CREATE

![image-20241229224635027](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229224635027.png)



![image-20241229224655519](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229224655519.png)

#### Database created

![image-20241229224859912](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229224859912.png)

#### Create the connection

![image-20241229225013690](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229225013690.png)

![image-20241229225038430](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229225038430.png)





#### Data Ingestion showing 

![image-20241229225101479](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229225101479.png)



#### Details of the columns



![image-20241229225124179](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229225124179.png)



#### Summarise the Data Connection

![image-20241229225140693](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229225140693.png)



#### Table showing data

#### ![image-20241229225202389](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229225202389.png) 





# Create real-time dashboard 



### Select Power Bi Workload

![image-20241229225234570](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229225234570.png)



### Select the workspace

![image-20241229225252815](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229225252815.png)



The workspace is showing all the artefacts we have created

#### Select the real-time dashboard

![image-20241229225457562](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229225457562.png)





### The canvas

![image-20241229225536000](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229225536000.png)



### Setting up visual

#### step 1 

![image-20241229225635573](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229225635573.png)



step 2

![image-20241229225704825](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229225704825.png)

step 3 

![image-20241229225716913](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229225716913.png)



![

](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229225729060.png)



### Executing KQL Query

![image-20241229225750539](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229225750539.png)



# The Dashboard

![image-20241229225808633](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229225808633.png)



#### Transaction Count by Transaction Type

![image-20241229225834336](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229225834336.png)

**Potential Insights:**

1.**Market Activity**:

•The consistent fluctuation could indicate a highly active market or frequent price updates from real-time trades.

2.**Monitoring Trends**:

•Any deviation outside the 1400–1800 range could signal abnormal market conditions or important events (e.g., announcements, market shocks).![image-20241229225927571](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229225927571.png)

3.**Opportunities**:

•If you're looking to identify trading opportunities, focus on detecting patterns or anomalies in the fluctuation.

4.**Additional Data Needed**:

1.Overlaying **volume data** or transaction counts could help correlate price changes with market activity. 	



#### Price Trend Over Time



The line chart, titled "Price Trend Over Time," tracks the **AvgPrice** metric over time. Here's an insight into the chart:

**Observations:**

1.**Range**:

1.The price fluctuates between **1400** and **1800**.

2.No extreme spikes or drops are visible, indicating a relatively stable price range.

2.**Volatility**:

1.There is considerable **short-term variability** within the range, as the line appears to oscillate frequently.

2.This could signify active trading or frequent adjustments to the average price.

3.**Timeframe**:

1.The data covers a specific time window (approximately from **6:00 AM to 7:30 AM**).

2.The selected time span seems to focus on capturing rapid real-time changes.

4.**Stability**:

1.While the price is volatile, it doesn’t stray far from the range of **1600 ± 200**, suggesting a predictable pattern.





#### Cumulative Qty over time

![image-20241229230003879](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229230003879.png)



**Potential Insights:**

1.**Data Reset**:

1.This could represent the clearing of cumulative values, possibly due to the end of a batch process, trading session, or real-time aggregation cycle.

2.**High Activity**:

1.A large quantity (30 million) being processed or consumed in just one minute implies high activity or significant event handling.

3.**Operational Efficiency**:

1.If this represents an operational metric, the controlled decrease suggests that processes are functioning as expected, without unexpected spikes or delays.

4.**Monitoring Opportunity**:

1.If the cumulative quantity reset is periodic, monitoring such cycles could help predict future behavior or anomalies.



**Recommendations:**

•**Add Annotations**:

•Highlight events or triggers that cause the cumulative quantity to reset.

•**Correlate with Other Metrics**:

•Pair this visual with related metrics like transaction count, processing time, or error rates for a holistic view.

•**Explore Patterns**:

•Check if similar resets occur at consistent intervals for trend analysis.





#### Total Quantity by Symbol

![image-20241229230038018](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229230038018.png)

**Recommendations:**

•**Trend Analysis**:

•Analyze historical trends for these entities to determine whether **GOOGL's** leadership is consistent or an anomaly.

•**Deeper Exploration**:

•Investigate the factors driving **GOOGL's** higher total quantity (e.g., campaigns, customer base, or market trends).

•**Real-Time Monitoring**:

•For real-time dashboards, highlight sudden changes in these values to catch emerging trends or events.



**Potential Insights:**

1.**Performance Benchmark**:

1.**GOOGL's** significantly higher value could indicate greater popularity, trading activity, or operational focus compared to the others.

2.Understanding why **GOOGL** outpaces others might provide actionable insights (e.g., market demand, recent announcements, or performance trends).

2.**Homogeneity Among Others**:

1.The similar values for **MSFT**, **TSLA**, and **AAPL** suggest these entities are competing on similar scales or metrics. This could imply a stable market or similar activity levels.

3.**Focus Area**:

1.If this data represents resource allocation or sales, it may indicate that resources or attention are disproportionately allocated to **GOOGL**.

4.**Opportunities for Growth**:

1.**MSFT**, **TSLA**, and **AAPL** could explore strategies to close the gap with **GOOGL**, such as targeted campaigns or new initiatives. 	 



**Observations:**

1.**GOOGL Leads**:

1.**GOOGL** has the highest total quantity, exceeding **600K**, indicating it is the most significant contributor or has the highest activity volume.

2.**MSFT, TSLA, and AAPL**:

1.The quantities for **MSFT**, **TSLA**, and **AAPL** are similar, with values slightly below **500K**.

2.This suggests that these entities are performing at a comparable level in terms of the tracked metric.

3.**Gap Between Leaders and Others**:

1.There's a noticeable gap between **GOOGL** and the other entities, which could indicate a disparity in performance, demand, or operational focus.



#### Symbol Contribution to Total Volume

![image-20241229230112244](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229230112244.png)



**Observations:**

1.**TSLA Leads**:

1.**TSLA** has the largest share, contributing **26.0%** to the total volume, making it the leading symbol in terms of activity or volume.

2.**Close Competitors**:

1.**GOOGL** follows with **25.3%**, and **AAPL** is close behind at **24.7%**.

2.These two symbols have nearly identical contributions, indicating a tight competition in terms of volume.

3.**MSFT Lags Slightly**:

1.**MSFT** has the smallest contribution, at **24.0%**, though the difference is marginal compared to the others.

4.**Balanced Distribution**:

1.The contributions are relatively well-distributed, with all symbols accounting for between **24.0% and 26.0%**, indicating a balanced total volume across the symbols.



**Insights:**

1.**High Activity for TSLA**:

1.**TSLA's** leading contribution might reflect higher market interest, trading activity, or demand compared to the other symbols.

2.**Strong Competition**:

1.The small percentage differences between **GOOGL**, **AAPL**, and **MSFT** suggest they are competing at nearly the same level in terms of volume.

3.**Market Stability**:

1.The evenly distributed contributions imply a stable market environment without any one symbol dominating the total volume significantly.

4.**Potential Growth Areas**:

1.While **MSFT** has the smallest share, the gap is marginal, indicating opportunities for it to close the gap and compete more strongly with **TSLA**, **GOOGL**, and **AAPL**.



**Recommendations:**

•**Analyze** **TSLA's Contribution**:

•Dive deeper into the factors driving **TSLA's** larger share—this could include market trends, recent news, or trading activity.

•**Monitor Shifts in Contributions**:

•Track changes in these percentages over time to identify emerging trends or shifts in symbol activity.

•**Evaluate MSFT's Strategy**:

•Explore why **MSFT** is slightly behind and consider strategies to boost its volume, such as promotional efforts or targeting high-activity markets.



Create APPs

![image-20241229230157518](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229230157518.png)





![image-20241229230237077](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229230237077.png)





### Select Item 

![image-20241229230302142](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229230302142.png) 	

#### The app and its content

![image-20241229230328381](C:\Users\pinakibasu\AppData\Roaming\Typora\typora-user-images\image-20241229230328381.png)





The Realtime  variation in graph

 

![Visual_movements](C:\Users\pinakibasu\Downloads\Visual_movements.gif)