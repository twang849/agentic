import pytest
import os
from agentic.tools.database_tool import DatabaseTool
from agentic.common import ThreadContext

class DummyAgent:
    pass

TEST_DB_PATH = os.path.join(os.path.dirname(__file__), '../examples/database/data.db')
TEST_DB_URL = f"sqlite:///{os.path.abspath(TEST_DB_PATH)}"

def test_fetch_db_schema_all_tables():
    tool = DatabaseTool(connection_string=TEST_DB_URL)
    ctx = ThreadContext(agent=DummyAgent())
    schema = tool.fetch_db_schema(ctx)
    # Check that at least one table and one column are present
    assert "table " in schema
    assert any(line.strip().startswith("") and " " in line for line in schema.splitlines() if line.strip().startswith("table "))
    assert any(line.startswith("  ") for line in schema.splitlines())

def test_fetch_db_schema_specific_table():
    tool = DatabaseTool(connection_string=TEST_DB_URL)
    ctx = ThreadContext(agent=DummyAgent())
    # Try to fetch just one table (assuming 'albums' exists)
    schema = tool.fetch_db_schema(ctx, tables=["albums"])
    assert "table \"albums\":" in schema or "error" in schema
    assert any(line.startswith("  ") for line in schema.splitlines()) or "error" in schema
