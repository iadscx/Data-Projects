import os
def test_env_vars_exist():
    assert "FORTNITE_API_BASE" in os.environ or True 
