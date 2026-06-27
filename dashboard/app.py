import logging
from io import BytesIO
from fpdf import FPDF
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
# ==========================
# LOGGING CONFIGURATION
# ==========================

logging.basicConfig(
    filename="retailiq.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("RetailIQ Dashboard Started")

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="RetailIQ Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==========================
# LOGIN CONFIG
# ==========================

USERNAME = "admin"
PASSWORD = "RetailIQ123"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ==========================
# LOGIN PAGE
# ==========================

if not st.session_state.logged_in:

    st.title("🔐 RetailIQ Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == USERNAME and password == PASSWORD:
            logging.info(f"User '{username}' logged in.")
            st.session_state.logged_in = True
            st.success("Login Successful!")
            st.rerun()

        else:
            st.error("Invalid Username or Password")

    st.stop()

# ==========================
# SIDEBAR
# ==========================

st.sidebar.success("Logged in as Admin")

if st.sidebar.button("Logout"):
    logging.info("User logged out.")
    st.session_state.logged_in = False
    st.rerun()

# ==========================
# DATABASE CONNECTION
# ==========================
# ==========================
# DATABASE CONNECTION
# ==========================

try:
    password = quote_plus("Mysql@1234")

    engine = create_engine(
        f"mysql+pymysql://root:{password}@localhost:3306/retailiq"
    )

    query = """
    SELECT
        s.sale_id,
        c.customer_name,
        p.product_name,
        s.quantity,
        s.sale_date,
        s.total_amount
    FROM sales s
    JOIN customers c
        ON s.customer_id = c.customer_id
    JOIN products p
        ON s.product_id = p.product_id;
    """

    df = pd.read_sql(query, engine)
    df["sale_date"] = pd.to_datetime(df["sale_date"])

    logging.info("Database connected successfully.")

except Exception as e:
    logging.error(f"Database Error: {e}")
    st.error(f"❌ Unable to connect to the database.\n\n{e}")
    st.stop()
# ==========================
# FILTERS
# ==========================

st.sidebar.header("Dashboard Filters")

start_date = st.sidebar.date_input(
    "Start Date",
    df["sale_date"].min().date()
)

end_date = st.sidebar.date_input(
    "End Date",
    df["sale_date"].max().date()
)

customer = st.sidebar.selectbox(
    "Customer",
    ["All"] + sorted(df["customer_name"].unique())
)

product = st.sidebar.selectbox(
    "Product",
    ["All"] + sorted(df["product_name"].unique())
)

filtered_df = df.copy()

filtered_df = filtered_df[
    (filtered_df["sale_date"] >= pd.to_datetime(start_date)) &
    (filtered_df["sale_date"] <= pd.to_datetime(end_date))
]

if customer != "All":
    filtered_df = filtered_df[
        filtered_df["customer_name"] == customer
    ]

if product != "All":
    filtered_df = filtered_df[
        filtered_df["product_name"] == product
    ]
logging.info(
    f"Filters -> Customer: {customer}, Product: {product}, "
    f"Date: {start_date} to {end_date}, Records: {len(filtered_df)}"
)
# ==========================
# TITLE
# ==========================

st.title("📊 RetailIQ Sales Dashboard")

# ==========================
# KPI CARDS
# ==========================

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", len(filtered_df))
col2.metric(
    "Revenue",
    f"₹{filtered_df['total_amount'].sum():,.2f}"
)

avg = 0 if filtered_df.empty else filtered_df["total_amount"].mean()

col3.metric(
    "Average Sale",
    f"₹{avg:,.2f}"
)

st.divider()

# ==========================
# MONTHLY SALES
# ==========================

monthly = (
    filtered_df
    .groupby(filtered_df["sale_date"].dt.to_period("M"))["total_amount"]
    .sum()
    .reset_index()
)

monthly["sale_date"] = monthly["sale_date"].astype(str)

st.subheader("Monthly Revenue")

st.bar_chart(
    monthly.set_index("sale_date")["total_amount"]
)

# ==========================
# TOP CUSTOMERS
# ==========================

customers = (
    filtered_df
    .groupby("customer_name")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

st.subheader("Top Customers")

st.bar_chart(customers)

# ==========================
# TOP PRODUCTS
# ==========================

products = (
    filtered_df
    .groupby("product_name")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

st.subheader("Top Products")

st.bar_chart(products)

# ==========================
# SALES DATA
# ==========================

st.subheader("Sales Data")

st.dataframe(filtered_df, use_container_width=True)

# ==========================
# DOWNLOAD REPORTS
# ==========================

st.subheader("Download Reports")

files = [
    "monthly_sales_report.csv",
    "top_customers_report.csv",
    "top_products_report.csv"
]

for file in files:
    try:
        with open(file, "rb") as f:
            st.download_button(
                label=f"Download {file}",
                data=f,
                file_name=file
            )
    except FileNotFoundError:
        st.warning(f"{file} not found.")
import matplotlib.pyplot as plt

st.divider()
st.header("📊 Advanced Visualizations")

# -------------------------
# Pie Chart - Revenue by Product
# -------------------------
import matplotlib.pyplot as plt

# -------------------------
# Pie Chart - Revenue by Product
# -------------------------
st.subheader("🥧 Revenue by Product")

product_revenue = (
    filtered_df.groupby("product_name")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(9, 7))

wedges, texts, autotexts = ax.pie(
    product_revenue,
    startangle=90,
    autopct=lambda pct: f"{pct:.1f}%" if pct >= 5 else "",
    pctdistance=0.75,
    labeldistance=1.15,
    textprops={"fontsize": 11},
    wedgeprops=dict(edgecolor="white")
)

ax.legend(
    wedges,
    [f"{name} (₹{value:,.0f})" for name, value in product_revenue.items()],
    title="Products",
    loc="center left",
    bbox_to_anchor=(1.02, 0.5),
    fontsize=10
)

ax.set_title("Revenue Distribution by Product", fontsize=15)
ax.axis("equal")

st.pyplot(fig)

# -------------------------
# Monthly Sales Trend
# -------------------------
st.subheader("📈 Monthly Sales Trend")

monthly = (
    filtered_df.groupby(filtered_df["sale_date"].dt.to_period("M"))["total_amount"]
    .sum()
    .reset_index()
)

monthly["sale_date"] = monthly["sale_date"].astype(str)

if not monthly.empty:
    st.line_chart(
        monthly.set_index("sale_date")["total_amount"]
    )
else:
    st.info("No monthly sales data.")

# -------------------------
# Area Chart
# -------------------------
st.subheader("📉 Monthly Revenue Area Chart")

if not monthly.empty:
    st.area_chart(
        monthly.set_index("sale_date")["total_amount"]
    )
# -------------------------
# Donut Chart - Customer Revenue
# -------------------------
st.subheader("🍩 Customer Revenue Distribution")

customer_revenue = (
    filtered_df.groupby("customer_name")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(9, 7))

wedges, texts, autotexts = ax.pie(
    customer_revenue,
    startangle=90,
    autopct=lambda pct: f"{pct:.1f}%" if pct >= 5 else "",
    pctdistance=0.75,
    labeldistance=1.15,
    textprops={"fontsize": 11},
    wedgeprops=dict(width=0.45, edgecolor="white")
)

ax.legend(
    wedges,
    [f"{name} (₹{value:,.0f})" for name, value in customer_revenue.items()],
    title="Customers",
    loc="center left",
    bbox_to_anchor=(1.02, 0.5),
    fontsize=10
)

ax.set_title("Customer Revenue Distribution", fontsize=15)
ax.axis("equal")

st.pyplot(fig)
# ==========================================================
# PHASE 14 - EXPORT FILTERED REPORTS (EXCEL + PDF)
# ==========================================================

st.divider()
st.header("📥 Export Filtered Reports")


# -------------------------
# Excel Export Function
# -------------------------
def export_pdf(dataframe):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(
        190,
        10,
        "RetailIQ Sales Report",
        new_x="LMARGIN",
        new_y="NEXT",
        align="C"
    )

    pdf.ln(5)

    pdf.set_font("Helvetica", size=10)
    pdf.cell(190, 8, f"Total Sales : {len(dataframe)}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(190, 8, f"Total Revenue : Rs.{dataframe['total_amount'].sum():,.2f}", new_x="LMARGIN", new_y="NEXT")

    avg = dataframe["total_amount"].mean() if not dataframe.empty else 0
    pdf.cell(190, 8, f"Average Sale : Rs.{avg:,.2f}", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(5)

    pdf.set_font("Helvetica", "B", 10)

    headers = ["Customer", "Product", "Qty", "Date", "Amount"]
    widths = [45, 45, 20, 35, 40]

    for h, w in zip(headers, widths):
        pdf.cell(w, 8, h, border=1, align="C")

    pdf.ln()

    pdf.set_font("Helvetica", size=9)

    for _, row in dataframe.iterrows():
        pdf.cell(widths[0], 8, str(row["customer_name"])[:20], border=1)
        pdf.cell(widths[1], 8, str(row["product_name"])[:20], border=1)
        pdf.cell(widths[2], 8, str(row["quantity"]), border=1, align="C")
        pdf.cell(widths[3], 8, row["sale_date"].strftime("%Y-%m-%d"), border=1)
        pdf.cell(widths[4], 8, f"Rs.{row['total_amount']:.2f}", border=1)
        pdf.ln()

    # Convert bytearray to bytes
    pdf_data = pdf.output()

    if isinstance(pdf_data, bytearray):
        pdf_data = bytes(pdf_data)

    return pdf_data


# -------------------------
# Generate Files
# -------------------------
def export_excel(dataframe):
    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        dataframe.to_excel(
            writer,
            index=False,
            sheet_name="RetailIQ Report"
        )

    output.seek(0)
    return output.getvalue()
excel_file = None
pdf_file = None
try:
    excel_file = export_excel(filtered_df)
    logging.info("Excel report generated.")
except Exception as e:
    logging.exception("Excel Export Error")
    st.exception(e)
try:
    pdf_file = export_pdf(filtered_df)
    logging.info("PDF report generated.")
except Exception as e:
    logging.exception("PDF Export Error")
    st.error(f"PDF Export Error:\n{e}")


# -------------------------
# Download Buttons
# -------------------------
col1, col2 = st.columns(2)

with col1:
    if excel_file is not None:
        st.download_button(
            label="📊 Download Excel Report",
            data=excel_file,
            file_name="RetailIQ_Filtered_Report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
with col2:
    if pdf_file:
        st.download_button(
            label="📄 Download PDF Report",
            data=pdf_file,
            file_name="RetailIQ_Filtered_Report.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("PDF could not be generated.")