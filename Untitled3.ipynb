{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fafa8647-74f5-4144-84a2-0ee8014b323c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import pymysql\n",
    "from sqlalchemy import create_engine\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "49406fd3-af50-41c8-9f49-65bba8a36bc1",
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = create_engine('mysql+pymysql://user10:123@localhost/ap')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e0b1125f-95a7-46e2-9ecf-9dc02552b9d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "conn = engine.connect()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "9ddbe8a5-1316-44f6-8764-37f2911f20ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "# read a simple query into DataFrame\n",
    "df=pd.read_sql_query(\"SELECT * FROM data1202.vgsales\", conn)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44d3f0fc-5761-44d1-b173-6c3836891e9a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24dfc3c3-7f8f-494e-a760-fa9c13b4b4eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "time_period_df = pd.read_sql('''\n",
    "                SELECT *,\n",
    "                CASE\n",
    "                    WHEN YEAR <= 2005 THEN 'pre-2005'\n",
    "                    WHEN YEAR > 2005 THEN 'post-2005'\n",
    "                    ELSE NULL\n",
    "                END AS TimePeriod\n",
    "                FROM data1202.vgsales\n",
    "                 ''', conn)\n",
    "time_period_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31f2eb0f-9cf2-46e2-91dc-db827a4f7f0a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_sales.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17da631d-ba09-45b5-a184-f00ce86a9eb4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visualization\n",
    "time_period_df = pd.read_sql('''\n",
    "                SELECT\n",
    "                CASE\n",
    "                    WHEN YEAR <= 2005 THEN 'pre-2005'\n",
    "                    WHEN YEAR > 2005 THEN 'post-2005'\n",
    "                    ELSE NULL\n",
    "                END AS Time_Period,\n",
    "                AVG(Global_Sales) AS Average_Global_Sales\n",
    "                FROM data1202.vgsales\n",
    "                GROUP BY Time_Period\n",
    "                 ''', conn)\n",
    "time_period_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fcc7e7d9-ad76-4253-b363-f588c4e4d498",
   "metadata": {},
   "outputs": [],
   "source": [
    "time_period_df['Average_Global_Sales']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cd8631e3-9644-4473-b837-be6016ab31fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "ax = sns.barplot(time_period_df, x='Time_Period', y='Average_Global_Sales', hue='Time_Period', estimator=\"mean\", errorbar=None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "bf2a53e4-f1f0-4a14-a822-9a670b77c1dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# # Create a new column that labels records before 2005 as 'pre-2005' and after 2005 as 'post-2005'\n",
    "df['Time Period'] = df['Year'].apply(lambda x: 'pre-2005' if x <= 2005 else 'post-2005' )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1d67ead9-0707-4c85-9a9d-6a07c672e4ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "# # Was the average of global sales higher before or after 2005 ?\n",
    "time_period_data = df.groupby('Time Period')['Global_Sales'].mean()\n",
    "time_period_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "306b60a3-e8f6-4daf-989a-b95a2e319c89",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(time_period_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e021b1dd-7c89-46d3-bda4-ab22173700af",
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c5b98c25-ca13-4a3f-ad80-8033dc80b028",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
