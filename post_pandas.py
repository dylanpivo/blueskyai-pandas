from pandasai import SmartDataframe, SmartDatalake
from pandasai.connectors import PostgreSQLConnector
import streamlit as st


class PostPandas:

    def __init__(self, llm):        
        self.customers_connector = None
        self.customer_customer_demo_connector = None
        self.customer_demographics_connector = None
        self.categories_connector = None
        self.dl = None
        self.products_df = None
        self.orders_df = None
        self.order_details_df = None
        self.df_config = None
        self.llm = llm

        self.connector_config = {
            "host": "localhost",
            "port": 5432,
            "database": "northwind",
            "username": "dylan",
            "password": "password",
        }

        self.setup_connectors()
        self.setup_dataframes()
        self.create_datalake()

    def setup_connectors(self):
        self.categories_connector = PostgreSQLConnector(config={**self.connector_config, "table": "categories"})
        self.customers_connector = PostgreSQLConnector(config={**self.connector_config, "table": "customers"})
        self.employee_territories_connector = PostgreSQLConnector(config={**self.connector_config, "table": "employee_territories"})
        self.employees_connector = PostgreSQLConnector(config={**self.connector_config, "table": "employees"})
        self.order_details_connector = PostgreSQLConnector(config={**self.connector_config, "table": "order_details"})
        self.orders_connector = PostgreSQLConnector(config={**self.connector_config, "table": "orders"})
        self.products_connector = PostgreSQLConnector(config={**self.connector_config, "table": "products"})
        self.region_connector = PostgreSQLConnector(config={**self.connector_config, "table": "region"})
        self.shippers_connector = PostgreSQLConnector(config={**self.connector_config, "table": "shippers"})
        self.suppliers_connector = PostgreSQLConnector(config={**self.connector_config, "table": "suppliers"})
        self.territories_connector = PostgreSQLConnector(config={**self.connector_config, "table": "territories"})
        self.us_states_connector = PostgreSQLConnector(config={**self.connector_config, "table": "us_states"})

    def setup_dataframes(self):
        self.df_config = {
            "llm": self.llm,
            "verbose": True
        }

        self.categories_df = SmartDataframe(self.categories_connector, config=self.df_config)
        self.customers_df = SmartDataframe(self.customers_connector, config=self.df_config)
        self.employee_territories_df = SmartDataframe(self.employee_territories_connector, config=self.df_config)
        self.employees_df = SmartDataframe(self.employees_connector, config=self.df_config)
        self.order_details_df = SmartDataframe(self.order_details_connector, config=self.df_config)
        self.orders_df = SmartDataframe(self.orders_connector, config=self.df_config)
        self.products_df = SmartDataframe(self.products_connector, config=self.df_config)
        self.region_df = SmartDataframe(self.region_connector, config=self.df_config)
        self.shippers_df = SmartDataframe(self.shippers_connector, config=self.df_config)
        self.suppliers_df = SmartDataframe(self.suppliers_connector, config=self.df_config)
        self.territories_df = SmartDataframe(self.territories_connector, config=self.df_config)
        self.us_states_df = SmartDataframe(self.us_states_connector, config=self.df_config)

    def create_datalake(self):
        self.dl = SmartDatalake([self.categories_df, self.customers_df,
                                 self.employee_territories_df, self.employees_df,
                                 self.order_details_df, self.orders_df, self.products_df,
                                 self.region_df, self.shippers_df, self.suppliers_df,
                                 self.territories_df, self.us_states_df], config={
            **self.df_config,
            "custom_whitelisted_dependencies": ["geopandas", "geopy", "folium", "opencage"]
        })

    def display(self):
        st.title("Pandas AI and Postgres")

        col1, col2 = st.columns(2, gap="medium")

        with col1:
            prompt = st.text_area("Enter your prompt:")

            if st.button("Generate"):
                if prompt:
                    with st.spinner("Generating data..."):
                        st.write(self.dl.chat(prompt))

        with col2:
            st.write("Here are samples of the tables you can query:")

            st.write("Categories")
            st.write(self.categories_df.dataframe.head(3))

            st.write("Customers")
            st.write(self.customers_df.dataframe.head(3))

            st.write("Employee Territories")
            st.write(self.employee_territories_df.dataframe.head(3))

            st.write("Employees")
            st.write(self.employees_df.dataframe.head(3))

            st.write("Order Details")
            st.write(self.order_details_df.dataframe.head(3))

            st.write("Orders")
            st.write(self.orders_df.dataframe.head(3))

            st.write("Products")
            st.write(self.products_df.dataframe.head(3))

            st.write("Region")
            st.write(self.region_df.dataframe.head(3))

            st.write("Shippers")
            st.write(self.shippers_df.dataframe.head(3))

            st.write("Suppliers")
            st.write(self.suppliers_df.dataframe.head(3))

            st.write("Territories")
            st.write(self.territories_df.dataframe.head(3))

            st.write("US States")
            st.write(self.us_states_df.dataframe.head(3))
