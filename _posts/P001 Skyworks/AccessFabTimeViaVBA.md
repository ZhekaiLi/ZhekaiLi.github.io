---
print_background: true
---

# Access FabTime Via VBA

<center>

Author: Zhekai Li, Todd Hays
Date: Aug 31, 2023
</center>

**ABSTRACT**: This doc illustrates how to connect to use VBA in Excel to access data in FabTime dashboard.

## 1. A Good Example

Suppose we want to obtain the downtime duration data of **<font color=blue>each Eqp</font>** (tool) that belongs to **<font color=blue>EqType = N_CAN</font>**, and the time range is from **<font color=blue>2023-07-29 to 2023-08-29</font>**.
<center><img src="/images/2023-05/Snipaste_2023-08-29_11-43-24.png" width="90%"></center>

### 1.1 Analyze the URL
The first step is to analyze the URL of the webpage. The URL of the webpage is as follows:
```html
http://nbpfabtime01/FabTime717/ChartPage.html?starttime=2023-7-29%205%3A30%3A0&endtime=2023-8-30%205%3A30%3A0&modelslike=N_CAN&byobjecttypeid=8&chartsortfield1=ObjectPlusDescription&stripecolor=Black&stripeaxis=Y&width=644&height=400&grid=None&datavalues=None&horizontal=0&pagemode=2&activemode=Javascript&chart=DURATIONCVPARETO&chartview=0&tableview=0&factoryid=1&goaluserid=951&editchart=0&UID=2023123117551693323656
```

after deleting the drawing related paramters, we can convert the link above into the following format (by Bing, GPT, ...):
```py
http://nbpfabtime01/FabTime717/ChartPage.html?
starttime=2023-7-29%205%3A30%3A0
endtime=2023-8-30%205%3A30%3A0
modelslike=N_CAN # according to the "EqType" option
byobjecttypeid=8 # according to the "Slice" option
chartsortfield1=ObjectPlusDescription
datavalues=None
horizontal=0
chart=DURATIONCVPARETO
factoryid=1
goaluserid=951
editchart=0
UID=2023123117551693323656
```

### 1.2 Fill parameters into Excel

In Excel, fill the values above into the Parameters table, if some keys above are missing (such as `modleslike` and `byobjecttypeid`), you can manually add them to the end of the table.
<img src="/images/2023-05/Snipaste_2023-08-31_08-06-07.png" width="100%">

### 1.3 Get column names

The logic of the VBA marco related to the `Run All` button is to query the data from FabTime that match the columns of `test` Table inside `details` Worksheet (from the picture above, these names could be customized).

Therefore, we need to firstly get the column names:
1. In macro editor, add a breakpoint
<img src="/images/2023-05/Snipaste_2023-08-31_08-08-59.png" width="100%">
2. Click `Run All` button, and then check the `Data` worksheet (if there is no `Data` worksheet, you have to create an empty one)
<img src="/images/2023-05/Snipaste_2023-08-31_08-12-47.png" width="100%">
3. Copy and paste the column names to the `test` Table in `details` Worksheet. And also delete the breakpoint in step 1
<img src="/images/2023-05/Snipaste_2023-08-31_08-15-40.png" width="100%">

### 1.4 Get data
Finally, just click the `Run All` button, and the data will be automatically filled into the `test` Table in `details` Worksheet.
<img src="/images/2023-05/Snipaste_2023-08-31_08-17-03.png" width="100%">


## 2. More about the Parameters Table

There are some columns in the Parameters Table that needed to be explained:
- `Pull Method` := Replace or Append. If `Replace`, the data in `test` Table will be replaced by the new data; if `Append`, the new data will be appended to the end of the table
- `UpdateType` := Today, Week, Month,... This column is used to change the start and end time of data, which can be modified through the `DataRange` Table