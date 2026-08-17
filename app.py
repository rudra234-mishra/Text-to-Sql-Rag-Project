import streamlit as st
from sqlquery_generator import answer_question


st.set_page_config(
    page_title="Text to SQL",
    layout="wide",
)


# ---------------------------------------------------------
# Custom CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: "Inter", sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at top right, rgba(6, 182, 212, 0.16), transparent 28%),
            radial-gradient(circle at bottom left, rgba(34, 197, 94, 0.12), transparent 32%),
            #05080d;
    }

    .block-container {
        max-width: 1450px;
        padding: 1.5rem 2.5rem 3rem;
    }

    h1, h2, h3 {
        color: #f1f5f9 !important;
        font-weight: 800 !important;
    }

    p, label, span {
        color: #cbd5e1;
    }

    textarea {
        background: #0f172a !important;
        color: #f8fafc !important;
        border: 1.5px solid #1d4ed8 !important;
        border-radius: 16px !important;
        font-size: 1rem !important;
        padding: 1rem !important;
        box-shadow: 0 8px 30px rgba(6, 182, 212, 0.12);
    }

    textarea:focus {
        border-color: #22d3ee !important;
        box-shadow: 0 0 0 4px rgba(6, 182, 212, 0.18) !important;
    }

    textarea::placeholder {
        color: #94a3b8 !important;
    }

    .stFormSubmitButton > button {
        width: 100%;
        min-height: 3rem;
        border: none !important;
        border-radius: 14px !important;
        background: linear-gradient(135deg, #2563eb, #06b6d4 55%, #22c55e) !important;
        color: white !important;
        font-weight: 800 !important;
        font-size: 1rem !important;
        box-shadow: 0 8px 24px rgba(6, 182, 212, 0.25);
        transition: all 0.2s ease;
    }

    .stFormSubmitButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 30px rgba(34, 197, 94, 0.28);
    }

    .stButton > button {
        border-radius: 12px !important;
        border: 1px solid #1d4ed8 !important;
        background: #0f172a !important;
        color: #67e8f9 !important;
        font-weight: 600 !important;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background: #172554 !important;
        border-color: #22d3ee !important;
        transform: translateY(-1px);
    }

    div[data-testid="stCode"] {
        border-radius: 16px !important;
        border: 1px solid #1e3a5f !important;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.16);
        overflow: hidden;
    }

    div[data-testid="stDataFrame"] {
        border-radius: 16px !important;
        border: 2px solid #06b6d4 !important;
        background: #ffffff !important;
        box-shadow: 0 10px 28px rgba(6, 182, 212, 0.20);
        overflow: hidden;
    }

    div[data-testid="stDataFrame"] [role="grid"] {
        background: #ffffff !important;
        color: #0f172a !important;
    }

    div[data-testid="stDataFrame"] [role="columnheader"] {
        background: linear-gradient(90deg, #1d4ed8, #06b6d4, #16a34a) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    div[data-testid="stDataFrame"] [role="gridcell"] {
        background: #ffffff !important;
        color: #0f172a !important;
        border-color: #dbeafe !important;
    }

    .results-table-wrap {
        overflow-x: auto;
        border: 2px solid #06b6d4;
        border-radius: 16px;
        background: #05080d;
        box-shadow: 0 10px 28px rgba(6, 182, 212, 0.20);
    }

    .results-table {
        width: 100%;
        border-collapse: collapse;
        background: #05080d;
        color: #f8fafc;
    }

    .results-table th {
        padding: 0.8rem 1rem;
        background: linear-gradient(90deg, #1d4ed8, #06b6d4, #16a34a);
        color: #ffffff;
        text-align: left;
        font-weight: 700;
    }

    .results-table td {
        padding: 0.75rem 1rem;
        background: #05080d;
        color: #f8fafc;
        border-top: 1px solid #1e293b;
    }

    .results-table tr:nth-child(even) td {
        background: #0f172a;
    }

    .hero-card {
        padding: 1.5rem 1.8rem;
        border-radius: 24px;
        background: linear-gradient(135deg, #172554, #0369a1 55%, #059669);
        color: white;
        box-shadow: 0 16px 40px rgba(6, 182, 212, 0.20);
        margin-bottom: 1.5rem;
    }

    .hero-card h1 {
        color: white !important;
        margin: 0;
        font-size: 2.4rem;
    }

    .hero-card p {
        color: #dbeafe !important;
        margin: 0.5rem 0 0;
        font-size: 1rem;
    }

    .metric-card {
        padding: 1rem;
        border-radius: 16px;
        border: 1px solid #dbeafe;
        background: rgba(255, 255, 255, 0.85);
        text-align: center;
        box-shadow: 0 8px 24px rgba(37, 99, 235, 0.07);
    }

    .metric-value {
        font-size: 1.65rem;
        font-weight: 800;
        color: #1d4ed8;
    }

    .metric-label {
        color: #64748b;
        font-size: 0.75rem;
        margin-top: 0.2rem;
    }

    .section-label {
        color: #67e8f9;
        font-size: 0.75rem;
        font-weight: 800;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }

    .empty-state {
        padding: 4rem 2rem;
        text-align: center;
        border: 2px dashed #0ea5e9;
        border-radius: 22px;
        background: rgba(15, 23, 42, 0.72);
    }

    .empty-icon {
        font-size: 3.5rem;
        margin-bottom: 0.8rem;
    }

    .empty-title {
        color: #e2e8f0;
        font-size: 1.2rem;
        font-weight: 800;
    }

    .empty-description {
        color: #94a3b8;
        margin-top: 0.5rem;
        line-height: 1.6;
    }

    .history-item {
        padding: 0.8rem 1rem;
        margin-bottom: 0.6rem;
        border-left: 4px solid #22d3ee;
        border-radius: 10px;
        background: #0f172a;
        color: #e2e8f0;
        font-size: 0.9rem;
    }

    code, pre {
        font-family: "JetBrains Mono", monospace !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Session state
# ---------------------------------------------------------

if "history" not in st.session_state:
    st.session_state.history = []

if "question_input" not in st.session_state:
    st.session_state.question_input = ""


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.markdown(
    """
    <div class="hero-card">
        <h1>🛢️ Text → SQL</h1>
        <p>Ask questions in plain English and generate executable PostgreSQL queries.</p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Main layout
# ---------------------------------------------------------

left_column, right_column = st.columns([5, 7], gap="large")


with left_column:
    st.markdown(
        '<div class="section-label">✏️ ASK YOUR DATABASE</div>',
        unsafe_allow_html=True,
    )

    quick_col_1, quick_col_2 = st.columns(2)

    with quick_col_1:
        if st.button("Top 5 salaries", use_container_width=True):
            st.session_state.question_input = (
                "Show the top 5 employees by salary"
            )
            st.rerun()

    with quick_col_2:
        if st.button("Count by department", use_container_width=True):
            st.session_state.question_input = (
                "Count employees in each department"
            )
            st.rerun()

    with st.form("question_form", clear_on_submit=False):
        question = st.text_area(
            "Database question",
            value=st.session_state.question_input,
            placeholder=(
                "Example: Show the top 5 employees by salary "
                "from the employee table"
            ),
            height=160,
            label_visibility="collapsed",
        )

        submitted = st.form_submit_button(
            "⚡ Generate and Run Query",
            use_container_width=True,
        )

    if submitted:
        cleaned_question = question.strip()

        if not cleaned_question:
            st.warning("Please enter a question first.")
        else:
            try:
                with st.status(
                    "Generating SQL and fetching results...",
                    expanded=True,
                ) as status:
                    st.write("Understanding your question...")
                    sql, result = answer_question(cleaned_question)

                    st.write("Executing generated SQL...")
                    st.session_state.history.insert(
                        0,
                        {
                            "question": cleaned_question,
                            "sql": sql,
                            "result": result,
                        },
                    )

                    status.update(
                        label="Query completed successfully",
                        state="complete",
                        expanded=False,
                    )

                st.session_state.question_input = cleaned_question
                st.toast("Query generated successfully", icon="✅")
                st.rerun()

            except Exception as exc:
                st.error(f"Query failed: {exc}")


with right_column:
    if not st.session_state.history:
        st.markdown(
            """
            <div class="empty-state">
                <div class="empty-icon">🧠</div>
                <div class="empty-title">Ready to query your database</div>
                <div class="empty-description">
                    Enter a natural-language question on the left,
                    then generate and run your SQL query.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:
        latest = st.session_state.history[0]

        st.markdown(
            '<div class="section-label">📊 LATEST QUERY</div>',
            unsafe_allow_html=True,
        )

        st.caption(f"Question: {latest['question']}")

        sql_tab, result_tab, details_tab = st.tabs(
            ["💻 SQL Query", "📈 Results", "ℹ️ Details"]
        )

        with sql_tab:
            st.code(latest["sql"], language="sql")

            copy_text = latest["sql"].replace("`", "\\`")

            st.markdown(
                f"""
                <div style="
                    padding:0.8rem 1rem;
                    margin-top:0.8rem;
                    border-radius:12px;
                    background:#0f172a;
                    border:1px solid #1d4ed8;
                    color:#a5f3fc;
                    font-size:0.85rem;">
                    💡 Review the generated SQL before using it in production.
                </div>
                """,
                unsafe_allow_html=True,
            )

        with result_tab:
            result = latest["result"]

            if result is None:
                st.info("No result was returned for this query.")

            elif hasattr(result, "empty") and result.empty:
                st.warning("The query ran successfully but returned no rows.")

            else:
                table_html = result.to_html(
                    index=False,
                    escape=True,
                    classes="results-table",
                )
                st.markdown(
                    f'<div class="results-table-wrap">{table_html}</div>',
                    unsafe_allow_html=True,
                )

                if hasattr(result, "shape"):
                    rows, columns = result.shape
                    st.caption(
                        f"Returned {rows} row(s) and {columns} column(s)."
                    )

        with details_tab:
            st.markdown("### Query details")
            st.write(f"**Natural-language question:** {latest['question']}")
            st.write("**Database:** PostgreSQL")
            st.write("**Generation mode:** AI-assisted SQL generation")

        st.divider()

        if len(st.session_state.history) > 1:
            st.markdown(
                '<div class="section-label">🕘 PREVIOUS QUERIES</div>',
                unsafe_allow_html=True,
            )

            for index, item in enumerate(
                st.session_state.history[1:],
                start=1,
            ):
                with st.expander(
                    f"{index}. {item['question']}"
                ):
                    st.code(item["sql"], language="sql")

                    if st.button(
                        "Run this question again",
                        key=f"rerun_{index}",
                    ):
                        st.session_state.question_input = item["question"]
                        st.rerun()
